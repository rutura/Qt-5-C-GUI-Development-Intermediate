#ifndef CHILDLINEEDIT_H
#define CHILDLINEEDIT_H

#include <QObject>
#include "parentlineedit.h"

class ChildLineEdit : public ParentLineEdit
{
    Q_OBJECT
public:
    explicit ChildLineEdit(QWidget *parent = nullptr);
protected:
    void keyPressEvent(QKeyEvent *event) override;

signals:

};

#endif // CHILDLINEEDIT_H
