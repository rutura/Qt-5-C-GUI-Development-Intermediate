#include "person.h"
#include <QDebug>

Person::Person(const QVector<QVariant> &data, Person *parent)
{
    //    this->names = names;
    //    this->proffession = proffession;
    this->parent = parent;
    columnFields = data;

}

Person::~Person()
{
    qDeleteAll(children);
}

void Person::appendChild(Person * childParam)
{
    children.append(childParam);
}

Person *Person::child(int row)
{
    return children.value(row);
}

int Person::childCount() const
{
    return children.count();
}

QVariant Person::data(int column) const
{
    return columnFields.value(column);
}

/*
 * return index of this person in the list of children of its parent
 * */

int Person::row() const
{
    if(parent){
        return  parent->children.indexOf(const_cast<Person*>(this));
    }
    return  0;
}

Person *Person::parentPerson()
{
    return parent;
}

//Recursive function
void Person::showInfo()
{
    qDebug() << "Person : "<< columnFields.at(0).toString()<< "(" <<  childCount() <<" children)";

    QStringList columns;
    foreach (QVariant column, columnFields) {
        columns.append(column.toString());
    }
    qDebug() << " Columns : " << columns;
    foreach (Person *child, children) {
        child->showInfo();
    }
}

int Person::columnCount() const
{
    return columnFields.count();
}

bool Person::insertChildren(int position, int count, int columns)
{
    if (position < 0 || position > children.size())
        return false;

    for( int row = 0; row < count ; row ++){
        QVector<QVariant> data(columns);
        Person * person = new Person(data,this);
        children.insert(position,person);
    }
    return  true;
}

bool Person::insertColumns(int position, int columns)
{

    if (position < 0 || position > columnFields.size())
        return false;
    for (int column = 0; column < columns; ++column){
        columnFields.insert(position, QVariant());
    }

    foreach (Person * person, children) {
        person->insertColumns(position,columns);
    }
    return true;
}

bool Person::removeChildren(int position, int count)
{
    if (position < 0 || position + count > children.size())
        return false;
    for(int row = 0 ; row < count ; row++){
        Person * child = children.takeAt(position);
        delete child;
    }

    return true;
}

bool Person::removeColumns(int position, int columns)
{
    if (position < 0 || position + columns > columnFields.size())
        return false;

    for (int column = 0; column < columns; ++column)
        columnFields.remove(position);
    foreach (Person * person, children) {
        person->removeColumns(position,columns);
    }
    return true;
}

int Person::childNumber() const
{
    if (parent)
        return parent->children.indexOf(const_cast<Person*>(this));

    return 0;
}

bool Person::setData(int column, const QVariant &value)
{
    if (column < 0 || column >= columnFields.size())
        return false;
    columnFields[column] = value;

    return  true;
}
