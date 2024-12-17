#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>

namespace Ui {
class Widget;
}

class Widget : public QWidget
{
    Q_OBJECT

public:
    explicit Widget(QWidget *parent = nullptr);
    ~Widget();

private:
    void newRow();
    Ui::Widget *ui;
    QVector<QVector<QString>> table;
};

#endif // WIDGET_H
