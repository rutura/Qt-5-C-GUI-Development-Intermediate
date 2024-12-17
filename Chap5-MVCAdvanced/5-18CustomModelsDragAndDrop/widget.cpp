#include "widget.h"
#include "ui_widget.h"
#include "personmodel.h"

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);

    PersonModel * model = new PersonModel(this);

    ui->listView->setModel(model);
    ui->listView->setDragEnabled(true);
    ui->listView->setAcceptDrops(true);

    ui->tableView->setModel(model);
    ui->tableView->setDragEnabled(true);
    ui->tableView->setAcceptDrops(true);

    ui->treeView->setModel(model);
    ui->treeView->setDragEnabled(true);
    ui->treeView->setAcceptDrops(true);
}

Widget::~Widget()
{
    delete ui;
}
