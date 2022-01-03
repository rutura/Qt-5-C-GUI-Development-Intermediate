#ifndef RESIZABLERECTITEM_H
#define RESIZABLERECTITEM_H

#include <QGraphicsRectItem>
#include "handleitem.h"

class ResizableRectItem : public QGraphicsRectItem
{

public:
    explicit ResizableRectItem();

    QRectF selectorFrameBounds() const;
    void setSelectorFrameBounds(QRectF boundsRect);

    QRectF boundingRect() const override;

    void paint(QPainter *painter, const QStyleOptionGraphicsItem *option, QWidget *widget) override;

    void drawHandlesIfNecessary();

private:
    void drawHandles();
    QRectF topleftHandleRect;
    QRectF topRightHandleRect;
    QRectF bottomRightHandleRect;
    QRectF bottomLeftHandleRect;

    QList<HandleItem * > handleList;
    bool handlesAddedToScene;
};

#endif // RESIZABLERECTITEM_H
