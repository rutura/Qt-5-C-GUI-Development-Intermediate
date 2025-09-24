#include "customdialog.h"
#include "ui_customdialog.h"

CustomDialog::CustomDialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::CustomDialog)
{
    ui->setupUi(this);

    //Set stylesheet on a specific container widget
    ui->pushButton->setStyleSheet("background-color : red;color : white ;");
    //ui->pushButton->setStyleSheet("QPushButton{background-color : red;color : white ;}");
}

CustomDialog::~CustomDialog()
{
    delete ui;
}
