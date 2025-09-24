#include "resizablehandlerect.h"
#include <QGraphicsScene>
#include <QDebug>

ResizableHandleRect::ResizableHandleRect()
{

}

ResizableHandleRect::~ResizableHandleRect()
{

}

void ResizableHandleRect::drawHandles()
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
    QPointF topLeftCorner = selectorFrameBounds().topLeft() + QPointF(-12.0,-12.0);
    topleftHandleRect  = QRectF(topLeftCorner,QSize(12,12));
    handleList[0]->setRect(topleftHandleRect);
    if(!handleList.isEmpty() && (!handlesAddedToScene)){
        handleList[0]->setPen(mPen);
        handleList[0]->setBrush(QBrush(Qt::gray));
        ownerItem->scene()->addItem(handleList[0]);
        handleList[0]->setParentItem(ownerItem);

    }

    //Top right
    QPointF topRightCorner = selectorFrameBounds().topRight() + QPointF(0,-12.0);
    topRightHandleRect  = QRectF(topRightCorner,QSize(12,12));
    handleList[1]->setRect(topRightHandleRect);
    if(!handleList.isEmpty() && (!handlesAddedToScene)){
        handleList[1]->setPen(mPen);
        handleList[1]->setBrush(QBrush(Qt::gray));
        ownerItem->scene()->addItem(handleList[1]);
        handleList[1]->setParentItem(ownerItem);
    }

    //Bottom right
    QPointF bottomRightCorner = selectorFrameBounds().bottomRight() + QPointF(0,0);
    bottomRightHandleRect  = QRectF(bottomRightCorner,QSize(12,12));
    handleList[2]->setRect(bottomRightHandleRect);
    if(!handleList.isEmpty() && (!handlesAddedToScene)){
        handleList[2]->setPen(mPen);
        handleList[2]->setBrush(QBrush(Qt::gray));
        ownerItem->scene()->addItem(handleList[2]);
        handleList[2]->setParentItem(ownerItem);
    }

    //Bottom left
    QPointF bottomLeftCorner = selectorFrameBounds().bottomLeft() + QPointF(-12,0);
    bottomLeftHandleRect  = QRectF(bottomLeftCorner,QSize(12,12));
    handleList[3]->setRect(bottomLeftHandleRect);
    if(!handleList.isEmpty() && (!handlesAddedToScene)){
        handleList[3]->setPen(mPen);
        handleList[3]->setBrush(QBrush(Qt::gray));
        ownerItem->scene()->addItem(handleList[3]);
        handleList[3]->setParentItem(ownerItem);
    }

    handlesAddedToScene = true;

}

void ResizableHandleRect::setOwnerItem(QGraphicsItem *value)
{
    ownerItem = value;
}

void ResizableHandleRect::drawHandlesIfNecessary()
{
    if(!ownerItem){
        qWarning() << "ResizableHandleRect : No ownerItem set. Not drawing any\
                      handle. Please call setOwnerItem on your ResizableHandleRect subclass";
                      return;
    }



    if(ownerItem->isSelected()){
        drawHandles();
        handlesAddedToScene = true;
    }else{

        //Remove the handles
        foreach (HandleItem * handleItem, handleList) {
            ownerItem->scene()->removeItem(handleItem);
        }
        qDeleteAll(handleList);
        handleList.clear();
        handlesAddedToScene = false;
    }

}
