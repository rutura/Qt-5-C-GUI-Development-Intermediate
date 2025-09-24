#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QPushButton>
#include <QCheckBox>
#include "paintcanvas.h"

QT_BEGIN_NAMESPACE
namespace Ui {
class MainWindow;
}
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void penWidthChanged(int width);
    void changePenColor();
    void changeFillColor();
    void changeFillProperty();


private:
    Ui::MainWindow *ui;
    PaintCanvas *canvas{nullptr};
    QPushButton *penColorButton{nullptr};
    QPushButton *fillColorButton{nullptr};
    QCheckBox *fillCheckBox{nullptr};
};
#endif // MAINWINDOW_H
