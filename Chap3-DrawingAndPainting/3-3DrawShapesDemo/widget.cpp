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

void Widget::paintEvent(QPaintEvent *event) {

    QPainter painter(this);
    QPen mPen;
    mPen.setColor(Qt::black);
    mPen.setWidth(5);

    painter.setPen(mPen);

    //Draw rect
    painter.setBrush(Qt::red);
    painter.drawRect(10,10,100,100);

    //Draw ellipse
    painter.setBrush(Qt::green);
    painter.drawEllipse(120,10,200,100);

    //Round rect
    painter.setBrush(Qt::gray);
    painter.drawRoundRect(330 , 10,200,100 );

    //Draw lines
    painter.drawLine(550,30,650,30);
    painter.drawLine(550,50,650,50);
    painter.drawLine(550,70,650,70);
    painter.drawLine(550,90,650,90);

    mPen.setColor(Qt::red);
    painter.setPen(mPen);
    QVector<QPointF> pointVec;
    pointVec << QPointF(660,30) << QPointF(760,30);
    pointVec << QPointF(660,50) << QPointF(760,50);
    pointVec << QPointF(660,70) << QPointF(760,70);
    pointVec << QPointF(660,90) << QPointF(760,90);

    painter.drawLines(pointVec);

    //Polygons
    QPolygonF polygon;
    polygon  << QPointF(240.0,150.0) <<  QPointF(10.0,150.0)<<
                QPointF(60.0,200.0) <<
                QPointF(30.0, 250.0) << QPointF(120.0, 250.0);
    painter.drawPolygon(polygon);

    //Arcs
    QRectF rectangle(250.0, 150.0, 150.0, 150.0);
    int startAngle = 30 * 16;
    int spanAngle = 240 * 16;
    painter.drawArc(rectangle, startAngle, spanAngle);

    //Chord
    QRectF chordRect(450.0, 150.0, 150.0, 150.0);
    startAngle = 30 * 16;
    spanAngle = 240 * 16;
    painter.drawChord(chordRect, startAngle, spanAngle);

    //Pie
    QRectF pieRect(650.0, 150.0, 150.0, 150.0);
    startAngle = 30 * 16;
    spanAngle = 240 * 16;
    painter.drawPie(pieRect, startAngle, spanAngle);

    //Text
    mPen.setColor(Qt::blue);
    painter.setPen(mPen);
    painter.setFont( QFont ("Times", 40, QFont::Bold));
    painter.drawText(50.0,400.0,"I'm loving Qt");

    //Pixmap
    QRectF target(520.0, 350.0, 200.0, 200.0);
    QPixmap mPix(":/images/LearnQt.png");
    QRect mSourceRect = mPix.rect();
    painter.drawPixmap(target,mPix,mSourceRect);
}
