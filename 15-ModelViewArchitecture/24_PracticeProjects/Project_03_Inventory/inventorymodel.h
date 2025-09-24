#ifndef INVENTORYMODEL_H
#define INVENTORYMODEL_H

#include <QAbstractTableModel>
#include <QVector>
#include <QColor>
#include "inventoryitem.h"

class InventoryModel : public QAbstractTableModel {
    Q_OBJECT

public:
    enum Column {
        ProductName = 0,
        Quantity,
        Supplier,
        ProductImage,
        Rating,
        ColumnCount
    };

    explicit InventoryModel(QObject *parent = nullptr);

    int rowCount(const QModelIndex &parent = QModelIndex()) const override;
    int columnCount(const QModelIndex &parent = QModelIndex()) const override;
    QVariant data(const QModelIndex &index, int role = Qt::DisplayRole) const override;
    bool setData(const QModelIndex &index, const QVariant &value, int role = Qt::EditRole) override;
    QVariant headerData(int section, Qt::Orientation orientation, int role = Qt::DisplayRole) const override;
    Qt::ItemFlags flags(const QModelIndex &index) const override;

    bool addItem(const InventoryItem &item);
    bool removeItem(int row);
    bool updateItem(int row, const InventoryItem &item);
    const InventoryItem &getItem(int row) const;
    bool saveToFile(const QString &filename);
    bool loadFromFile(const QString &filename);
    bool isProductNameUnique(const QString &name, int excludeRow = -1) const;
    void setSupplierList(const QStringList &suppliers);
    QStringList getSupplierList() const;

private:
    QVector<InventoryItem> items;
    QStringList supplierList;
};

#endif // INVENTORYMODEL_H
