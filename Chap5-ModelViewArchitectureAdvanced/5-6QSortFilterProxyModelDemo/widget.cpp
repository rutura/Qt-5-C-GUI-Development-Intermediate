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
    QPixmap mPixmap(ui->label->size());
    mPixmap.fill(QColor(proxyModel->data(index,Qt::DisplayRole).toString()));
    ui->label->setPixmap(mPixmap);


    qDebug() << "Showing all the colors";
    qDebug() << "--------------------->>> Model Internal String list " << model->stringList();
    qDebug() << "--------------------->>> Original External String list " << colorList;

}

void Widget::on_matchStringLineEdit_textChanged(const QString &arg1)
{
    Q_UNUSED(arg1);
    proxyModel->setFilterRegExp(ui->matchStringLineEdit->text());
}
