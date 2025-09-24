#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "view.h"
#include <QFileDialog>
#include "shapelist.h"
#include "colorlistwidget.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);


    scene = new Scene(this);

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

       View * view = new View(this);
       view->setScene(scene);


        ui->listLayout->addWidget(shapeList);
        ui->listLayout->addWidget(colorList);
        ui->viewLayout->addWidget(view);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_actionCursor_triggered()
{
    statusBar()->showMessage("Current tool is Cursor");
    scene->setTool(Scene::Cursor);
}

void MainWindow::on_actionAbout_triggered()
{

}

void MainWindow::on_actionStar_triggered()
{
    statusBar()->showMessage("Current tool is Star");
    scene->setTool(Scene::Star);
}

void MainWindow::on_actionRectangle_triggered()
{
    statusBar()->showMessage("Current tool is Rect");
    scene->setTool(Scene::Rect);
}

void MainWindow::on_actionEllipse_triggered()
{
    statusBar()->showMessage("Current tool is Ellipse");
    scene->setTool(Scene::Ellipse);
}

void MainWindow::on_actionEraser_triggered()
{
    statusBar()->showMessage("Current tool is Eraser");
    scene->setTool(Scene::Eraser);
}

void MainWindow::on_actionPen_triggered()
{
    statusBar()->showMessage("Current tool is Pen");
    scene->setTool(Scene::Pen);

}

void MainWindow::on_actionQuit_triggered()
{

}

void MainWindow::on_actionAdd_Image_triggered()
{
    QString fileName = QFileDialog::getOpenFileName(this, tr("Open File"),
                                                    "/home",
                                                    tr("Images (*.png *.xpm *.jpg)"));
    if(fileName.isNull())
        return;

    scene->addImageItem(fileName);

}
