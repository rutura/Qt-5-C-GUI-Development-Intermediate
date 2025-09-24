#include "widget.h"
#include "./ui_widget.h"

Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
    , filter( new KeyboardFilter(this))
{
    ui->setupUi(this);

    //Install the event filter on the line edit
    if( ui->lineEdit){
        ui->lineEdit->installEventFilter(filter);
    }
}

Widget::~Widget()
{
    delete ui;
}

void Widget::on_remove_Filter_Button_clicked()
{
    if( ui->lineEdit && filter){
        ui->lineEdit->removeEventFilter(filter);
    }

}

