#include "handleitem.h"
#include "resizablerectitem.h"
#include "resizablepixmapitem.h"
#include "resizablestaritem.h"
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
       // ResizableRectItem * rectItem = dynamic_cast<ResizableRectItem *>( parentItem());
      //  ResizablePixmapItem * rectItem = dynamic_cast<ResizablePixmapItem *>( parentItem());
        ResizablePixmapItem * rectItem = dynamic_cast<ResizablePixmapItem *>( parentItem());
        if(rectItem){

            QRectF boundingFrameRect = rectItem->selectorFrameBounds();

            boundingFrameRect.setTop(event->pos().y());
            boundingFrameRect.setLeft(event->pos().x());

            rectItem->setSelectorFrameBounds(boundingFrameRect);
        }

    }
        break;

    case TopRight:
    {
        ResizableRectItem * rectItem = dynamic_cast<ResizableRectItem *>( parentItem());
        if(rectItem){

            QRectF boundingFrameRect = rectItem->selectorFrameBounds();

            boundingFrameRect.setTop(event->pos().y());
            boundingFrameRect.setRight(event->pos().x());

            rectItem->setSelectorFrameBounds(boundingFrameRect);

        }

    }
        break;

    case BottomRight:
    {
        ResizableRectItem * rectItem = dynamic_cast<ResizableRectItem *>( parentItem());
        if(rectItem){

            QRectF boundingFrameRect = rectItem->selectorFrameBounds();

            boundingFrameRect.setRight(event->pos().x());
            boundingFrameRect.setBottom(event->pos().y());

            rectItem->setSelectorFrameBounds(boundingFrameRect);

        }

    }
        break;

    case BottomLeft:
    {
        ResizableRectItem * rectItem = dynamic_cast<ResizableRectItem *>( parentItem());
        if(rectItem){

            QRectF boundingFrameRect = rectItem->selectorFrameBounds();

            boundingFrameRect.setBottom(event->pos().y());
            boundingFrameRect.setLeft(event->pos().x());

            rectItem->setSelectorFrameBounds(boundingFrameRect);

        }

    }
        break;

    }

}
