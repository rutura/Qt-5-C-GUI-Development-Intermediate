#ifndef PARENTLINEEDIT_H
#define PARENTLINEEDIT_H

#include <QObject>
#include <QLineEdit>

class ParentLineEdit : public QLineEdit
{
    Q_OBJECT
public:
    explicit ParentLineEdit(QWidget *parent = nullptr);
protected:
    void keyPressEvent(QKeyEvent *event) override;

signals:

};

#endif // PARENTLINEEDIT_H
