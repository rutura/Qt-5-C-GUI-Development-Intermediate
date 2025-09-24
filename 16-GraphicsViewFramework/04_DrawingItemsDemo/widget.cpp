#include "widget.h"
#include "ui_widget.h"
#include <QGraphicsView>
#include <QGraphicsLineItem>
#include <QGraphicsRectItem>
#include <QGraphicsEllipseItem>
#include <QGraphicsPathItem>

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);

    scene = new QGraphicsScene(this);

    scene->setSceneRect(QRectF(-400,-400,800,800));
    scene->addLine(-400,0,400,0);
    scene->addLine(0,-400,0,400);



    QGraphicsView * view = new QGraphicsView(this);
    view->setScene(scene);

    ui->verticalLayout->addWidget(view);
}

Widget::~Widget()
{
    delete ui;
}

void Widget::on_lineButton_clicked()
{
    QLineF line(QPointF(10,10), QPointF(90, 90));
    QGraphicsLineItem * lineItem = new QGraphicsLineItem(line);
    lineItem->setPen(QPen(Qt::red,3));

    QGraphicsRectItem * boundRectItem = new QGraphicsRectItem();
    boundRectItem->setRect(lineItem->boundingRect().adjusted(-10,-10,10,10));
    boundRectItem->setFlag(QGraphicsItem::ItemIsMovable);
    lineItem->setParentItem(boundRectItem);

    scene->addItem(boundRectItem);
}

void Widget::on_ellipseButton_clicked()
{
    QRectF rect(10,10,80,60);
    QGraphicsEllipseItem *ellipseItem = new QGraphicsEllipseItem(rect);
    ellipseItem->setBrush(QBrush(Qt::green));

    QGraphicsRectItem * boundRectItem = new QGraphicsRectItem();
    boundRectItem->setRect(ellipseItem->boundingRect().adjusted(-10,-10,10,10));
    boundRectItem->setFlag(QGraphicsItem::ItemIsMovable);
    ellipseItem->setParentItem(boundRectItem);

    scene->addItem(boundRectItem);

}

void Widget::on_pathButton_clicked()
{
    QPainterPath path;
    path.addEllipse(QRectF(10,10,90,60));
    path.addRect(QRect(20,20,50,50));

    QGraphicsPathItem * painterPathItem = new QGraphicsPathItem(path);
    painterPathItem->setPen(QPen(Qt::black, 5));
    painterPathItem->setBrush(Qt::green);


    QGraphicsRectItem * boundRectItem = new QGraphicsRectItem();
    boundRectItem->setRect(painterPathItem->boundingRect().adjusted(-10,-10,10,10));
    boundRectItem->setFlag(QGraphicsItem::ItemIsMovable);
    painterPathItem->setParentItem(boundRectItem);

    scene->addItem(boundRectItem);
}

void Widget::on_pieButton_clicked()
{
    QPainterPath path(QPointF(60,60));
    path.arcTo(QRect(10,10,80,80), 30, 170);
    path.lineTo(QPointF(60,60));

    QGraphicsPathItem * piePath = new QGraphicsPathItem(path);
    piePath->setPen(QPen(Qt::black, 5));
    piePath->setBrush(Qt::green);


    QGraphicsRectItem * boundRectItem = new QGraphicsRectItem();
    boundRectItem->setRect(piePath->boundingRect().adjusted(-10,-10,10,10));
    boundRectItem->setFlag(QGraphicsItem::ItemIsMovable);
    piePath->setParentItem(boundRectItem);

    scene->addItem(boundRectItem);

}

void Widget::on_imageButton_clicked()
{
    QPixmap pixmap(":/images/LearnQt.png");
    QGraphicsPixmapItem *pixmapItem = new QGraphicsPixmapItem(pixmap.scaled(110,110));

    QGraphicsRectItem * boundRectItem = new QGraphicsRectItem();
    boundRectItem->setRect(pixmapItem->boundingRect().adjusted(-10,-10,10,10));
    boundRectItem->setFlag(QGraphicsItem::ItemIsMovable);
    pixmapItem->setParentItem(boundRectItem);

    scene->addItem(boundRectItem);

}

void Widget::on_starButton_clicked()
{
    QPolygon poly;
    poly << QPoint(0, 85) << QPoint(75, 75)
         << QPoint(100, 10) << QPoint(125, 75)
         << QPoint(200, 85) << QPoint(150, 125)
         << QPoint(160, 190) << QPoint(100, 150)
         << QPoint(40, 190) << QPoint(50, 125)
         << QPoint(0, 85);

    QPainterPath path;
    path.addPolygon(poly);

    QGraphicsPathItem * starPath = new QGraphicsPathItem(path);
    starPath->setPen(QPen(Qt::black, 5));
    starPath->setBrush(Qt::green);


    QGraphicsRectItem * boundRectItem = new QGraphicsRectItem();
    boundRectItem->setRect(starPath->boundingRect().adjusted(-10,-10,10,10));
    boundRectItem->setFlag(QGraphicsItem::ItemIsMovable);
    starPath->setParentItem(boundRectItem);

    scene->addItem(boundRectItem);


}
