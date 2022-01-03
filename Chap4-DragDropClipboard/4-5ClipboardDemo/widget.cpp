#include "widget.h"
#include "ui_widget.h"
#include <QKeyEvent>
#include <QDebug>
#include <QClipboard>
#include <QMimeData>
#include <QApplication>
#include <QFileInfo>

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);
}

Widget::~Widget()
{
    delete ui;
}

void Widget::keyPressEvent(QKeyEvent *event)
{
    if(event->matches(QKeySequence::Copy)){
        copy();
        event->accept();
        qDebug() << "Copy sequence detected";

    }else if (event->matches(QKeySequence::Paste)) {
        paste();
        event->accept();
        qDebug() << "Paste sequence detected";
    }else{
       QWidget::keyPressEvent(event);
    }

}

bool Widget::isImage(QString fullpath)
{
    QFileInfo file(fullpath);
        return ((file.suffix()=="png") ||
                (file.suffix() =="PNG") ||
                (file.suffix() == "jpg") ||
                (file.suffix() =="JPG")||
                (file.suffix() == "jpeg") ||
                (file.suffix() =="JPeG"));;
}

void Widget::copy()
{
    //NOP
}

void Widget::paste()
{
    const QMimeData * mimeData = QApplication::clipboard()->mimeData();

    if( mimeData->hasUrls()){

        QList<QUrl> urls = mimeData->urls();
        if(urls.count() > 1)
            return;
        QFileInfo file(urls.at(0).toLocalFile());

        if(isImage(file.absoluteFilePath())){
            QPixmap pixmap(file.absoluteFilePath());
            ui->label->setPixmap(pixmap.scaled(ui->label->size()));
        }
    }
}
