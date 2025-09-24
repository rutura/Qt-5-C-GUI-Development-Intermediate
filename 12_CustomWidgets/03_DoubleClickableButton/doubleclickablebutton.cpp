#include "doubleclickablebutton.h"
#include <QDebug>

DoubleClickableButton::DoubleClickableButton(QWidget *parent)
    : QPushButton{parent}
{}


void DoubleClickableButton::mouseDoubleClickEvent(QMouseEvent *event)
{
    if(event){
        qDebug() << "DoubleClickableButton double click event triggered";
        emit doubleClicked();
        QPushButton::mouseDoubleClickEvent(event);
    }
}
