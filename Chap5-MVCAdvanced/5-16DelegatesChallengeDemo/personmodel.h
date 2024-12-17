#ifndef PERSONMODEL_H
#define PERSONMODEL_H

#include <QAbstractTableModel>
#include "person.h"

class PersonModel : public QAbstractTableModel
{
    Q_OBJECT


public:
    enum PersonRoles{
        NamesRole = Qt::UserRole + 1,
        FavoriteColorRole,
        AgeRole,
        SociaScoreRole
    };
    explicit PersonModel(QObject *parent = nullptr);
    ~PersonModel() override;


    void addPerson( Person *person);
    void addPerson();
    void addPerson(const QString & names,const int & age,const int & socialScore);
    void removePerson(QModelIndex index);



    // QAbstractItemModel interface
    int rowCount(const QModelIndex &parent) const override;
    int columnCount(const QModelIndex &parent) const override;
    QVariant data(const QModelIndex &index, int role) const override;

    //Change the data in the model
    bool setData(const QModelIndex &index, const QVariant &value, int role) override;

    //Control data in the horizontal and vertical headers
    QVariant headerData(int section, Qt::Orientation orientation, int role) const override;

    //Flags the model as editable
    Qt::ItemFlags flags(const QModelIndex &index) const override;

    bool insertRows(int row, int count, const QModelIndex &parent = QModelIndex()) override;
    bool removeRows(int row, int count, const QModelIndex &parent = QModelIndex()) override;

    QHash<int, QByteArray> roleNames() const override;

signals:

public slots:
private:
    QList<Person * > persons;









    // QAbstractItemModel interface
public:
    bool hasChildren(const QModelIndex &parent) const override;
};

#endif // PERSONMODEL_H
