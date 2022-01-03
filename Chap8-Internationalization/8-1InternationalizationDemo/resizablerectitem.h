#ifndef RESIZABLERECTITEM_H
#define RESIZABLERECTITEM_H

#include <QGraphicsRectItem>
#include "resizablehandlerect.h"
#include "painterapptypes.h"


class ResizableRectItem : public QGraphicsRectItem,public ResizableHandleRect
{
public:
    explicit ResizableRectItem();
    enum {Type = ResizableRectType};
    int type() const override;

    QRectF boundingRect() const override;
    void paint(QPainter *painter, const QStyleOptionGraphicsItem *option, QWidget *widget) override;

    // ResizableHandleRect interface

    QRectF selectorFrameBounds() const override;
    void setSelectorFrameBounds(QRectF boundsRect) override;

    // QGraphicsItem interface
protected:
    void dragEnterEvent(QGraphicsSceneDragDropEvent *event) override;
    void dropEvent(QGraphicsSceneDragDropEvent *event) override;
};

//Write
QDataStream &operator<<(QDataStream &out,
                        const ResizableRectItem & mRect);
//Read
QDataStream &operator>>(QDataStream &in, ResizableRectItem & mRectItem);


#endif // RESIZABLERECTITEM_H
