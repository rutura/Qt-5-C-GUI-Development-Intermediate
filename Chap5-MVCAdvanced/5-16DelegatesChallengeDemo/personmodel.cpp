#include "personmodel.h"
#include <QDebug>

PersonModel::PersonModel(QObject *parent) : QAbstractTableModel(parent)
{

    //Populate with initial data
    persons.append (new Person("Jamie Lannister","red",33,2));
    persons.append(new Person("Marry Lane","cyan",26,5));
    persons.append(new Person("Steve Moors","yellow",44,3));
    persons.append(new Person("Victor Trunk","dodgerblue",30,2));
    persons.append(new Person("Ariel Geeny","blue",33,4));
    persons.append(new Person("Knut Vikran","lightblue",26,3));

}

PersonModel::~PersonModel()
{
    qDeleteAll(persons);
}

void PersonModel::addPerson(Person *person)
{
    /*
    const int index = persons.size();
    beginInsertRows(QModelIndex(),index,index);
    persons.append(person);
    endInsertRows();
    */
    insertRows(persons.size(),1);
    setData(index(persons.size() -1,0),person->names(),Qt::EditRole);
    setData(index(persons.size() -1,1),person->age(),Qt::EditRole);
    setData(index(persons.size() -1,2),person->favoriteColor(),Qt::EditRole);
}

void PersonModel::addPerson()
{
    Person *person = new Person("Added Person","yellowgreen",45,4,this);
    addPerson(person);
}

void PersonModel::addPerson(const QString &names, const int &age,const int & socialScore)
{
    Person *person=new Person(names,"yellowgreen",age,socialScore);
    addPerson(person);
}

void PersonModel::removePerson(QModelIndex index)
{
    /*
    beginRemoveRows(QModelIndex(),index.row(),index.row());

    persons.removeAt(index.row());

    endRemoveRows();
    */
    removeRows(index.row(),1);

}

int PersonModel::rowCount(const QModelIndex &parent) const
{
    Q_UNUSED(parent);
    return  persons.size();
}

int PersonModel::columnCount(const QModelIndex &parent) const
{
    Q_UNUSED(parent);
    return  4;
}

QVariant PersonModel::data(const QModelIndex &index, int role) const
{
    if (index.row() < 0 || index.row() >= persons.count())
        return QVariant();
    Person * person = persons[index.row()];
    if(role == Qt::DisplayRole || role == Qt::EditRole){

        if(index.column() == 0){
            //Names
            return person->names();
        }
        if(index.column() == 1){
            //Age
            return person->age();
        }
        if(index.column() == 2){
            //Favorite color
            return person->favoriteColor();
        }
        if(index.column() == 3){
            //Social Score
            return person->socialScore();
        }
    }


    if(role == NamesRole){
        return  person->names();
    }

    if(role == FavoriteColorRole){
        return  person->favoriteColor();
    }
    if(role == AgeRole){
        return person->age();
    }

    if(role == Qt::ToolTipRole){
        return  person->names();
    }
    return  QVariant();

}

bool PersonModel::setData(const QModelIndex &index, const QVariant &value, int role)
{
    if(!index.isValid()) {
        return false;
    }

    Person * person = persons[index.row()];
    bool somethingChanged = false;

    switch (role) {

    case Qt::EditRole:
    {

        if(index.column() == 0){
            //Names
            if( person->names()!= value.toString()){
                person->setNames(value.toString());
                somethingChanged = true;
            }
        }

        if(index.column() == 1){
            //Age
            if(person->age()!=value.toInt()){
                person->setAge(value.toInt());
                somethingChanged  = true;
            }
        }

        if(index.column() == 2){
            //FavoriteColor
            if(person->favoriteColor()!= value.toString()){
                person->setFavoriteColor(value.toString());
                somethingChanged  = true;

            }
        }

        if(index.column() == 3){
            //Social score
            if(person->socialScore()!= value.toInt()){
                person->setSocialScore(value.toInt());
                somethingChanged  = true;

            }
        }

    }break;


    case NamesRole:
    {
        qDebug() << "Names role changing names, index " << index.row();
        if( person->names()!= value.toString()){
            person->setNames(value.toString());
            somethingChanged = true;
        }
    }
        break;


    case AgeRole:
    {
        if( person->age()!= value.toInt()){
            person->setAge(value.toInt());
            somethingChanged = true;
        }
    }
        break;

    case FavoriteColorRole:
    {
        if( person->favoriteColor()!= value.toString()){
            person->setFavoriteColor(value.toString());
            somethingChanged = true;
        }
    }
    }

    if(somethingChanged){
        emit dataChanged(index,index);
        return true;
    }

    return false;
}

QVariant PersonModel::headerData(int section, Qt::Orientation orientation, int role) const
{

    if (role != Qt::DisplayRole) {
        return QVariant();
    }
    if (orientation == Qt::Horizontal) {
        switch (section) {
        case 0 :
            return QString("Names");
        case 1 :
            return QString("Age");
        case 2:
            return QString("Favorite color");
        case 3:
            return QString("Social Score");
        }

    }
    // vertical rows
    return QString("Person %1").arg(section);
}

Qt::ItemFlags PersonModel::flags(const QModelIndex &index) const
{
    if (!index.isValid()) {
        return QAbstractItemModel::flags(index);
    }
    return QAbstractItemModel::flags(index) | Qt::ItemIsEditable;
}

bool PersonModel::insertRows(int row, int count, const QModelIndex &parent)
{
    beginInsertRows(QModelIndex(), row, row+count-1);

    for (int i = 0; i < count; ++i) {
        persons.insert(row,new Person());
    }
    endInsertRows();
    return  true;
}

bool PersonModel::removeRows(int row, int count, const QModelIndex &parent)
{
    beginRemoveRows(QModelIndex(), row, row+count-1);

    for (int i = 0; i < count; ++i) {
        persons.removeAt(row);
    }
    endRemoveRows();
    return true;
}

QHash<int, QByteArray> PersonModel::roleNames() const
{
    QHash<int,QByteArray> roles;
    roles[NamesRole] = "names";
    roles[FavoriteColorRole] = "favoritecolor";
    roles[AgeRole] = "age";
    roles[SociaScoreRole] = "socialcore";
    return  roles;
}

bool PersonModel::hasChildren(const QModelIndex &parent) const
{
    if(parent.column() == 0)
        return  false;
    return true;
}
