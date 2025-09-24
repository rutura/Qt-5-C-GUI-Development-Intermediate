#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>
#include "personmodel.h"

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
    void on_add_person_button_clicked();

    void on_remove_person_button_clicked();

private:
    Ui::Widget *ui;
    PersonModel * model;
};
#endif // WIDGET_H
