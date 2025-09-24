#include "view.h"
#include <QMouseEvent>
#include <QGraphicsRectItem>
#include <QDebug>

View::View(QWidget *parent) : QGraphicsView(parent)
{

}

void View::mousePressEvent(QMouseEvent *event)
{
    qDebug() << "Mouse pressed in view at position (View Coord) : " << event->pos();

    QPointF scenePosition = mapToScene(event->pos());

    qDebug() << "Mouse pressed in view at position (Scene Coord) : " << scenePosition;


  QGraphicsRectItem * rect =  scene()->addRect(scenePosition.x(),scenePosition.y(),50,50);
  rect->setBrush(QBrush(Qt::blue));

}
