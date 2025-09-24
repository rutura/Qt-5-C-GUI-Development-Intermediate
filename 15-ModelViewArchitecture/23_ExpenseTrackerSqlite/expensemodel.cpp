#include "expensemodel.h"
#include <QDateTime>
#include <QDir>
#include <QFile>
#include <QTextStream>
#include <QSqlRecord>
#include <QSqlQuery>
#include <QSqlError>
#include <QStandardPaths>
#include <QDebug>

ExpenseModel::ExpenseModel(QObject *parent)
    : QSqlTableModel(nullptr, QSqlDatabase::addDatabase("QSQLITE", "ExpenseConnection"))
{
    if (!initializeModel()) {
        qWarning() << "Failed to initialize database model";
    }
}

ExpenseModel::~ExpenseModel()
{
    if (database().isOpen()) {
        database().close();
    }
    QString connectionName = database().connectionName();
    QSqlDatabase::removeDatabase(connectionName);
}

/*
    This function initializes our database with the following steps:
        1. Create a data directory if it doesn't exist.
        2. Set the database path to "data/expenses.db".
        3. Open the database connection.
        4. Create the "expenses" table if it doesn't exist.
        5. Set the model to use the "expenses" table.
        6. Set the edit strategy to "OnFieldChange".
        7. Set the header data for all columns.
        8. Load the data from the database into the model.
*/
bool ExpenseModel::initializeModel()
{
    // Create data directory if it doesn't exist
    QDir dataDir = QDir::current();
    if (!dataDir.exists("data")) {
        if (!dataDir.mkpath("data")) {
            qWarning() << "Failed to create data directory";
            return false;
        }
    }

    // Set up the database path
    QString dbPath = dataDir.absoluteFilePath("data/expenses.db");
    qDebug() << "Using database at:" << dbPath;

    // Set the database path
    database().setDatabaseName(dbPath);

    // Try to open the database
    if (!database().open()) {
        qWarning() << "Failed to open database:" << database().lastError().text();
        return false;
    }

    // Create table if it doesn't exist
    if (!createTable()) {
        qWarning() << "Failed to create table:" << database().lastError().text();
        return false;
    }

    // Configure the model
    setTable("expenses");
    setEditStrategy(QSqlTableModel::OnFieldChange);

    // Load the data
    if (!select()) {
        qWarning() << "Failed to select data:" << lastError().text();
        return false;
    }

    qDebug() << "Successfully initialized database with" << rowCount() << "rows";
    return true;
}

bool ExpenseModel::createTable()
{
    QSqlQuery query(database());
    bool success = query.exec(
        "CREATE TABLE IF NOT EXISTS expenses ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT,"
        "date DATE NOT NULL,"
        "item TEXT NOT NULL,"
        "amount REAL NOT NULL,"
        "category TEXT NOT NULL"
        ")"
    );

    if (!success) {
        qWarning() << "Create table error:" << query.lastError().text();
    }
    return success;
}

QVariant ExpenseModel::data(const QModelIndex &index, int role) const
{
    if (!index.isValid() || (role != Qt::DisplayRole && role != Qt::EditRole))
        return QSqlTableModel::data(index, role);

    QVariant value = QSqlTableModel::data(index, role);
    
    if (role == Qt::DisplayRole) {
        if (index.column() == 1)
            return value.toDate().toString("dd-MM-yyyy");
        if (index.column() == 3)
            return QString::number(value.toDouble(), 'f', 2);
    }
    else if (role == Qt::EditRole && index.column() == 1) {
        return value.toDate();
    }
    
    return value;
}

bool ExpenseModel::setData(const QModelIndex &index, const QVariant &value, int role)
{
    if (!index.isValid() || role != Qt::EditRole)
        return false;

    if (index.column() == 1) {
        QDate date = value.toDate();
        if (!date.isValid()) return false;
    }
    else if (index.column() == 3) {
        double amount = value.toDouble();
        if (amount < 0) return false;
    }

    // Submit changes to the database
    bool success = QSqlTableModel::setData(index, value, role);
    
    // Save changes and refresh the model if initial update was successful
    if (success) {
        success = submitAll();
        if (success) {
            success = select();
        }
    }
    
    return success;
}

QVariant ExpenseModel::headerData(int section, Qt::Orientation orientation, int role) const
{
    if (role != Qt::DisplayRole)
        return QVariant();

    if (orientation == Qt::Horizontal) {
        switch (section) {
            case 0: return tr("ID");
            case 1: return tr("Date");
            case 2: return tr("Item");
            case 3: return tr("Amount");
            case 4: return tr("Category");
            default: return QVariant();
        }
    }
    return QSqlTableModel::headerData(section, orientation, role);
}

Qt::ItemFlags ExpenseModel::flags(const QModelIndex &index) const
{
    if (!index.isValid())
        return Qt::NoItemFlags;

    return Qt::ItemIsEnabled | Qt::ItemIsSelectable | Qt::ItemIsEditable;
}

void ExpenseModel::addExpense(const QDate &date, const QString &item, double amount, const QString &category)
{
    QSqlRecord record = this->record(); // Create a new record
    record.setValue("date", date);
    record.setValue("item", item);
    record.setValue("amount", amount);
    record.setValue("category", category);
    
    if (!insertRecord(-1, record)) {
        qWarning() << "Failed to add expense:" << lastError().text();
    } else {
        submitAll();
        select(); // Refresh the view
        qDebug() << "Added expense:" << date << item << amount << category;
        qDebug() << "Current row count:" << rowCount();
    }
}

void ExpenseModel::removeExpense(const QModelIndex &index)
{
    if (!index.isValid())
        return;

    if (!removeRow(index.row())) {
        qWarning() << "Failed to remove expense:" << lastError().text();
    } else {
        submitAll();
        select(); // Refresh the view
    }
}