#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include "scene.h"
#include <QMap>

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
    void on_actionCursor_triggered();

    void on_actionAbout_triggered();

    void on_actionStar_triggered();

    void on_actionRectangle_triggered();

    void on_actionEllipse_triggered();

    void on_actionEraser_triggered();

    void on_actionPen_triggered();

    void on_actionQuit_triggered();

    void on_actionAdd_Image_triggered();

private:
    Ui::MainWindow *ui;
    Scene * scene;
    QMap<int,QString> shapeMap;
};

#endif // MAINWINDOW_H
