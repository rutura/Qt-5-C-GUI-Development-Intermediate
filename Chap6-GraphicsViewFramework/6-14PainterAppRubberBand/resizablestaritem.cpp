#include "resizablestaritem.h"
#include <QPen>
#include <QGraphicsScene>
#include <QPainter>
#include <QMimeData>

ResizableStarItem::ResizableStarItem()
{
     setRect (QRectF(10,10,300,300));
     setOwnerItem(this);
     setAcceptDrops(true);
}

QRectF ResizableStarItem::selectorFrameBounds() const
{
     return rect();
}

void ResizableStarItem::setSelectorFrameBounds(QRectF boundsRect)
{

    prepareGeometryChange();
    setRect(boundsRect);
    update();
}

QRectF ResizableStarItem::boundingRect() const
{
    return selectorFrameBounds();
}

void ResizableStarItem::paint(QPainter *painter, const QStyleOptionGraphicsItem *option, QWidget *widget)
{
    Q_UNUSED(option);
    Q_UNUSED(widget);
    painter->save();

    painter->setBrush(brush());

    painter->drawPath(starFromRect(boundingRect()));

    drawHandlesIfNecessary();

    painter->restore();
}



QPainterPath ResizableStarItem::starFromRect(QRectF mRectF)
{

    QPolygonF poly;

        //1
        poly << mRectF.topLeft() + QPointF(mRectF.width()/2,0.0);
        //2
        poly << mRectF.topLeft() + QPointF(mRectF.width() * 0.7, mRectF.height() * 0.3);
        //3
        poly << mRectF.topLeft() + QPointF(mRectF.width() , mRectF.height() * 0.5);
        //4 : mirror 2
        poly << mRectF.topLeft() + QPointF(mRectF.width() * 0.7, mRectF.height() * 0.7);
        //5
        poly << mRectF.topLeft() + QPointF(mRectF.width() * 0.75, mRectF.height());
        //6
        poly << mRectF.topLeft() + QPointF(mRectF.width() * 0.5 , mRectF.height() * 0.75);
        //7
        poly << mRectF.topLeft() + QPointF(mRectF.width() *0.25 , mRectF.height());
        //8
        poly << mRectF.topLeft() + QPointF(mRectF.width() * 0.3, mRectF.height() *0.7);
        //9
        poly << mRectF.topLeft() + QPointF(0,mRectF.height() * 0.5);
        //10
        poly << mRectF.topLeft() + QPointF(mRectF.width() * 0.3 , mRectF.height() * 0.3);
        //1
        poly << mRectF.topLeft() + QPointF(mRectF.width()/2,0.0);


        QPainterPath path;
        path.addPolygon(poly);
        return  path;


}

void ResizableStarItem::dragEnterEvent(QGraphicsSceneDragDropEvent *event)
{
    if(event->mimeData()->hasColor()){
        event->acceptProposedAction();
    }else{
        QGraphicsRectItem::dragEnterEvent(event);
    }

}

void ResizableStarItem::dropEvent(QGraphicsSceneDragDropEvent *event)
{
    if(event->mimeData()->hasColor()){
        setBrush(QBrush(event->mimeData()->colorData().value <QColor>())) ;
         event->acceptProposedAction();
     }else{
         QGraphicsRectItem::dropEvent(event);
     }

}
