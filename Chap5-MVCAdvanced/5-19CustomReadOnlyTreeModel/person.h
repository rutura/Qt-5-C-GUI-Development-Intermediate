#ifndef PERSON_H
#define PERSON_H

#include <QString>
#include <QList>

class Person
{
public:
    Person(QString names,QString proffession,Person * parent = nullptr);
    ~Person();
    void appendChild(Person * childParam);
    Person * child( int row);
    int childCount() const;
    QVariant data(int column) const;
    int row () const;
    Person *parentPerson();

    void showInfo();



private:

    QList<Person*> children;
    QString names;
    QString proffession;
    Person * parent;
};

#endif // PERSON_H
