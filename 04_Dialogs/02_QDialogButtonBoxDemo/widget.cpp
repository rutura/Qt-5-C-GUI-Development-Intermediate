#include "widget.h"
#include "ui_widget.h"
#include "infodialog.h"
#include <QDebug>

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);
}

Widget::~Widget()
{
    delete ui;
}

void Widget::on_showInfoButton_clicked()
{
    InfoDialog * dialog = new InfoDialog(this);

    connect(dialog,&InfoDialog::accepted,[=](){
        qDebug() << "Dialog Accepted";
    });

    connect(dialog,&InfoDialog::rejected,[=](){
        qDebug() << "Dialog Rejected";
    });

    dialog->exec();

}
