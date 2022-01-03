#include "resizablepixmapitem.h"
#include <QPen>
#include <QGraphicsScene>
#include <QPainter>

ResizablePixmapItem::ResizablePixmapItem(QPixmap pixmap) :
    mPixmap(pixmap)
{
     setRect (QRectF(10,10,300,300));
     setOwnerItem(this);
}

QRectF ResizablePixmapItem::selectorFrameBounds() const
{
    return  rect();
}

void ResizablePixmapItem::setSelectorFrameBounds(QRectF boundsRect)
{

    prepareGeometryChange();
    setRect(boundsRect);
    update();


}

QRectF ResizablePixmapItem::boundingRect() const
{
    return selectorFrameBounds();
}

void ResizablePixmapItem::paint(QPainter *painter, const QStyleOptionGraphicsItem *option, QWidget *widget)
{
    Q_UNUSED(option);
    Q_UNUSED(widget);
    painter->save();

//    painter->setBrush(brush());

//    painter->drawRect(rect());
    painter->drawPixmap(boundingRect(),mPixmap,mPixmap.rect());

    drawHandlesIfNecessary();

    painter->restore();
}





QPixmap ResizablePixmapItem::getPixmap() const
{
    return mPixmap;
}

void ResizablePixmapItem::setPixmap(const QPixmap &value)
{
    mPixmap = value;
}
