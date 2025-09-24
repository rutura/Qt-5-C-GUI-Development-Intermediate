#include "widget.h"
#include "./ui_widget.h"
#include "personmodel.h"

Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
{
    ui->setupUi(this);

    //Create an object of the model
    PersonModel * model = new PersonModel(this);
    ui->treeView->setModel(model);
}

Widget::~Widget()
{
    delete ui;
}

/*
First get the currently selected item's index and the tree model. Then insert a new row after the currently selected item (at index.row()+1) at the same hierarchical level (using index.parent()). After inserting the row, populate each column of the new row with placeholder text "[Empty Cell]".
*/
void Widget::on_AddRowButton_clicked()
{
    QModelIndex index = ui->treeView->selectionModel()->currentIndex();
    QAbstractItemModel* model = ui->treeView->model();

    if(!model->insertRow(index.row() + 1, index.parent()))
        return;
    //Loop through the colums to put in initial data.
    for(int column = 0; column < model->columnCount(index.parent()); ++column){
        QModelIndex child = model->index(index.row() + 1, column, index.parent());
        model->setData(child, QVariant("[Empty Cell]"), Qt::EditRole);
    }
}


/*
Get the currently selected item and remove that row from the tree model. This removes the selected item and all its children from the tree structure.
*/
void Widget::on_RemoveRowButton_clicked()
{
    QModelIndex  index = ui->treeView->selectionModel()->currentIndex();
    QAbstractItemModel* model = ui->treeView->model();
    model->removeRows(index.row(),1,index.parent());
}


/*
Add a new child item under the currently selected tree item. Unlike adding a row which adds a sibling, this creates a new item as a child of the selected item by using the selected index as the parent. We insert the new child at position 0 (making it the first child), initialize all its columns with "[Empty Cell]", and then update the selection to focus on the newly created child item.
QItemSelectionModel::ClearAndSelect clears the current selection and selects the new child item, making it the focus of the tree view.
*/
void Widget::on_AddChildbutton_clicked()
{
    QModelIndex index = ui->treeView->selectionModel()->currentIndex();
    QAbstractItemModel* model = ui->treeView->model();

    if(!model->insertRow(0, index))
        return;
    //Loop through the colums to put in initial data.
    for(int column = 0; column < model->columnCount(index.parent()); ++column){
        QModelIndex child = model->index(0, column, index);
        model->setData(child, QVariant("[Empty Cell]"), Qt::EditRole);
    }
    ui->treeView->selectionModel()->setCurrentIndex(model->index(0, 0, index),
                                                    QItemSelectionModel::ClearAndSelect);


}

