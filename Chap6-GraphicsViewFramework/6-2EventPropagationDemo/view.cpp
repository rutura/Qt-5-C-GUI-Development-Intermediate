#include "view.h"
#include <QDebug>
#include <QMouseEvent>

View::View(QWidget *parent) : QGraphicsView(parent)
{

}

void View::mousePressEvent(QMouseEvent *event) {
    qDebug() << "View : MousePressEvent at : " << event->pos();
    QGraphicsView::mousePressEvent(event);

}
void View::keyPressEvent(QKeyEvent *event) {
     qDebug() <<  "View : KeyPressEvent ";
     QGraphicsView::keyPressEvent(event);
}
