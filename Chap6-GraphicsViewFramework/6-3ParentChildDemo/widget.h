#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>
#include <QGraphicsScene>
#include <QGraphicsView>

namespace Ui {
class Widget;
}

class Widget : public QWidget
{
    Q_OBJECT

public:
    explicit Widget(QWidget *parent = nullptr);
    ~Widget();

private slots:
    void on_showHideButton_clicked();

    void on_removeItem_clicked();

private:
    Ui::Widget *ui;
    QGraphicsScene * scene;
    QGraphicsView * view;
    QGraphicsRectItem * rect1;
};

#endif // WIDGET_H
