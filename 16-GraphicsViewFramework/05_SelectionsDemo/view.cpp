#include "view.h"
#include <QGraphicsLineItem>
#include <QGraphicsRectItem>
#include <QGraphicsEllipseItem>
#include <QGraphicsPathItem>
#include <QMouseEvent>

View::View(QWidget *parent) : QGraphicsView(parent)
{

}

void View:: mousePressEvent(QMouseEvent *event) {

    switch (currentTool) {

    case Cursor:
    {
        QGraphicsView::mousePressEvent(event);
    }
        break;
    case Line:
    {
       addLine(mapToScene(event->pos()));
    }
        break;
    case Ellipse:{
            addEllipse(mapToScene(event->pos()));
        }break;
        case Path:{
            addPath(mapToScene(event->pos()));
        }break;
        case Pie:{
            addPie(mapToScene(event->pos()));
        }break;
        case Image:{
            addImage(mapToScene(event->pos()));
        }break;
        case Star:{
            addStar(mapToScene(event->pos()));
        }break;
    }

}

void View::addLine(QPointF pos)
{
    QLineF line(QPointF(10,10), QPointF(90, 90));
    QGraphicsLineItem * lineItem = new QGraphicsLineItem(line);
    lineItem->setPen(QPen(Qt::red,3));

    QGraphicsRectItem * boundRectItem = new QGraphicsRectItem();
    boundRectItem->setRect(lineItem->boundingRect().adjusted(-10,-10,10,10));
    boundRectItem->setFlags(QGraphicsItem::ItemIsMovable | QGraphicsItem::ItemIsSelectable);
    lineItem->setParentItem(boundRectItem);

    boundRectItem->setPos(pos);

    scene()->addItem(boundRectItem);

}

void View::addEllipse(QPointF pos)
{
    QRectF rect(10,10,80,60);
    QGraphicsEllipseItem *ellipseItem = new QGraphicsEllipseItem(rect);
    ellipseItem->setBrush(QBrush(Qt::green));

    QGraphicsRectItem * boundRectItem = new QGraphicsRectItem();
    boundRectItem->setRect(ellipseItem->boundingRect().adjusted(-10,-10,10,10));
    boundRectItem->setFlags(QGraphicsItem::ItemIsMovable | QGraphicsItem::ItemIsSelectable);
    ellipseItem->setParentItem(boundRectItem);

    boundRectItem->setPos(pos);
    scene()->addItem(boundRectItem);
}

void View::addPath(QPointF pos)
{
    QPainterPath path;
    path.addEllipse(QRectF(10,10,90,60));
    path.addRect(QRect(20,20,50,50));

    QGraphicsPathItem * painterPathItem = new QGraphicsPathItem(path);
    painterPathItem->setPen(QPen(Qt::black, 5));
    painterPathItem->setBrush(Qt::green);


    QGraphicsRectItem * boundRectItem = new QGraphicsRectItem();
    boundRectItem->setRect(painterPathItem->boundingRect().adjusted(-10,-10,10,10));
    boundRectItem->setFlags(QGraphicsItem::ItemIsMovable | QGraphicsItem::ItemIsSelectable);
    painterPathItem->setParentItem(boundRectItem);

    boundRectItem->setPos(pos);
    scene()->addItem(boundRectItem);
}

void View::addPie(QPointF pos)
{
    QPainterPath path(QPointF(60,60));
    path.arcTo(QRect(10,10,80,80), 30, 170);
    path.lineTo(QPointF(60,60));

    QGraphicsPathItem * piePath = new QGraphicsPathItem(path);
    piePath->setPen(QPen(Qt::black, 5));
    piePath->setBrush(Qt::green);


    QGraphicsRectItem * boundRectItem = new QGraphicsRectItem();
    boundRectItem->setRect(piePath->boundingRect().adjusted(-10,-10,10,10));
    boundRectItem->setFlags(QGraphicsItem::ItemIsMovable | QGraphicsItem::ItemIsSelectable);
    piePath->setParentItem(boundRectItem);
    boundRectItem->setPos(pos);
    scene()->addItem(boundRectItem);
}

void View::addImage(QPointF pos)
{
    QPixmap pixmap(":/images/LearnQt.png");
    QGraphicsPixmapItem *pixmapItem = new QGraphicsPixmapItem(pixmap.scaled(110,110));

    QGraphicsRectItem * boundRectItem = new QGraphicsRectItem();
    boundRectItem->setRect(pixmapItem->boundingRect().adjusted(-10,-10,10,10));
    boundRectItem->setFlags(QGraphicsItem::ItemIsMovable | QGraphicsItem::ItemIsSelectable);
    pixmapItem->setParentItem(boundRectItem);
    boundRectItem->setPos(pos);
    scene()->addItem(boundRectItem);
}

void View::addStar(QPointF pos)
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
    boundRectItem->setFlags(QGraphicsItem::ItemIsMovable | QGraphicsItem::ItemIsSelectable);
    starPath->setParentItem(boundRectItem);
    boundRectItem->setPos(pos);
    scene()->addItem(boundRectItem);
}

View::Tool View::getCurrentTool() const
{
    return currentTool;
}

void View::setCurrentTool(const Tool &value)
{
    currentTool = value;
}
