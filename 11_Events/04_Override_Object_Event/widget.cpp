#include "widget.h"
#include "./ui_widget.h"
#include "button.h"
#include <QDebug>

Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
{
    ui->setupUi(this);

    auto *button = new Button(this);
    button->setText("Button");

    //Make the connection to the slot
    connect(button,&Button::clicked,this,[](){
        qDebug() << "Button clicked";
    });

    // Add the button to the layout
    ui->verticalLayout->addWidget(button);
}

Widget::~Widget()
{
    delete ui;
}
