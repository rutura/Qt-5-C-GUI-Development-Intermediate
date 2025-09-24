#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>
#include "dragdroplabel.h"

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

private slots:
    void on_clearButton_clicked();
    void mimeChanged(const QMimeData* mimedata);

private:
    Ui::Widget *ui;
    DragDropLabel* dragDropLabel;
};
#endif // WIDGET_H
