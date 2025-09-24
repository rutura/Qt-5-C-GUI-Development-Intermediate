#include "rockwidget.h"
#include <QLabel>
#include <QPushButton>
#include <QMessageBox>

RockWidget::RockWidget(QWidget *parent) : QWidget(parent)
{
    //setWindowTitle("Rock Widget Here");
    //Add a label to the widget
    QLabel * label = new QLabel("This is my label",this);


    //Add a stytled widget and move it around
    QPalette label1Palette;
    label1Palette.setColor(QPalette::Window,Qt::yellow);
    label1Palette.setColor(QPalette::WindowText,Qt::blue);

    QFont label1Font("Times", 20, QFont::Bold);

    QLabel * label1 = new QLabel(this);
    label1->setAutoFillBackground(true);
    label1->setText("My colored label");
    label1->setFont(label1Font);
    label1->setPalette(label1Palette);
    label1->move(50,50);


    //Add another label
    QPalette label2Pallete;
    label2Pallete.setColor(QPalette::Window, Qt::green);
    label2Pallete.setColor(QPalette::WindowText, Qt::black);

    QLabel * mLabel2 = new QLabel(this);
    mLabel2->setAutoFillBackground(true);//If you don't set autoFillBackground this won't work.
    mLabel2->setPalette(label2Pallete);
    mLabel2->setText("This is my label2");
    mLabel2->move(70,170);
    QFont serifFont("Times", 20, QFont::Bold);
    mLabel2->setFont(serifFont);

    //Add a button and connect to slot
    QFont buttonFont("Times", 30, QFont::Bold);
    QPushButton * button = new QPushButton(this);
    button->setText("Click Me");
    button->setFont(buttonFont);
    button->move(100,250);
    connect(button,SIGNAL(clicked()),this,SLOT(buttonClicked()));

}

void RockWidget::buttonClicked()
{
    QMessageBox::information(this,"Message","You clicked on my button");
}

QSize RockWidget::sizeHint() const
{
    return QSize(500,500);
}

