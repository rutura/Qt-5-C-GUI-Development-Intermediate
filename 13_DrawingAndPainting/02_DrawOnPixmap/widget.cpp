#include "widget.h"
#include "./ui_widget.h"
#include <QPixmap>
#include <QPainter>
#include <QDebug>

Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
{
    ui->setupUi(this);

    //Set up the pixmap
    QPixmap pixmap( width() -10, height() - 10);
    pixmap.fill(Qt::gray);

    QPen pen;
    pen.setWidth(5);
    pen.setColor(Qt::white);

    const QFont font{"Consolas", 20, QFont::Bold};

    QPainter painter(&pixmap);
    painter.setPen(pen);
    painter.setBrush(Qt::green);
    painter.setFont(font);

    painter.drawRect(pixmap.rect());

    painter.setBrush(Qt::blue);
    painter.drawRect(50, 50, 100, 100);
    painter.drawText(30, 120, "I'm loving Qt");


    //Apply the pixmap to the label in the ui form
    ui->label->setPixmap(pixmap);
}

Widget::~Widget()
{
    delete ui;
}
