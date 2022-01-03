#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>
#include <QGraphicsScene>
#include "view.h"


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

    void on_chooseColorButton_clicked();

    void on_colorButton_clicked();

    void on_infoButton_clicked();

    void on_cursorButton_clicked();

private:
    void setSelectItemColor(QColor color);
    Ui::Widget *ui;
    QGraphicsScene * scene;
     View * view ;
     QColor currentColor;
};

#endif // WIDGET_H
