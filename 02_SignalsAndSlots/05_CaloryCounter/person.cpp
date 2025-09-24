#include "person.h"

//Leaving this here in case I need it
/*
Person::Person(QObject *parent)
    : QObject{parent}
{

}
*/

/*
void Person::setSex(Sex sex)
{
    if (m_sex != sex) {
        m_sex = sex;
        emit sexChanged();
    }
}

void Person::setAge(int age)
{
    if (m_age != age) {
        m_age = age;
        emit ageChanged();
    }
}
*/


void Person::setWeight(double weight)
{
    if (m_weight != weight) {
        m_weight = weight;
        emit weightChanged();
    }
}
