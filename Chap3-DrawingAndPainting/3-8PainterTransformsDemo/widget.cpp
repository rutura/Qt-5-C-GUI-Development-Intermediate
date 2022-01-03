#include "widget.h"
#include "ui_widget.h"
#include <QPainter>

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);
}

Widget::~Widget()
{
    delete ui;
}

void Widget:: paintEvent(QPaintEvent *event){

    QPainter painter(this);
    QPen mPen;
    mPen.setWidth(5);


    painter.setPen(mPen);
    painter.drawRect(100,100,200,200);

    //Rotate the coord system and draw rect
    painter.translate(200,200);
    painter.rotate(45);
    painter.translate(-200,-200);

    mPen.setColor(Qt::green);
    painter.setPen(mPen);

    painter.drawRect(100,100,200,200);

    //Scale
    painter.translate(200,200);
    painter.rotate(-45);
    painter.translate(-200,-200);

    painter.scale(0.6,0.6);


    mPen.setColor(Qt::blue);
    painter.setPen(mPen);
    painter.drawRect(100,100,200,200);

    //Reset transforms
    painter.resetTransform();


    mPen.setColor(Qt::red);
    painter.setPen(mPen);
    painter.drawRect(100,100,200,200);



    //Shear
    painter.translate(200,200);
    painter.shear(0.6,0.6);
    painter.translate(-200,-200);

    mPen.setColor(Qt::yellow);
    painter.setPen(mPen);
    painter.drawRect(100,100,200,200);
















}
