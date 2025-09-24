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

    // Draw background
    painter.fillRect(rect(), Qt::lightGray);

    QPen pen;
    pen.setColor(Qt::black);
    pen.setWidth(5);
    painter.setPen(pen);

    // Draw rect
    painter.setBrush(Qt::red);
    painter.drawRect(10, 10, 100, 100);

    // Draw ellipse
    painter.setBrush(Qt::green);
    painter.drawEllipse(120, 10, 200, 100);

    // Round rect
    painter.setBrush(Qt::gray);
    painter.drawRoundedRect(330, 10, 200, 100, 20, 20);


    // Draw lines
    painter.drawLine(550, 30, 650, 30);
    painter.drawLine(550, 50, 650, 50);
    painter.drawLine(550, 70, 650, 70);
    painter.drawLine(550, 90, 650, 90);


    pen.setColor(Qt::red);
    painter.setPen(pen);

    const QVector<QPointF> pointVec{
        QPointF(660, 30), QPointF(760, 30),
        QPointF(660, 50), QPointF(760, 50),
        QPointF(660, 70), QPointF(760, 70),
        QPointF(660, 90), QPointF(760, 90)
    };
    painter.drawLines(pointVec);


    // Polygons
    const QPolygonF polygon{
        QPointF(240.0, 150.0),
        QPointF(10.0, 150.0),
        QPointF(60.0, 200.0),
        QPointF(30.0, 250.0),
        QPointF(120.0, 250.0)
    };
    painter.drawPolygon(polygon);


    // Arcs
    constexpr int startAngle = 30 * 16;
    constexpr int spanAngle = 240 * 16;

    const QRectF rectangle(250.0, 150.0, 150.0, 150.0);
    painter.drawArc(rectangle, startAngle, spanAngle);

    // Chord
    const QRectF chordRect(450.0, 150.0, 150.0, 150.0);
    painter.drawChord(chordRect, startAngle, spanAngle);


    // Pie
    const QRectF pieRect(650.0, 150.0, 150.0, 150.0);
    painter.drawPie(pieRect, startAngle, spanAngle);

    // Text
    pen.setColor(Qt::blue);
    painter.setPen(pen);
    painter.setFont(QFont("Times", 40, QFont::Bold));
    painter.drawText(50.0, 400.0, "I'm loving Qt");


    // Pixmap
    const QRectF target(520.0, 350.0, 200.0, 200.0);
    const QPixmap pixmap(":/images/LearnQt.png");
    const QRect sourceRect = pixmap.rect();
    painter.drawPixmap(target, pixmap, sourceRect);


}
