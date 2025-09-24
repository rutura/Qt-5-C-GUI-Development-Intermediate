#include "widget.h"
#include "./ui_widget.h"
#include <QPainter>

Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
{
    ui->setupUi(this);
}

Widget::~Widget()
{
    delete ui;
}


void Widget::paintEvent(QPaintEvent *event)
{
    Q_UNUSED(event);
    QPainter painter(this);
    QPen pen;
    pen.setWidth(5);

    //Fill the rectangle with a light gray color
    painter.fillRect(rect(), Qt::lightGray);


    // Draw original rectangle
    painter.setPen(pen);
    painter.drawRect(100, 100, 200, 200);


    //Draw a rotated rectangle in green
    painter.translate(200,200);
    painter.rotate(45);
    painter.translate(-200, -200);

    pen.setColor(Qt::green);
    painter.setPen(pen);
    painter.drawRect(100, 100, 200, 200);


    // Draw scaled rectangle (blue)
    painter.translate(200, 200);
    painter.rotate(-45);
    painter.translate(-200, -200);

    painter.scale(0.6, 0.6);

    pen.setColor(Qt::blue);
    painter.setPen(pen);
    painter.drawRect(100, 100, 200, 200);


    //Draw the original rectangle in red
    painter.resetTransform();
    pen.setColor(Qt::red);
    painter.setPen(pen);
    painter.drawRect(100, 100, 200, 200);

    // Draw sheared rectangle (yellow)
    painter.translate(200, 200);
    painter.shear(0.6, 0.6);
    painter.translate(-200, -200);

    pen.setColor(Qt::yellow);
    painter.setPen(pen);
    painter.drawRect(100, 100, 200, 200);

}
