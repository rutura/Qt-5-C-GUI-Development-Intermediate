#include "widget.h"
#include "ui_widget.h"
#include <QPixmap>
#include <QPainter>
#include <QDebug>

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);

    QPixmap mPix (width() - 10, height() -10);
    mPix.fill(Qt::gray);

    QPen pen;
    pen.setWidth(5);
    pen.setColor(Qt::white);

    QFont mFont("Consolas", 20, QFont::Bold);


    QPainter painter(&mPix);
    painter.setPen(pen);
    painter.setBrush(Qt::green);
    painter.setFont(mFont);

    painter.drawRect(mPix.rect());

    painter.setBrush(Qt::blue);

    painter.drawRect(50,50,100,100);


    painter.drawText(30,120,"I'm loving Qt");


    qDebug() << "Painter window (logical) " << painter.window();
    qDebug() << "Painter viewPort( physical)" << painter.viewport();



    ui->label->setPixmap(mPix);



}

Widget::~Widget()
{
    delete ui;
}
