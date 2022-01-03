#include "resizablerectitem.h"
#include <QPen>
#include <QGraphicsScene>
#include <QPainter>
#include <QMimeData>
#include <QGraphicsSceneDragDropEvent>
#include <QDebug>

ResizableRectItem::ResizableRectItem()
{
    setOwnerItem(this);
    setAcceptDrops(true);
}

QRectF ResizableRectItem::boundingRect() const
{
    return selectorFrameBounds();
}

void ResizableRectItem::paint(QPainter *painter,
                              const QStyleOptionGraphicsItem *option,
                              QWidget *widget)
{
    Q_UNUSED(option);
    Q_UNUSED(widget);

    painter->setBrush(brush());
    painter->drawRect(rect());
    drawHandlesIfNecessary();
}

QRectF ResizableRectItem::selectorFrameBounds() const
{
    return rect();
}

void ResizableRectItem::setSelectorFrameBounds(QRectF boundsRect)
{
    prepareGeometryChange();
    setRect(boundsRect);
    update();
}

void ResizableRectItem::dragEnterEvent(QGraphicsSceneDragDropEvent *event)
{
    if(event->mimeData()->hasColor()){
        event->acceptProposedAction();
    }else{
        QGraphicsRectItem::dragEnterEvent(event);
    }
}

void ResizableRectItem::dropEvent(QGraphicsSceneDragDropEvent *event)
{
     if(event->mimeData()->hasColor()){
         setBrush(QBrush(event->mimeData()->colorData().value <QColor>())) ;
          event->acceptProposedAction();
      }else{
          QGraphicsRectItem::dropEvent(event);
      }
}




