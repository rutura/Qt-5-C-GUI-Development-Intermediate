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
    QPainter painter(this);

    // Linear Gradient
    const QPointF linearStart(70, 20);
    const QPointF linearEnd(70, 170);
    QLinearGradient linearGradient(linearStart,linearEnd);
    linearGradient.setColorAt(0, Qt::red);
    linearGradient.setColorAt(0.5, Qt::gray);
    linearGradient.setColorAt(1, Qt::yellow);
    linearGradient.setSpread(QGradient::ReflectSpread);

    painter.setBrush(QBrush(linearGradient));
    painter.drawRect(20, 20, 100, 300);
    painter.drawLine(QLineF(linearStart, linearEnd));


    // Radial Gradient
    const QPointF radialCenter(280, 170);
    constexpr qreal radialRadius = 75;
    QRadialGradient radialGradient(radialCenter, radialRadius);
    radialGradient.setColorAt(0, Qt::blue);
    radialGradient.setColorAt(1, Qt::yellow);
    radialGradient.setSpread(QGradient::RepeatSpread);

    painter.setBrush(QBrush(radialGradient));
    painter.drawRect(130, 20, 300, 300);


    // Conical Gradient
    const QPointF conicalCenter(600, 170);
    constexpr qreal startAngle = 90;
    QConicalGradient conicalGradient(conicalCenter, startAngle);
    conicalGradient.setColorAt(0, Qt::blue);
    conicalGradient.setColorAt(1, Qt::yellow);

    painter.setBrush(QBrush(conicalGradient));
    painter.drawEllipse(450, 20, 300, 300);

}
