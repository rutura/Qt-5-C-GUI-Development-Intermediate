#include "widget.h"
#include "./ui_widget.h"
#include "personmodel.h"

Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
{
    ui->setupUi(this);

    //Set up the model
    PersonModel *model = new PersonModel(this);


    //Set the views

    ui->listView->setDragEnabled(true);
    ui->listView->setAcceptDrops(true);
    ui->listView->setModel(model);

    ui->tableView->setDragEnabled(true);
    ui->tableView->setAcceptDrops(true);
    ui->tableView->setModel(model);

    ui->treeView->setDragEnabled(true);
    ui->treeView->setAcceptDrops(true);
    ui->treeView->setModel(model);
}

Widget::~Widget()
{
    delete ui;
}
