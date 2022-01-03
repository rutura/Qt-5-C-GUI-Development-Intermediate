#include "filter.h"
#include <QEvent>
#include <QDebug>

Filter::Filter(QObject *parent) : QObject(parent)
{

}

bool Filter::eventFilter(QObject *watched, QEvent *event)
{
    if( event->type() == QEvent::MouseButtonPress
               || event->type() == QEvent::MouseButtonDblClick){

        qDebug() << " Event hijacked in filter";
        //return true; //Event handled no need to notify original destination
        return false;

    }
    return  QObject::eventFilter(watched,event);
}
