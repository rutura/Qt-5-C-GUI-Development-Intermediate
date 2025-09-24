#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>
#include <string_view>

QT_BEGIN_NAMESPACE
namespace Ui {
class Widget;
}
QT_END_NAMESPACE

class Widget : public QWidget
{
    Q_OBJECT

public:
    Widget(QWidget *parent = nullptr);
    ~Widget();
    // QWidget interface
protected:
    void keyPressEvent(QKeyEvent *event) override;

private:
    void copy();
    void paste();
    bool isImage(std::string_view fullpath);

private:
    Ui::Widget *ui;

};
#endif // WIDGET_H
