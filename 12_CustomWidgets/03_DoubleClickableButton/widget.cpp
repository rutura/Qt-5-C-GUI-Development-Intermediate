#include "widget.h"
#include "./ui_widget.h"
#include "doubleclickablebutton.h"
#include <QDebug>

Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
{
    ui->setupUi(this);

    //Create an instance of the custom widget
    auto* button = new DoubleClickableButton(this);
    button->setText("DoubleClickableButton");


    connect(button, &DoubleClickableButton::doubleClicked, this, [](){
        qDebug() << "Button double clicked slot triggered";
    });

    //Add the button to the layout
    ui->verticalLayout->addWidget(button);
}

Widget::~Widget()
{
    delete ui;
}
