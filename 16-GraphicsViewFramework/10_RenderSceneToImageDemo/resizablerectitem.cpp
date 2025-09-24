#include "resizablerectitem.h"
#include <QPen>
#include <QGraphicsScene>
#include <QPainter>

ResizableRectItem::ResizableRectItem()
{
    setOwnerItem(this);
}

QRectF ResizableRectItem::boundingRect() const
{
    return selectorFrameBounds();
}

void ResizableRectItem::paint(QPainter *painter,
                              const QStyleOptionGraphicsItem *option,
                              QWidget *widget)
{
    Q_UNUSED(option);
    Q_UNUSED(widget);

    painter->setBrush(brush());
    painter->drawRect(rect());
    drawHandlesIfNecessary();
}

QRectF ResizableRectItem::selectorFrameBounds() const
{
    return rect();
}

void ResizableRectItem::setSelectorFrameBounds(QRectF boundsRect)
{
    prepareGeometryChange();
    setRect(boundsRect);
    update();
}


