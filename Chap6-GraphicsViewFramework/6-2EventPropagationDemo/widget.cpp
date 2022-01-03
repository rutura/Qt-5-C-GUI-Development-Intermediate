#include "widget.h"
#include "ui_widget.h"
#include "view.h"
#include "scene.h"
#include "rect.h"

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);

    Scene * scene = new Scene(this);

    Rect * rectItem = new Rect();
    rectItem->setRect(10,10,200,200);

    scene->addItem(rectItem);

    rectItem->setFlag(QGraphicsItem::ItemIsFocusable);
    rectItem->setFlag(QGraphicsItem::ItemIsMovable);
    rectItem->setFocus();


    View * view = new View(this);
    view->setScene(scene);

    ui->verticalLayout->addWidget(view);
}

Widget::~Widget()
{
    delete ui;
}
