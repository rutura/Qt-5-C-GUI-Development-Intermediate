#include "keyboardfilter.h"
#include <QKeyEvent>
#include <QDebug>

KeyboardFilter::KeyboardFilter(QObject *parent) : QObject(parent)
{

}

bool KeyboardFilter::eventFilter(QObject *watched, QEvent *event)
{
    if( event->type() == QEvent::KeyPress )
    {
        QKeyEvent *keyEvent = static_cast<QKeyEvent*>( event );
         QString numbers = QString("1234567890");
        if( numbers.indexOf(keyEvent->text()) != -1){
            qDebug() << "Number filtered out";
            return true;//Event handled , no need to notify the destination
        }
    }
    return QObject::eventFilter(watched,event);

}
