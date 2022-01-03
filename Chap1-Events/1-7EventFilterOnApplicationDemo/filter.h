#ifndef FILTER_H
#define FILTER_H

#include <QObject>

class Filter : public QObject
{
    Q_OBJECT
public:
    explicit Filter(QObject *parent = nullptr);

signals:

public slots:

    // QObject interface
public:
    bool eventFilter(QObject *watched, QEvent *event) override;
};

#endif // FILTER_H
