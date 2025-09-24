#ifndef RESIZABLESTARITEM_H
#define RESIZABLESTARITEM_H

#include <QGraphicsRectItem>
#include "resizablehandlerect.h"
#include "painterapptypes.h"
#include <QGraphicsSceneDragDropEvent>

class ResizableStarItem : public QGraphicsRectItem, public ResizableHandleRect
{

public:
    explicit ResizableStarItem();
    enum {Type = ResizableStarType};
    int type() const override;


    QRectF selectorFrameBounds() const override;
    void setSelectorFrameBounds(QRectF boundsRect) override;

    QRectF boundingRect() const override;

    void paint(QPainter *painter, const QStyleOptionGraphicsItem *option, QWidget *widget) override;

private:


     QPainterPath starFromRect( QRectF mRectF);


     // QGraphicsItem interface
protected:
     void dragEnterEvent(QGraphicsSceneDragDropEvent *event) override;
     void dropEvent(QGraphicsSceneDragDropEvent *event) override;
};

//Write
QDataStream &operator<<(QDataStream &out,
                        const ResizableStarItem & mStar);

//Read
QDataStream &operator>>(QDataStream &in, ResizableStarItem & mStar);


#endif // RESIZABLESTARITEM_H
