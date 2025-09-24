#ifndef PERSONMODEL_H
#define PERSONMODEL_H

#include <QObject>
#include <QAbstractTableModel>
#include "person.h"

class PersonModel : public QAbstractTableModel
{
    Q_OBJECT

    enum PersonRoles{
        NamesRole = Qt::UserRole + 1,
        FavoriteColorRole,
        AgeRole
    };

public:
    explicit PersonModel(QObject *parent = nullptr);
    ~PersonModel() override;

    void addPerson( Person* person);
    void addPerson();
    void addPerson(const QString& names, const int age);
    void removePerson(QModelIndex index);

    //QAbstractItemModel interface
    int rowCount(const QModelIndex & parent) const override;
    int columnCount(const QModelIndex & parent) const override;
    QVariant data(const QModelIndex & index, int role) const override;


    //Make the model editable
    bool setData(const QModelIndex &index, const QVariant &value, int role = Qt::EditRole) override;
    QVariant headerData(int section, Qt::Orientation orientation, int role = Qt::DisplayRole) const override;
    Qt::ItemFlags flags(const QModelIndex &index) const override;


    bool insertRows(int row, int count, const QModelIndex& index) override;
    bool removeRows(int row, int count, const QModelIndex& index) override;

    QHash<int, QByteArray> roleNames() const override;

signals:
private:
    QList<Person*> persons;
};

#endif // PERSONMODEL_H
