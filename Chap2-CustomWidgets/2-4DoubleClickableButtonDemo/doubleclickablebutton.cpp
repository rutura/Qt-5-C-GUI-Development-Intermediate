#include "doubleclickablebutton.h"

DoubleClickableButton::DoubleClickableButton(QWidget *parent) : QPushButton(parent)
{

}

void DoubleClickableButton::mouseDoubleClickEvent(QMouseEvent *event)
{
    emit doubleClicked();
    QPushButton::mouseDoubleClickEvent(event);
}
