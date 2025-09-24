#include "widget.h"
#include "./ui_widget.h"
#include "indicator.h"
#include "watertank.h"

Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
{
    ui->setupUi(this);

    Indicator* indicator = new Indicator(this);
    WaterTank* tank = new WaterTank(this);


    //Connect water tank signals to indicator slots
    connect(tank, &WaterTank::normal, indicator, &Indicator::activateNormal);
    connect(tank, &WaterTank::warning, indicator, &Indicator::activateWarning);
    connect(tank, &WaterTank::danger, indicator, &Indicator::activateDanger);


    //Add the widget to the layout
    ui->horizontalLayout->addWidget(tank);
    ui->horizontalLayout->addWidget(indicator);
}

Widget::~Widget()
{
    delete ui;
}
