#include "widget.h"
#include "ui_widget.h"
#include <QGraphicsRectItem>

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);

    QGraphicsScene * scene = new QGraphicsScene(this);
    //Draw the center guide lines
    scene->addLine(-400,0,400,0,QPen(Qt::blue));
    scene->addLine(0,-400,0,400,QPen(Qt::blue));
    scene->setSceneRect(-800,-400,1600,800);

    scene->setBackgroundBrush(Qt::gray);

    QGraphicsRectItem * rect =  scene->addRect(20,20,200,100);
    rect->setFlag(QGraphicsItem::ItemIsSelectable);

    //Add item to scene
    QGraphicsRectItem * greenRect = scene->addRect(-50,-50,100,100);
    greenRect->setPen(Qt::NoPen);
    greenRect->setFlag(QGraphicsItem::ItemIsSelectable);
    greenRect->setFlag(QGraphicsItem::ItemIsMovable);
    greenRect->setBrush(QBrush(Qt::green));

    QGraphicsRectItem * blueRect = scene->addRect(-100,-100,100,100);
    blueRect->setPen(Qt::NoPen);
    blueRect->setFlag(QGraphicsItem::ItemIsSelectable);
    blueRect->setFlag(QGraphicsItem::ItemIsMovable);
    blueRect->setBrush(QBrush(Qt::blue));

    redEllipse = scene->addEllipse(-850,-50,500,500);
    redEllipse->setPen(Qt::NoPen);
    redEllipse->setFlag(QGraphicsItem::ItemIsSelectable);
    redEllipse->setFlag(QGraphicsItem::ItemIsMovable);
    redEllipse->setBrush(QBrush(Qt::red));




    view = new View(this);
    view->setScene(scene);



    ui->viewLayout->addWidget(view);

    ui->showGridCheckbox->setChecked(view->getDrawGridLines());


}

Widget::~Widget()
{
    delete ui;
}

void Widget::on_centerInViewButton_clicked()
{
    view->centerOn(QPoint());
}

void Widget::on_showGridCheckbox_toggled(bool checked)
{
    view->setDrawGridLines(checked);
}

void Widget::on_ensureVisibleButton_clicked()
{
    redEllipse->ensureVisible();
}

void Widget::on_fitInViewButton_clicked()
{
    view->fitInView(redEllipse);

}

void Widget::on_zoomInButton_clicked()
{
    double scaleFactor = 1.1;
    view->scale(scaleFactor,scaleFactor);

}

void Widget::on_zoomOutButton_clicked()
{
    double scaleFactor = 1.1;
    view->scale(1/scaleFactor,1/scaleFactor);
}

void Widget::on_resetButton_clicked()
{
    view->resetTransform();
}
