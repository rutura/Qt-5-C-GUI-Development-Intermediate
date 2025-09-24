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
    void normal();  ///< Emitted when water level is normal
    void warning(); ///< Emitted when water level is high
    void danger();  ///< Emitted when water level is critical

    // QWidget interface
public:
    QSize sizeHint() const override;
    void paintEvent(QPaintEvent *event) override;

protected:
    void wheelEvent(QWheelEvent *event) override;

private:
    static constexpr int DEFAULT_WATER_HEIGHT = 50;
    static constexpr int MIN_WATER_HEIGHT = 10;
    static constexpr int WATER_HEIGHT_STEP = 10;

    int m_waterHeight{DEFAULT_WATER_HEIGHT}; ///< Current water height in pixels
    QTimer* m_timer{nullptr};

};

#endif // WATERTANK_H
