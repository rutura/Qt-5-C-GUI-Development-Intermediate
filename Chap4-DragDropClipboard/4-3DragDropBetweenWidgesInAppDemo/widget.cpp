#include "widget.h"
#include "ui_widget.h"
#include <QSplitter>
#include "container.h"

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);

    QSplitter * splitter = new QSplitter(this);

    splitter->addWidget(new Container(this));

    splitter->addWidget(new Container(this));

    ui->verticalLayout->addWidget(splitter);
}

Widget::~Widget()
{
    delete ui;
}
