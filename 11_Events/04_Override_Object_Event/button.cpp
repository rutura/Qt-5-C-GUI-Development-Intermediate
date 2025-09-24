#include "button.h"
#include <QEvent>

Button::Button(QWidget *parent)
    : QPushButton{parent}
{}


bool Button::event(QEvent *event)
{
    // Check for specific event types
    if (event->type() == QEvent::MouseButtonPress ||
        event->type() == QEvent::MouseButtonDblClick) {
        qDebug() << "Button: mouse press or double-click detected";
        //return true;
        //return false;
    }

    // Always call the parent implementation for other cases
    return QPushButton::event(event);

}
