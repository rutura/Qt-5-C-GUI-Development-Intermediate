#include "dragdroplabel.h"
#include <QDragEnterEvent>

DragDropLabel::DragDropLabel(QWidget *parent) : QLabel(parent)
{
    setMinimumSize(100,100);
    setAlignment(Qt::AlignCenter);
    setAcceptDrops(true);
    setText("DROP SPACE");
    setAutoFillBackground(true);

}

void DragDropLabel::dragEnterEvent(QDragEnterEvent *event)
{
    setText(tr("DROP YOUR DATA HERE"));
    setBackgroundRole(QPalette::Highlight);
    event->acceptProposedAction();
    emit mimeChanged(event->mimeData());

}

void DragDropLabel::dragMoveEvent(QDragMoveEvent *event)
{
    event->acceptProposedAction();
}

void DragDropLabel::dragLeaveEvent(QDragLeaveEvent *event)
{
    clear();
}

void DragDropLabel::dropEvent(QDropEvent *event)
{
    const QMimeData * mimeData = event->mimeData();

    if(mimeData->hasText()){
        setText(mimeData->text());
        setTextFormat(Qt::PlainText);
    }else if(mimeData->hasImage()){
        setPixmap(qvariant_cast<QPixmap>(mimeData->imageData()));
    }else if(mimeData->hasHtml()) {
        setText(mimeData->html());
        setTextFormat(Qt::RichText);
    }else if(mimeData->hasUrls()){
        QList<QUrl> urlList = mimeData->urls();
        QString text;
        for (int i = 0; i < urlList.size(); ++i)
            text += urlList.at(i).path() + "-----";
        setText(text);

    }else{
        setText(tr("Data cannot be displayed"));
    }
}

void DragDropLabel::clear()
{
    setText("DROP SPACE");
    setBackgroundRole(QPalette::Dark);
    emit mimeChanged();
}
