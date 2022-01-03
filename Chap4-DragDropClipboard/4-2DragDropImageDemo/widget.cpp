#include "widget.h"
#include "ui_widget.h"
#include <QDragEnterEvent>
#include <QDragMoveEvent>
#include <QDragLeaveEvent>
#include <QDropEvent>
#include <QFileInfo>
#include <QMimeData>
#include <QDebug>

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);
    setAcceptDrops(true);
}

Widget::~Widget()
{
    delete ui;
}

void Widget::dragEnterEvent(QDragEnterEvent *event)
{
    event->accept();
}

void Widget::dragMoveEvent(QDragMoveEvent *event)
{
    event->accept();
}

void Widget::dragLeaveEvent(QDragLeaveEvent *event)
{
    event->accept();
}

void Widget::dropEvent(QDropEvent *event)
{
    if(event->mimeData()->hasUrls()){
        QList<QUrl> urls = event->mimeData()->urls();
        if(urls.count() > 1)
            return;

        QFileInfo file(urls.at(0).toLocalFile());
        QPixmap mPixmap;
        if(isImage(file.absoluteFilePath()) && (mPixmap.load(file.absoluteFilePath()))){
           ui->label->setPixmap(mPixmap.scaled(ui->label->size())) ;
        }

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
            (file.suffix() =="JPeG"));
}
