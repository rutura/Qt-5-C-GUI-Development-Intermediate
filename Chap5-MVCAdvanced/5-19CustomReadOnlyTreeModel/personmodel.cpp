#include "personmodel.h"
#include <QTextStream>
#include <QDebug>

PersonModel::PersonModel(QObject *parent) : QAbstractItemModel(parent)
{
    rootPerson = new Person("Names","Proffession");
    readFile();
}

PersonModel::~PersonModel()
{
    //Memory management
    delete rootPerson;
}

QModelIndex PersonModel::index(int row, int column, const QModelIndex &parent) const
{
    if (!hasIndex(row, column, parent))
        return QModelIndex();
    Person * parentPerson;

    if(!parent.isValid()){
        parentPerson = rootPerson;
    }else{
        parentPerson = static_cast<Person*>(parent.internalPointer());
    }

    Person * chilPerson = parentPerson->child(row);
    if(chilPerson)
        return createIndex(row,column,chilPerson);
    return QModelIndex();
}

QModelIndex PersonModel::parent(const QModelIndex &child) const
{
    if (!child.isValid())
        return QModelIndex();

    Person * childPerson = static_cast<Person*>(child.internalPointer());
    Person * parentPerson = childPerson->parentPerson();
    if(parentPerson== rootPerson)
        return QModelIndex();
    return createIndex(parentPerson->row(),0,parentPerson);
}

int PersonModel::rowCount(const QModelIndex &parent) const
{
    Person * parentPerson;
    /*
         * Only the first columns can have children
         * */
    if(parent.column() > 0)
        return 0;

    if(!parent.isValid()){
        parentPerson = rootPerson;
    }else{
        parentPerson = static_cast<Person*>(parent.internalPointer());
    }

    return  parentPerson->childCount();

}

int PersonModel::columnCount(const QModelIndex &parent) const
{
    Q_UNUSED(parent);
    return  2;
}

QVariant PersonModel::data(const QModelIndex &index, int role) const
{
    if (!index.isValid())
        return QVariant();

    //No need to handle edit role here, the model is not editable anyway.
    if (role != Qt::DisplayRole)
        return QVariant();

    Person * person = static_cast<Person*>(index.internalPointer());

    return person->data(index.column());

}

QVariant PersonModel::headerData(int section, Qt::Orientation orientation, int role) const
{
    if(orientation == Qt::Horizontal && (role == Qt::DisplayRole)){
        return  rootPerson->data(section);
    }
    return QVariant();
}

Qt::ItemFlags PersonModel::flags(const QModelIndex &index) const
{
    if (!index.isValid())
        return nullptr;
    return QAbstractItemModel::flags(index);
}




void PersonModel::readFile()
{
    QString filename = ":/data/familytree1.txt";
    QFile inputFile(filename);
    if(inputFile.open(QIODevice::ReadOnly)){
        int lastIndentation = 0;
        Person * lastParent = rootPerson;
        Person * lastPerson = nullptr;

        QTextStream in(&inputFile);

        while (!in.atEnd()) {

            QString line = in.readLine();

            int currentIndentation = line.count("\t");

            qDebug() << "Read line : " << line << " tab count : " << QString::number(currentIndentation);

            QStringList infoList = getNamesAndProffession(line);


            int diffIndent = currentIndentation - lastIndentation;

            if(diffIndent == 0){
                //First Level Person
                Person * person = new Person(infoList[0],infoList[1],lastParent);
                lastParent->appendChild(person);
                lastPerson = person;

            }else if(diffIndent > 0){
                //Move the parent down
                lastParent = lastPerson;
                Person * person = new Person(infoList[0],infoList[1],lastParent);
                lastParent->appendChild(person);
                lastPerson = person;
            }else{
                //Move up the parent chain looking the  correct parent
                int iterations = - diffIndent;
                for(int i = 0; i < iterations ; i++){
                    lastParent = lastParent->parentPerson();
                }
                Person * person = new Person(infoList[0],infoList[1],lastParent);
                lastParent->appendChild(person);
                lastPerson = person;
            }
            lastIndentation = currentIndentation;
        }
        inputFile.close();
    }

}


QStringList PersonModel::getNamesAndProffession(QString txtString)
{
    //Get rid of the spaces
    QString cleanedUpStr = txtString.trimmed();
    QStringList split = cleanedUpStr.split("(");
    split[1].chop(1);
    return split;
}
