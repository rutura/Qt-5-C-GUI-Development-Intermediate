#include "expenseproxymodel.h"
#include "expensemodel.h"
#include <QDate>

ExpenseProxyModel::ExpenseProxyModel(QObject *parent)
    : QSortFilterProxyModel(parent)
{
}

bool ExpenseProxyModel::lessThan(const QModelIndex &left, const QModelIndex &right) const
{
    QVariant leftData = sourceModel()->data(left, Qt::EditRole);
    QVariant rightData = sourceModel()->data(right, Qt::EditRole);

    switch (left.column()) {
        case 1: // Date column
            return leftData.toDate() < rightData.toDate();
        case 3: // Amount column
            return leftData.toDouble() < rightData.toDouble();
        default: // ID, Item and Category columns - default string comparison
            return leftData.toString().toLower() < rightData.toString().toLower();
    }
}