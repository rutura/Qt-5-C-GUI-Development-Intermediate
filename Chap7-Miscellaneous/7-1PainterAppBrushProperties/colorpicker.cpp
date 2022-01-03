#include "colorpicker.h"
#include <QColorDialog>
#include <QGridLayout>

ColorPicker::ColorPicker(QWidget *parent) : QWidget(parent)
{
    populateColors();


    //Row1
    DoubleclickButton * button1 = new DoubleclickButton(this);
    button1->setFixedSize(30,30);
    setButtonColor(button1,colors[0]);
    makeConnections(button1,0);


    DoubleclickButton * button2 = new DoubleclickButton(this);
    button2->setFixedSize(30,30);
    setButtonColor(button2,colors[1]);
    makeConnections(button2,1);

    DoubleclickButton * button3 = new DoubleclickButton(this);
    button3->setFixedSize(30,30);
    setButtonColor(button3,colors[2]);
    makeConnections(button3,2);

    DoubleclickButton * button4 = new DoubleclickButton(this);
    button4->setFixedSize(30,30);
    setButtonColor(button4,colors[3]);
    makeConnections(button4,3);

    DoubleclickButton * button5 = new DoubleclickButton(this);
    button5->setFixedSize(30,30);
    setButtonColor(button5,colors[4]);
    makeConnections(button5,4);


    DoubleclickButton * button6 = new DoubleclickButton(this);
    button6->setFixedSize(30,30);
    setButtonColor(button6,colors[5]);
    makeConnections(button6,5);


    DoubleclickButton * button7 = new DoubleclickButton(this);
    button7->setFixedSize(30,30);
    setButtonColor(button7,colors[6]);
    makeConnections(button7,6);

    //Row2
    DoubleclickButton * button8 = new DoubleclickButton(this);
    button8->setFixedSize(30,30);
    setButtonColor(button8,colors[7]);
    makeConnections(button8,7);


    DoubleclickButton * button9 = new DoubleclickButton(this);
    button9->setFixedSize(30,30);
    setButtonColor(button9,colors[8]);
    makeConnections(button9,8);


    DoubleclickButton * button10 = new DoubleclickButton(this);
    button10->setFixedSize(30,30);
    setButtonColor(button10,colors[9]);
    makeConnections(button10,9);


    DoubleclickButton * button11 = new DoubleclickButton(this);
    button11->setFixedSize(30,30);
    setButtonColor(button11,colors[10]);
    makeConnections(button11,10);


    DoubleclickButton * button12 = new DoubleclickButton(this);
    button12->setFixedSize(30,30);
    setButtonColor(button12,colors[11]);
    makeConnections(button12,11);


    DoubleclickButton * button13 = new DoubleclickButton(this);
    button13->setFixedSize(30,30);
    setButtonColor(button13,colors[12]);
    makeConnections(button13,12);


    DoubleclickButton * button14 = new DoubleclickButton(this);
    button14->setFixedSize(30,30);
    setButtonColor(button14,colors[13]);
    makeConnections(button14,13);


    QGridLayout * layout = new QGridLayout(this);
    layout->addWidget(button1,0,0);
    layout->addWidget(button2,0,1);
    layout->addWidget(button3,0,2);
    layout->addWidget(button4,0,3);
    layout->addWidget(button5,0,4);
    layout->addWidget(button6,0,5);
    layout->addWidget(button7,0,6);

    layout->addWidget(button8,1,0);
    layout->addWidget(button9,1,1);
    layout->addWidget(button10,1,2);
    layout->addWidget(button11,1,3);
    layout->addWidget(button12,1,4);
    layout->addWidget(button13,1,5);
    layout->addWidget(button14,1,6);

    setLayout(layout);


}

void ColorPicker::populateColors()
{
    colors.append({QColor(34,56,78),QColor(67,156,200),QColor(134,6,98),
                   QColor(14,56,178),QColor(114,16,208),QColor(34,56,78),QColor(67,156,200),
                   QColor(51, 102, 255),QColor(255, 0, 102),QColor(204, 51, 153),
                   QColor(204, 204, 0),QColor(255, 102, 255),QColor(51, 153, 255),
                   QColor(153, 255, 153)});

}

void ColorPicker::setButtonColor(DoubleclickButton *button, QColor color)
{
    button->setStyleSheet(QString("background-color: %1")
                          .arg(color.name()));
}

void ColorPicker::makeConnections(DoubleclickButton *button, int index)
{
    connect(button,&DoubleclickButton::clicked,[=](){
        emit colorChanged(colors.at(index));
    });

    connect(button,&DoubleclickButton::doubleClicked,[=](){
        QColor color = QColorDialog::getColor(colors.at(index),this,"Pick Color");
        if(color.isValid()){
            colors.replace(index,color);
            setButtonColor(button,color);
        }
    });

}
