#include "widget.h"
#include "./ui_widget.h"
#include <QDebug>

Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
{
    ui->setupUi(this);

    fruitList << "Apple"  << "Avocado" << "Banana"
              << "Blueberries" << "Cucumber" << "EggFruit"
              << "Fig" << "Grape" << "Mango" << "Pear"
              << "Pineapple" << "Watermellon";

    foreach (QString fruit, fruitList) {
        QListWidgetItem * item = new QListWidgetItem(fruit, ui->listWidget);
        QString filename = ":/images/" + fruit.toLower() + ".png";
        item->setIcon(QIcon(filename));
        item->setData(Qt::DisplayRole,fruit);

    }

    //ui->listWidget->addItems(fruitList);
}

Widget::~Widget()
{
    delete ui;
}

void Widget::on_pushButton_clicked()
{
    QString data = ui->listWidget->currentItem()->data(Qt::DisplayRole).toString();
    qDebug() << "Current item: " << data;
    qDebug() << "Current index: " << ui->listWidget->currentIndex().row();
}

