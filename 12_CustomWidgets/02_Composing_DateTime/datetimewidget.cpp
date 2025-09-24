#include "datetimewidget.h"
#include <QVBoxLayout>

DateTimeWidget::DateTimeWidget(QWidget *parent)
    : QWidget{parent}
    , m_timer{this}
    , m_dateLabel{new QLabel(this)}
    , m_timeLabel{new QLabel(this)}
    , m_currentDate{QDate::currentDate().toString(Qt::TextDate)}
    , m_currentTime{QTime::currentTime().toString()}
{
    auto layout = new QVBoxLayout(this);
    const QFont displayFont{"Consolas", 20, QFont::Bold};
    const QSizePolicy sizePolicy{QSizePolicy::Expanding, QSizePolicy::Fixed};

    // Setup date label
    m_dateLabel->setText(m_currentDate);
    m_dateLabel->setFont(displayFont);
    m_dateLabel->setAlignment(Qt::AlignCenter);

    // Setup time label
    m_timeLabel->setText(m_currentTime);
    m_timeLabel->setFont(displayFont);
    m_timeLabel->setAlignment(Qt::AlignCenter);
    m_timeLabel->setSizePolicy(sizePolicy);
    m_timeLabel->setStyleSheet(R"(
        background-color: #00eff9;
        color: #fffff1
    )");

    //Layout setup
    layout->addWidget(m_dateLabel);
    layout->addWidget(m_timeLabel);
    setLayout(layout);
    setSizePolicy(sizePolicy);

    //Timer setup
    m_timer.setInterval(1000);
    connect(&m_timer, &QTimer::timeout, this, &DateTimeWidget::updateTime);
    m_timer.start();
}

void DateTimeWidget::updateTime()
{
    const QString newTime = QTime::currentTime().toString();
    m_timeLabel->setText(newTime);
    m_currentTime = newTime;


    const QString newDate = QDate::currentDate().toString(Qt::TextDate);
    if (m_currentDate != newDate) {
        m_dateLabel->setText(newDate);
        m_currentDate = newDate;
    }
}
