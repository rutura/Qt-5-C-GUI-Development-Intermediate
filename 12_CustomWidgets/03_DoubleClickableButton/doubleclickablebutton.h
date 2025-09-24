#ifndef DOUBLECLICKABLEBUTTON_H
#define DOUBLECLICKABLEBUTTON_H

#include <QWidget>
#include <QPushButton>

class DoubleClickableButton : public QPushButton
{
    Q_OBJECT
public:
    explicit DoubleClickableButton(QWidget *parent = nullptr);

protected:
    void mouseDoubleClickEvent(QMouseEvent *event) override;
signals:
    void doubleClicked();
};

#endif // DOUBLECLICKABLEBUTTON_H
