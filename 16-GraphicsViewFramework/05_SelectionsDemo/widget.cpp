#include "widget.h"
#include "ui_widget.h"
#include <QColorDialog>
#include <QGraphicsItem>
#include <QDebug>


Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);

    scene = new QGraphicsScene(this);

    scene->setSceneRect(QRectF(-400,-400,800,800));
    scene->addLine(-400,0,400,0);
    scene->addLine(0,-400,0,400);



    view = new View(this);
    view->setScene(scene);
    view->setCurrentTool(View::Cursor);
    view->setDragMode(QGraphicsView::RubberBandDrag);

    ui->verticalLayout->addWidget(view);
}

Widget::~Widget()
{
    delete ui;
}

void Widget::on_lineButton_clicked()
{
   view->setCurrentTool(View::Line);
}

void Widget::on_ellipseButton_clicked()
{
    view->setCurrentTool(View::Ellipse);

}

void Widget::on_pathButton_clicked()
{
   view->setCurrentTool(View::Path);
}

void Widget::on_pieButton_clicked()
{
   view->setCurrentTool(View::Pie);
}

void Widget::on_imageButton_clicked()
{
  view->setCurrentTool(View::Image);

}

void Widget::on_starButton_clicked()
{
    view->setCurrentTool(View::Star);
}

void Widget::on_chooseColorButton_clicked()
{
     QColor color = QColorDialog::getColor(currentColor);
     if(color.isValid()){
         currentColor = color;
         QString qss = QString("background-color: %1").arg(currentColor.name());
         ui->colorButton->setStyleSheet(qss);
         setSelectItemColor(color);
     }
}

void Widget::on_colorButton_clicked()
{
setSelectItemColor(currentColor);
}

void Widget::on_infoButton_clicked()
{
    qDebug() << "Item count : " << scene->items().count();
    qDebug() << "Selected items : " << scene->selectedItems().count();

}

void Widget::on_cursorButton_clicked()
{
    view->setCurrentTool(View::Cursor);
}

void Widget::setSelectItemColor(QColor color)
{
    if(scene->selectedItems().count()!= 0){
        //Loop through the selected items
        foreach (QGraphicsItem * item, scene->selectedItems()) {

            //Loop to find children
            foreach (QGraphicsItem * childItem, item->childItems()) {
                //Is rect ?
                QGraphicsRectItem* mItem = qgraphicsitem_cast<QGraphicsRectItem*>(childItem);
                if(mItem){
                    mItem->setBrush(QBrush(color));
                }

                //Is path ?
                QGraphicsPathItem* pathItem = qgraphicsitem_cast<QGraphicsPathItem*>(childItem);
                if(pathItem){
                    pathItem->setBrush(QBrush(color));
                }



                //Is ellipse?
                QGraphicsEllipseItem* ellipseItem = qgraphicsitem_cast<QGraphicsEllipseItem*>(childItem);
                if(ellipseItem){
                    ellipseItem->setBrush(QBrush(color));
                }


            }

        }
    }
}
