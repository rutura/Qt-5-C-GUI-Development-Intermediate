#include "persondelegate.h"
#include "personmodel.h"
#include <QComboBox>

PersonDelegate::PersonDelegate(QObject *parent)
    : QStyledItemDelegate{parent}
{}


QWidget * PersonDelegate::createEditor(QWidget *parent, const QStyleOptionViewItem &option,
                                      const QModelIndex &index) const {
    if(index.column() == 2){
        //Set a custom editor widget
        QComboBox* editor = new QComboBox(parent);

        // Set black background and white text for the combobox
        editor->setStyleSheet("QComboBox { background-color: black; color: white; }"
                              "QComboBox QAbstractItemView { background-color: black; color: white; }");

        foreach(QString color, QColor::colorNames()){
            QPixmap pix(50,50);
            pix.fill(QColor(color));
            editor->addItem(QIcon(pix), color);
        }

        return editor;
    }else{
        return QStyledItemDelegate::createEditor(parent, option, index);
    }
}

void PersonDelegate::setEditorData(QWidget *editor, const QModelIndex &index) const {

    //Read the right data from the model and display that in the editor widget.
    if(index.column() == 2){

        QComboBox *combo = static_cast<QComboBox*>(editor);
        auto colorList = QColor::colorNames();
        auto currentColorString = index.data(Qt::DisplayRole).toString();
        auto idx = colorList.indexOf(currentColorString);
        combo->setCurrentIndex(idx);

    }else{
        return QStyledItemDelegate::setEditorData(editor,index);
    }


}
void PersonDelegate::setModelData(QWidget *editor, QAbstractItemModel *model,
                                  const QModelIndex &index) const {
    //Read the data from the editor and write that back into the model
    if(index.column() == 2){
        QComboBox *combo = static_cast<QComboBox*>(editor);
        model->setData(index,combo->currentText(),Qt::EditRole);
        //model->setData(index,combo->currentText(),PersonModel::FavoriteColorRole);

    }else{
        return QStyledItemDelegate::setModelData(editor,model,index);
    }

}

void PersonDelegate::updateEditorGeometry(QWidget *editor, const QStyleOptionViewItem &option,
                                          const QModelIndex &index) const {

    //Make sure that the editor widget is properly sized and styled to fit and blend in with the view
    editor->setGeometry(option.rect);
}



QSize PersonDelegate::sizeHint(const QStyleOptionViewItem &option, const QModelIndex &index) const{
    return QStyledItemDelegate::sizeHint(option,index).expandedTo(QSize(64,option.fontMetrics.height() + 10));

}

void PersonDelegate::paint(QPainter *painter, const QStyleOptionViewItem &option, const QModelIndex &index) const {

    if(index.column() == 2){

        //Get the favorite color
        QString favColor = index.data(PersonModel::FavoriteColorRole).toString();

        painter->save();

        painter->setBrush(QBrush(QColor(favColor)));// Set up the fill color

        //Draw the color rectangle
        painter->drawRect(option.rect.adjusted(3,3,-3,-3));

        //Text size
        QSize textSize = option.fontMetrics.size(Qt::TextSingleLine,favColor);

        painter->setBrush(QBrush(Qt::white)); // this is a fill color
        painter->setPen(Qt::black);	// this is the color we draw text with

        //Compute the width and height adjustments
        int widthAdjust = ((option.rect.width() - textSize.width())/2 - 3);
        int heightAdjust = ((option.rect.height() - textSize.height())/2);

        painter->drawRect(option.rect.adjusted(widthAdjust,heightAdjust,-widthAdjust,-heightAdjust));

        painter->drawText(option.rect,favColor,Qt::AlignHCenter| Qt::AlignVCenter);

        painter->restore();

    }else{
        QStyledItemDelegate::paint(painter,option,index);
    }

}
