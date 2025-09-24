#ifndef HANDLEITEM_H
#define HANDLEITEM_H

#include <QGraphicsRectItem>

class HandleItem : public QGraphicsRectItem
{
public:

    enum Position
    {
        TopLeft,
        //TopCenter,
        TopRight,
        //RightCenter,
        BottomRight,
       // BottomCenter,
        BottomLeft,
        //LeftCenter
    };
    explicit HandleItem(Position position);


    // QGraphicsItem interface
protected:
    void mouseMoveEvent(QGraphicsSceneMouseEvent *event) override;
private:
    Position handlePosition;
};

#endif // HANDLEITEM_H
