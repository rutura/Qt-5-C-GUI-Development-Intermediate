#include "resizablestaritem.h"
#include <QPen>
#include <QGraphicsScene>
#include <QPainter>
#include <QMimeData>

ResizableStarItem::ResizableStarItem()
{
    setRect (QRectF(10,10,300,300));
    setOwnerItem(this);
    setAcceptDrops(true);
}

int ResizableStarItem::type() const
{
    return  Type;
}

QRectF ResizableStarItem::selectorFrameBounds() const
{
    return rect();
}

void ResizableStarItem::setSelectorFrameBounds(QRectF boundsRect)
{

    prepareGeometryChange();
    setRect(boundsRect);
    update();
}

QRectF ResizableStarItem::boundingRect() const
{
    return selectorFrameBounds();
}

void ResizableStarItem::paint(QPainter *painter, const QStyleOptionGraphicsItem *option, QWidget *widget)
{
    Q_UNUSED(option);
    Q_UNUSED(widget);
    painter->save();

    painter->setPen(pen());
    painter->setBrush(brush());

    painter->drawPath(starFromRect(boundingRect()));

    drawHandlesIfNecessary();

    painter->restore();
}



QPainterPath ResizableStarItem::starFromRect(QRectF mRectF)
{

    QPolygonF poly;

    //1
    poly << mRectF.topLeft() + QPointF(mRectF.width()/2,0.0);
    //2
    poly << mRectF.topLeft() + QPointF(mRectF.width() * 0.7, mRectF.height() * 0.3);
    //3
    poly << mRectF.topLeft() + QPointF(mRectF.width() , mRectF.height() * 0.5);
    //4 : mirror 2
    poly << mRectF.topLeft() + QPointF(mRectF.width() * 0.7, mRectF.height() * 0.7);
    //5
    poly << mRectF.topLeft() + QPointF(mRectF.width() * 0.75, mRectF.height());
    //6
    poly << mRectF.topLeft() + QPointF(mRectF.width() * 0.5 , mRectF.height() * 0.75);
    //7
    poly << mRectF.topLeft() + QPointF(mRectF.width() *0.25 , mRectF.height());
    //8
    poly << mRectF.topLeft() + QPointF(mRectF.width() * 0.3, mRectF.height() *0.7);
    //9
    poly << mRectF.topLeft() + QPointF(0,mRectF.height() * 0.5);
    //10
    poly << mRectF.topLeft() + QPointF(mRectF.width() * 0.3 , mRectF.height() * 0.3);
    //1
    poly << mRectF.topLeft() + QPointF(mRectF.width()/2,0.0);


    QPainterPath path;
    path.addPolygon(poly);
    return  path;


}

void ResizableStarItem::dragEnterEvent(QGraphicsSceneDragDropEvent *event)
{
    if(event->mimeData()->hasColor()){
        event->acceptProposedAction();
    }else{
        QGraphicsRectItem::dragEnterEvent(event);
    }

}

void ResizableStarItem::dropEvent(QGraphicsSceneDragDropEvent *event)
{
    if(event->mimeData()->hasColor()){
        setBrush(QBrush(event->mimeData()->colorData().value <QColor>())) ;
        event->acceptProposedAction();
    }else{
        QGraphicsRectItem::dropEvent(event);
    }

}
//Write
QDataStream &operator<<(QDataStream &out, const ResizableStarItem &mStar)
{
    //Frame Rect
    qreal x = mStar.selectorFrameBounds().x();
    qreal y = mStar.selectorFrameBounds().y();
    qreal width = mStar.selectorFrameBounds().width();
    qreal height = mStar.selectorFrameBounds().height();


    qreal posX= mStar.scenePos().x();
    qreal posY = mStar.scenePos().y();

    //Brush Color
    QColor brushColor = mStar.brush().color();

    //Pen color and width
    QPen mPen = mStar.pen();

    out << x << y << width << height << posX << posY
        << brushColor.red() << brushColor.green() << brushColor.blue()
        << mPen.color().red() << mPen.color().green() << mPen.color().green()
        << static_cast<int>(mPen.style()) << mPen.width();

    return out;
}

//Read
QDataStream &operator>>(QDataStream &in, ResizableStarItem &mStar)
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

    in >> rectX >> rectY >> rectWidth >> rectHeight >> posX >> posY
            >>brushRed >> brushGreen >> brushBlue
            >>penRed >> penGreen >>penBlue
            >>penStyle >>penWidth;

    mStar.setSelectorFrameBounds(QRectF(rectX,rectY,rectWidth,rectHeight));
    mStar.setBrush(QBrush(QColor(brushRed,brushGreen,brushBlue)));

    QPen mPen;
    mPen.setColor(QColor(penRed,penGreen,penBlue));
    //Figure out how to serialize the style here.
    mPen.setStyle(static_cast<Qt::PenStyle>(penStyle));
    mPen.setWidth(penWidth);
    mStar.setPen(mPen);

    mStar.setPos(QPointF(posX,posY));

    return in;
}
