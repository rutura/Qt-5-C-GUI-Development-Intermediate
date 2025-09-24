#include <QFile>
#include <QTextStream>
#include <QDebug>
#include "personmodel.h"

PersonModel::PersonModel(QObject *parent)
    : QAbstractItemModel{parent}
{
    QVector<QVariant> rootData;
    rootData << "Names" << "Proffession";
    rootPerson = std::make_unique<Person>(rootData);

    readFile();
}


QModelIndex PersonModel::index(int row, int column, const QModelIndex &parent) const
{
    if(!hasIndex(row,column,parent))
        return QModelIndex();

    //Go from the language of QAbstractItemModel to the language of our Person tree structure.
    Person * parentPerson = parent.isValid() ? static_cast<Person*> (parent.internalPointer())
                                            : rootPerson.get();

    //Get the child at a given row:
    Person * childPerson = parentPerson->child(row);
    if(childPerson){
        return createIndex(row,column,childPerson);
    }
    return QModelIndex();
}

QModelIndex PersonModel::parent(const QModelIndex &child) const
{
    if(!child.isValid()){
        return QModelIndex();
    }
    Person* childPerson = static_cast<Person*>(child.internalPointer());
    Person* parentPerson = childPerson->parentPerson();

    if(parentPerson == rootPerson.get())
        return QModelIndex();

    return createIndex(parentPerson->row(),0, parentPerson);

}

int PersonModel::rowCount(const QModelIndex &parent) const
{
    //Make sure we process children only for items in the first column
    if(parent.column() > 0)
        return 0;

    //Go from a QModelIndex to a raw Person pointer.
    Person * parentPerson = parent.isValid() ? static_cast<Person*> (parent.internalPointer())
                                            : rootPerson.get();
    return parentPerson->childCount();
}

int PersonModel::columnCount(const QModelIndex &parent) const
{
    Q_UNUSED(parent);
    return 2; // Names and Proffession
}

QVariant PersonModel::data(const QModelIndex &index, int role) const
{
    if(!index.isValid())
        return QVariant();

    if (role != Qt::DisplayRole && role != Qt::EditRole)
        return QVariant();

    Person* person = static_cast<Person*> (index.internalPointer());
    return person->data(index.column());
}

bool PersonModel::setData(const QModelIndex &index, const QVariant &value, int role)
{
    if (role != Qt::EditRole)
        return false;
    Person* person = static_cast<Person*> (index.internalPointer());
    bool result = person->setData(index.column(), value);

    if(result){
        emit dataChanged(index,index,{role});
        saveFile();
    }
    return result;
}

bool PersonModel::insertRows(int position, int rows, const QModelIndex &parent)
{
    Person* parentItem = parent.isValid() ? static_cast<Person*>(parent.internalPointer())
                                          : rootPerson.get();
    bool success;
    beginInsertRows(parent,position, position + rows  -1);

    success = parentItem->insertChildren(position, rows, 2);

    endInsertRows();
    if(success){
        saveFile();
    }
    return success;
}

bool PersonModel::removeRows(int position, int rows, const QModelIndex &parent)
{
    Person* parentItem = parent.isValid() ? static_cast<Person*>(parent.internalPointer())
                                          : rootPerson.get();

    bool success;

    beginRemoveRows(parent,position, position + rows -1);

    success = parentItem->removeChildren(position, rows);

    endRemoveRows();

    if(success){
        saveFile();
    }
    return success;

}

QVariant PersonModel::headerData(int section, Qt::Orientation orientation, int role) const
{
    if (orientation == Qt::Horizontal && role == Qt::DisplayRole) {
        if (section == 0)
            return tr("Names");
        else if (section == 1)
            return tr("Profession");
    }
    return QVariant();
}

Qt::ItemFlags PersonModel::flags(const QModelIndex &index) const
{
    if (!index.isValid())
        return Qt::NoItemFlags;

    return Qt::ItemIsEnabled | Qt::ItemIsSelectable | Qt::ItemIsEditable;
}

void PersonModel::readFile()
{
    QString filename = "data/familytree.txt";
    QFile inputFile(filename);

    if(!inputFile.open(QIODevice::ReadOnly)){
        qDebug() << "Could not open the file: " << filename;
        return;
    }else{
        qDebug() << "File opened successfuly for reading!";
    }

    QTextStream in(&inputFile);
    Person* lastParent = rootPerson.get();
    Person* lastPerson = nullptr;
    int lastIndentation{0};

    while(!in.atEnd()){
        QString line = in.readLine();
        int currentIndentation = line.count('\t');

        QVector<QVariant> data = parsePersonData(line.trimmed());

        int indentDiff = currentIndentation - lastIndentation;

        if(indentDiff == 0){
            //Add the child under the current parent
            auto person = std::make_unique<Person>(data,lastParent);
            lastPerson = person.get();
            lastParent->appendChild(std::move(person));
        }else if( indentDiff > 0){
            //Go deeper in the hierarchy
            lastParent = lastPerson;
            auto person = std::make_unique<Person>(data,lastParent);
            lastPerson = person.get();
            lastParent->appendChild(std::move(person));
        }else{
            //Dif in indentation is negative: Navigate back in the tree structure to figure out the right parent.
            for( int i = 0; i < -indentDiff; ++i){
                lastParent = lastParent->parentPerson();
            }

            auto person = std::make_unique<Person>(data,lastParent);
            lastPerson = person.get();
            lastParent->appendChild(std::move(person));

        }
        lastIndentation = currentIndentation;
    }
    inputFile.close();
}

QVector<QVariant> PersonModel::parsePersonData(const QString &line)
{
    QStringList parts = line.split('(');
    QVector<QVariant> data;
    data << parts[0].trimmed();
    if(parts.size() > 1){
        QString proffesion = parts[1];
        proffesion.chop(1);
        data << proffesion;
    }else{
        data << QString();
    }
    return data;
}

bool PersonModel::saveFile()
{
    QString filename = "data/familytree.txt";
    QFile outputFile(filename);
    if(!outputFile.open(QIODevice::WriteOnly | QIODevice::Text)){
        qDebug() << "Cannot open file for writing:" << filename << " - " << outputFile.errorString();
        return false;
    }

    QTextStream out(&outputFile);

    //Write all children of the root item
    for(int i = 0; i < rootPerson->childCount(); ++i){
        writePersonToStream(out,rootPerson->child(i), 0);
    }

    out.flush();
    outputFile.close();
    return true;
}

void PersonModel::writePersonToStream(QTextStream &out, Person *person, int indent) const
{
    if(!person)
        return;

    //Create indentation with tabs
    QString indentation;
    for(int i = 0; i < indent; ++i){
        indentation += "\t";
    }

    //Format the line: name(proffession)
    QString name = person->data(0).toString();
    QString proffession = person->data(1).toString();
    QString line = indentation + name;

    if(!proffession.isEmpty()){
        line += "(" + proffession + ")";
    }
    out << line << "\n";

    //Write the the children recursively
    for(int i = 0; i < person->childCount(); ++i){
        writePersonToStream(out,person->child(i), indent + 1);
    }
}























