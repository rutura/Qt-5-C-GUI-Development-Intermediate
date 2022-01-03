#ifndef PARENTLINEEDIT_H
#define PARENTLINEEDIT_H

#include <QObject>
#include <QLineEdit>

class ParentLineEdit : public QLineEdit
{
    Q_OBJECT
public:
    explicit ParentLineEdit(QWidget *parent = nullptr);

signals:

public slots:

    // QWidget interface
protected:
    void keyPressEvent(QKeyEvent *event) override;
};

#endif // PARENTLINEEDIT_H
