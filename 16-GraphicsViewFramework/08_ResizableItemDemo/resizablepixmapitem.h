#ifndef RESIZABLEPIXMAPITEM_H
#define RESIZABLEPIXMAPITEM_H

#include <QGraphicsRectItem>
#include "handleitem.h"

class ResizablePixmapItem : public QGraphicsRectItem
{

public:
    explicit ResizablePixmapItem(QPixmap pixmap);

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

    QPixmap mPixmap;

};

#endif // RESIZABLEPIXMAPITEM_H
