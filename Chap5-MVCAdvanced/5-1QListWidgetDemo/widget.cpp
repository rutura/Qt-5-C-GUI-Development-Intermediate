#include "widget.h"
#include "ui_widget.h"
#include <QDebug>

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);

    ui->listWidget->setIconSize(QSize(70,70));

    fruitList << "Apple" << "Avocado" << "Banana"
              << "Blueberries" << "Cucumber" << "EggFruit"
              << "Fig" << "Grape" << "Mango" << "Pear"
              << "Pineapple" << "Watermellon";

    /*
    foreach (QString fruit, fruitList) {
        QListWidgetItem * item = new QListWidgetItem(fruit,ui->listWidget);
        QString filename = ":/images/" + fruit.toLower()+  ".png";
        item->setIcon(QIcon(filename));
        item->setData(Qt::UserRole,fruit);
    }
    */

    ui->listWidget->addItems(fruitList);

    for(int i =0 ; i < ui->listWidget->count() ; i++){
        QListWidgetItem * item = ui->listWidget->item(i);
        QString filename = ":/images/" + fruitList[i].toLower()+  ".png";
        item->setIcon(QIcon(filename));
        item->setData(Qt::UserRole,fruitList[i]);
        item->setData(Qt::DisplayRole,fruitList[i]+"Funny");

    }


}

Widget::~Widget()
{
    delete ui;
}

void Widget::on_readDataButton_clicked()
{
    QString fruit = ui->listWidget->currentItem()->data(Qt::DisplayRole).toString();
    qDebug() << " Current fruit : " << fruit;
    qDebug() << "Current index : " << ui->listWidget->currentIndex().row();
}
