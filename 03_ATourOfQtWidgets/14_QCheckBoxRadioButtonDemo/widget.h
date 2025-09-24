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
    void on_windowsCheckbox_toggled(bool checked);

    void on_beerCheckBox_toggled(bool checked);

    void on_aRadioButton_toggled(bool checked);

    void on_grabData_clicked();

    void on_setStateButton_clicked();

private:
    Ui::Widget *ui;
};

#endif // WIDGET_H
