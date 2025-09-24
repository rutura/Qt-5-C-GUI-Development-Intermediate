#include "indicator.h"
#include <QPainter>
#include <QPen>
#include <QBrush>

namespace {
    constexpr int LIGHT_WIDTH = 100;
    constexpr int LIGHT_HEIGHT = 100;
    constexpr int LIGHT_MARGIN = 10;
    constexpr int LIGHT_SPACING = 115;
    constexpr int FRAME_WIDTH = 120;
    constexpr int FRAME_HEIGHT = 330;
    constexpr int PEN_WIDTH = 3;
    constexpr int BLINK_INTERVAL = 300;
}

Indicator::Indicator(QWidget *parent)
    : QWidget{parent}
    , m_greenActive{false}
    , m_redActive{false}
    , m_yellowActive{false}
    , m_lightsOn{true}
    , m_timer{new QTimer(this)}
{
    setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    activateDanger();

    m_timer->setInterval(BLINK_INTERVAL);
    connect(m_timer, &QTimer::timeout, this, &Indicator::toogleLights);
    m_timer->start();
}


QSize Indicator::sizeHint() const
{
    return QSize(FRAME_WIDTH, FRAME_HEIGHT + 20);
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
    QPen pen(Qt::black, PEN_WIDTH);
    painter.setPen(pen);
    painter.setBrush(Qt::gray);

    //Draw the frame
    painter.drawRect(0,0,FRAME_WIDTH, FRAME_HEIGHT);


    const auto drawLight = [&] (int yPos, bool isActive, const QColor& activeColor){
        painter.setBrush(isActive && m_lightsOn? activeColor : Qt::black);
        painter.drawEllipse(LIGHT_MARGIN, yPos, LIGHT_WIDTH, LIGHT_HEIGHT);
    };

    //Draw the lights
    if(m_redActive){
        drawLight(LIGHT_MARGIN,true, Qt::red);
        drawLight(LIGHT_SPACING, false, Qt::black);
        drawLight(LIGHT_SPACING * 2, false, Qt::black);
    }else if (m_greenActive){
        drawLight(LIGHT_MARGIN,false, Qt::black);
        drawLight(LIGHT_SPACING, true, Qt::green);
        drawLight(LIGHT_SPACING * 2, false, Qt::black);
    }else if(m_yellowActive){
        drawLight(LIGHT_MARGIN,false, Qt::black);
        drawLight(LIGHT_SPACING, false, Qt::black);
        drawLight(LIGHT_SPACING * 2, true, Qt::yellow);
    }

}

void Indicator::toogleLights()
{
    m_lightsOn = !m_lightsOn;
    update();
}
