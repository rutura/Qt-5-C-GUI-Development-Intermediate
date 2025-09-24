#include "personmodel.h"

PersonModel::PersonModel(QObject *parent)
    : QAbstractListModel{parent}
{

    //Populate with initial data
    persons.append (new Person("Jamie Lannister","red",33));
    persons.append(new Person("Marry Lane","cyan",26));
    persons.append(new Person("Steve Moors","yellow",44));
    persons.append(new Person("Victor Trunk","dodgerblue",30));
    persons.append(new Person("Ariel Geeny","blue",33));
    persons.append(new Person("Knut Vikran","lightblue",26));
}

PersonModel::~PersonModel(){
    qDeleteAll(persons);
}


//Add or remove persons explicitly. This is not the best way to do it.
/*
void PersonModel::addPerson( Person* person){
    //Figure out where to add the person: they will go at the end
    const int index = persons.size();
    beginInsertRows(QModelIndex(), index, index);
    persons.append(person);
    endInsertRows();
}
*/

//Go through insertRows and removeRows
void PersonModel::addPerson(Person* person){
    const int index = persons.size();
    if(insertRows(index, 1, QModelIndex())){
        persons[index] = person;
    }
}

void PersonModel::addPerson(){
    Person *person = new Person("Added Person","yellowgreen",45,this);
    addPerson(person);
}

void PersonModel::addPerson(const QString& names, const int age){
    Person *person=new Person(names,"yellowgreen",age);
    addPerson(person);
}



//Add or remove persons explicitly. This is not the best way to do it.
/*
void PersonModel::removePerson(QModelIndex index){
    beginRemoveRows(QModelIndex(),index.row(), index.row());
    persons.removeAt(index.row());
    endRemoveRows();
}
*/

void PersonModel::removePerson(QModelIndex index){
    if(index.isValid()){
        removeRows(index.row(), 1, QModelIndex());
    }
}

//QAbstractItemModel interface
int PersonModel::rowCount(const QModelIndex & parent) const {
    Q_UNUSED(parent);
    return persons.size();
}

QVariant PersonModel::data(const QModelIndex & index, int role) const {
    if (index.row() < 0 || index.row() >= persons.count())
        return QVariant();

    Person* person = persons[index.row()];

    if(role == Qt::DisplayRole || role == Qt::ToolTipRole || role == Qt::EditRole){
        return person->names();
    }

    return QVariant();
}

QVariant PersonModel::headerData(int section, Qt::Orientation orientation, int role ) const{
    if(role != Qt::DisplayRole){
        return QVariant();
    }

    if(orientation == Qt::Horizontal){
        return QString("Person names");
    }

    //Vertical headers
    return QString("Person %1").arg(section);
}


//Methods to make the model editable
bool PersonModel::setData(const QModelIndex &index, const QVariant &value, int role){

    if(!index.isValid()){
        return false;
    }

    Person * person = persons[index.row()];
    bool somethingChanged {false};

    switch (role) {
        case Qt::EditRole:{

            if(person->names() != value.toString()){
                person->setNames(value.toString());
                somethingChanged = true;
            }
        }
        break;

        if(somethingChanged){
            emit dataChanged(index,index);
            return true;
        }
    }
    return false;
}

Qt::ItemFlags PersonModel::flags(const QModelIndex &index) const{

    if(!index.isValid()){
        return QAbstractListModel::flags(index);
    }
    return QAbstractListModel::flags(index) | Qt::ItemIsEditable;
}

bool PersonModel::insertRows(int row, int count, const QModelIndex& index) {

    beginInsertRows(QModelIndex(), row, row + count - 1);

    for(int i = 0; i < count; ++i){
        persons.insert(row, nullptr); // Insert a placeholder instead of a true Person.
    }

    endInsertRows();
    return true;
}


bool PersonModel::removeRows(int row, int count, const QModelIndex& index) {
    beginRemoveRows(QModelIndex(), row, row + count - 1);

    persons.removeAt(row);

    endRemoveRows();
    return true;
}




















