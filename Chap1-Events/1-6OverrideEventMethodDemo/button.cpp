#include "button.h"
#include <QEvent>
#include <QDebug>

Button::Button(QWidget *parent) : QPushButton(parent)
{

}

bool Button::event(QEvent *event)
{
    if( (event->type() == QEvent::MouseButtonPress)
                || (event->type() == QEvent::MouseButtonDblClick)){
        qDebug() << "Button : mouse press or doubleclick detected";
      //  return true;
    }
    return  QPushButton::event(event);
}
