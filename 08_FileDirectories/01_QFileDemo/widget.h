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
    void on_writeButton_clicked();

    void on_readButton_clicked();

    void on_selectFileButton_clicked();

    void on_copyFileButton_clicked();

private:
    Ui::Widget *ui;
};

#endif // WIDGET_H
