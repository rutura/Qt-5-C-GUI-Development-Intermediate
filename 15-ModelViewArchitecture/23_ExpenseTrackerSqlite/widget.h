#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>
#include "expensemodel.h"
#include "expenseproxymodel.h"

namespace Ui {
class Widget;
}

class Widget : public QWidget
{
    Q_OBJECT

public:
    explicit Widget(QWidget *parent = nullptr);
    ~Widget();

private slots:
    void on_addExpenseButton_clicked();
    void on_removeExpenseButton_clicked();
    void on_filterLineEdit_textChanged(const QString &text);
    void on_filterColumnComboBox_currentIndexChanged(int index);

private:
    Ui::Widget *ui;
    ExpenseModel *model;
    ExpenseProxyModel *proxyModel;
};

#endif // WIDGET_H
