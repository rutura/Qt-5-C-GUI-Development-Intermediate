#ifndef RESIZABLESTARITEM_H
#define RESIZABLESTARITEM_H

#include <QGraphicsRectItem>
#include "resizablehandlerect.h"
#include <QGraphicsSceneDragDropEvent>

class ResizableStarItem : public QGraphicsRectItem, public ResizableHandleRect
{

public:
    explicit ResizableStarItem();
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

#endif // RESIZABLESTARITEM_H
