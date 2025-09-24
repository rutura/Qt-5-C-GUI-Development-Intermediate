#ifndef RECT_H
#define RECT_H

#include <QGraphicsRectItem>

class Rect : public QGraphicsRectItem
{    
public:
    explicit Rect();

    // QGraphicsItem interface
protected:
    void keyPressEvent(QKeyEvent *event) override;
};

#endif // RECT_H
