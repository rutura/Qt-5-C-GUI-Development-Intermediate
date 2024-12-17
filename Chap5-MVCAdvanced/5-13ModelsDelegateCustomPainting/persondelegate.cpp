#include "persondelegate.h"
#include "personmodel.h"
#include <QComboBox>
#include <QPainter>

PersonDelegate::PersonDelegate(QObject *parent) : QStyledItemDelegate(parent)
{

}

QWidget *PersonDelegate::createEditor(QWidget *parent, const QStyleOptionViewItem &option,
                                      const QModelIndex &index) const
{
    if(index.column() == 2){

        QComboBox *editor = new QComboBox(parent);

        foreach (QString color, QColor::colorNames()) {
            QPixmap mPix(50,50);
            mPix.fill(QColor(color));
            editor->addItem(QIcon(mPix),color);
        }

        return editor;
    }else{
        return QStyledItemDelegate::createEditor(parent,option,index);
    }

}

void PersonDelegate::setEditorData(QWidget *editor, const QModelIndex &index) const
{
    if(index.column() == 2){
        QComboBox *combo = static_cast<QComboBox *>(editor);
        int idx = QColor::colorNames().indexOf(index.data(Qt::DisplayRole).toString());
        combo->setCurrentIndex(idx);
    }else{
        QStyledItemDelegate::setEditorData(editor,index);
    }

}

void PersonDelegate::setModelData(QWidget *editor, QAbstractItemModel *model,
                                  const QModelIndex &index) const
{
    if(index.column() == 2){
        QComboBox *combo = static_cast<QComboBox *>(editor);
        model->setData(index,combo->currentText(),PersonModel::FavoriteColorRole);
        //model->setData(index,combo->currentText(),Qt::EditRole);
    }else{
        QStyledItemDelegate::setModelData(editor,model,index);
    }

}

void PersonDelegate::updateEditorGeometry(QWidget *editor,
                                          const QStyleOptionViewItem &option,
                                          const QModelIndex &index) const
{
    Q_UNUSED(index);

    editor->setGeometry(option.rect);

}

QSize PersonDelegate::sizeHint(const QStyleOptionViewItem &option, const QModelIndex &index) const
{
    return QStyledItemDelegate::sizeHint(option, index).
            expandedTo(QSize(64,option.fontMetrics.height() + 10));
}

void PersonDelegate::paint(QPainter *painter, const QStyleOptionViewItem &option,
                           const QModelIndex &index) const
{
     if(index.column() == 2){

         //Highlight selected cell
         if (option.state & QStyle::State_Selected)
                     painter->fillRect(option.rect, option.palette.highlight());

         //Get fav color
         QString favColor = index.data(PersonModel::FavoriteColorRole).toString();

         painter->save();

         painter->setBrush(QBrush(QColor(favColor)));

         //Draw color rect
         painter->drawRect(option.rect.adjusted(3,3,-3,-3));

         //Text Size
         QSize textSize= option.fontMetrics.size(Qt::TextSingleLine,favColor);

         painter->setBrush(QBrush(QColor(Qt::white)));


         //Adustments for inner white rectangle
         int widthAdjust = (option.rect.width() - textSize.width())/2 - 3;
         int heightAdjust = (option.rect.height() - textSize.height())/2;

         painter->drawRect(option.rect.adjusted(widthAdjust,heightAdjust,
                                                -widthAdjust,-heightAdjust));

         painter->drawText(option.rect,favColor,Qt::AlignHCenter|Qt::AlignVCenter);


         painter->restore();

     }else{
         QStyledItemDelegate::paint(painter,option,index);
     }

}
