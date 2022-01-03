#include "widget.h"
#include "ui_widget.h"
#include <QDebug>
#include <QMouseEvent>
#include <QMenu>

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

void Widget::mousePressEvent(QMouseEvent *event)
{
    qDebug() << "Widget , Mouse Pressed at " << event->pos();
}

void Widget::mouseReleaseEvent(QMouseEvent *event)
{
    qDebug() << "Widget, Mouse Released at " << event->pos();

}

void Widget::mouseMoveEvent(QMouseEvent *event)
{
    qDebug() << "Widget ,Mouse Move at " << event->pos();

}

void Widget::closeEvent(QCloseEvent *event)
{
    qDebug() << "Widget about to close";
    //event->ignore();
}

void Widget::contextMenuEvent(QContextMenuEvent *event)
{
    qDebug() << "ContextMenu event";
    QMenu *mMenu = new QMenu(this);
    mMenu->addAction(tr("Action1"));
    mMenu->addAction(tr("Action2"));

    mMenu->popup(mapToGlobal(event->pos()));

    qDebug() << "Event x :" << event->x() << " event y : " <<event->y();

    qDebug() << "Event reason : " << event->reason();

}

void Widget::enterEvent(QEvent *event)
{
    qDebug() << "Enter event";
}

void Widget::leaveEvent(QEvent *event)
{
    qDebug() << "Leave event";
}

void Widget::keyPressEvent(QKeyEvent *event)
{
    //qDebug() << "Key pressed : "  << event->key() << " : " << event->text();

    //    if ( event->modifiers()&Qt::ShiftModifier){
    //        qDebug() << "Shift + " << event->text();
    //    }
    if ( event->modifiers()&Qt::ControlModifier){
        qDebug() << "Control + " << event->text();
    }
    if ( event->modifiers()&Qt::AltModifier){
        qDebug() << "Alt + " << event->text();
    }

    //Detect Shift+A
    if ( event->modifiers()&Qt::ShiftModifier){
        if(event->key() ==Qt::Key_A ){
            qDebug() << "Shift + A detected";
        }
    }
}

void Widget::wheelEvent(QWheelEvent *event)
{
    qDebug() << "Weel Event Delta : " << event->delta();
    qDebug() << " x : " << event->x() << ", y : " <<event->y();
    qDebug() << " Orientation : " << event->orientation();
}

void Widget::resizeEvent(QResizeEvent *event)
{
    qDebug() << "Widget resized , old size : " << event->oldSize();
        qDebug() << " new size : " << event->size();
}

void Widget::paintEvent(QPaintEvent *event)
{
    qDebug() << "Paint event triggered";
}


