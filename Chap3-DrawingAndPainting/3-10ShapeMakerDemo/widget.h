#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>
#include "shapecanvas.h"


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
    void on_shapeCombo_activated(int index);

    void on_penWidthSpinbox_valueChanged(int arg1);

    void on_penStyleCombobox_activated(int index);

    void on_penCapCombobox_activated(int index);

    void on_penJoinComboBox_activated(int index);

    void on_brushStyleCombobox_activated(int index);

    void on_antiAlisingCheckbox_toggled(bool checked);

    void on_transformsCheckbox_toggled(bool checked);

    void penChanged();
    void brushChanged();

private:
    Ui::Widget *ui;
    ShapeCanvas * canvas;
};

#endif // WIDGET_H
