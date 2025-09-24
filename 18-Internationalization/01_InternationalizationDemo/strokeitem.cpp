#include "strokeitem.h"
#include <QGraphicsLineItem>
#include <QPen>

StrokeItem::StrokeItem()
{

}

int StrokeItem::type() const
{
    return Type;
}

//Write
QDataStream &operator<<(QDataStream &out, const StrokeItem &mStroke)
{
    qreal posX= mStroke.scenePos().x();
    qreal posY = mStroke.scenePos().y();

    //Write position of item
    out << posX << posY;

    //Write line count
    out << mStroke.childItems().count();

    //Write Pen
    foreach (QGraphicsItem * item, mStroke.childItems()) {
        QGraphicsLineItem * lineItem = dynamic_cast<QGraphicsLineItem*>(item);
        if(lineItem){
            out << lineItem->pen();
            break;
        }
    }

    //Write composing lines
    QList<QGraphicsItem*> children = mStroke.childItems();
    foreach (QGraphicsItem * item, children) {
        QGraphicsLineItem * lineItem = dynamic_cast<QGraphicsLineItem*>(item);
        if(lineItem){
            out << lineItem->line();
        }
    }

    return  out;
}


//Read
QDataStream &operator>>(QDataStream &in, StrokeItem &mStroke)
{
    qreal posX;
    qreal posY;

    //Read Pos
    in >> posX >> posY;

    //Read line count
    int lineCount ;
    in >> lineCount;

    //Read Pen
    QPen mPen;
    in >> mPen;

    QLineF mLine;

    for(int i=0; i < lineCount ; i++){
        in >> mLine;
        QGraphicsLineItem * lineItem = new QGraphicsLineItem(mLine);
        lineItem->setPen(mPen);
        mStroke.addToGroup(lineItem);
    }

    mStroke.setPos(QPointF(posX,posY));

    return in;
}
