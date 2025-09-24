#ifndef PERSON_H
#define PERSON_H

#include <memory>
#include <QVector>
#include <QVariant>

class Person
{
public:
    Person(const QVector<QVariant> & data, Person * parent = nullptr);
    ~Person() = default;

    void appendChild(std::unique_ptr<Person> child);
    Person* child(int row);
    int childCount() const;
    int columnCount() const;
    QVariant data(int column) const;
    int row() const;
    Person* parentPerson();
    void printTree(int indent = 0) const;

    bool insertChildren(int position, int count, int columns);
    bool removeChildren(int position, int count);
    bool setData(int column, const QVariant& value);
private:
    std::vector<std::unique_ptr<Person>> children;
    QVector<QVariant> itemData;
    Person* parent;
};

#endif // PERSON_H
