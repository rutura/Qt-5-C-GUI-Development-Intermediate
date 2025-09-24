#include "widget.h"
#include "./ui_widget.h"
#include "childbutton.h"
#include "childlineedit.h"
#include <QDebug>

Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
{
    ui->setupUi(this);

    auto * button = new ChildButton(this);
    button->setText("Child Button");
    connect(button, &ChildButton::clicked, [this](){
            qDebug() << "Button clicked";

    });

    auto* lineEdit = new ChildLineEdit(this);

    //Add the button to the layout
    ui->verticalLayout->addWidget(button);
    ui->verticalLayout->addWidget(lineEdit);
}

Widget::~Widget()
{
    delete ui;
}
