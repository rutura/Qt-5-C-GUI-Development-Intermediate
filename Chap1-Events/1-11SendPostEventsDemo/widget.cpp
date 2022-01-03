#include "widget.h"
#include "ui_widget.h"
#include <QMouseEvent>
#include <QDebug>

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);

    button1 = new Button(this);
    button1->setText("I am the phoenex king");
}

Widget::~Widget()
{
    delete ui;
}

void Widget::on_button2_clicked()
{

    QMouseEvent * mouseEvent = new QMouseEvent(QEvent::MouseButtonPress, QPointF(10,10),
                                             Qt::LeftButton, Qt::LeftButton,Qt::NoModifier);

    //Send
//    if(QApplication::sendEvent(button1,mouseEvent)){
//        qDebug() << "Event accepted";
//    }else{
//     qDebug() << "Event not accepted" ;
//    }


    //Post
    QApplication::postEvent(button1,mouseEvent);

}
