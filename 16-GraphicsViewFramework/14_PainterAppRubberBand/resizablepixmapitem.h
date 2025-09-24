#ifndef RESIZABLEPIXMAPITEM_H
#define RESIZABLEPIXMAPITEM_H

#include <QGraphicsRectItem>
#include "resizablehandlerect.h"

class ResizablePixmapItem : public QGraphicsRectItem,public ResizableHandleRect
{

public:
    explicit ResizablePixmapItem(QPixmap pixmap);

    QRectF selectorFrameBounds() const override;
    void setSelectorFrameBounds(QRectF boundsRect) override;

    QRectF boundingRect() const override;

    void paint(QPainter *painter, const QStyleOptionGraphicsItem *option, QWidget *widget) override;

    QPixmap getPixmap() const;
    void setPixmap(const QPixmap &value);

private:
    QPixmap mPixmap;

};

#endif // RESIZABLEPIXMAPITEM_H
