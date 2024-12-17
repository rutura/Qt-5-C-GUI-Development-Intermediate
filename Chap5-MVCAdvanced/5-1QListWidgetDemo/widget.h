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

private slots:
    void on_readDataButton_clicked();

private:
    Ui::Widget *ui;
    QStringList fruitList;
};

#endif // WIDGET_H
