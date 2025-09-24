#include "widget.h"
#include "./ui_widget.h"
#include <QDebug>
#include <QMessageBox>

Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
{
    ui->setupUi(this);
}

Widget::~Widget()
{
    delete ui;
}


void Widget::on_pushButton_clicked()
{
    qDebug() << "User clicked on a button";
        QMessageBox::information(this,"Message","You had to click on that button didn't you!",QMessageBox::Ok);
}

