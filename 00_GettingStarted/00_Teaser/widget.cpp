#include "widget.h"
#include "./ui_widget.h"
#include <QDebug>

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


void Widget::on_submitButton_clicked()
{
    qDebug() << "Submitting data.." ;
       qDebug() << "Lastname is :" << ui->lastnameLineEdit->text();
       qDebug() << "Firstname is :" << ui->firstnameLineEdit->text();
       qDebug() << "Message is :" << ui->messageTextEdit->toPlainText();
}

