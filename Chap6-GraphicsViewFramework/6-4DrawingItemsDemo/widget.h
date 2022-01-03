#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>
#include <QGraphicsScene>

namespace Ui {
class Widget;
}

class Widget : public QWidget
{
    Q_OBJECT

public:
    explicit Widget(QWidget *parent = nullptr);
    ~Widget();

private slots:
    void on_lineButton_clicked();

    void on_ellipseButton_clicked();

    void on_pathButton_clicked();

    void on_pieButton_clicked();

    void on_imageButton_clicked();

    void on_starButton_clicked();

private:
    Ui::Widget *ui;
    QGraphicsScene * scene;
};

#endif // WIDGET_H
