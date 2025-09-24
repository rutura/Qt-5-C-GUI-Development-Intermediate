#ifndef EXPENSEPROXYMODEL_H
#define EXPENSEPROXYMODEL_H

#include <QSortFilterProxyModel>

class ExpenseProxyModel : public QSortFilterProxyModel
{
    Q_OBJECT

public:
    explicit ExpenseProxyModel(QObject *parent = nullptr);

protected:
    bool lessThan(const QModelIndex &left, const QModelIndex &right) const override;
};

#endif // EXPENSEPROXYMODEL_H