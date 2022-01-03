#ifndef PERSON_H
#define PERSON_H

#include <QObject>

class Person : public QObject
{
    Q_OBJECT

public:
    explicit Person(QObject *parent = nullptr);
    Person(const QString &names, const QString &favoritecolor,
           const int &age , QObject * parent = nullptr);

    QString names() const;
    QString favoriteColor() const;
    int age() const;
    void setNames(QString names);
    void setFavoriteColor(QString favoriteColor);
    void setAge(int age);

signals:
    void namesChanged(QString names);
    void favoriteColorChanged(QString favoriteColor);
    void ageChanged(int age);

private:
    QString m_names;
    QString m_favoriteColor;
    int m_age;
};

#endif // PERSON_H
