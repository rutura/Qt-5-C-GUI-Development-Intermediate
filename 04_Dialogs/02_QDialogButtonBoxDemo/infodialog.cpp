#include "infodialog.h"
#include "ui_infodialog.h"
#include <QDebug>

InfoDialog::InfoDialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::InfoDialog)
{
    ui->setupUi(this);
}

InfoDialog::~InfoDialog()
{
    delete ui;
}

void InfoDialog::on_buttonBox_clicked(QAbstractButton *button)
{
    QDialogButtonBox::StandardButton stdButton = ui->buttonBox->standardButton(button);

    if( stdButton == QDialogButtonBox::Ok)
    {
        accept();
        qDebug() << "OK button Clicked";
    }
    /*
    if( stdButton == QDialogButtonBox::Save)
    {
        qDebug() << "Save button Clicked";
    }
    if( stdButton == QDialogButtonBox::SaveAll)
    {
        qDebug() << "SaveAll button Clicked";
    }
    if( stdButton == QDialogButtonBox::Open)
    {
        qDebug() << "Open button Clicked";
    }
    if( stdButton == QDialogButtonBox::No)
    {
        qDebug() << "No button Clicked";
    }
    if( stdButton == QDialogButtonBox::NoToAll)
    {
        qDebug() << "NoToAll button Clicked";
    }*/
    if( stdButton == QDialogButtonBox::Cancel)
    {
        qDebug() << "Cancel button Clicked";
        reject();
    }

}
