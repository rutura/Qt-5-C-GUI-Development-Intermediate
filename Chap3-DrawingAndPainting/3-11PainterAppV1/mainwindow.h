#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include "paintcanvas.h"
#include <QPushButton>
#include <QCheckBox>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void penWidthChanged(int width);
    void changePenColor();
    void changeFillColor();
    void changeFillProperty();

private:
    Ui::MainWindow *ui;
    PaintCanvas * canvas;
    QPushButton * penColorButton;
    QPushButton * fillColorButton;
    QCheckBox * fillCheckBox;
};

#endif // MAINWINDOW_H
