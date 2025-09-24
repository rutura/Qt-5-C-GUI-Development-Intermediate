#include "widget.h"
#include "./ui_widget.h"
#include <QFileInfo>
#include <QKeyEvent>
#include <QMimeData>
#include <QApplication>
#include <QClipboard>

Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
{
    ui->setupUi(this);
}

Widget::~Widget()
{
    delete ui;
}


void Widget::keyPressEvent(QKeyEvent *event)
{
        if (event->matches(QKeySequence::Copy)) {
            copy();
            event->accept();
            qDebug() << "Copy sequence detected";
        } else if (event->matches(QKeySequence::Paste)) {
            paste();
            event->accept();
            qDebug() << "Paste sequence detected";
        } else {
            QWidget::keyPressEvent(event);
        }
}

void Widget::copy()
{
    // NOP - No operation
}


void Widget::paste()
{
    const QMimeData* mimeData = QApplication::clipboard()->mimeData();

    if (mimeData->hasUrls()) {

        const QList<QUrl> urls = mimeData->urls();
        if (urls.count() != 1) {
            return;
        }

        const QFileInfo file(urls.at(0).toLocalFile());
        if (isImage(file.absoluteFilePath().toStdString())) {
            const QPixmap pixmap(file.absoluteFilePath());
            ui->label->setPixmap(pixmap.scaled(ui->label->size()));
        }
    }
}

bool Widget::isImage(std::string_view fullpath)
{
    QFileInfo file(QString::fromStdString(std::string(fullpath)));
    const auto suffix = file.suffix().toLower();
    return suffix == "png" || suffix == "jpg" || suffix == "jpeg";
}
