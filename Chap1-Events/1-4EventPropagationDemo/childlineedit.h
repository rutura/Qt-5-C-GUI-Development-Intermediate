#ifndef CHILDLINEEDIT_H
#define CHILDLINEEDIT_H

#include "parentlineedit.h"

class ChildLineEdit : public ParentLineEdit
{
    Q_OBJECT
public:
    explicit ChildLineEdit(QWidget *parent = nullptr);

signals:

public slots:

    // QWidget interface
protected:
    void keyPressEvent(QKeyEvent *event) override;
};

#endif // CHILDLINEEDIT_H
