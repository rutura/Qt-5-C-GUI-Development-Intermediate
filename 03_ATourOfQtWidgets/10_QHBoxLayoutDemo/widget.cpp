#include "widget.h"
#include "ui_widget.h"
#include <QHBoxLayout>

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);
    /*
    //Define the layout
    QHBoxLayout * layout = new QHBoxLayout(); //Memory Leak?

    //Add things to the layout
    layout->addWidget(ui->oneButton);
    layout->addWidget(ui->twoButton);
    layout->addWidget(ui->threeButton);
    layout->addWidget(ui->fourButton);
    layout->addWidget(ui->fiveButton);

    //Set layout to widget
    setLayout(layout); // Check the documentation for this
                        // in terms of memory management
    */



}

Widget::~Widget()
{
    delete ui;
}
