#ifndef KEYBOARDFILTER_H
#define KEYBOARDFILTER_H

#include <QObject>

class KeyboardFilter : public QObject
{
    Q_OBJECT
public:
    explicit KeyboardFilter(QObject *parent = nullptr);

public:
    bool eventFilter(QObject *watched, QEvent *event) override;
signals:


private:
    static constexpr const char* ALLOWED_NUMBERS = "1234567890";
};

#endif // KEYBOARDFILTER_H
