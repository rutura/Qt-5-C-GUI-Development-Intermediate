## Changes 
- Added support for cmake build systems. 
- Refactored the table vector to support a person model.
- Person model
```cpp
struct Person
{
  QString firstname, lastname;
  quint16 age;
  QString  occupation;
  MaritalStatus maritalStatus;
  QString   county, country;
  quint16 postalCode;
};
```
- Update widget table to support persons models and the different type of members in the person model. 