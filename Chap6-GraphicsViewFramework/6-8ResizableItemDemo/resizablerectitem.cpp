#include "resizablerectitem.h"
#include <QPen>
#include <QGraphicsScene>
#include <QPainter>

ResizableRectItem::ResizableRectItem() : handlesAddedToScene(false)
{

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

QRectF ResizableRectItem::boundingRect() const
{
    return selectorFrameBounds();
}

void ResizableRectItem::paint(QPainter *painter, const QStyleOptionGraphicsItem *option,
                              QWidget *widget)
{
    Q_UNUSED(option);
    Q_UNUSED(widget);
    painter->save();

    painter->setBrush(brush());

    painter->drawRect(rect());

    drawHandlesIfNecessary();

    painter->restore();
}

void ResizableRectItem::drawHandlesIfNecessary()
{
    if(isSelected()){
        drawHandles();
        handlesAddedToScene = true;
    }else{
        //Remove the handles
        foreach (HandleItem * handleItem, handleList) {
            scene()->removeItem(handleItem);
        }
        qDeleteAll(handleList);
        handleList.clear();
        handlesAddedToScene = false;
    }

}

void ResizableRectItem::drawHandles()
{
    //Populate handles in list
    if(handleList.count() == 0){
        handleList.append(new HandleItem(HandleItem::TopLeft));
        handleList.append(new HandleItem(HandleItem::TopRight));
        handleList.append(new HandleItem(HandleItem::BottomRight));
        handleList.append(new HandleItem(HandleItem::BottomLeft));
    }


    //Set up pen
    QPen mPen;
    mPen.setWidth(2);
    mPen.setColor(Qt::black);

    //Top left handle
    QPointF topLeftCorner = boundingRect().topLeft() + QPointF(-12.0,-12.0);
    topleftHandleRect  = QRectF(topLeftCorner,QSize(12,12));
    handleList[0]->setRect(topleftHandleRect);
    if(!handleList.isEmpty() && (!handlesAddedToScene)){
        handleList[0]->setPen(mPen);
        handleList[0]->setBrush(QBrush(Qt::gray));
        scene()->addItem(handleList[0]);
        handleList[0]->setParentItem(this);

    }

    //Top right
    QPointF topRightCorner = boundingRect().topRight() + QPointF(0,-12.0);
    topRightHandleRect  = QRectF(topRightCorner,QSize(12,12));
    handleList[1]->setRect(topRightHandleRect);
    if(!handleList.isEmpty() && (!handlesAddedToScene)){
        handleList[1]->setPen(mPen);
        handleList[1]->setBrush(QBrush(Qt::gray));
        scene()->addItem(handleList[1]);
        handleList[1]->setParentItem(this);
    }

    //Bottom right
    QPointF bottomRightCorner = boundingRect().bottomRight() + QPointF(0,0);
    bottomRightHandleRect  = QRectF(bottomRightCorner,QSize(12,12));
    handleList[2]->setRect(bottomRightHandleRect);
    if(!handleList.isEmpty() && (!handlesAddedToScene)){
        handleList[2]->setPen(mPen);
        handleList[2]->setBrush(QBrush(Qt::gray));
        scene()->addItem(handleList[2]);
        handleList[2]->setParentItem(this);
    }

    //Bottom left
    QPointF bottomLeftCorner = boundingRect().bottomLeft() + QPointF(-12,0);
    bottomLeftHandleRect  = QRectF(bottomLeftCorner,QSize(12,12));
    handleList[3]->setRect(bottomLeftHandleRect);
    if(!handleList.isEmpty() && (!handlesAddedToScene)){
        handleList[3]->setPen(mPen);
        handleList[3]->setBrush(QBrush(Qt::gray));
        scene()->addItem(handleList[3]);
        handleList[3]->setParentItem(this);
    }

    handlesAddedToScene = true;

}
