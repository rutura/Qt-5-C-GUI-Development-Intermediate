#ifndef DOUBLECLICKABLEBUTTON_H
#define DOUBLECLICKABLEBUTTON_H

#include <QPushButton>

class DoubleClickableButton : public QPushButton
{
    Q_OBJECT
public:
    explicit DoubleClickableButton(QWidget *parent = nullptr);

signals:
    void doubleClicked();

public slots:

    // QWidget interface
protected:
    void mouseDoubleClickEvent(QMouseEvent *event) override;
};

#endif // DOUBLECLICKABLEBUTTON_H
