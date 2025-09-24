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
        case 0: // Date column
            return leftData.toDate() < rightData.toDate();
        case 2: // Amount column
            return leftData.toDouble() < rightData.toDouble();
        default: // Item and Category columns - default string comparison
            return leftData.toString().toLower() < rightData.toString().toLower();
    }
}