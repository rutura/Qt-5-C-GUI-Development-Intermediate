#include "container.h"
#include <QLabel>
#include <QPainter>
#include <QMouseEvent>
#include <QApplication>
#include <QMimeData>
#include <QDrag>
#include "pixmapmime.h"

Container::Container(QWidget *parent)
    : QWidget{parent}
{
    setMinimumSize(150, 150);
    setAcceptDrops(true);

    auto *qtIcon = new QLabel(this);
    qtIcon->setPixmap(QPixmap{":/images/qt.png"});
    qtIcon->move(20, 20);
    qtIcon->show();
    qtIcon->setAttribute(Qt::WA_DeleteOnClose);

    auto *cppIcon = new QLabel(this);
    cppIcon->setPixmap(QPixmap{":/images/cpp.png"});
    cppIcon->move(150, 20);
    cppIcon->show();
    cppIcon->setAttribute(Qt::WA_DeleteOnClose);

    auto *terminalIcon = new QLabel(this);
    terminalIcon->setPixmap(QPixmap{":/images/terminal.png"});
    terminalIcon->move(20, 150);
    terminalIcon->show();
    terminalIcon->setAttribute(Qt::WA_DeleteOnClose);
}


void Container::mousePressEvent(QMouseEvent *event)
{
    if (event->button() == Qt::LeftButton)
        startPos = event->pos();
    QWidget::mousePressEvent(event);
}

void Container::mouseMoveEvent(QMouseEvent *event)
{

    if (event->buttons() & Qt::LeftButton) {

        int distance = (event->pos() - startPos).manhattanLength();

        if (distance >= QApplication::startDragDistance())
        {
            //Start Drag Operation
            QLabel * child = static_cast<QLabel *>(childAt(event->pos()));
            if(!child)
                return;

            //We have a label below the event position
            //Package the data
            QPixmap mPixmap = child->pixmap();
            auto *mimeData = new PixmapMime(mPixmap,
                                            QPoint(event->pos() - child->pos()),
                                            "Item icon");

            QDrag * drag = new QDrag(this);
            drag->setMimeData(mimeData);
            drag->setPixmap(mPixmap);
            drag->setHotSpot(event->pos() - child->pos()); // Make sure the cursor is at the right position relative to the dragged item

            //Blur the original label
            QPixmap tempPix = mPixmap;
            QPainter painter(&tempPix);
            painter.fillRect(tempPix.rect(),QColor(127, 127, 127, 127)); // Semi-transparent effect
            child->setPixmap(tempPix);

            //Call to drag->exec() is blocking
            if(drag->exec(Qt::MoveAction | Qt::CopyAction,Qt::CopyAction)
                == Qt::MoveAction){
                //Move data
                qDebug()<< "Moving data";
                child->close(); // We assume the data has made it to the new widget, so we close(delete) the original widget
            }else{
                //Copy action
                child->setPixmap(mPixmap);
                qDebug() << "Copying data";
            }

        }

    }
}

void Container::paintEvent(QPaintEvent *event)
{
    QPainter painter(this);
    painter.drawRoundedRect(0,5,width()-10, height()-10,3,3);

    QWidget::paintEvent(event);

}

void Container::dragEnterEvent(QDragEnterEvent *event)
{
    if (const auto *mimeData = qobject_cast<const PixmapMime*>(event->mimeData())) {
        if (event->source() == this) {
            event->setDropAction(Qt::MoveAction);
            event->accept();
        } else {
            event->acceptProposedAction();
        }
    } else {
        event->ignore();
    }
}

void Container::dropEvent(QDropEvent *event)
{
    const auto *mimeData = qobject_cast<const PixmapMime*>(event->mimeData());
    if (!mimeData) {
        event->ignore();
        return;
    }

    //Extract the data
    QPixmap mPixmap = mimeData->pix();
    QPoint offset = mimeData->offset();

    //Create a label that we will drop
    QLabel * newLabel = new QLabel(this);
    newLabel->setPixmap(mPixmap);
    newLabel->move(event->position().toPoint() - offset);
    newLabel->show();
    newLabel->setAttribute(Qt::WA_DeleteOnClose);

    if (event->source() == this) {
        event->setDropAction(Qt::MoveAction);
        event->accept();
            //event->ignore();
    } else {
        event->acceptProposedAction();
    }
}
















