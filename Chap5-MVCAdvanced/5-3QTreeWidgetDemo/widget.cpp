#include "widget.h"
#include "ui_widget.h"
#include <QDebug>

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);
    ui->treeWidget->setColumnCount(2);

    /*
    QTreeWidgetItem * googleRoot = new QTreeWidgetItem(ui->treeWidget);
    googleRoot->setText(0,"Google Inc");
    googleRoot->setText(1,"Head Quarters");

    QTreeWidgetItem * googleIndia = new QTreeWidgetItem();
    googleIndia->setText(0, "Google India");
    googleIndia->setText(1, "Google India Branch");
    googleRoot->addChild(googleIndia);

    QTreeWidgetItem *googleBangalore = new QTreeWidgetItem();
    googleBangalore->setText(0, "Bangalore");
    googleBangalore->setText(1, "Sales");
    googleIndia->addChild(googleBangalore);

    QTreeWidgetItem *googleMumbai = new QTreeWidgetItem();
    googleMumbai->setText(0, "Mumbai");
    googleMumbai->setText(1, "AI Research");
    googleIndia->addChild(googleMumbai);

    QTreeWidgetItem *googleGhana = new QTreeWidgetItem();
    googleGhana->setText(0, "Google Ghana");
    googleGhana->setText(1, "Google Ghana AI Branch");
    googleRoot->addChild(googleGhana);

    QTreeWidgetItem *googleAkra = new QTreeWidgetItem();
    googleAkra->setText(0, "Akra");
    googleAkra->setText(1, "AI Research");
    googleGhana->addChild(googleAkra);
    */

    QTreeWidgetItem * googleRoot = addRootOrganization("Google Inc","Head Quarters");

    QTreeWidgetItem * googleIndia = addChildOrganization(googleRoot,"Google India","Google India Branch");

    addChildOrganization(googleIndia,"Mumbai","AI Research");

    addChildOrganization(googleIndia,"Bangalore","Sales");

    QTreeWidgetItem * googleGhana = addChildOrganization(googleRoot,"Google Ghana","Ghana Branch");
    addChildOrganization(googleGhana,"Akra","AI");




}

Widget::~Widget()
{
    delete ui;
}

QTreeWidgetItem *Widget::addRootOrganization(QString company, QString purpose)
{
    QTreeWidgetItem * item = new QTreeWidgetItem(ui->treeWidget);
    item->setText(0,company);
    item->setText(1,purpose);
    return item;

}

QTreeWidgetItem *Widget::addChildOrganization(QTreeWidgetItem *parent, QString branch, QString description)
{
    QTreeWidgetItem * item = new QTreeWidgetItem();
    item->setText(0, branch);
    item->setText(1, description);
    parent->addChild(item);
    return  item;

}

void Widget::on_treeWidget_itemClicked(QTreeWidgetItem *item, int column)
{
    qDebug() << " Clicked on :" << item->text(0) << " column : " << column;
}
