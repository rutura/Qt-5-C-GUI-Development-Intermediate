#include "widget.h"
#include "ui_widget.h"

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);

    filter = new KeyboardFilter(this);

    ui->lineEdit->installEventFilter(filter);
}

Widget::~Widget()
{
    delete ui;
}

void Widget::on_removeFilterButton_clicked()
{
    ui->lineEdit->removeEventFilter(filter);
}
