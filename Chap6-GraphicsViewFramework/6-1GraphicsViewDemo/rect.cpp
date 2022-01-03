#include "rect.h"
#include <QDebug>
#include <QKeyEvent>

Rect::Rect()
{

}

void Rect::keyPressEvent(QKeyEvent *event)
{
    qDebug() << "Keypress event triggered for rect item";
    if( event->key() == Qt::Key_Left){
        //Move left
        moveBy(-20,0);
    }
    if( event->key() == Qt::Key_Right){
        //Move Right
        moveBy(20,0);
    }
    if( event->key() == Qt::Key_Up){
        //Move UP
        moveBy(0,-20);
    }
    if( event->key() == Qt::Key_Down){
        //Move DOWN
        moveBy(0,20);
    }

}
