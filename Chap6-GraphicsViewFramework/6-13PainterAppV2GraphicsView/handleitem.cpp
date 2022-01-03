#include "handleitem.h"
#include "resizablehandlerect.h"

#include <QGraphicsSceneMouseEvent>

HandleItem::HandleItem(Position position) :
    handlePosition(position)
{
    setFlag(QGraphicsItem::ItemIsMovable);

}

void HandleItem::mouseMoveEvent(QGraphicsSceneMouseEvent *event)
{
    switch (handlePosition) {

    case TopLeft:
    {

        ResizableHandleRect * rectItem = dynamic_cast<ResizableHandleRect *>( parentItem());
        if(rectItem){

            QRectF boundingFrameRect = rectItem->selectorFrameBounds();

            boundingFrameRect.setTop(event->pos().y() + 6);
            boundingFrameRect.setLeft(event->pos().x() +6);

            rectItem->setSelectorFrameBounds(boundingFrameRect.normalized());
        }
    }
        break;

    case TopRight:
    {
        ResizableHandleRect * rectItem = dynamic_cast<ResizableHandleRect *>( parentItem());
        if(rectItem){

            QRectF boundingFrameRect = rectItem->selectorFrameBounds();

            boundingFrameRect.setTop(event->pos().y() + 6);
            boundingFrameRect.setRight(event->pos().x() -6);

            rectItem->setSelectorFrameBounds(boundingFrameRect.normalized());

        }

    }
        break;

    case BottomRight:
    {
        ResizableHandleRect * rectItem = dynamic_cast<ResizableHandleRect *>( parentItem());
        if(rectItem){

            QRectF boundingFrameRect = rectItem->selectorFrameBounds();

            boundingFrameRect.setRight(event->pos().x() - 6);
            boundingFrameRect.setBottom(event->pos().y() -6);

            rectItem->setSelectorFrameBounds(boundingFrameRect.normalized());

        }

    }
        break;

    case BottomLeft:
    {
        ResizableHandleRect * rectItem = dynamic_cast<ResizableHandleRect *>( parentItem());
        if(rectItem){

            QRectF boundingFrameRect = rectItem->selectorFrameBounds();

            boundingFrameRect.setBottom(event->pos().y() -6);
            boundingFrameRect.setLeft(event->pos().x() + 6);

            rectItem->setSelectorFrameBounds(boundingFrameRect.normalized());
        }

    }
        break;

    }

}
