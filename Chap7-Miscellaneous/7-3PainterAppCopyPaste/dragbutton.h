#ifndef DRAGBUTTON_H
#define DRAGBUTTON_H

#include <QPushButton>

class DragButton : public QPushButton
{
    Q_OBJECT
public:
    explicit DragButton(QWidget *parent = nullptr);

    QColor getButtonColor() const;
    void setButtonColor(const QColor &value);

signals:

public slots:

    // QWidget interface
protected:
    void mousePressEvent(QMouseEvent *event) override;
    void mouseMoveEvent(QMouseEvent *event) override;

private:
    QPoint lastPos;
    QColor buttonColor;
};

#endif // DRAGBUTTON_H
