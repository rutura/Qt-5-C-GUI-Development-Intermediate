#include "widget.h"
#include "ui_widget.h"
#include "personmodel.h"
#include <QTextStream>

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);

    PersonModel * model = new PersonModel(this);

    ui->treeView->setModel(model);

    ui->treeView->setAlternatingRowColors(true);
}

Widget::~Widget()
{
    delete ui;
}







void Widget::on_addRowButton_clicked()
{
    //Get hold of the current index and model. currentIndex() probably calls your
    //model's index() method.
    QModelIndex index = ui->treeView->selectionModel()->currentIndex();
    QAbstractItemModel *model = ui->treeView->model();

    //We insert the item past the current item. We pass the parent of the index as
    //the index because we want the inserted item to be on the same level as the current
    //item. Make this clear with a graph or image somehow.
    if (!model->insertRow(index.row()+1, index.parent()))
        return;

    //Loop through the columns setting the data to [Empty Cell] for the new inserted row.
    for (int column = 0; column < model->columnCount(index.parent()); ++column) {
        QModelIndex child = model->index(index.row()+1, column, index.parent());
        model->setData(child, QVariant("[Empty Cell]"), Qt::EditRole);
    }

}

void Widget::on_removeRowButton_clicked()
{
    QModelIndex index = ui->treeView->selectionModel()->currentIndex();
    QAbstractItemModel *model = ui->treeView->model();

    //model->removeRow(index.row(), index.parent());
    model->removeRows(index.row(),1,index.parent());

}

void Widget::on_addColumnButton_clicked()
{
    QAbstractItemModel *model = ui->treeView->model();
    int column = ui->treeView->selectionModel()->currentIndex().column();

    // Insert a column in the parent item.
    //bool changed = model->insertColumn(column + 1);
    bool changed = model->insertColumns(column+1,1);
    if (changed)
        model->setHeaderData(column + 1, Qt::Horizontal,
                             QVariant("[No header]"), Qt::EditRole);

}

void Widget::on_removeColumnButton_clicked()
{
    QAbstractItemModel *model = ui->treeView->model();
    int column = ui->treeView->selectionModel()->currentIndex().column();
    model->removeColumn(column);
}

void Widget::on_addChildButton_clicked()
{
    QModelIndex index = ui->treeView->selectionModel()->currentIndex();
    QAbstractItemModel *model = ui->treeView->model();

    //If there are zero columns under index, we insert a new column under it
    //If that fails, we get out .This will be the case when the tree is completely empty
    if (model->columnCount(index) == 0) {
        if (!model->insertColumn(0, index))
            return;
    }

    //We then insert new row
    if (!model->insertRow(0, index))
        return;

    //Loop around in each column of the new child setting all the
    for (int column = 0; column < model->columnCount(index); ++column) {

        //The new added child is always at row 0
        QModelIndex child = model->index(0, column, index);
        model->setData(child, QVariant("[Empty Cell]"), Qt::EditRole);
    }

    //Set the newly added item as the current item
    ui->treeView->selectionModel()->setCurrentIndex(model->index(0, 0, index),
                                                    QItemSelectionModel::ClearAndSelect);

}
