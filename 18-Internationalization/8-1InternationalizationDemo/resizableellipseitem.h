#ifndef RESIZABLEELLIPSEITEM_H
#define RESIZABLEELLIPSEITEM_H

#include <QGraphicsRectItem>
#include "resizablehandlerect.h"
#include "painterapptypes.h"

class ResizableEllipseItem : public QGraphicsRectItem,public ResizableHandleRect
{
public:
    ResizableEllipseItem();
    enum {Type = ResizableEllipseType};
    int type() const override;

    // QGraphicsItem interface
public:
    QRectF boundingRect() const override;
    void paint(QPainter *painter, const QStyleOptionGraphicsItem *option, QWidget *widget) override;

    // ResizableHandleRect interface
public:
    QRectF selectorFrameBounds() const override;
    void setSelectorFrameBounds(QRectF boundsRect) override;


    // QGraphicsItem interface
protected:
    void dragEnterEvent(QGraphicsSceneDragDropEvent *event) override;
    void dropEvent(QGraphicsSceneDragDropEvent *event) override;
};

//Write
QDataStream &operator<<(QDataStream &out,
                        const ResizableEllipseItem & mEllipse);
//Read
QDataStream &operator>>(QDataStream &in, ResizableEllipseItem & mEllipse);

#endif // RESIZABLEELLIPSEITEM_H
