#include "mainwindow.h"
#include <QApplication>
#include <QTranslator>
#include <QSettings>
#include <QDebug>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    QTranslator translator;
    QTranslator guiTranslator;


    QSettings settings("Blikoon Technologies", "Painter App");

    QString userLanguage = settings.value("language","english").toString();

    QString systemLang = QLocale::system().name();

    qDebug() << "Sytem language is :" << systemLang;

    if(userLanguage == "default"){

        if(systemLang == "zh_CN"){
            translator.load(":/translations/chinese.qm");
            guiTranslator.load(":/translations/qt_zh_CN_official.qm");
            a.installTranslator(&translator);
            a.installTranslator(&guiTranslator);
        }

        if(systemLang == "fr_FR"){
            translator.load(":/translations/french.qm");
            guiTranslator.load(":/translations/qt_fr_FR_official.qm");
            a.installTranslator(&translator);
            a.installTranslator(&guiTranslator);

        }

    }

    if(userLanguage == "english"){
        //English loaded by default
    }

    if(userLanguage == "french"){
        translator.load(":/translations/french.qm");
        guiTranslator.load(":/translations/qt_fr_FR_official.qm");

    }

    if(userLanguage == "chinese"){
        translator.load(":/translations/chinese.qm");
        guiTranslator.load(":/translations/qt_zh_CN_official.qm");
    }

    if((userLanguage == "french") || (userLanguage == "chinese")){
           a.installTranslator(&translator);
           a.installTranslator(&guiTranslator);
       }

    MainWindow w;
    w.show();

    return a.exec();
}
