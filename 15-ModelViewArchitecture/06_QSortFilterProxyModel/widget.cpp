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


    proxyModel = new QSortFilterProxyModel(this);
    proxyModel->setSourceModel(model);

    ui->listView->setModel(proxyModel);

}

Widget::~Widget()
{
    delete ui;
}

void Widget::on_listView_clicked(const QModelIndex &index)
{
    QPixmap pixmap(ui->label->size());
    auto colorString = proxyModel->data(index, Qt::DisplayRole).toString();
    pixmap.fill(QColor(colorString));
    ui->label->setPixmap(pixmap);


    //qDebug() << "Our data: "<<  model->stringList();
    qDebug() << "Our data (current): " << colorString; //This will print the currently selected color
    qDebug() << "Our data: " << colorList;

}


void Widget::on_lineEdit_textChanged(const QString &arg1)
{
    proxyModel->setFilterRegularExpression(arg1);
}

