#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "view.h"
#include <QFileDialog>
#include <QColorDialog>
#include "shapelist.h"
#include "colorpicker.h"

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

       /*
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
       */

       ColorPicker * colorPicker = new ColorPicker(this);

       connect(colorPicker,&ColorPicker::colorChanged,[=](QColor color){
           scene->setPenColor(color);
           ui->penColorButton->setStyleSheet(QString("background-color: %1")
                                             .arg(scene->getPenColor().name()));
       });

       View * view = new View(this);
       view->setScene(scene);

       ui->colorPickerLayout->addWidget(colorPicker);

        ui->listLayout->addWidget(shapeList);
  //      ui->listLayout->addWidget(colorList);
        ui->viewLayout->addWidget(view);


       QString colorQss = QString("background-color: %1").arg(scene->getPenColor().name());
       ui->penColorButton->setStyleSheet(colorQss);

       //Populate pen style combo
       ui->penStyleCombobox->addItem(QIcon(":/images/pen_style_solid.png") ,"Solid");
       ui->penStyleCombobox->addItem(QIcon(":/images/pen_style_dashed.png"),"Dashed");
       ui->penStyleCombobox->addItem(QIcon(":/images/pen_style_dotted.png"),"Dotted");
       ui->penStyleCombobox->addItem(QIcon(":/images/pen_style_dot_dashed.png"),"Dot Dashed");


       ui->penWidthSpinbox->setValue(scene->getPenWidth());


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

void MainWindow::on_actionSave_triggered()
{

}

void MainWindow::on_actionLoad_triggered()
{

}

void MainWindow::on_actionCopy_triggered()
{

}

void MainWindow::on_actionCut_triggered()
{

}

void MainWindow::on_actionPaste_triggered()
{

}

void MainWindow::on_actionUndo_triggered()
{

}

void MainWindow::on_actionRedo_triggered()
{

}

void MainWindow::on_penColorButton_clicked()
{
    QColor color = QColorDialog::getColor(Qt::black,this);

    if(color.isValid()){
        scene->setPenColor(color);
         QString colorQss = QString("background-color: %1").arg(color.name());
        ui->penColorButton->setStyleSheet(colorQss);

    }
}

void MainWindow::on_penWidthSpinbox_valueChanged(int arg1)
{
    scene->setPenWidth(arg1);
}

void MainWindow::on_penStyleCombobox_activated(int index)
{
    switch (index) {

    case 0 :{
        //Solid
        scene->setPenStyle(Qt::SolidLine);
        break;
    }

    case 1 :{
        //Dashed
        scene->setPenStyle(Qt::DashLine);
        break;
    }

    case 2 :{
        //Dotted
        scene->setPenStyle(Qt::DotLine);
        break;
    }

    case 3 :{
        //Dot Dashed
        scene->setPenStyle(Qt::DashDotLine);
        break;
    }

    }

}
