#ifndef PERSONMODEL_H
#define PERSONMODEL_H

#include <QObject>
#include <QAbstractItemModel>
#include <memory>
#include "person.h"

class PersonModel : public QAbstractItemModel
{
    Q_OBJECT
public:
    explicit PersonModel(QObject *parent = nullptr);

// QAbstractItemModel interface
public:
    QModelIndex index(int row, int column, const QModelIndex &parent) const override;
    QModelIndex parent(const QModelIndex &child) const override;

    int rowCount(const QModelIndex &parent) const override;
    int columnCount(const QModelIndex &parent) const override;
    QVariant data(const QModelIndex &index, int role) const override;
    bool setData(const QModelIndex &index, const QVariant &value, int role) override;
    QVariant headerData(int section, Qt::Orientation orientation, int role) const override;
    Qt::ItemFlags flags(const QModelIndex &index) const override;

signals:

private:
    void readFile();
    QVector<QVariant> parsePersonData(const QString& line);
    std::unique_ptr<Person> rootPerson;

};

#endif // PERSONMODEL_H
