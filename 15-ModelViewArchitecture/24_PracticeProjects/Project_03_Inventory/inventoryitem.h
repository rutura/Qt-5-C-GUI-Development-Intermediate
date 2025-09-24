#ifndef INVENTORYITEM_H
#define INVENTORYITEM_H

#include <QString>
#include <QPixmap>
#include <QDateTime>

class InventoryItem {
public:
    InventoryItem() : quantity(0), rating(0), lastUpdated(QDateTime::currentDateTime()) {}
    
    QString productName;
    int quantity;
    QString supplier;
    QString imagePath;
    QPixmap image;
    int rating; // 1-5 stars
    QString description;
    QDateTime lastUpdated;
};

#endif // INVENTORYITEM_H
