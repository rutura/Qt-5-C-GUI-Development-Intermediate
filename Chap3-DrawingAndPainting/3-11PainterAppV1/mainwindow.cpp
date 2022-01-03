#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QLabel>
#include <QSpinBox>
#include <QColorDialog>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    canvas = new PaintCanvas(this);
    setCentralWidget(canvas);

    //Pen width
    QLabel * penWidthLabel = new QLabel("Pen Width",this);
    QSpinBox * penWidthSpinBox = new QSpinBox(this);
    penWidthSpinBox->setValue(2);
    penWidthSpinBox->setRange(1,15);

    //Pen color
    QLabel * penColorLabel = new QLabel("Pen Color",this);
    penColorButton = new QPushButton(this);

    //Fill Color
    QLabel * fillColorLabel = new QLabel("Fill Color",this);
    fillColorButton = new QPushButton(this);

    //Fill
    fillCheckBox = new QCheckBox("Fill Shape",this);


    //Tool Buttons
    QPushButton * rectButton = new QPushButton(this);
    rectButton->setIcon(QIcon(":/images/rectangle.png"));

    QPushButton * penButton = new QPushButton(this);
    penButton->setIcon(QIcon(":/images/pen.png"));

    QPushButton * ellipseButton = new QPushButton(this);
    ellipseButton->setIcon(QIcon(":/images/circle.png"));


    QPushButton * eraserButton = new QPushButton(this);
    eraserButton->setIcon(QIcon(":/images/eraser.png"));


    connect(rectButton,&QPushButton::clicked,[=](){
        //Set current tool to rect
        canvas->setTool(PaintCanvas::Rect);
        statusBar()->showMessage("Current tool : Rect");
    });

    connect(penButton,&QPushButton::clicked,[=](){
            //Set current tool to rect
            canvas->setTool(PaintCanvas::Pen);
            statusBar()->showMessage("Current tool : Pen");

        });


    connect(ellipseButton,&QPushButton::clicked,[=](){
           //Set current tool to rect
           canvas->setTool(PaintCanvas::Ellipse);
           statusBar()->showMessage("Current tool : Ellipse");

       });


    connect(eraserButton,&QPushButton::clicked,[=](){
            //Set current tool to rect
            canvas->setTool(PaintCanvas::Eraser);
            statusBar()->showMessage("Current tool : Eraser");

        });









    //Slots connections
    connect(penWidthSpinBox, SIGNAL(valueChanged(int)), this, SLOT(penWidthChanged(int)));
    connect(penColorButton, SIGNAL(clicked()), this, SLOT(changePenColor()));
    connect(fillColorButton, SIGNAL(clicked()), this, SLOT(changeFillColor()));
    connect(fillCheckBox, SIGNAL(clicked()), this, SLOT(changeFillProperty()));


    ui->mainToolBar->addWidget(penWidthLabel);
    ui->mainToolBar->addWidget(penWidthSpinBox);
    ui->mainToolBar->addWidget(penColorLabel);
    ui->mainToolBar->addWidget(penColorButton);
    ui->mainToolBar->addWidget(fillColorLabel);
    ui->mainToolBar->addWidget(fillColorButton);
    ui->mainToolBar->addWidget(fillCheckBox);
    ui->mainToolBar->addSeparator();
    ui->mainToolBar->addWidget(penButton);
    ui->mainToolBar->addWidget(rectButton);
    ui->mainToolBar->addWidget(ellipseButton);
    ui->mainToolBar->addWidget(eraserButton);

    QString css = QString("background-color : %1").arg(canvas->getPenColor().name());
    penColorButton->setStyleSheet(css);

    css = QString("background-color : %1").arg(canvas->getFillColor().name());
    fillColorButton->setStyleSheet(css);


}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::penWidthChanged(int width)
{
    canvas->setPenWidth(width);
}

void MainWindow::changePenColor()
{
    QColor color = QColorDialog::getColor(canvas->getPenColor());
    if(color.isValid()){
        canvas->setPenColor(color);
        QString css = QString("background-color : %1").arg(color.name());
        penColorButton->setStyleSheet(css);
    }

}

void MainWindow::changeFillColor()
{
    QColor color = QColorDialog::getColor(canvas->getPenColor());
    if(color.isValid()){
        canvas->setFillColor(color);
        QString css = QString("background-color : %1").arg(color.name());
        fillColorButton->setStyleSheet(css);
    }

}

void MainWindow::changeFillProperty()
{
    canvas->setFill(fillCheckBox->isChecked());
}
