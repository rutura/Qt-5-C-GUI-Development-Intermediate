#include "widget.h"
#include "ui_widget.h"
#include "colorpicker.h"
#include <QDebug>

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);

    ColorPicker * colorPicker = new ColorPicker(this);
    connect(colorPicker,&ColorPicker::colorChanged,this,&Widget::colorChanged);

    ui->verticalLayout->addWidget(colorPicker);
}

Widget::~Widget()
{
    delete ui;
}

void Widget::colorChanged(QColor color)
{
    qDebug() << "Color changed to : " << color.name();
}
