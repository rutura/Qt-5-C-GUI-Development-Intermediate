#ifndef PARENTBUTTON_H
#define PARENTBUTTON_H

#include <QPushButton>

class ParentButton : public QPushButton
{
    Q_OBJECT
public:
    explicit ParentButton(QWidget *parent = nullptr);

signals:

public slots:

    // QWidget interface
protected:
    void mousePressEvent(QMouseEvent *event) override;
};

#endif // PARENTBUTTON_H
