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

int ResizableRectItem::type() const
{
    return  Type;
}

QRectF ResizableRectItem::boundingRect() const
{
 return selectorFrameBounds().adjusted(-pen().width(),-pen().width(),
                                       pen().width(),pen().width());
}

void ResizableRectItem::paint(QPainter *painter,
                              const QStyleOptionGraphicsItem *option,
                              QWidget *widget)
{
    Q_UNUSED(option);
    Q_UNUSED(widget);

    painter->setPen(pen());
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




//Write
QDataStream &operator<<(QDataStream &out, const ResizableRectItem &mRect)
{

    //Frame Rect
    qreal x = mRect.selectorFrameBounds().x();
    qreal y = mRect.selectorFrameBounds().y();
    qreal width = mRect.selectorFrameBounds().width();
    qreal height = mRect.selectorFrameBounds().height();

    //Position
    qreal posX= mRect.scenePos().x();
    qreal posY = mRect.scenePos().y();

    //Pen and Brush
    //Brush Color
    QColor brushColor = mRect.brush().color();

    //Pen color and width
    QPen mPen = mRect.pen();

    out << x << y << width << height << posX << posY <<
           brushColor.red() << brushColor.green() << brushColor.blue() <<
           mPen.color().red() << mPen.color().green() << mPen.color().blue() <<
           static_cast<int>(mPen.style()) << mPen.width();

    return  out;


}


//Read
QDataStream &operator>>(QDataStream &in, ResizableRectItem &mRectItem)
{

    qreal rectX;
    qreal rectY;
    qreal rectWidth;
    qreal rectHeight;

    qreal posX;
    qreal posY;

    int brushRed;
    int brushGreen;
    int brushBlue;

    int penRed;
    int penGreen;
    int penBlue;

    int penStyle;
    int penWidth;

    in >> rectX >> rectY >> rectWidth >> rectHeight >> posX >> posY >>
            brushRed >> brushGreen >> brushBlue >>
            penRed >> penGreen >> penBlue >>
            penStyle >> penWidth;

    mRectItem.setSelectorFrameBounds(QRectF(rectX,rectY,rectWidth,rectHeight));
    mRectItem.setBrush(QBrush(QColor(brushRed,brushGreen,brushBlue)));

    QPen mPen;
    mPen.setColor(QColor(penRed,penGreen,penBlue));
    mPen.setStyle(static_cast<Qt::PenStyle>(penStyle));
    mPen.setWidth(penWidth);
    mRectItem.setPen(mPen);

    mRectItem.setPos(QPointF(posX,posY));

    return  in;
}
