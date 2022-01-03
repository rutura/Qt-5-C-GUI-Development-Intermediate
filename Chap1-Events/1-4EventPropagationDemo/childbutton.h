#ifndef CHILDBUTTON_H
#define CHILDBUTTON_H

#include "parentbutton.h"

class ChildButton : public ParentButton
{
    Q_OBJECT
public:
    explicit ChildButton(QWidget *parent = nullptr);

signals:

public slots:

    // QWidget interface
protected:
    void mousePressEvent(QMouseEvent *event) override;
};

#endif // CHILDBUTTON_H
