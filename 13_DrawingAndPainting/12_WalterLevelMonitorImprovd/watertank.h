#ifndef WATERTANK_H
#define WATERTANK_H

#include <QWidget>
#include <QTimer>

/**
 * @brief The WaterTank class represents a water tank widget that simulates
 * water level monitoring with visual feedback and status signals
 */
class WaterTank : public QWidget
{
    Q_OBJECT
    Q_PROPERTY(int waterLevel READ waterLevel WRITE setWaterLevel NOTIFY waterLevelChanged)
    Q_PROPERTY(int warningThreshold READ warningThreshold WRITE setWarningThreshold NOTIFY warningThresholdChanged)
    Q_PROPERTY(int dangerThreshold READ dangerThreshold WRITE setDangerThreshold NOTIFY dangerThresholdChanged)

public:
    static constexpr int MIN_WATER_HEIGHT = 10;
    static constexpr int MAX_WATER_HEIGHT = 290;
    static constexpr int DEFAULT_WATER_HEIGHT = 50;
    static constexpr int WATER_HEIGHT_STEP = 10;

    explicit WaterTank(QWidget *parent = nullptr);

    // QWidget interface
    [[nodiscard]] QSize sizeHint() const override;

    // Property getters and setters
    int waterLevel() const { return m_waterHeight; }
    void setWaterLevel(int height);
    int warningThreshold() const { return m_warningThreshold; }
    void setWarningThreshold(int threshold);
    int dangerThreshold() const { return m_dangerThreshold; }
    void setDangerThreshold(int threshold);

    void startSimulation();
    void stopSimulation();
    void resetWaterLevel();

signals:
    void normal();  ///< Emitted when water level is normal
    void warning(); ///< Emitted when water level is high
    void danger();  ///< Emitted when water level is critical
    void waterLevelChanged(int level);
    void warningThresholdChanged(int threshold);
    void dangerThresholdChanged(int threshold);

protected:
    void paintEvent(QPaintEvent *event) override;
    void wheelEvent(QWheelEvent *event) override;

private:
    int m_waterHeight{DEFAULT_WATER_HEIGHT}; ///< Current water height in pixels
    int m_warningThreshold{210}; ///< Warning threshold level
    int m_dangerThreshold{239}; ///< Danger threshold level
    QTimer* m_timer{nullptr};
};

#endif // WATERTANK_H
