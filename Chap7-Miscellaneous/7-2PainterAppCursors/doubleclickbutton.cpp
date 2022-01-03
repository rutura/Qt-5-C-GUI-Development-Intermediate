#include "doubleclickbutton.h"

DoubleclickButton::DoubleclickButton(QWidget *parent) : QPushButton(parent)
{

}

void DoubleclickButton::mouseDoubleClickEvent(QMouseEvent *event)
{
    emit doubleClicked();
    QPushButton::mouseDoubleClickEvent(event);

}
