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

void Widget::drawCar(QPainter *painter)
{

    QPen mPen(Qt::black);
    mPen.setWidth(3);
    painter->setPen(mPen);


    /*
     * Upper Section
     * */
    int startAngle = 15 * 16;
    int spanAngle = 150 * 16; //This is the span angle, not the end angle
    QRectF outRect(100,100,200,200);
    QRectF inRect(110,110,180,180);


    //Draw the upper roofs
    painter->drawArc(outRect,startAngle,spanAngle);
    painter->drawArc(inRect,20*16,65*16);
    painter->drawArc(inRect,92*16,68*16);


    //Draw upper vertical lines
    painter->drawLine(197,110,197,170);
    painter->drawLine(207,110,207,170);

    //Draw low horizontal line
    painter->drawLine(120,170,195,170);
    painter->drawLine(210,170,285,170);

    /*
     * Back Section
     * */

    painter->drawLine(105,174, 50,179);//Horizontal top
    painter->drawLine(50,179,45,235);//Vertical back

    /*
     * Front Section
     * */

    painter->drawLine(300,174, 390,175);//Horizontal top
    painter->drawLine(390,175,400,235);


    /*
     * Tires
     * */

    //Frames
    QRectF backTireFrame(90,200,80,80);
    QRectF frontTireFrame(270,200,80,80);
    painter->drawArc(backTireFrame,0,170*16);

    painter->drawArc(frontTireFrame,10*16,170*16);


    //Lower connectors
    painter->drawLine(45,235,93,232);//Back

    painter->drawLine(170,240,270,240);//Middle

    painter->drawLine(350,235,400,235);//Front

    //Back Tire
    painter->drawEllipse(100,210,60,60);
    painter->setBrush(Qt::black);

    painter->drawEllipse(110,220,40,40);
    painter->setBrush(Qt::NoBrush);


    //Front Tire
    painter->drawEllipse(280,210,60,60);
    painter->setBrush(Qt::black);
    painter->drawEllipse(290,220,40,40);
    painter->setBrush(Qt::NoBrush);
}

void Widget::drawCarV2(QPainter *painter, QRectF rect, QColor tireColor)
{
    QPen mPen(Qt::black);
    mPen.setWidth(3);
    painter->setPen(mPen);

    /*
     * Upper Section
     * */
    int startAngle = 15 * 16;
    int spanAngle = 150 * 16; //This is the span angle, not the end angle
    //QRectF outRect(100,100,200,200);
    QRectF outRect(rect);
    QRectF inRect(outRect.topLeft().x()+10,outRect.topLeft().y()+10,
                  outRect.width()-20,outRect.height()-20);


    //Draw the upper roofs
    painter->drawArc(outRect,startAngle,spanAngle);
    painter->drawArc(inRect,20*16,65*16);
    painter->drawArc(inRect,92*16,68*16);

    //Draw upper vertical lines

    painter->drawLine(outRect.topLeft()+QPointF(97,10),
                      outRect.topLeft()+QPointF(97,70));

    painter->drawLine(outRect.topLeft()+QPointF(107,10),
                      outRect.topLeft()+QPointF(107,70));

    //Draw low horizontal line
    painter->drawLine(outRect.topLeft()+QPointF(20,70),
                      outRect.topLeft()+QPointF(95,70));
    painter->drawLine(outRect.topLeft()+QPointF(110,70),
                      outRect.topLeft()+QPointF(185,70));

    /*
     * Back Section
     * */


    painter->drawLine(outRect.topLeft()+QPointF(5,74),
                      outRect.topLeft()+QPointF(-50,79));//Horizontal top

    painter->drawLine(outRect.topLeft()+QPointF(-50,79),
                      outRect.topLeft()+QPointF(-55,135));//Vertical back


    /*
         * Front Section
         * */
    painter->drawLine(outRect.topLeft()+QPointF(200,74),
                      outRect.topLeft()+QPointF(290,75));
    painter->drawLine(outRect.topLeft()+QPointF(290,75),
                      outRect.topLeft()+QPointF(300,135));

    /*
         * Tires
         * */

    //Frames

    QRectF backTireFrame(outRect.topLeft()+ QPointF(-10,100),QSize(80,80));
    QRectF frontTireFrame(outRect.topLeft()+ QPointF(170,100),QSize(80,80));

    painter->drawArc(backTireFrame,0,170*16);
    painter->drawArc(frontTireFrame,10*16,170*16);


    //Lower connectors
    painter->drawLine(outRect.topLeft()+QPointF(-55,135),
                      outRect.topLeft()+QPointF(-7,132));

    painter->drawLine(outRect.topLeft()+QPointF(70,140),
                      outRect.topLeft()+QPointF(170,140));

    painter->drawLine(outRect.topLeft()+QPointF(250,135),
                      outRect.topLeft()+QPointF(300,135));

    //Back Tire
    painter->drawEllipse(QRectF(outRect.topLeft()+QPointF(0,110),QSize(60,60)));
    painter->setBrush(tireColor);

    painter->drawEllipse(QRectF(outRect.topLeft()+QPointF(10,120),QSize(40,40)));
    painter->setBrush(Qt::NoBrush);

    //Front Tire
    painter->drawEllipse(QRectF(outRect.topLeft()+QPointF(180,110),QSize(60,60)));
    painter->setBrush(tireColor);

    painter->drawEllipse(QRectF(outRect.topLeft()+QPointF(190,120),QSize(40,40)));
    painter->setBrush(Qt::NoBrush);




}

void Widget::paintEvent(QPaintEvent *event)
{
    QPainter painter(this);
    drawCar(&painter);
    drawCarV2(&painter,QRectF(500,100,200,200),Qt::red);
    drawCarV2(&painter,QRectF(500,300,200,200),Qt::green);
    drawCarV2(&painter,QRectF(100,300,200,200),Qt::blue);



}
