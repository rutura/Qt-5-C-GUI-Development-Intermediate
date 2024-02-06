#ifndef PERSON_H
#define PERSON_H

#include <QString>


enum class MaritalStatus{
  SINGLE,
  MARRIED,
};


struct Person
{
  QString firstname, lastname;
  quint16 age;
  QString  occupation;
  MaritalStatus maritalStatus;
  QString   county, country;
  quint16 postalCode;
};

constexpr const char* maritalStatusToString(const MaritalStatus& status){
  switch(status){
  case MaritalStatus::SINGLE:
    return "Single";
  case MaritalStatus::MARRIED:
    return "Married";
  }
}

#endif// PERSON_H
