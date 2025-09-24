#include "widget.h"
#include "./ui_widget.h"
#include "indicator.h"
#include "watertank.h"

Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
{
    ui->setupUi(this);

    //Connect water tank signals to indicator slots
    connect(ui->tank, &WaterTank::normal, ui->indicator, &Indicator::activateNormal);
    connect(ui->tank, &WaterTank::warning, ui->indicator, &Indicator::activateWarning);
    connect(ui->tank, &WaterTank::danger, ui->indicator, &Indicator::activateDanger);
}

Widget::~Widget()
{
    delete ui;
}
