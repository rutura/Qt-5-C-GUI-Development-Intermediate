#include "datetimewidget.h"
#include <QVBoxLayout>

DateTimeWidget::DateTimeWidget(QWidget *parent) : QWidget(parent)
{
    QVBoxLayout * layout = new QVBoxLayout(this);
    QFont mFont("Consolas", 20, QFont::Bold);
    QSizePolicy policy(QSizePolicy::Expanding,QSizePolicy::Fixed);


    dateString = QDate::currentDate().toString(Qt::TextDate);
    labelTop = new QLabel(this);
    labelTop->setText(dateString);
    labelTop->setFont(mFont);
    labelTop->setAlignment(Qt::AlignCenter);
    //setSizePolicy(policy);


    timeString = QTime::currentTime().toString();
    labelBottom = new QLabel(this);
    labelBottom->setText(timeString);
    labelBottom->setFont(mFont);
    labelBottom->setAlignment(Qt::AlignCenter);
    labelBottom->setSizePolicy(policy);
    QString css = QString("background-color : #00eff9; color : #fffff1");
    labelBottom->setStyleSheet(css);

    layout->addWidget(labelTop);
    layout->addWidget(labelBottom);
    setLayout(layout);
    setSizePolicy(policy);

    //Set up timer
    timer = new QTimer(this);
    timer->setInterval(1000);
    connect(timer,&QTimer::timeout,this,&DateTimeWidget::updateTime);
    timer->start();


}

void DateTimeWidget::updateTime()
{
    timeString = QTime::currentTime().toString();
    labelBottom->setText(timeString);

    if(dateString != (QDate::currentDate().toString(Qt::TextDate))){
        dateString = QDate::currentDate().toString(Qt::TextDate);
        labelTop->setText(dateString);
    }
}
