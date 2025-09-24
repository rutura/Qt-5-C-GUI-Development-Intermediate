#include "widget.h"
#include "ui_widget.h"
#include <stdlib.h>     /* srand, rand */
#include <time.h>       /* time */
#include <QDebug>

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);

    //Initialize
    srand (static_cast<unsigned int>(time(nullptr)));

    //Generate (1-10)
    secretNumber = rand() % 10 + 1;
    qDebug() << "Secret Number generated : " << QString::number(secretNumber);

    ui->startOverButton->setDisabled(true);

    //Clear the message label
    ui->messageLabel->setText("");
}

Widget::~Widget()
{
    delete ui;
}


void Widget::on_guessButton_clicked()
{
    guessNumber = ui->spinBox->value();
    qDebug() << "The guess number is  : " << QString::number(guessNumber);

    if( guessNumber == secretNumber)
    {
        //Congratulations
        ui->messageLabel->setText("Congratulations , number is :"+QString::number(secretNumber));
        //Disable the guess button
        ui->guessButton->setDisabled(true);
        ui->startOverButton->setDisabled(false);
    }else
    {
        if(secretNumber < guessNumber){
            ui->messageLabel->setText("Number is lower than that");
        }
        if ( secretNumber > guessNumber){
           ui->messageLabel->setText("Number is higher than that");
        }
    }

}


void Widget::on_startOverButton_clicked()
{
    //Enable the Guess Button
    ui->guessButton->setDisabled(false);

    //Disable the Start Over Button
    ui->startOverButton->setDisabled(true);

    //Put the spinbox back to 1
    ui->spinBox->setValue(1);

    //Regenerate the random number
    secretNumber = rand() % 10 + 1;

    //Clear the message label
    ui->messageLabel->setText("");
}
/*
///////////////
void Widget::on_guessButton_clicked(){
  qDebug() << "Secret Number generated: " << QString::number(secretNumber);
  this->guessNumber = ui->spinBox->value();
  qDebug() << "Guess Number is: " << QString::number(this->guessNumber);

  if(secretNumber == guessNumber){
    ui->messageLabel->setText("The number is correct, congratulations... number is: "
                              + QString::number(secretNumber));
    qDebug() << "The number is correct, congratulations... number is: " << QString::number(this->secretNumber);
  }
  else{
    if(secretNumber < guessNumber){
      ui->messageLabel->setText("Your Number is lower than that");
      qDebug() << "Your Number is lower than that";
    }
    if(secretNumber > guessNumber){
      ui->messageLabel->setText("Your Number is higher than that");
      qDebug() << "Your Number is higher than that";
    }
  }
}
*/
