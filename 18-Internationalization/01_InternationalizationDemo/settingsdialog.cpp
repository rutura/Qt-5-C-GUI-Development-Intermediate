#include "settingsdialog.h"
#include "ui_settingsdialog.h"
#include <QDebug>
#include <QSettings>

SettingsDialog::SettingsDialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::SettingsDialog)
{
    ui->setupUi(this);
}

SettingsDialog::~SettingsDialog()
{
    delete ui;
}

void SettingsDialog::on_buttonBox_accepted()
{
    qDebug() << "Pressed OK";
    QSettings settings("Blikoon Technologies", "Painter App");

    switch (ui->languageCombobox->currentIndex()) {

    case 0 : {
        //Default
        qDebug() << "Active language is default";
        settings.setValue("language","default");

        break;
    }
    case 1 : {
        //English
        qDebug() << "Active language is english";
        settings.setValue("language","english");

        break;
    }
    case 2 : {
        //French
        qDebug() << "Active language is french";
        settings.setValue("language","french");

        break;
    }
    case 3 : {
        //Chinese
        qDebug() << "Active language is chinese";
        settings.setValue("language","chinese");

        break;
    }

    }
}

void SettingsDialog::on_buttonBox_rejected()
{
    qDebug() << "Pressed Cancel";
}
