#include "widget.h"
#include "ui_widget.h"
#include "datetimewidget.h"

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);

    DateTimeWidget * datetimeWidget = new DateTimeWidget(this);

    ui->verticalLayout->addWidget(datetimeWidget);


}

Widget::~Widget()
{
    delete ui;
}
