#include "widget.h"
#include "ui_widget.h"
#include <QFontDialog>
#include <QMessageBox>

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);
}

Widget::~Widget()
{
    delete ui;
}

void Widget::on_chooseFontButton_clicked()
{
    bool ok;
     QFont font = QFontDialog::getFont(
                     &ok,
                 //QFont("Helvetica [Cronyx]", 10),
                 ui->label->font(),
                 this);
     if (ok) {
         ui->label->setFont(font);

     } else {
         QMessageBox::information(this,"Message","User did not choose font");
     }
}
