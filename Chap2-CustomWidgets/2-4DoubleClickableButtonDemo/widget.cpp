#include "widget.h"
#include "ui_widget.h"
#include "doubleclickablebutton.h"
#include <QDebug>

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);
    DoubleClickableButton * button  = new DoubleClickableButton(this);
    button->setText("Double Clickable Button");
    connect(button,&DoubleClickableButton::doubleClicked,[=](){
        qDebug() << "Button double clicked";
    });
}

Widget::~Widget()
{
    delete ui;
}
