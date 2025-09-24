#ifndef RESIZABLEPIXMAPITEM_H
#define RESIZABLEPIXMAPITEM_H

#include <QGraphicsRectItem>
#include "resizablehandlerect.h"
#include "painterapptypes.h"

class ResizablePixmapItem : public QGraphicsRectItem,public ResizableHandleRect
{

public:
    explicit ResizablePixmapItem(QPixmap pixmap);
    enum {Type = ResizablePixmapType};
    int type() const override;

    QRectF selectorFrameBounds() const override;
    void setSelectorFrameBounds(QRectF boundsRect) override;

    QRectF boundingRect() const override;

    void paint(QPainter *painter, const QStyleOptionGraphicsItem *option, QWidget *widget) override;

    QPixmap getPixmap() const;
    void setPixmap(const QPixmap &value);

private:
    QPixmap mPixmap;

};
//Write
QDataStream &operator<<(QDataStream &out,
                        const ResizablePixmapItem & mPixmap);

//Read
QDataStream &operator>>(QDataStream &in, ResizablePixmapItem & mPixmap);


#endif // RESIZABLEPIXMAPITEM_H
