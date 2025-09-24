#include "shapelist.h"
#include <QDrag>
#include <QMimeData>
#include <QDebug>

ShapeList::ShapeList(QWidget *parent) : QListWidget(parent)
{
    setMinimumWidth(200);
    setMaximumWidth(300);
    setSelectionMode(QAbstractItemView::SingleSelection);
    setViewMode(QListView::IconMode);

}

void ShapeList::startDrag(Qt::DropActions supportedActions)
{
    Q_UNUSED(supportedActions);
    QList<QListWidgetItem *> items = selectedItems();
    if(items.count()>0){

        QDrag * drag = new QDrag(this);
        QMimeData * mimeData = new QMimeData;

        QListWidgetItem * item = items[0];

        int key = item->data(Qt::UserRole).toInt();

        mimeData->setProperty("Key",QVariant::fromValue(key));

        drag->setMimeData(mimeData);
        QPixmap pix = item->icon().pixmap( 50,50 );
        drag->setPixmap( pix );

        drag->setHotSpot(pix.rect().center());

        if(drag->exec() == Qt::IgnoreAction){
            qDebug() << "Drag ignored";
        }
    }

}
