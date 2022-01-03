#include "widget.h"
#include "ui_widget.h"
#include <QDebug>


Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);

    colorList = QColor::colorNames();

    model  = new QStringListModel(colorList,this);


    ui->listView->setModel(model);
}

Widget::~Widget()
{
    delete ui;
}

void Widget::on_listView_clicked(const QModelIndex &index)
{
    QPixmap mPixmap(ui->label->size());
    mPixmap.fill(QColor(model->data(index,Qt::DisplayRole).toString()));
    ui->label->setPixmap(mPixmap);


    qDebug() << "Showing all the colors";
    qDebug() << "--------------------->>> Model Internal String list " << model->stringList();
    qDebug() << "--------------------->>> Original External String list " << colorList;

}
