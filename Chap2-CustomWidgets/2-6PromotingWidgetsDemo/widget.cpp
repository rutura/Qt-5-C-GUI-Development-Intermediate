#include "widget.h"
#include "ui_widget.h"
#include "indicator.h"
#include "watertank.h"

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);



    connect(ui->waterTank,&WaterTank::normal,ui->indicator,&Indicator::activateNormal);
    connect(ui->waterTank,&WaterTank::warning,ui->indicator,&Indicator::activateWarning);
    connect(ui->waterTank,&WaterTank::danger,ui->indicator,&Indicator::activateDanger);



}

Widget::~Widget()
{
    delete ui;
}
