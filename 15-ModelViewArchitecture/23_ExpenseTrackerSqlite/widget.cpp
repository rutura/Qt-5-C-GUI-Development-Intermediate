#include "widget.h"
#include "ui_widget.h"
#include <QInputDialog>
#include <QMessageBox>
#include <QSqlError>

Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
{
    ui->setupUi(this);
    model = new ExpenseModel(this);
    
    if (!model->database().isValid()) {
        QMessageBox::critical(this, "Database Error",
                            "Failed to initialize database connection.");
        return;
    }
    
    // Set up proxy model
    proxyModel = new ExpenseProxyModel(this);
    proxyModel->setSourceModel(model);
    proxyModel->setFilterCaseSensitivity(Qt::CaseInsensitive);
    
    // Set up table view
    ui->tableView->setModel(proxyModel);
    ui->tableView->hideColumn(0);  // Hide the ID column
    ui->tableView->resizeColumnsToContents();
    ui->tableView->horizontalHeader()->setSectionResizeMode(QHeaderView::Stretch);
    ui->tableView->setSortingEnabled(true);
    ui->tableView->verticalHeader()->hide(); // Hide row numbers
    
    // Initialize filter column combo box with only visible columns
    ui->filterColumnComboBox->addItems({"All Columns", "Date", "Item", "Amount", "Category"});
}

Widget::~Widget()
{
    delete ui;
}

void Widget::on_addExpenseButton_clicked()
{
    bool ok;
    QString item = QInputDialog::getText(this, "Add Expense",
                                       "Item name:", QLineEdit::Normal,
                                       "Coffee", &ok);
    if (ok && !item.isEmpty()) {
        double amount = QInputDialog::getDouble(this, "Add Expense",
                                              "Amount:", 0.00, 0.00, 1000000.00, 2, &ok);
        if (ok) {
            QString category = QInputDialog::getText(this, "Add Expense",
                                                   "Category:", QLineEdit::Normal,
                                                   "Food", &ok);
            if (ok && !category.isEmpty()) {
                model->addExpense(QDate::currentDate(), item, amount, category);
            }
        }
    }
}

void Widget::on_removeExpenseButton_clicked()
{
    QModelIndex index = ui->tableView->currentIndex();
    if (index.isValid()) {
        model->removeExpense(proxyModel->mapToSource(index));
    }
}

void Widget::on_filterLineEdit_textChanged(const QString &text)
{
    proxyModel->setFilterFixedString(text);
}

void Widget::on_filterColumnComboBox_currentIndexChanged(int index)
{
    proxyModel->setFilterKeyColumn(index == 0 ? -1 : index);
}
