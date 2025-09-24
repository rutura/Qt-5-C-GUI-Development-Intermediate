#include "widget.h"
#include "./ui_widget.h"
#include <QDebug>
#include <QMouseEvent>
#include <QCloseEvent>
#include <QMenu>

Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
{
    ui->setupUi(this);
}

Widget::~Widget()
{
    delete ui;
}

void Widget::mousePressEvent(QMouseEvent *event)
{
    qDebug() << "\n=== Mouse Press Event ===";
    qDebug() << "Position (local):" << event->position().toPoint();
    qDebug() << "Position (global):" << event->globalPosition().toPoint();
    qDebug() << "Button:" << [event]() {
        switch (event->button()) {
        case Qt::LeftButton: return "Left Button";
        case Qt::RightButton: return "Right Button";
        case Qt::MiddleButton: return "Middle Button";
        default: return "Other Button";
        }
    }();
    qDebug() << "Buttons held: " << event->buttons();
    qDebug() << "Modifiers: " << event->modifiers();

}


void Widget::mouseMoveEvent(QMouseEvent *event)
{
    qDebug() << "\n=== Mouse Move Event ===";
    qDebug() << "Position (local):" << event->position().toPoint();
    qDebug() << "Position (global):" << event->globalPosition().toPoint();
    qDebug() << "Buttons held:" << event->buttons();
    qDebug() << "Modifiers:" << event->modifiers();
}

void Widget::mouseReleaseEvent(QMouseEvent *event)
{
    qDebug() << "\n=== Mouse Release Event ===";
    qDebug() << "Position (local):" << event->position().toPoint();
    qDebug() << "Position (global):" << event->globalPosition().toPoint();
    qDebug() << "Button released:" << [event]() {
        switch (event->button()) {
        case Qt::LeftButton: return "Left Button";
        case Qt::RightButton: return "Right Button";
        case Qt::MiddleButton: return "Middle Button";
        default: return "Other Button";
        }
    }();
}



void Widget::closeEvent(QCloseEvent *event)
{
    qDebug() << "\n=== Close Event ===";
    qDebug() << "Spontaneous:" << event->spontaneous();
    qDebug() << "Type:" << event->type();
}


void Widget::contextMenuEvent(QContextMenuEvent *event)
{
    qDebug() << "\n=== Context Menu Event ===";
    qDebug() << "Position (local): (" << event->x() << "," << event->y() << ")";
    qDebug() << "Position (global):" << event->globalPos();
    qDebug() << "Reason:" << [event]() {
        switch (event->reason()) {
        case QContextMenuEvent::Mouse: return "Mouse (right-click)";
        case QContextMenuEvent::Keyboard: return "Keyboard (menu key)";
        case QContextMenuEvent::Other: return "Other";
        default: return "Unknown";
        }
    }();

    //Create a menu
    QMenu menu(this);
    menu.addAction("Action1");
    menu.addAction("Action2");
    //menu.exec(mapToGlobal(event->pos()));

    QAction* selectedAction = menu.exec(mapToGlobal(event->pos()));
    if(selectedAction){
        qDebug() << "Selected action:" << selectedAction->text();
    }else{
        qDebug() << "No action selected (menu dismissed)";
    }
}


void Widget::enterEvent(QEnterEvent *event)
{
    qDebug() << "\n=== Enter Event ===";
    qDebug() << "Position (local):" << event->position().toPoint();
    qDebug() << "Position (global):" << event->globalPosition().toPoint();
}

void Widget::leaveEvent(QEvent *event)
{
    qDebug() << "\n=== Leave Event ===";
    qDebug() << "Type: " << event->type();
    qDebug() << "Spontaneous: " << event->spontaneous();
}


void Widget::keyPressEvent(QKeyEvent *event)
{
    qDebug() << "\n=== Key Press Event ===";
    qDebug() << "Key:" << event->key();
    qDebug() << "Text:" << event->text();
    qDebug() << "Modifiers:" << [event]() {
        QStringList mods;
        if (event->modifiers() & Qt::ShiftModifier) mods << "Shift";
        if (event->modifiers() & Qt::ControlModifier) mods << "Control";
        if (event->modifiers() & Qt::AltModifier) mods << "Alt";
        if (event->modifiers() & Qt::MetaModifier) mods << "Meta";
        return mods.join(" + ");
    }();
    qDebug() << "Is auto repeat:" << event->isAutoRepeat();
    qDebug() << "Native modifiers:" << event->nativeModifiers();
}

void Widget::wheelEvent(QWheelEvent *event)
{
    qDebug() << "\n=== Wheel Event ===";
    qDebug() << "Position (local):" << event->position();
    qDebug() << "Position (global):" << event->globalPosition();
    qDebug() << "Pixel Delta:" << event->pixelDelta();
    qDebug() << "Angle Delta:" << event->angleDelta();
    qDebug() << "Buttons:" << event->buttons();
    qDebug() << "Modifiers:" << event->modifiers();
    qDebug() << "Inverted:" << event->inverted();
    qDebug() << "Phase:" << event->phase();

}

void Widget::paintEvent(QPaintEvent *event)
{
    qDebug() << "\n=== Paint Event ===";
    qDebug() << "Region to paint:" << event->region();
    qDebug() << "Rectangle to paint:" << event->rect();
    qDebug() << "Is region exposed:" << !event->region().isEmpty();

}

void Widget::resizeEvent(QResizeEvent *event)
{
    qDebug() << "\n=== Resize Event ===";
    qDebug() << "Old size:" << event->oldSize();
    qDebug() << "New size:" << event->size();
    qDebug() << "Spontaneous:" << event->spontaneous();
}