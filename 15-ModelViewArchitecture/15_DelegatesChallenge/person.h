#ifndef PERSON_H
#define PERSON_H

#include <QObject>

class Person : public QObject
{
    Q_OBJECT

public:
    explicit Person(QObject *parent = nullptr);
    Person(const QString &names, const QString &favoritecolor,
           const int &age , const int & socialScore, QObject * parent = nullptr);

    QString names() const;
    QString favoriteColor() const;
    int age() const;
    void setNames(QString names);
    void setFavoriteColor(QString favoriteColor);
    void setAge(int age);

    int socicalScore() const;
    void setSocicalScore(int newSocicalScore);

signals:
    void namesChanged(QString names);
    void favoriteColorChanged(QString favoriteColor);
    void ageChanged(int age);
    void socialScoreChanged(int socialScore);

private:
    QString m_names;
    QString m_favoriteColor;
    int m_age;
    int m_socialScore{1};
};

#endif // PERSON_H
