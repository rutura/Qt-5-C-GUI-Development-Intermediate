#include "watertank.h"
#include <QPainter>
#include <QWheelEvent>

namespace {
    constexpr int TANK_LEFT = 10;
    constexpr int TANK_TOP = 10;
    constexpr int TANK_BOTTOM = 300;
    constexpr int TANK_RIGHT = 300;
    constexpr int TANK_WIDTH = 290;
    constexpr int PEN_WIDTH = 3;
    constexpr int UPDATE_INTERVAL = 1000;
    constexpr int WATER_INCREMENT = 15;
    constexpr int NORMAL_THRESHOLD = 210;
    constexpr int WARNING_THRESHOLD = 239;
}



WaterTank::WaterTank(QWidget *parent)
    : QWidget{parent}
    , m_waterHeight{DEFAULT_WATER_HEIGHT}
    , m_timer{new QTimer{this}}
{
    setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    m_timer->setInterval(UPDATE_INTERVAL);

    connect(m_timer, &QTimer::timeout, this, [this](){
        m_waterHeight += WATER_INCREMENT;
        update();

        // Emit appropriate signal based on water level
        if (m_waterHeight <= NORMAL_THRESHOLD) {
            emit normal();
        } else if (m_waterHeight <= WARNING_THRESHOLD) {
            emit warning();
        } else {
            emit danger();
        }
    });
    m_timer->start();
}


QSize WaterTank::sizeHint() const
{
    return QSize(400,400);
}

void WaterTank::wheelEvent(QWheelEvent *event)
{

    int delta = event->angleDelta().y();

    if( delta < 0 && m_waterHeight > MIN_WATER_HEIGHT){
        //Scroll down to decrease the water level
        m_waterHeight -= WATER_HEIGHT_STEP;
        update();

        // Emit appropriate signal based on updated water level
        if (m_waterHeight <= NORMAL_THRESHOLD) {
            emit normal();
        } else if (m_waterHeight <= WARNING_THRESHOLD) {
            emit warning();
        } else {
            emit danger();
        }
    }
}

void WaterTank::paintEvent(QPaintEvent *event)
{
    Q_UNUSED(event);

    QPainter painter(this);

    // Set up painter
    QPen pen(Qt::yellow, PEN_WIDTH);
    painter.setPen(pen);

    // Draw the tank outline
    painter.drawLine(TANK_LEFT, TANK_TOP, TANK_LEFT, TANK_BOTTOM);     // Left
    painter.drawLine(TANK_LEFT, TANK_BOTTOM, TANK_RIGHT, TANK_BOTTOM); // Bottom
    painter.drawLine(TANK_RIGHT, TANK_BOTTOM, TANK_RIGHT, TANK_TOP);   // Right


    //Draw the water
    painter.setBrush(Qt::blue);
    painter.drawRect(TANK_LEFT, TANK_BOTTOM - m_waterHeight, TANK_WIDTH, m_waterHeight);
}












