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

public slots:
    void updateTime();

private:
    QTimer * timer;
    QLabel * labelTop;//Date
    QLabel * labelBottom;//Time
    QString dateString;
    QString timeString;
};

#endif // DATETIMEWIDGET_H
