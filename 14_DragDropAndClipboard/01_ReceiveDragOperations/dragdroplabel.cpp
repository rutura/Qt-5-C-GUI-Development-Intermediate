#include "dragdroplabel.h"
#include <QDragEnterEvent>

DragDropLabel::DragDropLabel(QWidget *parent)
    : QLabel{parent}
{
    setMinimumSize(100, 100);
    setAlignment(Qt::AlignCenter);
    setAcceptDrops(true);
    setText(tr("DROP SPACE"));
    setAutoFillBackground(true);
}

void DragDropLabel::clear()
{
    setText(tr("DROP SPACE"));
    setBackgroundRole(QPalette::Dark);
    emit mimeChanged();
}

// What do we do when the drag operation enters our widget?
// The event parameter contains information about the drag operation.
void DragDropLabel::dragEnterEvent(QDragEnterEvent *event)
{
    setText(tr("DROP YOUR DATA HERE"));
    setBackgroundRole(QPalette::Highlight);
    event->acceptProposedAction();
    emit mimeChanged(event->mimeData());
}

// What doe we do when the drag operation moves within our widget?
void DragDropLabel::dragMoveEvent(QDragMoveEvent *event)
{
    event->acceptProposedAction();
}

// What doe we do when the drag operation leaves this widget?
void DragDropLabel::dragLeaveEvent(QDragLeaveEvent *event)
{
    clear();
}

// What do we do when the drag operation is dropped onto our widget?
void DragDropLabel::dropEvent(QDropEvent *event)
{
    //Extract the data
    const QMimeData* const mimeData = event->mimeData();

    if (mimeData->hasText()) {
        setText(mimeData->text());
        setTextFormat(Qt::PlainText);
    } else if (mimeData->hasImage()) {
        setPixmap(qvariant_cast<QPixmap>(mimeData->imageData()));
    } else if (mimeData->hasHtml()) {
        setText(mimeData->html());
        setTextFormat(Qt::RichText);
    }else if (mimeData->hasUrls()) {
        const QList<QUrl> urlList = mimeData->urls();
        QString text;
        for (const auto& url : urlList) {
            text += url.path() + "-----";
        }
        setText(text);
    } else {
        setText(tr("Data cannot be displayed"));
    }



}


















