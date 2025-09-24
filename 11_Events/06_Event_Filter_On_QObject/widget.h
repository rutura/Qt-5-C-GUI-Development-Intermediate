#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>
#include <memory>
#include "keyboardfilter.h"

QT_BEGIN_NAMESPACE
namespace Ui {
class Widget;
}
QT_END_NAMESPACE

class Widget : public QWidget
{
    Q_OBJECT

public:
    Widget(QWidget *parent = nullptr);
    ~Widget();

private slots:
    void on_remove_Filter_Button_clicked();

private:
    Ui::Widget *ui;
    KeyboardFilter* filter{nullptr};

};
#endif // WIDGET_H
