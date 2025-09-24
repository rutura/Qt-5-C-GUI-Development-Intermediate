#include "commands.h"

AddCommand::AddCommand(QGraphicsItem * item, QGraphicsScene * scene) :
    mItem(item) , mScene(scene)
{

}

void AddCommand::undo()
{
    if(mItem){
        mScene->removeItem(mItem);
    }
}

void AddCommand::redo()
{
    if(mItem){
        mScene->addItem(mItem);
    }


}

RemoveCommand::RemoveCommand(QGraphicsItem *item, QGraphicsScene *scene):
    mItem(item) , mScene(scene)
{

}

void RemoveCommand::undo()
{
    if(mItem){
        mScene->addItem(mItem);
    }
}

void RemoveCommand::redo()
{
    if(mItem)
        mScene->removeItem(mItem);
}

MoveCommand::MoveCommand(QGraphicsItem *item,
                         QGraphicsScene *scene, QPointF oldPos, QPointF newPos) :
    mItem(item) , mScene(scene), mOldPosition(oldPos),
    mNewPosition(newPos)
{

}

void MoveCommand::undo()
{
    if(mItem){
        mItem->setPos(mOldPosition);
    }

}

void MoveCommand::redo()
{
    if(mItem)
        mItem->setPos(mNewPosition);
}
