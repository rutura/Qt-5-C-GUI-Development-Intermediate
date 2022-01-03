#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>
#include <QGraphicsScene>

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
    void on_xTranslateSpinbox_valueChanged(int arg1);

    void on_yTranslateSpinbox_valueChanged(int arg1);

    void on_xScaleSpinbox_valueChanged(int arg1);

    void on_yScaleSpinbox_valueChanged(int arg1);

    void on_xShearSpinbox_valueChanged(int arg1);

    void on_yShearSpinbox_valueChanged(int arg1);

    void on_rotationSpinbox_valueChanged(int arg1);

private:
     QGraphicsItem *getSelectedItem();
    Ui::Widget *ui;
    int rotation_angle;

    QGraphicsScene * scene;
};

#endif // WIDGET_H
