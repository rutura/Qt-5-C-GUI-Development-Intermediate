#include "widget.h"
#include "ui_widget.h"
#include "rect.h"
#include "view.h"
#include <QGraphicsView>
#include <QGraphicsScene>
#include <QGraphicsRectItem>

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);

    QGraphicsScene * scene = new QGraphicsScene(this);
    scene->setBackgroundBrush(QBrush(QColor(Qt::yellow)));
    scene->setSceneRect(-300,-300,600,600);



    QPen mPen;
    mPen.setWidth(5);
    mPen.setColor(Qt::red);

    Rect * rectItem = new Rect();
    rectItem->setRect(10,10,200,200);
    rectItem->setFlag(QGraphicsItem::ItemIsFocusable);
    rectItem->setFocus();

    rectItem->setPen(mPen);
    rectItem->setBrush(QBrush(Qt::green));

    scene->addItem(rectItem);



    /*
    QGraphicsRectItem * rectItem  = scene->addRect(10,10,200,200);
    rectItem->setPen(mPen);
    rectItem->setBrush(QBrush(Qt::green));
    rectItem->setFlag(QGraphicsItem::ItemIsMovable);
    rectItem->setFlag(QGraphicsItem::ItemIsSelectable);
    */




    //Add lines

    //Horizontal
    scene->addLine(-300,0,300,0);
    //Vertical
    scene->addLine(0,-300,0,300);



    View * view = new View(this);

    /*
    view->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
    view->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
    */

    //view->setAlignment(Qt::AlignBottom | Qt::AlignRight);
    view->setScene(scene);
    ui->verticalLayout->addWidget(view);
}

Widget::~Widget()
{
    delete ui;
}
