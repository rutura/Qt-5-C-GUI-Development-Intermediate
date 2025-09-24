#ifndef INDICATOR_H
#define INDICATOR_H

#include <QWidget>
#include <QTimer>

/**
 * @brief The Indicator class represents a traffic light-style indicator widget
 * with three states: normal (green), warning (yellow), and danger (red)
 */
class Indicator : public QWidget
{
    Q_OBJECT

public:
    explicit Indicator(QWidget *parent = nullptr);

    // QWidget interface
    [[nodiscard]] QSize sizeHint() const override;

public slots:
    void activateNormal();  ///< Activates the green light
    void activateWarning(); ///< Activates the yellow light
    void activateDanger();  ///< Activates the red light

protected:
    void paintEvent(QPaintEvent *event) override;

private:
    void toggleLights();

    bool m_greenActive{false};
    bool m_redActive{false};
    bool m_yellowActive{false};
    bool m_lightsOn{true};
    QTimer* m_timer{nullptr};
};

#endif // INDICATOR_H
