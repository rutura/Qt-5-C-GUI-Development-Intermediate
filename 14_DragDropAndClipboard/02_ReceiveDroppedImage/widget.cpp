#include "widget.h"
#include "./ui_widget.h"
#include <QDragEnterEvent>
#include <QMimeData>
#include <QFileInfo>

Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
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
    event->acceptProposedAction();
}

void Widget::dragMoveEvent(QDragMoveEvent *event)
{
    event->acceptProposedAction();
}

void Widget::dragLeaveEvent(QDragLeaveEvent *event)
{
    event->accept();
}

void Widget::dropEvent(QDropEvent *event)
{
    if (!event->mimeData()->hasUrls()) {
        return;
    }

    const QList<QUrl> urls = event->mimeData()->urls();
    if (urls.count() != 1) {
        return;
    }

    const QFileInfo file(urls.at(0).toLocalFile());
    QPixmap pixmap;
    if (isImage(file.absoluteFilePath().toStdString()) && pixmap.load(file.absoluteFilePath())) {
        ui->label->setPixmap(pixmap.scaled(ui->label->size()));
    }


}

bool Widget::isImage(std::string_view filepath)
{
    const QFileInfo file(QString::fromStdString(std::string(filepath)));
    const QString suffix = file.suffix().toLower();
    return suffix == "png" || suffix == "jpg" || suffix == "jpeg";

}

















