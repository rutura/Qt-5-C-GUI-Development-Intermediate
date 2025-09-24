#ifndef EXPENSEMODEL_H
#define EXPENSEMODEL_H

#include <QSqlTableModel>
#include <QSqlDatabase>
#include <QSqlError>
#include <QSqlQuery>
#include <QDate>

class ExpenseModel : public QSqlTableModel
{
    Q_OBJECT

public:
    explicit ExpenseModel(QObject *parent = nullptr);
    ~ExpenseModel() override;

    // Database initialization
    bool initializeModel();
    
    // Overridden functions for custom formatting
    QVariant data(const QModelIndex &index, int role = Qt::DisplayRole) const override;
    bool setData(const QModelIndex &index, const QVariant &value, int role = Qt::EditRole) override;
    QVariant headerData(int section, Qt::Orientation orientation, int role = Qt::DisplayRole) const override;
    Qt::ItemFlags flags(const QModelIndex &index) const override;

    // Helper functions with new implementation
    void addExpense(const QDate &date, const QString &item, double amount, const QString &category);
    void removeExpense(const QModelIndex &index);

private:
    bool createTable();
};

#endif // EXPENSEMODEL_H