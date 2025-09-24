#include "button.h"
#include <QDebug>
#include <QMouseEvent>

Button::Button(QWidget *parent)
    : QPushButton{parent}
{}


void Button::mousePressEvent(QMouseEvent *event)
{
    qDebug() << "Button: Mouse press at" << event->position();
    QPushButton::mousePressEvent(event);
}

void Button::mouseReleaseEvent(QMouseEvent *event)
{
    qDebug() << "Button: Mouse release at" << event->position();
    QPushButton::mouseReleaseEvent(event);
}

void Button::mouseMoveEvent(QMouseEvent *event)
{
    qDebug() << "Button: Mouse move at" << event->position();
    QPushButton::mouseMoveEvent(event);
}
