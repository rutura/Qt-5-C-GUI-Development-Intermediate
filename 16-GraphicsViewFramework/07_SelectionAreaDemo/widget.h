#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>
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
    void on_centerInViewButton_clicked();

    void on_showGridCheckbox_toggled(bool checked);

    void on_ensureVisibleButton_clicked();

    void on_fitInViewButton_clicked();

    void on_zoomInButton_clicked();

    void on_zoomOutButton_clicked();

    void on_resetButton_clicked();

private:
    Ui::Widget *ui;
     View * view ;
     QGraphicsEllipseItem * redEllipse;
};

#endif // WIDGET_H
