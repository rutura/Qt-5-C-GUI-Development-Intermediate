#ifndef PERSONMODEL_H
#define PERSONMODEL_H

#include <QObject>
#include <QAbstractListModel>
#include "person.h"

class PersonModel : public QAbstractListModel
{
    Q_OBJECT
public:
    explicit PersonModel(QObject *parent = nullptr);
    ~PersonModel() override;

    //QAbstractItemModel interface
    int rowCount(const QModelIndex & parent) const override;
    QVariant data(const QModelIndex & index, int role) const override;

signals:
private:
    QList<Person*> persons;
};

#endif // PERSONMODEL_H
