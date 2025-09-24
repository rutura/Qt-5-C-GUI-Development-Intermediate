#include "colorlistwidget.h"
#include <QDrag>
#include <QMimeData>
#include <QDebug>

ColorListWidget::ColorListWidget(QWidget *parent) : QListWidget(parent)
{
    setMinimumWidth(200);
    setMaximumWidth(300);
    setSelectionMode(QAbstractItemView::SingleSelection);
    setViewMode(QListView::IconMode);

}

void ColorListWidget::startDrag(Qt::DropActions supportedActions)
{
    QList<QListWidgetItem *> items = selectedItems();
    if(items.count() > 0){

        QDrag* drag = new QDrag(this);
        QMimeData *mimeData = new QMimeData;

        QColor color(items[0]->text());

        mimeData->setColorData(color);

        QPixmap pix(20, 20);
        pix.fill(color);
        drag->setPixmap(pix);
        drag->setMimeData(mimeData);
        drag->exec(supportedActions);

//        if(drag->exec() == Qt::IgnoreAction){
//            qDebug() << "Drag ignored";
//        }
    }

}
