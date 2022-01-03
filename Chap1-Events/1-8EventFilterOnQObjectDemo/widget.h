#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>
#include "keyboardfilter.h"


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
    void on_removeFilterButton_clicked();

private:
    Ui::Widget *ui;
    KeyboardFilter * filter;
};

#endif // WIDGET_H
