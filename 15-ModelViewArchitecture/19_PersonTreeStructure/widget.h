#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>
#include "person.h"
#include <memory>

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
    void on_pushButton_clicked();

private:
    Ui::Widget *ui;
    std::unique_ptr<Person> rootPerson;
};
#endif // WIDGET_H
