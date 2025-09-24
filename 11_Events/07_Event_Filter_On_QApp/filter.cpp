#include "filter.h"
#include <QEvent>
#include <QDebug>

Filter::Filter(QObject *parent)
    : QObject{parent}
{}


bool Filter::eventFilter(QObject *watched, QEvent *event)
{
    if (event->type() == QEvent::MouseButtonPress ||
        event->type() == QEvent::MouseButtonDblClick) {
        qDebug() << "Event hijacked in filter";
        //return false; // Let the event propagate to its destination
        return true; // We don't want the event to propagate
    }

    return QObject::eventFilter(watched,event);
}
