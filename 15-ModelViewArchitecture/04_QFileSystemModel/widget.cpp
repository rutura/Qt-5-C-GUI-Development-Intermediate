#include "widget.h"
#include "./ui_widget.h"
#include <QInputDialog>
#include <QMessageBox>

Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
{
    ui->setupUi(this);

    model = new QFileSystemModel(this);
    model->setReadOnly(false);

    /*
         * Sets the directory that is being watched by the model to newPath
         *  by installing a file system watcher on it. Any changes to files
         *  and directories within this directory will be reflected in the model.
     * */
    model->setRootPath(QDir::currentPath());


    ui->treeView->setModel(model);
    ui->treeView->setAlternatingRowColors(true);

    auto index = model->index(QDir::currentPath());

    ui->treeView->expand(index);
    ui->treeView->scrollTo(index);
    ui->treeView->resizeColumnToContents(0);
}

Widget::~Widget()
{
    delete ui;
}

void Widget::on_addButton_clicked()
{
    auto index = ui->treeView->currentIndex();
    if(!index.isValid()){
        return;
    }

    QString dirName = QInputDialog::getText(this,
                                            "Create Directory",
                                            "Directory name");
    if(!dirName.isEmpty()){

        if(!model->mkdir(index,dirName).isValid()){
            QMessageBox::information(this, "Create Directory",
                                     "Failed to create the directory");
        }
    }
}


void Widget::on_removeButton_clicked()
{
    auto index = ui->treeView->currentIndex();
    if(!index.isValid()){
        return;
    }

    bool ok;
    //Check to see if a dir or a file that you are deleting
    if(model->fileInfo(index).isDir()){
        ok = model->rmdir(index);
    }else{
        ok = model->remove(index);
    }

    if(!ok){
        QMessageBox::information(this, "Delete",
                                 QString("Failed to delete %1").arg(model->fileName(index)));
    }
}

