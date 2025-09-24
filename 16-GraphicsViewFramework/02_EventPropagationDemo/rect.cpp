#include "rect.h"
#include <QDebug>
#include <QGraphicsSceneMouseEvent>

Rect::Rect()
{

}

void Rect::keyPressEvent(QKeyEvent *event) {

    qDebug() << "Rect Item : Key press event";
    QGraphicsRectItem::keyPressEvent(event);

}
void Rect::mousePressEvent(QGraphicsSceneMouseEvent *event) {

    qDebug() << "Rect Item : Mouse pressed at : " << event->pos();
    QGraphicsRectItem::mousePressEvent(event);

}
