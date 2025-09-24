#include "inventorymodel.h"
#include <QJsonDocument>
#include <QJsonArray>
#include <QJsonObject>
#include <QFile>
#include <QDir>

InventoryModel::InventoryModel(QObject *parent)
    : QAbstractTableModel(parent)
{
}

int InventoryModel::rowCount(const QModelIndex &parent) const
{
    if (parent.isValid())
        return 0;
    return items.size();
}

int InventoryModel::columnCount(const QModelIndex &parent) const
{
    if (parent.isValid())
        return 0;
    return Column::ColumnCount;
}

QVariant InventoryModel::data(const QModelIndex &index, int role) const
{
    if (!index.isValid() || index.row() >= items.size())
        return QVariant();

    const InventoryItem &item = items[index.row()];

    if (role == Qt::DisplayRole || role == Qt::EditRole) {
        switch (index.column()) {
            case ProductName:
                return item.productName;
            case Quantity:
                return item.quantity;
            case Supplier:
                return item.supplier;
            case ProductImage:
                return item.imagePath;
            case Rating:
                return item.rating;
            default:
                return QVariant();
        }
    } else if (role == Qt::DecorationRole && index.column() == ProductImage) {
        if (!item.image.isNull()) {
            return item.image.scaled(64, 64, Qt::KeepAspectRatio, Qt::SmoothTransformation);
        }
    } else if (role == Qt::ToolTipRole) {
        switch (index.column()) {
            case ProductName:
                return item.description;
            case ProductImage:
                return tr("Double-click to change image");
            default:
                return QVariant();
        }
    }

    return QVariant();
}

bool InventoryModel::setData(const QModelIndex &index, const QVariant &value, int role)
{
    if (!index.isValid() || index.row() >= items.size())
        return false;

    if (role == Qt::EditRole) {
        InventoryItem &item = items[index.row()];
        bool changed = false;

        switch (index.column()) {
            case ProductName:
                if (value.toString() != item.productName && !value.toString().isEmpty() &&
                    isProductNameUnique(value.toString(), index.row())) {
                    item.productName = value.toString();
                    changed = true;
                }
                break;
            case Quantity:
                item.quantity = value.toInt();
                changed = true;
                break;
            case Supplier:
                item.supplier = value.toString();
                changed = true;
                break;
            case ProductImage:
                item.imagePath = value.toString();
                if (!value.toString().isEmpty()) {
                    item.image = QPixmap(value.toString());
                } else {
                    item.image = QPixmap();
                }
                changed = true;
                break;
            case Rating:
                item.rating = value.toInt();
                changed = true;
                break;
        }

        if (changed) {
            item.lastUpdated = QDateTime::currentDateTime();
            emit dataChanged(index, index);
            return true;
        }
    }

    return false;
}

QVariant InventoryModel::headerData(int section, Qt::Orientation orientation, int role) const
{
    if (role != Qt::DisplayRole || orientation != Qt::Horizontal)
        return QVariant();

    switch (section) {
        case ProductName: return tr("Product Name");
        case Quantity: return tr("Quantity");
        case Supplier: return tr("Supplier");
        case ProductImage: return tr("Image");
        case Rating: return tr("Rating");
        default: return QVariant();
    }
}

Qt::ItemFlags InventoryModel::flags(const QModelIndex &index) const
{
    if (!index.isValid())
        return Qt::NoItemFlags;

    return Qt::ItemIsEditable | Qt::ItemIsEnabled | Qt::ItemIsSelectable;
}

bool InventoryModel::addItem(const InventoryItem &item)
{
    if (item.productName.isEmpty() || !isProductNameUnique(item.productName))
        return false;

    beginInsertRows(QModelIndex(), items.size(), items.size());
    items.append(item);
    endInsertRows();
    return true;
}

bool InventoryModel::removeItem(int row)
{
    if (row < 0 || row >= items.size())
        return false;

    // Delete the image file if it exists
    if (!items[row].imagePath.isEmpty()) {
        QFile::remove(items[row].imagePath);
    }

    beginRemoveRows(QModelIndex(), row, row);
    items.removeAt(row);
    endRemoveRows();
    return true;
}

bool InventoryModel::updateItem(int row, const InventoryItem &item)
{
    if (row < 0 || row >= items.size())
        return false;

    if (item.productName != items[row].productName &&
        !isProductNameUnique(item.productName, row))
        return false;

    items[row] = item;
    emit dataChanged(index(row, 0), index(row, ColumnCount - 1));
    return true;
}

const InventoryItem &InventoryModel::getItem(int row) const
{
    return items[row];
}

bool InventoryModel::saveToFile(const QString &filename)
{
    QJsonArray itemsArray;
    for (const InventoryItem &item : items) {
        QJsonObject itemObj;
        itemObj["productName"] = item.productName;
        itemObj["quantity"] = item.quantity;
        itemObj["supplier"] = item.supplier;
        itemObj["imagePath"] = item.imagePath;
        itemObj["rating"] = item.rating;
        itemObj["description"] = item.description;
        itemObj["lastUpdated"] = item.lastUpdated.toString(Qt::ISODate);
        itemsArray.append(itemObj);
    }

    QJsonObject root;
    root["items"] = itemsArray;
    root["suppliers"] = QJsonArray::fromStringList(supplierList);

    QJsonDocument doc(root);
    QFile file(filename);
    if (!file.open(QIODevice::WriteOnly))
        return false;

    file.write(doc.toJson());
    return true;
}

bool InventoryModel::loadFromFile(const QString &filename)
{
    QFile file(filename);
    if (!file.open(QIODevice::ReadOnly))
        return false;

    QJsonDocument doc = QJsonDocument::fromJson(file.readAll());
    if (doc.isNull())
        return false;

    QJsonObject root = doc.object();
    QJsonArray itemsArray = root["items"].toArray();
    QJsonArray suppliersArray = root["suppliers"].toArray();

    beginResetModel();
    items.clear();
    for (const QJsonValue &val : itemsArray) {
        QJsonObject obj = val.toObject();
        InventoryItem item;
        item.productName = obj["productName"].toString();
        item.quantity = obj["quantity"].toInt();
        item.supplier = obj["supplier"].toString();
        item.imagePath = obj["imagePath"].toString();
        if (!item.imagePath.isEmpty()) {
            item.image = QPixmap(item.imagePath);
        }
        item.rating = obj["rating"].toInt();
        item.description = obj["description"].toString();
        item.lastUpdated = QDateTime::fromString(obj["lastUpdated"].toString(), Qt::ISODate);
        if (!item.lastUpdated.isValid()) {
            item.lastUpdated = QDateTime::currentDateTime();
        }
        items.append(item);
    }

    supplierList.clear();
    for (const QJsonValue &val : suppliersArray) {
        supplierList.append(val.toString());
    }
    endResetModel();

    return true;
}

bool InventoryModel::isProductNameUnique(const QString &name, int excludeRow) const
{
    for (int i = 0; i < items.size(); ++i) {
        if (i != excludeRow && items[i].productName == name)
            return false;
    }
    return true;
}

void InventoryModel::setSupplierList(const QStringList &suppliers)
{
    supplierList = suppliers;
}

QStringList InventoryModel::getSupplierList() const
{
    return supplierList;
}
