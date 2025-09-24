#include "widget.h"
#include "ui_widget.h"
#include <QInputDialog>
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

void Widget::on_pushButton_clicked()
{
    /*
    bool ok;
    double d = QInputDialog::getDouble(this, tr("QInputDialog::getDouble()"),
                                            tr("Amount:"), 37.56, -10000, 10000, 2, &ok);
    if (ok)
    {
        qDebug() << "Your double value is " << QString::number(d);
    }
    */

    QStringList items;
          items << tr("Spring") << tr("Summer") << tr("Fall") << tr("Winter");
    bool ok;
    QString item = QInputDialog::getItem(this, tr("QInputDialog::getItem()"),
                                               tr("Season:"), items, 0, false, &ok);
    if (ok && !item.isEmpty())
    {
        qDebug() << "Your chosen item is "<< item;
    }



}
