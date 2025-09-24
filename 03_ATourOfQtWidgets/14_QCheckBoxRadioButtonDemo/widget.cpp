#include "widget.h"
#include "ui_widget.h"
#include  <QButtonGroup>
#include <QDebug>

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);

    //Make the check boxes exclusive
    QButtonGroup * buttonGroup = new QButtonGroup(this);
    buttonGroup->addButton(ui->windowsCheckbox);
    buttonGroup->addButton(ui->macCheckBox);
    buttonGroup->addButton(ui->linuxCheckBox);
    buttonGroup->setExclusive(true);
}

Widget::~Widget()
{
    delete ui;
}

void Widget::on_windowsCheckbox_toggled(bool checked)
{
   if( checked)
   {
       qDebug() << "Windows Checkbox is checked";
   }else
   {
       qDebug() << "Windows Checkbox is unchecked";
   }
}

void Widget::on_beerCheckBox_toggled(bool checked)
{
    if( checked)
    {
        qDebug() << "Beer Checkbox is checked";
    }else
    {
        qDebug() << "Beer Checkbox is unchecked";
    }
}

void Widget::on_aRadioButton_toggled(bool checked)
{
    if( checked)
    {
        qDebug() << "A radiobutton  is checked";
    }else
    {
        qDebug() << "A radiobutton is unchecked";
    }
}

void Widget::on_grabData_clicked()
{
    if( ui->windowsCheckbox->isChecked())
    {
          qDebug() << "Windows Checkbox is checked";
    }else
    {
          qDebug() << "Windows Checkbox is unchecked";
    }


}

void Widget::on_setStateButton_clicked()
{
    //Exclusive
    if( ui->windowsCheckbox->isChecked()){
        ui->windowsCheckbox->setChecked(false); // Won't do this because
                                                // the group is exclusive
    }else{
        ui->windowsCheckbox->setChecked(true);
    }

    //Non exclusive checkbox group
    if( ui->beerCheckBox->isChecked()){
        ui->beerCheckBox->setChecked(false);
    }else{
        ui->beerCheckBox->setChecked(true);
    }
}
