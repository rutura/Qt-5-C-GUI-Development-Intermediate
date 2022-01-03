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

void Widget:: paintEvent(QPaintEvent *event) {

    QPainter painter(this);
    QPen mPen;// No pen style set , default is Qt::SolidLine
    mPen.setColor(Qt::black);
    mPen.setWidth(5);


    /*
     * Pen Style
     * */
    mPen.setStyle(Qt::SolidLine);
    painter.setPen(mPen);
    //Draw line
    painter.setBrush(Qt::red);
    //Default : Qt::SolidLine
    painter.drawRect(10,10,100,100); // Drawn with default SolidLine


    //Qt::NoPen
    mPen.setStyle(Qt::NoPen);
    painter.setPen(mPen);
    painter.drawRect(120,10,100,100); // Drawn with Qt::NoPen

    //Qt::DashLine
    mPen.setStyle(Qt::DashLine);
    painter.setPen(mPen);
    painter.drawRect(230,10,100,100); // Drawn with Qt::DashLine

    //Qt::DotLine
    mPen.setStyle(Qt::DotLine);
    painter.setPen(mPen);
    painter.drawRect(340,10,100,100); // Drawn with Qt::DotLine

    //Qt::DashDotLine
    mPen.setStyle(Qt::DashDotLine);
    painter.setPen(mPen);
    painter.drawRect(450,10,100,100); // Drawn with Qt::DashDotLine


    //Qt::DashDotDotLine
    mPen.setStyle(Qt::DashDotDotLine);
    painter.setPen(mPen);
    painter.drawRect(450,10,100,100); // Drawn with Qt::DashDotDotLine

    //CustomDash Line
    QVector<qreal> dashes;
    qreal space = 4;
    dashes << 1 << space << 3 << space << 9 << space
           << 27 << space << 9 << space;
    mPen.setDashPattern(dashes);
    painter.drawRect(560,10,100,100);

    /*
     * Cap Style
     * */

    QPoint start(100,150);
    QPoint end(500,150);
    mPen.setWidth(20);
    mPen.setStyle(Qt::SolidLine);
    mPen.setCapStyle(Qt::FlatCap);
    painter.setPen(mPen);
    painter.drawLine(start, end);

    start.setY(200);
    end.setY(200);
    mPen.setCapStyle(Qt::SquareCap);
    painter.setPen(mPen);
    painter.drawLine(start, end);

    start.setY(250);
    end.setY(250);
    mPen.setCapStyle(Qt::RoundCap);
    painter.setPen(mPen);
    painter.drawLine(start, end);



    /*
     * Join Style
     * */


    QPointF points[4] = {
        QPointF(10.0, 380.0),
        QPointF(50.0, 310.0),
        QPointF(320.0, 330.0),
        QPointF(250.0, 370.0)
    };

    mPen.setWidth(10);
    mPen.setStyle(Qt::SolidLine);

    mPen.setJoinStyle(Qt::MiterJoin);

    painter.setPen(mPen);

    painter.drawPolygon(points, 4);


    //Move the points down and draw blue polygon
    points[0].setY(points[0].y()+100.0);
    points[1].setY(points[1].y()+100);
    points[2].setY(points[2].y()+100);
    points[3].setY(points[3].y()+100);

    mPen.setJoinStyle(Qt::BevelJoin);
    painter.setPen(mPen);

    painter.setBrush(Qt::blue);
    painter.drawPolygon(points, 4);


    //Move the points right and draw yellow polygon
    points[0].setX(points[0].x()+300);
    points[1].setX(points[1].x()+300);
    points[2].setX(points[2].x()+300);
    points[3].setX(points[3].x()+300);

    mPen.setJoinStyle(Qt::RoundJoin);
    painter.setPen(mPen);


    painter.setBrush(Qt::yellow);
    painter.drawPolygon(points, 4);



}
