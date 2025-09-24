#include "keyboardfilter.h"
#include <QKeyEvent>

KeyboardFilter::KeyboardFilter(QObject *parent)
    : QObject{parent}
{}


bool KeyboardFilter::eventFilter(QObject *watched, QEvent *event)
{
    if (!watched || !event) {
        return false;
    }

    //Filter out key press events
    if (event->type() == QEvent::KeyPress){
        const auto* keyEvent = static_cast<const QKeyEvent*>(event);
        if (keyEvent && QString(ALLOWED_NUMBERS).contains(keyEvent->text())) {
            qDebug() << "Number filtered out:" << keyEvent->text();
            return true; // Event handled, no need to notify the destination
        }

    }

    //Call the parent implementation
    return QObject::eventFilter(watched,event);

}
