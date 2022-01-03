#ifndef STROKEITEM_H
#define STROKEITEM_H

#include <QGraphicsItemGroup>
#include "painterapptypes.h"

class StrokeItem : public QGraphicsItemGroup
{

public:
    explicit StrokeItem();
    enum {Type = StrokeType};
    // QGraphicsItem interface
    int type() const override;
};

//Read
QDataStream &operator<<(QDataStream &out,
                        const StrokeItem & mStroke);
//Write
QDataStream &operator>>(QDataStream &in, StrokeItem & mStroke);

#endif // STROKEITEM_H
