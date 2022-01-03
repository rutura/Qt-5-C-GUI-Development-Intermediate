#include "widget.h"
#include "ui_widget.h"
#include <QGraphicsView>
#include "resizablerectitem.h"
#include "resizableellipseitem.h"
#include "resizablepixmapitem.h"
#include  "resizablestaritem.h"
#include <QFileDialog>

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);

    scene = new QGraphicsScene(this);




    ResizableRectItem * rectItem = new ResizableRectItem();
    rectItem->setRect(-50,-50,100,100);
    rectItem->setBrush(QBrush(Qt::green));
    rectItem->setFlags(QGraphicsItem::ItemIsSelectable | QGraphicsItem::ItemIsMovable);
    scene->addItem(rectItem);



    ResizableEllipseItem * ellipse = new ResizableEllipseItem();
    ellipse->setRect(-400,-400,200,200);
    ellipse->setBrush(QBrush(Qt::red));
    ellipse->setFlags(QGraphicsItem::ItemIsSelectable | QGraphicsItem::ItemIsMovable);
    scene->addItem(ellipse);



    ResizablePixmapItem * pixItem = new ResizablePixmapItem(QPixmap(":/images/Quick.png"));
    pixItem->setFlags(QGraphicsItem::ItemIsSelectable | QGraphicsItem::ItemIsMovable);
    scene->addItem(pixItem);



    ResizableStarItem * starItem = new ResizableStarItem();
    starItem->setBrush(QBrush(Qt::blue));
    starItem->setFlags(QGraphicsItem::ItemIsSelectable | QGraphicsItem::ItemIsMovable);
    scene->addItem(starItem);




    QGraphicsView * view = new QGraphicsView(this);
    view->setScene(scene);

    ui->verticalLayout->addWidget(view);
}

Widget::~Widget()
{
    delete ui;
}

void Widget::on_renderScene_clicked()
{

    QString fileName = QFileDialog::getSaveFileName(this, tr("Save File"),
                               "/home/jana/untitled.png",
                               tr("Images (*.png *.xpm *.jpg)"));
    if(fileName.isNull())
        return;

    QRect  rect = scene->sceneRect().toAlignedRect();
    QImage image(rect.size(),QImage::Format_ARGB32);
    image.fill(Qt::transparent);

    QPainter painter(&image);

    scene->render(&painter);

    image.save(fileName);

}
