#ifndef KEYBOARDFILTER_H
#define KEYBOARDFILTER_H

#include <QObject>

class KeyboardFilter : public QObject
{
    Q_OBJECT
public:
    explicit KeyboardFilter(QObject *parent = nullptr);

signals:

public slots:

    // QObject interface
public:
    bool eventFilter(QObject *watched, QEvent *event) override;
};

#endif // KEYBOARDFILTER_H
