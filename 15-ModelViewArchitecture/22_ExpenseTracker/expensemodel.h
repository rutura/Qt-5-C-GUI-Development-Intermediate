#ifndef EXPENSEMODEL_H
#define EXPENSEMODEL_H

#include <QAbstractTableModel>
#include <QList>
#include "expense.h"

class ExpenseModel : public QAbstractTableModel
{
    Q_OBJECT

public:
    explicit ExpenseModel(QObject *parent = nullptr);
    ~ExpenseModel() override;

    // Core table model functions
    int rowCount(const QModelIndex &parent = QModelIndex()) const override;
    int columnCount(const QModelIndex &parent = QModelIndex()) const override;
    QVariant data(const QModelIndex &index, int role = Qt::DisplayRole) const override;
    QVariant headerData(int section, Qt::Orientation orientation, int role = Qt::DisplayRole) const override;
    bool setData(const QModelIndex &index, const QVariant &value, int role = Qt::EditRole) override;
    Qt::ItemFlags flags(const QModelIndex &index) const override;

    // Helper functions
    void addExpense(Expense *expense);
    void removeExpense(const QModelIndex &index);

private:
    bool saveExpenses();
    bool loadExpenses();
    
private:
    QList<Expense*> m_expenses;
    const QStringList m_headers = {"Date", "Item", "Amount", "Category"};
};

#endif // EXPENSEMODEL_H