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
    void drawCar(QPainter * painter);
    void drawCarV2(QPainter * painter,QRectF rect,QColor tireColor );
    Ui::Widget *ui;

    // QWidget interface
protected:
    void paintEvent(QPaintEvent *event) override;
};

#endif // WIDGET_H
