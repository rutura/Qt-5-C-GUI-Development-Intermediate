#include "widget.h"
#include "ui_widget.h"
#include <QGraphicsView>
#include "resizablerectitem.h"
#include "resizableellipseitem.h"
#include "resizablepixmapitem.h"
#include  "resizablestaritem.h"
#include "shapelist.h"
#include "colorlistwidget.h"
#include <QFileDialog>

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);

    scene = new Scene(this);
    scene->addLine(-400,0,400,0,QPen(Qt::blue));
       scene->addLine(0,-400,0,400,QPen(Qt::blue));
       scene->setSceneRect(-800,-400,1600,800);


    ShapeList * shapeList = new ShapeList(this);
    shapeMap.insert(10, "Ellipse");
    shapeMap.insert(20, "Quick");
    shapeMap.insert(30, "Rectangle");
    shapeMap.insert(40, "Star");

    foreach (int key, shapeMap.keys()) {
        QListWidgetItem * item = new QListWidgetItem(shapeMap[key],shapeList);
        QString filename = ":/images/" + shapeMap[key].toLower()+".png";
        item->setIcon(QIcon(filename));
        item->setData(Qt::UserRole,key);

    }

    ColorListWidget * colorList = new ColorListWidget(this);
    colorList->addItems(QColor::colorNames());

    QStringList colors = QColor::colorNames();

    for( int i = 0 ; i < colors.size(); i++){
        QPixmap mPix(40,40);
        mPix.fill(colors[i]);
        QIcon icon;
        icon.addPixmap(mPix);
        colorList->item(i)->setIcon(icon);

    }

    QGraphicsView * view = new QGraphicsView(this);
    view->setScene(scene);


     ui->listLayout->addWidget(shapeList);
     ui->listLayout->addWidget(colorList);
     ui->viewLayout->addWidget(view);


}

Widget::~Widget()
{
    delete ui;
}


