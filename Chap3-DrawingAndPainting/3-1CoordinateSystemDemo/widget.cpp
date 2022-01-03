#include "widget.h"
#include "ui_widget.h"
#include <QPainter>
#include <QDebug>

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

void Widget::paintEvent(QPaintEvent *event)
{
    QPen mPen(Qt::red);
    mPen.setWidth(3);

    QPainter painter(this);

    painter.setPen(mPen);

    qDebug() << "Logical coordinates : " << painter.window();
    qDebug() << " Physical coordinates : " << painter.viewport();

    painter.drawRect(50,50,100,100);

    //Change the logical coordinates . Keep physical coords the same

    painter.save();

    painter.setWindow(0,0,300,200);
    //painter.setViewport(0,0,300,200);
    mPen.setColor(Qt::green);
    painter.setPen(mPen);

    painter.drawRect(50,50,100,100);


    painter.restore();

    //Change physical coordinates . Keep logical the same

     painter.save();

     mPen.setColor(Qt::blue);
     painter.setPen(mPen);
     painter.setViewport(0,0,300,200);

     painter.drawRect(50,50,100,100);



     painter.restore();


}
