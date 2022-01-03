#include "colorpicker.h"
#include <QVBoxLayout>
#include <QPushButton>

ColorPicker::ColorPicker(QWidget *parent) : QWidget(parent)
{
    populateColors();
    setupUi();
}

QColor ColorPicker::getColor() const
{
    return color;
}

void ColorPicker::setColor(const QColor &value)
{
    color = value;
}

void ColorPicker::button1Clicked()
{
    QString css = QString("background-color : %1")
            .arg(colorList.at(0).name());
    label->setStyleSheet(css);

    emit colorChanged(colorList[0]);
}

void ColorPicker::button2Clicked()
{
    QString css = QString("background-color : %1")
            .arg(colorList.at(1).name());
    label->setStyleSheet(css);

    emit colorChanged(colorList[1]);
}

void ColorPicker::button3Clicked()
{

    QString css = QString("background-color : %1")
            .arg(colorList.at(2).name());
    label->setStyleSheet(css);

    emit colorChanged(colorList[2]);
}

void ColorPicker::button4Clicked()
{

    QString css = QString("background-color : %1")
            .arg(colorList.at(3).name());
    label->setStyleSheet(css);

    emit colorChanged(colorList[3]);
}

void ColorPicker::button5Clicked()
{

    QString css = QString("background-color : %1")
            .arg(colorList.at(4).name());
    label->setStyleSheet(css);

    emit colorChanged(colorList[4]);
}

void ColorPicker::button6Clicked()
{

    QString css = QString("background-color : %1")
            .arg(colorList.at(5).name());
    label->setStyleSheet(css);

    emit colorChanged(colorList[5]);
}

void ColorPicker::button7Clicked()
{

    QString css = QString("background-color : %1")
            .arg(colorList.at(6).name());
    label->setStyleSheet(css);
    emit colorChanged(colorList[6]);
}

void ColorPicker::button8Clicked()
{

    QString css = QString("background-color : %1")
            .arg(colorList.at(7).name());
    label->setStyleSheet(css);

    emit colorChanged(colorList[7]);
}

void ColorPicker::button9Clicked()
{

    QString css = QString("background-color : %1")
            .arg(colorList.at(8).name());
    label->setStyleSheet(css);

    emit colorChanged(colorList[8]);
}

void ColorPicker::populateColors()
{
    colorList << Qt::red <<
                 Qt::green <<
                 Qt::blue <<
                 Qt::cyan <<
                 Qt::darkRed <<
                 Qt::darkGray <<
                 Qt::gray <<
                 Qt::yellow <<
                 Qt::darkYellow;

}

void ColorPicker::setupUi()
{
    QVBoxLayout * vLayout = new QVBoxLayout(this);
    gLayout = new QGridLayout();
    QSizePolicy policy(QSizePolicy::Minimum,QSizePolicy::Expanding);

    QPushButton * button1 = new QPushButton("one",this);
    button1->setSizePolicy(policy);
    QString css = QString("background-color : %1").arg(colorList.at(0).name());
    button1->setStyleSheet(css);
    connect(button1,&QPushButton::clicked,this,&ColorPicker::button1Clicked);

    QPushButton * button2 = new QPushButton("two",this);
    button2->setSizePolicy(policy);
    css = QString("background-color : %1").arg(colorList.at(1).name());
    button2->setStyleSheet(css);
    connect(button2,&QPushButton::clicked,this,&ColorPicker::button2Clicked);

    QPushButton * button3 = new QPushButton("three",this);
    button3->setSizePolicy(policy);
    css = QString("background-color : %1").arg(colorList.at(2).name());
    button3->setStyleSheet(css);
    connect(button3,&QPushButton::clicked,this,&ColorPicker::button3Clicked);

    QPushButton * button4 = new QPushButton("four",this);
    button4->setSizePolicy(policy);
    css = QString("background-color : %1").arg(colorList.at(3).name());
    button4->setStyleSheet(css);
    connect(button4,&QPushButton::clicked,this,&ColorPicker::button4Clicked);

    QPushButton * button5 = new QPushButton("five",this);
    button5->setSizePolicy(policy);
    css = QString("background-color : %1").arg(colorList.at(4).name());
    button5->setStyleSheet(css);
    connect(button5,&QPushButton::clicked,this,&ColorPicker::button5Clicked);

    QPushButton * button6 = new QPushButton("six",this);
    button6->setSizePolicy(policy);
    css = QString("background-color : %1").arg(colorList.at(5).name());
    button6->setStyleSheet(css);
    connect(button6,&QPushButton::clicked,this,&ColorPicker::button6Clicked);

    QPushButton * button7 = new QPushButton("seven",this);
    button7->setSizePolicy(policy);
    css = QString("background-color : %1").arg(colorList.at(6).name());
    button7->setStyleSheet(css);
    connect(button7,&QPushButton::clicked,this,&ColorPicker::button7Clicked);


    QPushButton * button8 = new QPushButton("eight",this);
    button8->setSizePolicy(policy);
    css = QString("background-color : %1").arg(colorList.at(7).name());
    button8->setStyleSheet(css);
    connect(button8,&QPushButton::clicked,this,&ColorPicker::button8Clicked);


    QPushButton * button9 = new QPushButton("nine",this);
    button9->setSizePolicy(policy);
    css = QString("background-color : %1").arg(colorList.at(8).name());
    button9->setStyleSheet(css);
    connect(button9,&QPushButton::clicked,this,&ColorPicker::button9Clicked);

    gLayout->addWidget(button1,0,0);
    gLayout->addWidget(button2,0,1);
    gLayout->addWidget(button3,0,2);

    gLayout->addWidget(button4,1,0);
    gLayout->addWidget(button5,1,1);
    gLayout->addWidget(button6,1,2);

    gLayout->addWidget(button7,2,0);
    gLayout->addWidget(button8,2,1);
    gLayout->addWidget(button9,2,2);


    label = new QLabel("Color");
    css = QString("background-color : #eeeab6");
    label->setFixedHeight(50);
    label->setStyleSheet(css);

    vLayout->addWidget(label);
    vLayout->addLayout(gLayout);
}
