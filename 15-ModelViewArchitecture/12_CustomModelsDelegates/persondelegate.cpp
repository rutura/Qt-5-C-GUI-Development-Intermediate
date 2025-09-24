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