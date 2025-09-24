#ifndef PARENTBUTTON_H
#define PARENTBUTTON_H

#include <QObject>
#include <QPushButton>

class ParentButton : public QPushButton
{
    Q_OBJECT
public:
    explicit ParentButton(QWidget *parent = nullptr);
protected:
    void mousePressEvent(QMouseEvent *event) override;

signals:

};

#endif // PARENTBUTTON_H
