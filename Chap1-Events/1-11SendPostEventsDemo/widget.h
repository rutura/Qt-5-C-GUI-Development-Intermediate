#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>
#include "button.h"

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
    void on_button2_clicked();

private:
    Ui::Widget *ui;
    Button * button1;
};

#endif // WIDGET_H
