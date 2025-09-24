#include "widget.h"
#include "./ui_widget.h"
#include "datetimewidget.h"

Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
{
    ui->setupUi(this);


    auto* dateTimeWidget = new DateTimeWidget(this);
    ui->verticalLayout->addWidget(dateTimeWidget);
}

Widget::~Widget()
{
    delete ui;
}
