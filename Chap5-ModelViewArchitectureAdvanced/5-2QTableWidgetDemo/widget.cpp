#include "widget.h"
#include "ui_widget.h"

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);

    // table.append({"John","Doe","32","Farmer","Single","Gounduana","Mestkv","89"});
    // table.append({"Mary","Jane","27","Teacher","Married","Verkso","Tukk","55"});
    // table.append({"John","Doe","32","Farmer","Single","Gounduana","Mestkv","67"});
    // table.append({"Mary","Jane","27","Teacher","Married","Verkso","Tukk","78"});
    // table.append({"John","Doe","32","Farmer","Single","Gounduana","Mestkv","51"});
    // table.append({"Mary","Jane","27","Teacher","Married","Verkso","Tukk","83"});
    // table.append({"John","Doe","32","Farmer","Single","Gounduana","Mestkv","59"});
    // table.append({"Mary","Jane","27","Teacher","Married","Verkso","Tukk","62"});
    // table.append({"John","Doe","32","Farmer","Single","Gounduana","Mestkv","69"});
    // table.append({"Mary","Jane","27","Teacher","Married","Verkso","Tukk","58"});
    // table.append({"John","Doe","32","Farmer","Single","Gounduana","Mestkv","73"});
    // table.append({"Mary","Jane","27","Teacher","Married","Verkso","Tukk","83"});
    // table.append({"John","Doe","32","Farmer","Single","Gounduana","Mestkv","71"});
    // table.append({"Mary","Jane","27","Teacher","Married","Verkso","Tukk","65"});
    // table.append({"John","Doe","32","Farmer","Single","Gounduana","Mestkv","77"});
    // table.append({"Mary","Jane","27","Teacher","Married","Verkso","Tukk","64"});
    // table.append({"John","Doe","32","Farmer","Single","Gounduana","Mestkv","88"});
    // table.append({"Mary","Jane","27","Teacher","Married","Verkso","Tukk","86"});
    // table.append({"John","Doe","32","Farmer","Single","Gounduana","Mestkv","58"});
    // table.append({"Mary","Jane","27","Teacher","Married","Verkso","Tukk","72"});

    table.append(Person{"John","Doe",32,"Farmer",MaritalStatus::SINGLE,"Gounduana","Mestkv",89});
    table.append(Person{"Mary","Jane",27,"Teacher",MaritalStatus::MARRIED,"Verkso","Tukk",55});
    table.append(Person{"John","Doe",32,"Farmer",MaritalStatus::SINGLE,"Gounduana","Mestkv",67});
    table.append(Person{"Mary","Jane",27,"Teacher",MaritalStatus::MARRIED,"Verkso","Tukk",78});
    table.append(Person{"John","Doe",32,"Farmer",MaritalStatus::SINGLE,"Gounduana","Mestkv",51});
    table.append(Person{"Mary","Jane",27,"Teacher",MaritalStatus::MARRIED,"Verkso","Tukk",83});
    table.append(Person{"John","Doe",32,"Farmer",MaritalStatus::SINGLE,"Gounduana","Mestkv",59});
    table.append(Person{"Mary","Jane",27,"Teacher",MaritalStatus::MARRIED,"Verkso","Tukk",62});
    table.append(Person{"John","Doe",32,"Farmer",MaritalStatus::SINGLE,"Gounduana","Mestkv",69});
    table.append(Person{"Mary","Jane",27,"Teacher",MaritalStatus::MARRIED,"Verkso","Tukk",58});
    table.append(Person{"John","Doe",32,"Farmer",MaritalStatus::SINGLE,"Gounduana","Mestkv",73});
    table.append(Person{"Mary","Jane",27,"Teacher",MaritalStatus::MARRIED,"Verkso","Tukk",83});
    table.append(Person{"John","Doe",32,"Farmer",MaritalStatus::SINGLE,"Gounduana","Mestkv",71});
    table.append(Person{"Mary","Jane",27,"Teacher",MaritalStatus::MARRIED,"Verkso","Tukk",65});
    table.append(Person{"John","Doe",32,"Farmer",MaritalStatus::SINGLE,"Gounduana","Mestkv",77});
    table.append(Person{"Mary","Jane",27,"Teacher",MaritalStatus::MARRIED,"Verkso","Tukk",64});
    table.append(Person{"John","Doe",32,"Farmer",MaritalStatus::SINGLE,"Gounduana","Mestkv",88});
    table.append(Person{"Mary","Jane",27,"Teacher",MaritalStatus::MARRIED,"Verkso","Tukk",86});
    table.append(Person{"John","Doe",32,"Farmer",MaritalStatus::SINGLE,"Gounduana","Mestkv",58});
    table.append(Person{"Mary","Jane",27,"Teacher",MaritalStatus::MARRIED,"Verkso","Tukk",72});

    QStringList labels;

    labels << "First Name"<<"Last Name"<<"Age"<<"Proffession"<<"Marital Status"
               <<"Country"<<"City"<<"Social Score";

    ui->tableWidget->setHorizontalHeaderLabels(labels);

    int rows = table.size();
    // int columns = table[0].size();

    for( int row = 0 ; row < rows ; row++){
        newRow();
        ui->tableWidget->item(row, 0)->setText(table[row].firstname);
        ui->tableWidget->item(row, 1)->setText(table[row].lastname);
        ui->tableWidget->item(row, 2)->setText(QString::number(table[row].age));
        ui->tableWidget->item(row, 3)->setText(table[row].occupation);
        ui->tableWidget->item(row, 4)->setText(maritalStatusToString(table[row].maritalStatus));
        ui->tableWidget->item(row, 5)->setText(table[row].county);
        ui->tableWidget->item(row, 6)->setText(table[row].country);
        ui->tableWidget->item(row, 7)->setText(QString::number(table[row].postalCode));
        // for( int col = 0 ; col < columns ; col++){
        //     //We are in a table cell
        //     ui->tableWidget->item(row, col)->setText(table[row][col]);
        // }
    }

    ui->tableWidget->setAlternatingRowColors(true);
}

Widget::~Widget()
{
    delete ui;
}

void Widget::newRow()
{
    int row = ui->tableWidget->rowCount();

    ui->tableWidget->insertRow(row);

    QTableWidgetItem * first = nullptr;

    for(int i =0; i < 8; i++){
        QTableWidgetItem * item = new QTableWidgetItem;
        if(i == 0)
            first = item;
        item->setTextAlignment(Qt::AlignRight | Qt::AlignVCenter);
        ui->tableWidget->setItem(row,i,item);
    }

    if(first)
        ui->tableWidget->setCurrentItem(first);

}
