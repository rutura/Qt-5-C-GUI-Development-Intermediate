#include "widget.h"
#include "ui_widget.h"
#include <QVBoxLayout>

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);


    //Create the layout
    QVBoxLayout * layout = new QVBoxLayout();

    //Add widgets to the layout
    layout->addWidget(ui->oneButton);
    layout->addWidget(ui->twoButton);
    layout->addWidget(ui->threeButton);
    layout->addWidget(ui->fourButton);
    layout->addWidget(ui->fiveButton);


    //Set the layout to the widget
    setLayout(layout);




}

Widget::~Widget()
{
    delete ui;
}
