#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>

namespace Ui {
class Widget;
}

class Widget : public QWidget
{
    Q_OBJECT

public:
    explicit Widget(QWidget *parent = nullptr);
    ~Widget();

private:
    Ui::Widget *ui;

    // QWidget interface
protected:
    void keyPressEvent(QKeyEvent *event) override;
private:
    bool isImage (QString fullpath);
    void copy();
    void paste();
};

#endif // WIDGET_H
