#ifndef RESIZABLESTARITEM_H
#define RESIZABLESTARITEM_H

#include <QGraphicsRectItem>
#include "handleitem.h"

class ResizableStarItem : public QGraphicsRectItem
{

public:
    explicit ResizableStarItem();
    QRectF selectorFrameBounds() const;
    void setSelectorFrameBounds(QRectF boundsRect);

    QRectF boundingRect() const override;

    void paint(QPainter *painter, const QStyleOptionGraphicsItem *option, QWidget *widget) override;

    void drawHandlesIfNecessary();

    QPixmap getPixmap() const;
    void setPixmap(const QPixmap &value);

private:
    void drawHandles();
    QRectF topleftHandleRect;
    QRectF topRightHandleRect;
    QRectF bottomRightHandleRect;
    QRectF bottomLeftHandleRect;

    QList<HandleItem * > handleList;
    bool handlesAddedToScene;

     QPainterPath starFromRect( QRectF mRectF);

};

#endif // RESIZABLESTARITEM_H
