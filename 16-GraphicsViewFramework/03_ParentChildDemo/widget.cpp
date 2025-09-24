#include "widget.h"
#include "ui_widget.h"
#include "imageitem.h"
#include <QGraphicsRectItem>
#include <QGraphicsEllipseItem>

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);

    scene = new QGraphicsScene(this);

    rect1 = new QGraphicsRectItem(-50,-50,100,100);
    rect1->setFlag(QGraphicsItem::ItemIsMovable);
    rect1->setBrush(QBrush(Qt::yellow));


    QGraphicsEllipseItem * ellipse1 = new QGraphicsEllipseItem(-20,-20,40,40);
    ellipse1->setBrush(QBrush(Qt::red));
    ellipse1->setParentItem(rect1);

    QGraphicsEllipseItem * ellipse2 = new QGraphicsEllipseItem(20,20,20,40);
    ellipse2->setBrush(QBrush(Qt::green));
    ellipse2->setParentItem(rect1);


    ImageItem * imageItem = new ImageItem();
    imageItem->setPixmap(QPixmap(":/images/Quick.png"));
    imageItem->setParentItem(rect1);



    scene->addItem(rect1);


    view = new QGraphicsView(this);
    view->setScene(scene);

    ui->verticalLayout->addWidget(view);
}

Widget::~Widget()
{
    delete ui;
}

void Widget::on_showHideButton_clicked()
{
    bool isVisible = rect1->isVisible();
    rect1->setVisible(!isVisible);

}

void Widget::on_removeItem_clicked()
{
    scene->removeItem(rect1);
    delete rect1;

}
