#include "resizableellipseitem.h"
#include <QGraphicsSceneDragDropEvent>
#include <QMimeData>

ResizableEllipseItem::ResizableEllipseItem()
{
    setOwnerItem(this);
    setAcceptDrops(true);
}

int ResizableEllipseItem::type() const
{
    return Type;
}

QRectF ResizableEllipseItem::boundingRect() const
{
    return selectorFrameBounds();
}

void ResizableEllipseItem::paint(QPainter *painter,
                                 const QStyleOptionGraphicsItem *option,
                                 QWidget *widget)
{
    Q_UNUSED(option);
    Q_UNUSED(widget);

    painter->save();
    painter->setPen(pen());
    painter->setBrush(brush());
    painter->drawEllipse(rect());

    drawHandlesIfNecessary();

    painter->restore();

}

QRectF ResizableEllipseItem::selectorFrameBounds() const
{
    return rect();
}

void ResizableEllipseItem::setSelectorFrameBounds(QRectF boundsRect)
{
    prepareGeometryChange();
    setRect(boundsRect);
    update();

}

void ResizableEllipseItem::dragEnterEvent(QGraphicsSceneDragDropEvent *event)
{
    if(event->mimeData()->hasColor()){
        event->acceptProposedAction();
    }else{
        QGraphicsRectItem::dragEnterEvent(event);
    }

}

void ResizableEllipseItem::dropEvent(QGraphicsSceneDragDropEvent *event)
{
    if(event->mimeData()->hasColor()){
        setBrush(QBrush(event->mimeData()->colorData().value <QColor>())) ;
        event->acceptProposedAction();
    }else{
        QGraphicsRectItem::dropEvent(event);
    }
}


//Write
QDataStream &operator<<(QDataStream &out, const ResizableEllipseItem &mEllipse)
{
    //Frame Rect
    qreal x = mEllipse.selectorFrameBounds().x();
    qreal y = mEllipse.selectorFrameBounds().y();
    qreal width = mEllipse.selectorFrameBounds().width();
    qreal height = mEllipse.selectorFrameBounds().height();

    qreal posX= mEllipse.scenePos().x();
    qreal posY = mEllipse.scenePos().y();

    //Brush Color
    QColor brushColor = mEllipse.brush().color();

    //Pen color and width
    QPen mPen = mEllipse.pen();

    out << x << y << width << height << posX << posY
        << brushColor.red() << brushColor.green() << brushColor.blue()
        << mPen.color().red() << mPen.color().green() << mPen.color().green()
        << static_cast<int>(mPen.style()) << mPen.width();

    return out;

}


//Read
QDataStream &operator>>(QDataStream &in, ResizableEllipseItem &mEllipse)
{
    qreal rectX;qreal rectY;qreal rectWidth;qreal rectHeight;
    qreal posX;qreal posY;
    int brushRed;int brushGreen;int brushBlue;
    int penRed;int penGreen;int penBlue;int penStyle;int penWidth;


    in >> rectX >> rectY >> rectWidth >> rectHeight >> posX >> posY
            >>brushRed >> brushGreen >> brushBlue
            >>penRed >> penGreen >>penBlue
            >> penStyle >>penWidth;

    mEllipse.setSelectorFrameBounds(QRectF(rectX,rectY,rectWidth,rectHeight));
    mEllipse.setBrush(QBrush(QColor(brushRed,brushGreen,brushBlue)));

    QPen mPen;
    mPen.setColor(QColor(penRed,penGreen,penBlue));
    // Figure out how to serialize the style here.
    mPen.setStyle(static_cast<Qt::PenStyle>(penStyle));
    mPen.setWidth(penWidth);
    mEllipse.setPen(mPen);

    mEllipse.setPos(QPointF(posX,posY) + QPointF(10,10));

    return in;
}
