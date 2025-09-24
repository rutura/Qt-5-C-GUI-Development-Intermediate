#include "expensemodel.h"
#include <QDateTime>
#include <QDir>
#include <QFile>
#include <QTextStream>

ExpenseModel::ExpenseModel(QObject *parent)
    : QAbstractTableModel(parent)
{
    loadExpenses();
}

ExpenseModel::~ExpenseModel()
{
    saveExpenses();
    qDeleteAll(m_expenses);
}

int ExpenseModel::rowCount(const QModelIndex &parent) const
{
    Q_UNUSED(parent);
    return m_expenses.size();
}

int ExpenseModel::columnCount(const QModelIndex &parent) const
{
    Q_UNUSED(parent);
    return 4; // Date, Item, Amount, Category
}

QVariant ExpenseModel::data(const QModelIndex &index, int role) const
{
    if (!index.isValid() || index.row() >= m_expenses.count())
        return QVariant();

    Expense *expense = m_expenses[index.row()];

    if (role == Qt::DisplayRole) {
        switch (index.column()) {
            case 0: // Date
                return expense->date().toString("dd-MM-yyyy");
            case 1: // Item
                return expense->item();
            case 2: // Amount
                return QString::number(expense->amount(), 'f', 2);
            case 3: // Category
                return expense->category();
        }
    }
    else if (role == Qt::EditRole) {
        switch (index.column()) {
            case 0: // Date
                return expense->date();
            case 1: // Item
                return expense->item();
            case 2: // Amount
                return expense->amount();
            case 3: // Category
                return expense->category();
        }
    }

    return QVariant();
}

QVariant ExpenseModel::headerData(int section, Qt::Orientation orientation, int role) const
{
    if (role != Qt::DisplayRole)
        return QVariant();

    if (orientation == Qt::Horizontal) {
        return m_headers[section];
    }

    return QVariant();
}

bool ExpenseModel::setData(const QModelIndex &index, const QVariant &value, int role)
{
    if (!index.isValid() || role != Qt::EditRole)
        return false;

    Expense *expense = m_expenses[index.row()];
    bool changed = false;

    switch (index.column()) {
        case 0: // Date
            {
                QDate date;
                if (value.typeId() == QMetaType::QString) {
                    // Try to parse string input
                    date = QDate::fromString(value.toString(), "dd-MM-yyyy");
                } else {
                    // Handle QDate input directly
                    date = value.toDate();
                }
                
                if (date.isValid()) {
                    expense->setDate(date);
                    changed = true;
                }
            }
            break;
        case 1: // Item
            if (!value.toString().isEmpty()) {
                expense->setItem(value.toString());
                changed = true;
            }
            break;
        case 2: // Amount
            {
                bool ok;
                double amount = value.toDouble(&ok);
                if (ok && amount >= 0) {
                    expense->setAmount(amount);
                    changed = true;
                }
            }
            break;
        case 3: // Category
            if (!value.toString().isEmpty()) {
                expense->setCategory(value.toString());
                changed = true;
            }
            break;
    }

    if (changed) {
        emit dataChanged(index, index, {role});
        saveExpenses();
        return true;
    }

    return false;
}

Qt::ItemFlags ExpenseModel::flags(const QModelIndex &index) const
{
    if (!index.isValid())
        return Qt::NoItemFlags;

    return Qt::ItemIsEnabled | Qt::ItemIsSelectable | Qt::ItemIsEditable;
}

void ExpenseModel::addExpense(Expense *expense)
{
    int row = m_expenses.size();
    beginInsertRows(QModelIndex(), row, row);
    m_expenses.append(expense);
    endInsertRows();
    saveExpenses(); // Save happens automatically
}

void ExpenseModel::removeExpense(const QModelIndex &index)
{
    if (!index.isValid())
        return;

    beginRemoveRows(QModelIndex(), index.row(), index.row());
    delete m_expenses.takeAt(index.row());
    endRemoveRows();
    saveExpenses(); // Save happens automatically
}

bool ExpenseModel::saveExpenses()
{
    QDir dir("data");
    if (!dir.exists()) {
        dir.mkpath(".");
    }

    QFile file("data/expenses.txt");
    if (!file.open(QIODevice::WriteOnly | QIODevice::Text)) {
        return false;
    }

    QTextStream out(&file);
    for (const Expense* expense : m_expenses) {
        out << expense->date().toString("dd-MM-yyyy") << "\t"
            << expense->item() << "\t"
            << QString::number(expense->amount(), 'f', 2) << "\t"
            << expense->category() << "\n";
    }

    return true;
}

/*
    We assume there is a file named "expenses.txt" in the "data" directory, starting the location of the executable.
    If the file is not there, it will be created when saving expenses.
*/

bool ExpenseModel::loadExpenses()
{
    QFile file("data/expenses.txt");
    if (!file.exists() || !file.open(QIODevice::ReadOnly | QIODevice::Text)) {
        return false;
    }

    beginResetModel();

    //Clear existing expenses to make way for new ones
    qDeleteAll(m_expenses);
    m_expenses.clear();

    //We'll read new expenses from the file
    QTextStream in(&file);
    while (!in.atEnd()) {
        QString line = in.readLine();
        QStringList fields = line.split('\t');
        
        if (fields.size() >= 4) {
            QDate date = QDate::fromString(fields[0], "dd-MM-yyyy");
            QString item = fields[1];
            double amount = fields[2].toDouble();
            QString category = fields[3];
            
            if (date.isValid() && amount >= 0) {
                addExpense(new Expense(date, item, amount, category, this));
            }
        }
    }

    endResetModel();
    return true;
}