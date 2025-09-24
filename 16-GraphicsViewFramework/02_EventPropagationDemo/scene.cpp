#include "scene.h"
#include <QDebug>
#include <QKeyEvent>
#include <QGraphicsSceneMouseEvent>

Scene::Scene(QObject *parent) : QGraphicsScene(parent)
{

}

void Scene::keyPressEvent(QKeyEvent *event)
{
    qDebug() << "Scene : KeypressEvent : " ;
    QGraphicsScene::keyPressEvent(event);

}

void Scene::mousePressEvent(QGraphicsSceneMouseEvent *event)
{
    qDebug() << "Scene : MousePressEvent at : " << event->scenePos();
    QGraphicsScene::mousePressEvent(event);

}
