#include "widget.h"
#include "ui_widget.h"

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);

    table.append({"John","Doe","32","Farmer","Single","Gounduana","Mestkv","89"});
    table.append({"Mary","Jane","27","Teacher","Married","Verkso","Tukk","55"});
    table.append({"John","Doe","32","Farmer","Single","Gounduana","Mestkv","67"});
    table.append({"Mary","Jane","27","Teacher","Married","Verkso","Tukk","78"});
    table.append({"John","Doe","32","Farmer","Single","Gounduana","Mestkv","51"});
    table.append({"Mary","Jane","27","Teacher","Married","Verkso","Tukk","83"});
    table.append({"John","Doe","32","Farmer","Single","Gounduana","Mestkv","59"});
    table.append({"Mary","Jane","27","Teacher","Married","Verkso","Tukk","62"});
    table.append({"John","Doe","32","Farmer","Single","Gounduana","Mestkv","69"});
    table.append({"Mary","Jane","27","Teacher","Married","Verkso","Tukk","58"});
    table.append({"John","Doe","32","Farmer","Single","Gounduana","Mestkv","73"});
    table.append({"Mary","Jane","27","Teacher","Married","Verkso","Tukk","83"});
    table.append({"John","Doe","32","Farmer","Single","Gounduana","Mestkv","71"});
    table.append({"Mary","Jane","27","Teacher","Married","Verkso","Tukk","65"});
    table.append({"John","Doe","32","Farmer","Single","Gounduana","Mestkv","77"});
    table.append({"Mary","Jane","27","Teacher","Married","Verkso","Tukk","64"});
    table.append({"John","Doe","32","Farmer","Single","Gounduana","Mestkv","88"});
    table.append({"Mary","Jane","27","Teacher","Married","Verkso","Tukk","86"});
    table.append({"John","Doe","32","Farmer","Single","Gounduana","Mestkv","58"});
    table.append({"Mary","Jane","27","Teacher","Married","Verkso","Tukk","72"});

    QStringList labels;

    labels << "First Name"<<"Last Name"<<"Age"<<"Proffession"<<"Marital Status"
               <<"Country"<<"City"<<"Social Score";

    ui->tableWidget->setHorizontalHeaderLabels(labels);

    int rows = table.size();
    int columns = table[0].size();

    for( int row = 0 ; row < rows ; row++){
        newRow();
        for( int col = 0 ; col < columns ; col++){
            //We are in a table cell
            ui->tableWidget->item(row, col)->setText(table[row][col]);
        }
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
