#ifndef WATERTANK_H
#define WATERTANK_H

#include <QWidget>
#include <QTimer>

class WaterTank : public QWidget
{
    Q_OBJECT
public:
    explicit WaterTank(QWidget *parent = nullptr);

signals:
    void normal();//Green
    void warning();//Yellow
    void danger();//Red

public slots:


    // QWidget interface
protected:
    void paintEvent(QPaintEvent *event) override;
    QSize sizeHint() const override;
    void wheelEvent(QWheelEvent *event) override;

private:
    int waterHeight;//Coming from the sensor on the tank
    QTimer * timer;

};

#endif // WATERTANK_H
