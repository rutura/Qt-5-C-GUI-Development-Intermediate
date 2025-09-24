#include "widget.h"
#include "./ui_widget.h"
#include <memory>
#include <QMouseEvent>

Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
{
    ui->setupUi(this);

    button1 = new Button(this);
    button1->setText("First Button");
}

Widget::~Widget()
{
    delete ui;
}

void Widget::on_button2_clicked()
{
    auto mouseEvent = std::make_unique<QMouseEvent>(
        QEvent::MouseButtonPress,
        QPointF(10, 10),
        button1->mapToGlobal(QPointF(10, 10)),
        Qt::LeftButton,
        Qt::LeftButton,
        Qt::NoModifier
        );

    //Post event -  Qt takes ownership of the event. See the docs
    //QApplication::postEvent(button1, mouseEvent.release());


    //Send event - Qt is not going to take ownership here. See the docs
    if (QApplication::sendEvent(button1,mouseEvent.get())){
        qDebug() << "Event accepted";
    }else{
        qDebug() << "Event not accepted";
    }

}

