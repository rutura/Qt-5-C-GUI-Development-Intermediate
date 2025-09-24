#include "person.h"
#include <algorithm>
#include <QDebug>

Person::Person(const QVector<QVariant> & data, Person * parent)
    : itemData(data), parent(parent)
    {}

void Person::appendChild(std::unique_ptr<Person> child)
{
    children.push_back(std::move(child));
}

Person *Person::child(int row)
{
    //Make sure you don't go over bounds
    if (row < 0 || row >= static_cast<int>(children.size()))
        return nullptr;
    return children[row].get();

}

int Person::childCount() const
{
    return static_cast<int>(children.size());
}

int Person::columnCount() const
{
    return itemData.size();
}

QVariant Person::data(int column) const
{
    return itemData.value(column);
}

int Person::row() const
{
    if(parent){

        //Find the pointer equal to this pointer in the list of our parent's children
        auto it = std::find_if(parent->children.begin(),parent->children.end(),[this](const auto& child){
            return child.get() == this;
        });

        //Find the location
        if( it != parent->children.end()){
            //We have found our iterator. We just need to return the index.
            return std::distance(parent->children.begin(),it);
        }
    }
    return 0;
}

Person *Person::parentPerson()
{
    return parent;
}

void Person::printTree(int indent) const
{
    QString indentStr = QString(indent, ' ');

    //Print the current node
    QStringList dataStrings;
    for(const QVariant& item: itemData){
        dataStrings << item.toString();
    }

    qDebug().noquote() << indentStr << "+-" << dataStrings.join(" | ");

    //Print children
    for( const auto& child: children){
        child->printTree(indent + 4);
    }

}

bool Person::insertChildren(int position, int count, int columns)
{
    if (position < 0 || position > static_cast<int>(children.size()))
        return false;
    for(int row = 0; row < count; ++ row){
        QVector<QVariant> data(columns);
        auto person = std::make_unique<Person>(data,this);
        children.insert(children.begin() + position, std::move(person));

    }
    return true;
}

bool Person::removeChildren(int position, int count)
{

    if (position < 0 || position + count > static_cast<int>(children.size()))
        return false;
    children.erase(children.begin() + position, children.begin() + position + count);
    return true;
}

bool Person::setData(int column, const QVariant &value)
{
    if (column < 0 || column >= itemData.size())
        return false;
    itemData[column] = value;
    return true;

}
