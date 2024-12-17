#include "widget.h"
#include "ui_widget.h"
#include <QStandardItemModel>

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);

    QStandardItemModel * model = new QStandardItemModel(this);

    QStandardItem * item0 = new QStandardItem();
    item0->setDragEnabled(true);
    item0->setDropEnabled(true);
    item0->setText("Item0 [CAN DRAG] [CAN DROP]");

    QStandardItem * item1 = new QStandardItem();
    item1->setDragEnabled(true);
    item1->setDropEnabled(false);
    item1->setText("Item1 [CAN DRAG] [CAN'T DROP]");

    QStandardItem * item2 = new QStandardItem();
    item2->setDragEnabled(false);
    item2->setDropEnabled(true);
    item2->setText("item2 [CAN'T DRAG] [CAN DROP]");

    QStandardItem * item3 = new QStandardItem();
    item3->setDragEnabled(false);
    item3->setDropEnabled(false);
    item3->setText("item3 [CAN'T DRAG] [CAN'T DROP]");

    model->appendRow(item0);
    model->appendRow(item1);
    model->appendRow(item2);
    model->appendRow(item3);


    ui->listView->setAcceptDrops(true);
    ui->listView->setDragEnabled(true);
    ui->listView->setModel(model);


    ui->tableView->setAcceptDrops(false);
    ui->tableView->setDragEnabled(true);
    ui->tableView->setModel(model);


    ui->treeView->setAcceptDrops(true);
    ui->treeView->setDragEnabled(false);
    ui->treeView->setModel(model);
}

Widget::~Widget()
{
    delete ui;
}
