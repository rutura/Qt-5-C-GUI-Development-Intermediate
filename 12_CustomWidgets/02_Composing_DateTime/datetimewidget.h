#ifndef DATETIMEWIDGET_H
#define DATETIMEWIDGET_H

#include <QWidget>
#include <QDate>
#include <QLabel>
#include <QTimer>

class DateTimeWidget : public QWidget
{
    Q_OBJECT
public:
    explicit DateTimeWidget(QWidget *parent = nullptr);

signals:

private slots:
    void updateTime();


private:
    QTimer m_timer;
    QLabel * m_dateLabel{nullptr};
    QLabel * m_timeLabel{nullptr};
    QString m_currentDate;
    QString m_currentTime;
};

#endif // DATETIMEWIDGET_H
