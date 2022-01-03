#include "resizablepixmapitem.h"
#include <QPen>
#include <QGraphicsScene>
#include <QPainter>

ResizablePixmapItem::ResizablePixmapItem(QPixmap pixmap) :
    mPixmap(pixmap)
{
    setRect (QRectF(10,10,300,300));
    setOwnerItem(this);
}

int ResizablePixmapItem::type() const
{
    return Type;
}

QRectF ResizablePixmapItem::selectorFrameBounds() const
{
    return  rect();
}

void ResizablePixmapItem::setSelectorFrameBounds(QRectF boundsRect)
{

    prepareGeometryChange();
    setRect(boundsRect);
    update();


}

QRectF ResizablePixmapItem::boundingRect() const
{
    return selectorFrameBounds();
}

void ResizablePixmapItem::paint(QPainter *painter, const QStyleOptionGraphicsItem *option, QWidget *widget)
{
    Q_UNUSED(option);
    Q_UNUSED(widget);
    painter->save();

    //    painter->setBrush(brush());

    //    painter->drawRect(rect());
    painter->drawPixmap(boundingRect(),mPixmap,mPixmap.rect());

    drawHandlesIfNecessary();

    painter->restore();
}





QPixmap ResizablePixmapItem::getPixmap() const
{
    return mPixmap;
}

void ResizablePixmapItem::setPixmap(const QPixmap &value)
{
    mPixmap = value;
}

//Write
QDataStream &operator<<(QDataStream &out, const ResizablePixmapItem &mPixmap)
{
    //Frame Rect
    qreal x = mPixmap.selectorFrameBounds().x();
    qreal y = mPixmap.selectorFrameBounds().y();
    qreal width = mPixmap.selectorFrameBounds().width();
    qreal height = mPixmap.selectorFrameBounds().height();


    qreal posX= mPixmap.scenePos().x();
    qreal posY = mPixmap.scenePos().y();

    QPixmap mPix = mPixmap.getPixmap();

    out << x << y << width << height << posX << posY << mPix;

    return out;
}

//Read
QDataStream &operator>>(QDataStream &in, ResizablePixmapItem &mPixmap)
{
    qreal rectX;
    qreal rectY;
    qreal rectWidth;
    qreal rectHeight;

    qreal posX;
    qreal posY;

    QPixmap mPix;

    in >> rectX >> rectY >> rectWidth >> rectHeight >> posX >> posY >> mPix;

    mPixmap.setPixmap(mPix);
    /*
         *  Note : To keep the size of the original item that you copied,
         *  setSelectorFrameBounds has to come after we set the pixmap, because
         *  the pixmap is at full size and we need the copy to have whatever size
         *  was in the original object.
         * */
    mPixmap.setSelectorFrameBounds(QRectF(rectX,rectY,rectWidth,rectHeight));

    mPixmap.setPos(QPointF(posX,posY) + QPointF(10,10));

    return in;
}
