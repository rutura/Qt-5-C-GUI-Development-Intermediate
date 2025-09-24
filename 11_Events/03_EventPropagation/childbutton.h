#ifndef CHILDBUTTON_H
#define CHILDBUTTON_H

#include <QObject>
#include "parentbutton.h"

class ChildButton : public ParentButton
{
    Q_OBJECT
public:
    explicit ChildButton(QWidget *parent = nullptr);
protected:
    void mousePressEvent(QMouseEvent *event) override;

signals:

};

#endif // CHILDBUTTON_H
