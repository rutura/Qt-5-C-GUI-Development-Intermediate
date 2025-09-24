#include "watertank.h"
#include <QPainter>
#include <QPainterPath>
#include <QWheelEvent>
#include <QTimer>
#include <cmath>

namespace {
    constexpr int TANK_LEFT = 10;
    constexpr int TANK_TOP = 10;
    constexpr int TANK_BOTTOM = 300;
    constexpr int TANK_RIGHT = 300;
    constexpr int TANK_WIDTH = 290;
    constexpr int PEN_WIDTH = 3;
    constexpr int UPDATE_INTERVAL = 1000;
    constexpr int WATER_INCREMENT = 15;
}

WaterTank::WaterTank(QWidget *parent)
    : QWidget(parent)
    , m_waterHeight{DEFAULT_WATER_HEIGHT}
    , m_warningThreshold{210}
    , m_dangerThreshold{239}
    , m_timer{new QTimer(this)}
{
    setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    
    m_timer->setInterval(UPDATE_INTERVAL);
    connect(m_timer, &QTimer::timeout, this, [this]() {
        setWaterLevel(m_waterHeight + WATER_INCREMENT);
    });
}

void WaterTank::paintEvent(QPaintEvent *event)
{
    Q_UNUSED(event);
    
    QPainter painter(this);
    painter.setRenderHint(QPainter::Antialiasing);
    
    // Draw shadow effect first
    painter.setPen(Qt::NoPen);
    painter.setBrush(QColor(0, 0, 0, 50));
    painter.drawRect(TANK_LEFT + 5, TANK_TOP + 5, TANK_WIDTH, TANK_BOTTOM - TANK_TOP);


    
    // Draw tank background with beautiful gradient
    QLinearGradient tankGradient(TANK_LEFT, TANK_TOP, TANK_RIGHT, TANK_BOTTOM);
    tankGradient.setColorAt(0, QColor(250, 250, 250));
    tankGradient.setColorAt(0.5, QColor(230, 230, 230));
    tankGradient.setColorAt(1, QColor(200, 200, 200));
    painter.setBrush(QBrush(tankGradient));
    painter.setPen(QPen(QColor(180, 180, 180), 1));
    painter.drawRect(TANK_LEFT, TANK_TOP, TANK_WIDTH, TANK_BOTTOM - TANK_TOP);


    // Draw metallic tank outline with 3D effect
    QPen tankPen(QColor(60, 60, 60), PEN_WIDTH);
    painter.setPen(tankPen);
    painter.setBrush(Qt::NoBrush);
    
    // Draw main tank outline with rounded corners
    QPainterPath tankPath;
    tankPath.moveTo(TANK_LEFT, TANK_TOP + 10);
    tankPath.quadTo(TANK_LEFT, TANK_TOP, TANK_LEFT + 10, TANK_TOP);
    tankPath.lineTo(TANK_RIGHT - 10, TANK_TOP);
    tankPath.quadTo(TANK_RIGHT, TANK_TOP, TANK_RIGHT, TANK_TOP + 10);
    tankPath.lineTo(TANK_RIGHT, TANK_BOTTOM);
    tankPath.lineTo(TANK_LEFT, TANK_BOTTOM);
    tankPath.closeSubpath();
    
    painter.setPen(QPen(QColor(80, 80, 80), PEN_WIDTH));
    painter.drawPath(tankPath);
    
    // Draw tank rivets for industrial look
    painter.setPen(Qt::NoPen);
    painter.setBrush(QColor(120, 120, 120));
    for (int i = 0; i < 6; ++i) {
        int rivetY = TANK_TOP + 30 + i * 40;
        painter.drawEllipse(TANK_LEFT - 6, rivetY - 3, 6, 6);
        painter.drawEllipse(TANK_RIGHT + 2, rivetY - 3, 6, 6);
    }
    
    // Draw water with enhanced gradient and animation effect
    if (m_waterHeight > 0) {
        QLinearGradient waterGradient(TANK_LEFT, TANK_BOTTOM - m_waterHeight, TANK_LEFT, TANK_BOTTOM);
        
        // Dynamic water color based on level with more vibrant colors
        QColor waterColor;
        if (m_waterHeight <= m_warningThreshold) {
            waterColor = QColor(30, 144, 255); // Bright blue
        } else if (m_waterHeight <= m_dangerThreshold) {
            waterColor = QColor(255, 140, 0); // Dark orange
        } else {
            waterColor = QColor(220, 20, 60); // Crimson red
        }
        
        waterGradient.setColorAt(0, waterColor.lighter(130));
        waterGradient.setColorAt(0.3, waterColor);
        waterGradient.setColorAt(0.7, waterColor.darker(110));
        waterGradient.setColorAt(1, waterColor.darker(130));
        
        painter.setBrush(QBrush(waterGradient));
        painter.setPen(QPen(waterColor.darker(150), 1));
        
        // Create water shape with subtle curves
        QPainterPath waterPath;
        waterPath.moveTo(TANK_LEFT + 1, TANK_BOTTOM);
        waterPath.lineTo(TANK_LEFT + 1, TANK_BOTTOM - m_waterHeight + 5);
        
        // Add wavy water surface
        int surfaceY = TANK_BOTTOM - m_waterHeight;
        for (int x = TANK_LEFT + 1; x < TANK_RIGHT - 1; x += 20) {
            int waveOffset = static_cast<int>(3 * sin((x - TANK_LEFT) * 0.1));
            waterPath.lineTo(x, surfaceY + waveOffset);
        }
        
        waterPath.lineTo(TANK_RIGHT - 1, TANK_BOTTOM - m_waterHeight + 5);
        waterPath.lineTo(TANK_RIGHT - 1, TANK_BOTTOM);
        waterPath.closeSubpath();
        
        painter.drawPath(waterPath);
        
        // Add water reflections
        painter.setPen(QPen(waterColor.lighter(180), 2));
        for (int i = 0; i < 4; ++i) {
            int reflectY = surfaceY + 10 + i * 20;
            if (reflectY < TANK_BOTTOM - 10) {
                painter.drawLine(TANK_LEFT + 20, reflectY, TANK_LEFT + 80, reflectY);
                painter.drawLine(TANK_RIGHT - 80, reflectY, TANK_RIGHT - 20, reflectY);
            }
        }

        // Add surface sparkle effect
        painter.setPen(QPen(Qt::white, 1));
        painter.setBrush(Qt::white);
        for (int i = 0; i < 8; ++i) {
            int sparkleX = TANK_LEFT + 30 + (i * 30);
            int sparkleY = surfaceY + static_cast<int>(2 * sin(i * 0.5));
            painter.drawEllipse(sparkleX, sparkleY, 2, 2);
        }
    }


    // Enhanced level indicators with labels
    painter.setPen(QPen(Qt::darkGray, 2));
    painter.setBrush(Qt::NoBrush);
    
    // Warning threshold line with enhanced styling
    int warningY = TANK_BOTTOM - m_warningThreshold;
    painter.setPen(QPen(QColor(255, 165, 0), 3, Qt::DashLine));
    painter.drawLine(TANK_LEFT - 10, warningY, TANK_RIGHT + 10, warningY);

    // Warning label
    painter.setPen(QPen(QColor(255, 140, 0), 2));
    painter.setFont(QFont("Arial", 9, QFont::Bold));
    painter.drawText(TANK_RIGHT + 40, warningY + 5, "WARNING");
    
    // Danger threshold line with enhanced styling
    int dangerY = TANK_BOTTOM - m_dangerThreshold;
    painter.setPen(QPen(QColor(255, 0, 0), 3, Qt::DashLine));
    painter.drawLine(TANK_LEFT - 10, dangerY, TANK_RIGHT + 10, dangerY);
    
    // Danger label
    painter.setPen(QPen(QColor(220, 20, 60), 2));
    painter.setFont(QFont("Arial", 9, QFont::Bold));
    painter.drawText(TANK_RIGHT + 40, dangerY + 5, "DANGER");
    
    // Enhanced measurement scale
    painter.setPen(QPen(Qt::black, 1));
    painter.setFont(QFont("Arial", 8));
    for (int i = 0; i <= 10; ++i) {
        int scaleY = TANK_BOTTOM - (i * (TANK_BOTTOM - TANK_TOP) / 10);
        painter.drawLine(TANK_RIGHT + 2, scaleY, TANK_RIGHT + 12, scaleY);
        painter.drawText(TANK_RIGHT + 16, scaleY + 3 , QString::number(i * 10) + "%");
    }

}

