#include "indicator.h"
#include <QPainter>
#include <QPen>
#include <QBrush>

namespace {
    constexpr int LIGHT_WIDTH = 100;
    constexpr int LIGHT_HEIGHT = 100;
    constexpr int LIGHT_MARGIN = 5;
    constexpr int LIGHT_SPACING = 110;
    constexpr int FRAME_WIDTH = 120;
    constexpr int FRAME_HEIGHT = 330;
    constexpr int PEN_WIDTH = 3;
    constexpr int BLINK_INTERVAL = 300;
}

Indicator::Indicator(QWidget *parent)
    : QWidget(parent)
    , m_greenActive{false}
    , m_redActive{false}
    , m_yellowActive{false}
    , m_lightsOn{true}
    , m_timer{new QTimer(this)}
{
    setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    activateNormal();

    m_timer->setInterval(BLINK_INTERVAL);
    connect(m_timer, &QTimer::timeout, this, &Indicator::toggleLights);
    m_timer->start();
}

void Indicator::activateNormal()
{
    m_greenActive = true;
    m_yellowActive = m_redActive = false;
}

void Indicator::activateWarning()
{
    m_yellowActive = true;
    m_redActive = m_greenActive = false;
}

void Indicator::activateDanger()
{
    m_redActive = true;
    m_yellowActive = m_greenActive = false;
}

void Indicator::paintEvent(QPaintEvent *event)
{
    Q_UNUSED(event);
    QPainter painter(this);
    painter.setRenderHint(QPainter::Antialiasing);
    
    // Draw the frame with gradient and 3D effect
    QLinearGradient frameGradient(0, 0, FRAME_WIDTH, FRAME_HEIGHT);
    frameGradient.setColorAt(0, QColor(150, 150, 150));
    frameGradient.setColorAt(0.5, QColor(120, 120, 120));
    frameGradient.setColorAt(1, QColor(90, 90, 90));
    
    painter.setBrush(QBrush(frameGradient));
    painter.setPen(QPen(QColor(60, 60, 60), PEN_WIDTH));
    painter.drawRoundedRect(0, 0, FRAME_WIDTH, FRAME_HEIGHT, 15, 15);

    // Draw inner frame shadow
    painter.setPen(QPen(QColor(40, 40, 40), 2));
    painter.setBrush(Qt::NoBrush);
    painter.drawRoundedRect(5, 5, FRAME_WIDTH - 10, FRAME_HEIGHT - 10, 10, 10);


    // Helper function to draw enhanced lights
    const auto drawEnhancedLight = [&](int yPos, bool isActive, const QColor& activeColor) {
        // Draw light housing with metallic effect
        painter.setPen(QPen(QColor(80, 80, 80), 2));
        painter.setBrush(QColor(40, 40, 40));
        painter.drawEllipse(LIGHT_MARGIN - 5 , yPos -5, LIGHT_WIDTH + 10, LIGHT_HEIGHT + 10);
        
        // Draw the light itself
        if (isActive && m_lightsOn) {
            // Create radial gradient for glowing effect
            QRadialGradient lightGradient(LIGHT_MARGIN + LIGHT_WIDTH/2, yPos + LIGHT_HEIGHT/2, LIGHT_WIDTH/2);
            lightGradient.setColorAt(0, activeColor.lighter(150));
            lightGradient.setColorAt(0.3, activeColor);
            lightGradient.setColorAt(0.7, activeColor.darker(120));
            lightGradient.setColorAt(1, activeColor.darker(150));
            
            painter.setBrush(QBrush(lightGradient));
            painter.setPen(QPen(activeColor.darker(130), 2));
            painter.drawEllipse(LIGHT_MARGIN, yPos, LIGHT_WIDTH, LIGHT_HEIGHT);
            
            // Add highlight effect
            painter.setPen(Qt::NoPen);
            painter.setBrush(QColor(255, 255, 255, 80));
            painter.drawEllipse(LIGHT_MARGIN + 15, yPos + 15, 25, 25);
            
            // Add outer glow effect
            painter.setPen(QPen(activeColor.lighter(120), 4));
            painter.setBrush(Qt::NoBrush);
            painter.drawEllipse(LIGHT_MARGIN - 2, yPos - 2, LIGHT_WIDTH + 4, LIGHT_HEIGHT + 4);

        } else {
            // Inactive light with subtle gradient
            QRadialGradient inactiveGradient(LIGHT_MARGIN + LIGHT_WIDTH/2, yPos + LIGHT_HEIGHT/2, LIGHT_WIDTH/2);
            inactiveGradient.setColorAt(0, QColor(60, 60, 60));
            inactiveGradient.setColorAt(0.7, QColor(30, 30, 30));
            inactiveGradient.setColorAt(1, QColor(10, 10, 10));
            
            painter.setBrush(QBrush(inactiveGradient));
            painter.setPen(QPen(QColor(20, 20, 20), 2));
            painter.drawEllipse(LIGHT_MARGIN, yPos, LIGHT_WIDTH, LIGHT_HEIGHT);
        }
    };

    // Draw the three lights with labels
    if (m_redActive) {
        drawEnhancedLight(LIGHT_MARGIN, true, QColor(255, 50, 50));
        drawEnhancedLight(LIGHT_SPACING, false, Qt::green);
        drawEnhancedLight(LIGHT_SPACING * 2, false, Qt::yellow);
    } else if (m_yellowActive) {
        drawEnhancedLight(LIGHT_MARGIN, false, Qt::red);
        drawEnhancedLight(LIGHT_SPACING, false, Qt::green);
        drawEnhancedLight(LIGHT_SPACING * 2, true, QColor(255, 255, 50));
    } else if (m_greenActive) {
        drawEnhancedLight(LIGHT_MARGIN, false, Qt::red);
        drawEnhancedLight(LIGHT_SPACING, true, QColor(50, 255, 50));
        drawEnhancedLight(LIGHT_SPACING * 2, false, Qt::yellow);
    }


}

QSize Indicator::sizeHint() const
{
    return QSize(FRAME_WIDTH, FRAME_HEIGHT + 20); // Add some padding
}

void Indicator::toggleLights()
{
    m_lightsOn = !m_lightsOn;
    update();
}
