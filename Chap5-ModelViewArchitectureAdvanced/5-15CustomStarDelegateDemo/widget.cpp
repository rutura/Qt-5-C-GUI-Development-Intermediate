#include "widget.h"
#include "ui_widget.h"
#include "stardelegate.h"

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);

    StarDelegate * delegate = new StarDelegate(this);


    data.append({"Beginning Qt C++ GUI Development","Qt C++ GUI",2});
    data.append({"Qt Quick and QML For Beginners","QML",5});
    data.append({"Qt Quick and QML Intermediate","QML",4});
    data.append({"Qt Quick and QML Advanced","QML",4});
    data.append({"Qt 5 C++ GUI Intermediate","Qt C++ GUI",1});
    data.append({"Qt 5 C++ GUI Advanced","Qt C++ GUI",5});

    ui->tableWidget->setRowCount(data.size());
    ui->tableWidget->setColumnCount(data[0].size());
    ui->tableWidget->setItemDelegateForColumn(2,delegate);


    for( int row = 0 ; row < data.size() ; row++){

        QTableWidgetItem *item0 = new QTableWidgetItem(data[row][0].toString());
        QTableWidgetItem *item1 = new QTableWidgetItem(data[row][1].toString());
        QTableWidgetItem *item2 = new QTableWidgetItem(data[row][2].toString());

        ui->tableWidget->setItem(row, 0, item0);
        ui->tableWidget->setItem(row, 1, item1);
        ui->tableWidget->setItem(row, 2, item2);
    }
}

Widget::~Widget()
{
    delete ui;
}
