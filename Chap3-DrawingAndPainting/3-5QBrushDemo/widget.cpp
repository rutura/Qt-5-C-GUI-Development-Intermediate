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


    QBrush mBrush;
    mBrush.setColor(Qt::red);
    mBrush.setStyle(Qt::SolidPattern);

    //First Row
    painter.setBrush(mBrush);
    painter.drawRect(20,20,100,100);

    mBrush.setColor(Qt::blue);
    mBrush.setStyle(Qt::Dense1Pattern);
    painter.setBrush(mBrush);
    painter.drawRect(130,20,100,100);


    mBrush.setColor(Qt::red);
    mBrush.setStyle(Qt::Dense2Pattern);
    painter.setBrush(mBrush);
    painter.drawRect(240,20,100,100);


    mBrush.setColor(Qt::black);
    mBrush.setStyle(Qt::Dense3Pattern);
    painter.setBrush(mBrush);
    painter.drawRect(350,20,100,100);


    mBrush.setColor(Qt::blue);
    mBrush.setStyle(Qt::Dense4Pattern);
    painter.setBrush(mBrush);
    painter.drawRect(460,20,100,100);

    mBrush.setColor(Qt::blue);
    mBrush.setStyle(Qt::Dense5Pattern);
    painter.setBrush(mBrush);
    painter.drawRect(570,20,100,100);


    mBrush.setColor(Qt::blue);
    mBrush.setStyle(Qt::Dense6Pattern);
    painter.setBrush(mBrush);
    painter.drawRect(680,20,100,100);

    mBrush.setColor(Qt::blue);
    mBrush.setStyle(Qt::Dense7Pattern);
    painter.setBrush(mBrush);
    painter.drawRect(790,20,100,100);



    //Second Row
    mBrush.setColor(Qt::blue);
    mBrush.setStyle(Qt::HorPattern);
    painter.setBrush(mBrush);
    painter.drawRect(20,130,100,100);

    mBrush.setColor(Qt::blue);
    mBrush.setStyle(Qt::VerPattern);
    painter.setBrush(mBrush);
    painter.drawRect(130,130,100,100);

    mBrush.setColor(Qt::blue);
    mBrush.setStyle(Qt::CrossPattern);
    painter.setBrush(mBrush);
    painter.drawRect(240,130,100,100);


    mBrush.setColor(Qt::blue);
    mBrush.setStyle(Qt::BDiagPattern);
    painter.setBrush(mBrush);
    painter.drawRect(350,130,100,100);


    mBrush.setColor(Qt::blue);
    mBrush.setStyle(Qt::FDiagPattern);
    painter.setBrush(mBrush);
    painter.drawRect(460,130,100,100);

    mBrush.setColor(Qt::blue);
    mBrush.setStyle(Qt::DiagCrossPattern);
    painter.setBrush(mBrush);
    painter.drawRect(570,130,100,100);

    QPixmap mPix("://images/LearnQt.png");
    mBrush.setTexture(mPix.scaled(50,50));
    painter.setBrush(mBrush);
    painter.drawRect(680,130,210,100);


}
