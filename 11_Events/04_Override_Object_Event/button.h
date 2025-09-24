#ifndef BUTTON_H
#define BUTTON_H

#include <QObject>
#include <QPushButton>

class Button : public QPushButton
{
    Q_OBJECT
public:
    explicit Button(QWidget *parent = nullptr);

public:
    bool event(QEvent *event) override;
signals:

};

#endif // BUTTON_H
