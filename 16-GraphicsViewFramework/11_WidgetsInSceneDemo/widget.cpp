#include "widget.h"
#include "ui_widget.h"
#include <QGraphicsRectItem>
#include <QDial>
#include <QGraphicsProxyWidget>
#include <QDebug>

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);

    scene = new QGraphicsScene(this);

    scene->addLine(-400,0,400,0,QPen(Qt::blue));
    scene->addLine(0,-400,0,400,QPen(Qt::blue));
    scene->setSceneRect(-800,-400,1600,800);

    //Add Rect
    QGraphicsRectItem * rect =  scene->addRect(-200,-100,200,70);
    rect->setBrush(QBrush(Qt::red));

    //Dial
    QDial * dial = new QDial();
    dial->setMinimum(0);
    dial->setMaximum(360);


    connect(dial,&QDial::valueChanged,[=](){
        qDebug() << "Dial value changed to : " << dial->value();
        rect->setRotation(dial->value());


    });


    QGraphicsProxyWidget * proxyWidget = new QGraphicsProxyWidget();
    proxyWidget->setWidget(dial);
    proxyWidget->setPos(100,-300);



    scene->addItem(proxyWidget);



    view = new QGraphicsView(this);
    view->setScene(scene);

    ui->verticalLayout->addWidget(view);
}

Widget::~Widget()
{
    delete ui;
}
