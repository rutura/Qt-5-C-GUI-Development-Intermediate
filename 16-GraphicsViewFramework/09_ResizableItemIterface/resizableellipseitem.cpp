#include "resizableellipseitem.h"

ResizableEllipseItem::ResizableEllipseItem()
{
    setOwnerItem(this);
}

QRectF ResizableEllipseItem::boundingRect() const
{
    return selectorFrameBounds();
}

void ResizableEllipseItem::paint(QPainter *painter,
                                 const QStyleOptionGraphicsItem *option,
                                 QWidget *widget)
{
    Q_UNUSED(option);
    Q_UNUSED(widget);

    painter->save();
    painter->setBrush(brush());
    painter->drawEllipse(rect());

    drawHandlesIfNecessary();

    painter->restore();

}

QRectF ResizableEllipseItem::selectorFrameBounds() const
{
    return rect();
}

void ResizableEllipseItem::setSelectorFrameBounds(QRectF boundsRect)
{
    prepareGeometryChange();
    setRect(boundsRect);
    update();

}
