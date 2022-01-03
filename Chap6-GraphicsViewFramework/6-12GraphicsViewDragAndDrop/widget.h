#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>
#include "scene.h"
#include <QMap>


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


private:
    Ui::Widget *ui;
    Scene * scene;
    QMap<int,QString> shapeMap;
};

#endif // WIDGET_H
