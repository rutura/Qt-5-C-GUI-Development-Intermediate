#ifndef RESIZABLEHANDLERECT_H
#define RESIZABLEHANDLERECT_H

#include <QRectF>
#include <QPainter>
#include <QGraphicsItem>
#include "handleitem.h"


class ResizableHandleRect
{
public:
    ResizableHandleRect();
    virtual ~ ResizableHandleRect();

    virtual QRectF selectorFrameBounds() const = 0;
    virtual void setSelectorFrameBounds(QRectF boundsRect) = 0;

    void drawHandlesIfNecessary();

    QPixmap getPixmap() const;
    void setPixmap(const QPixmap &value);

    void setOwnerItem(QGraphicsItem *value);

private:
    void drawHandles();
    QRectF topleftHandleRect;
    QRectF topRightHandleRect;
    QRectF bottomRightHandleRect;
    QRectF bottomLeftHandleRect;

    QList<HandleItem * > handleList;
    bool handlesAddedToScene;
    QGraphicsItem * ownerItem;

};

#endif // RESIZABLEHANDLERECT_H
