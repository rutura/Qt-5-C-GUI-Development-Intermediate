#include "widget.h"
#include "./ui_widget.h"
#include "personmodel.h"
#include "persondelegate.h"
#include <QInputDialog>
#include <QMessageBox>

Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
{
    ui->setupUi(this);

    // You can share the same delegate instance (problematic):
    /*
    // You'll get a warning in the application output window when you try to change the data and hit enter through one of the views. 
    // Here is the warning:
    // ---
    // QAbstractItemView::commitData called with an editor that does not belong to this view
    // QAbstractItemView::commitData called with an editor that does not belong to this view 
    // ---
    // This is because we are sharing a single PersonDelegate instance across multiple views (listView, tableView, treeView) that also shared the same selection model. When an editor is created in one view, Qt gets confused about which view should handle the commit operation, leading to the warning. You can fix this by creating separate instances of PersonDelegate for each view, as shown (in the fixed part) the uncommented code below.

    PersonDelegate * personDelegate = new PersonDelegate(this);
    ui->listView->setItemDelegate(personDelegate);
    ui->tableView->setItemDelegate(personDelegate);
    ui->treeView->setItemDelegate(personDelegate);
    */

    // (fixed):
    PersonDelegate * listDelegate = new PersonDelegate(this);
    PersonDelegate * tableDelegate = new PersonDelegate(this);
    PersonDelegate * treeDelegate = new PersonDelegate(this);
    ui->listView->setItemDelegate(listDelegate);
    ui->tableView->setItemDelegate(tableDelegate);
    ui->treeView->setItemDelegate(treeDelegate);

    model = new PersonModel(this);

    ui->listView->setModel(model);
    ui->listView->setItemDelegate(listDelegate);

    ui->tableView->setModel(model);
    ui->tableView->setItemDelegate(tableDelegate);

    ui->treeView->setModel(model);
    ui->treeView->setItemDelegate(treeDelegate);

    ui->tableView->setSelectionModel(ui->listView->selectionModel());
    ui->treeView->setSelectionModel(ui->listView->selectionModel());
}

Widget::~Widget()
{
    delete ui;
}

void Widget::on_add_person_button_clicked()
{
    bool ok;
    QString name = QInputDialog::getText(nullptr, "Names",
                                         tr("Person name:"), QLineEdit::Normal,
                                         "Type in name", &ok);

    if( ok && !name.isEmpty()){

        int age = QInputDialog::getInt(nullptr,"Person Age","Age",20,15,120);

        Person* person = new Person(name, "blue", age, this);
        model->addPerson(person);

    }else{
        QMessageBox::information(nullptr,"Failure","Must specify name and age");
    }
}


void Widget::on_remove_person_button_clicked()
{

    QModelIndex index = ui->listView->currentIndex();
    model->removePerson(index);

}

