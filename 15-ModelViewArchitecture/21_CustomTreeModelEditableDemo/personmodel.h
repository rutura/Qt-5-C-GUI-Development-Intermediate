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
    QVariant headerData(int section, Qt::Orientation orientation, int role) const override;

    //Make the model editable
    Qt::ItemFlags flags(const QModelIndex &index) const override;
    bool setData(const QModelIndex &index, const QVariant &value, int role) override;
    bool insertRows( int position, int rows, const QModelIndex & parent = QModelIndex())override;
    bool removeRows( int position, int rows, const QModelIndex & parent = QModelIndex()) override;

signals:

private:
    //Read data
    void readFile();
    QVector<QVariant> parsePersonData(const QString& line);

    //Write data
    bool saveFile();
    void writePersonToStream(QTextStream &out, Person *person, int indent = 0) const;

    //Member variables
    std::unique_ptr<Person> rootPerson;

};

#endif // PERSONMODEL_H
