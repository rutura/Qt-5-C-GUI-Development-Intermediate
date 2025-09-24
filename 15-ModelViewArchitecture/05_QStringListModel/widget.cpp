#include "widget.h"
#include "./ui_widget.h"
#include <QDebug>

Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
{
    ui->setupUi(this);

    colorList = QColor::colorNames();
    model = new QStringListModel(colorList,this);

    ui->listView->setModel(model);

}

Widget::~Widget()
{
    delete ui;
}

void Widget::on_listView_clicked(const QModelIndex &index)
{
    QPixmap pixmap(ui->label->size());
    auto colorString = model->data(index, Qt::DisplayRole).toString();
    pixmap.fill(QColor(colorString));
    ui->label->setPixmap(pixmap);


    //qDebug() << "Our data: "<<  model->stringList();
    qDebug() << "Our data (current): " << colorString; //This will print the currently selected color
    qDebug() << "Our data: " << colorList;

}

