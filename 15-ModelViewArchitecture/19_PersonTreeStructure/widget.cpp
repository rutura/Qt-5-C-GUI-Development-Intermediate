#include "widget.h"
#include "./ui_widget.h"

Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
{
    ui->setupUi(this);

    //Initialize the root person
    QVector<QVariant> rootData;
    rootData << "John Doe" << "CEO";
    rootPerson = std::make_unique<Person>(rootData);

    //Create and add the managers
    auto manager1 = std::make_unique<Person>(QVector<QVariant>{"Jane Smith", "Manager"}, rootPerson.get());
    auto manager2 = std::make_unique<Person>(QVector<QVariant>{"Bob Johnson", "Manager"}, rootPerson.get());


    // Add employees under manager1
    manager1->appendChild(std::make_unique<Person>(QVector<QVariant>{"Alice Brown", "Developer"}, manager1.get()));
    manager1->appendChild(std::make_unique<Person>(QVector<QVariant>{"Tom Wilson", "Designer"}, manager1.get()));

    // Add employees under manager2
    manager2->appendChild(std::make_unique<Person>(QVector<QVariant>{"Charlie Davis", "Developer"}, manager2.get()));
    manager2->appendChild(std::make_unique<Person>(QVector<QVariant>{"Eve Anderson", "Tester"}, manager2.get()));



    //Add managers under root
    rootPerson->appendChild(std::move(manager1));
    rootPerson->appendChild(std::move(manager2));
}

Widget::~Widget()
{
    delete ui;
}

void Widget::on_pushButton_clicked()
{

    qDebug() << "Button clicked!";
    if (rootPerson) {
        qDebug() << "Printing Organization Tree:";
        rootPerson->printTree();
    } else {
        qDebug() << "Root person is null!";
    }
}

