#include "widget.h"
#include "./ui_widget.h"
#include "personmodel.h"

Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
{
    ui->setupUi(this);

    //Create an object of the model
    PersonModel * model = new PersonModel(this);
    ui->treeView->setModel(model);
}

Widget::~Widget()
{
    delete ui;
}