QSize WaterTank::sizeHint() const
{
    return QSize(400, 400);
}

void WaterTank::wheelEvent(QWheelEvent *event)
{
    int delta = event->angleDelta().y();
    
    if (delta < 0 && m_waterHeight > MIN_WATER_HEIGHT) {
        // Scroll down to decrease water level
        setWaterLevel(m_waterHeight - WATER_HEIGHT_STEP);
    } else if (delta > 0) {
        setWaterLevel(m_waterHeight + WATER_HEIGHT_STEP);
    }
}

void WaterTank::setWaterLevel(int height)
{
    if (height < MIN_WATER_HEIGHT)
        height = MIN_WATER_HEIGHT;
    if (height > MAX_WATER_HEIGHT)
        height = MAX_WATER_HEIGHT;
    
    if (m_waterHeight != height) {
        m_waterHeight = height;
        emit waterLevelChanged(height);
        update();
        
        // Emit appropriate signal based on water level
        if (m_waterHeight <= m_warningThreshold) {
            emit normal();
        } else if (m_waterHeight <= m_dangerThreshold) {
            emit warning();
        } else {
            emit danger();
        }
    }
}

void WaterTank::setWarningThreshold(int threshold)
{
    if (m_warningThreshold != threshold && threshold > MIN_WATER_HEIGHT && threshold < m_dangerThreshold) {
        m_warningThreshold = threshold;
        emit warningThresholdChanged(threshold);
        // Re-evaluate current state
        setWaterLevel(m_waterHeight);
        // Force a redraw to show the new threshold line
        update();
    }
}

void WaterTank::setDangerThreshold(int threshold)
{
    if (m_dangerThreshold != threshold && threshold > m_warningThreshold && threshold < MAX_WATER_HEIGHT) {
        m_dangerThreshold = threshold;
        emit dangerThresholdChanged(threshold);
        // Re-evaluate current state
        setWaterLevel(m_waterHeight);
        // Force a redraw to show the new threshold line
        update();
    }
}

void WaterTank::startSimulation()
{
    m_timer->start();
}

void WaterTank::stopSimulation()
{
    m_timer->stop();
}

void WaterTank::resetWaterLevel()
{
    setWaterLevel(DEFAULT_WATER_HEIGHT);
}
