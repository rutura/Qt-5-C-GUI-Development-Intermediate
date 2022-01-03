#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include "scene.h"
#include "view.h"
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

    void on_actionSave_triggered();

    void on_actionLoad_triggered();

    void on_actionCopy_triggered();

    void on_actionCut_triggered();

    void on_actionPaste_triggered();

    void on_actionUndo_triggered();

    void on_actionRedo_triggered();

    void on_penColorButton_clicked();

    void on_penWidthSpinbox_valueChanged(int arg1);

    void on_penStyleCombobox_activated(int index);

    void on_brushColorButton_clicked();

    void on_brushStyleComboBox_activated(int index);

    void on_showgridCheckbox_toggled(bool checked);

    void on_centerSceneButton_clicked();

    void on_sceneBackgroundButton_clicked();

private:
    void setActiveTool(Scene::ToolType tool);
    Ui::MainWindow *ui;
    Scene * scene;
    QMap<int,QString> shapeMap;
    View * view;
};

#endif // MAINWINDOW_H
