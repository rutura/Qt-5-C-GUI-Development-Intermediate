#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>
#include "scene.h"

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
    void on_startGameButton_clicked();

private:
    Ui::Widget *ui;

    Scene * scene;
};

#endif // WIDGET_H
