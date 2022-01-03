#include "parentbutton.h"
#include <QDebug>

ParentButton::ParentButton(QWidget *parent) : QPushButton(parent)
{

}

void ParentButton::mousePressEvent(QMouseEvent *event)
{
    qDebug() << "ParentButton mousePressEvent Called";
    QPushButton::mousePressEvent(event);
}
