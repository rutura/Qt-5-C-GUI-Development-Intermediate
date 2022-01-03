#include "button.h"
#include <QMouseEvent>
#include <QDebug>

Button::Button(QWidget *parent) : QPushButton(parent)
{

}

void Button::mousePressEvent(QMouseEvent *event)
{
    qDebug() << "Button : Mouse press at " << event->pos() ;
    QPushButton::mouseMoveEvent(event);

}

void Button::mouseReleaseEvent(QMouseEvent *event)
{
    qDebug() << "Button : Mouse release at " << event->pos() ;
    QPushButton::mouseReleaseEvent(event);
}

void Button::mouseMoveEvent(QMouseEvent *event)
{
    qDebug() << "Button : Mouse move at " << event->pos() ;
    QPushButton::mouseMoveEvent(event);
}
