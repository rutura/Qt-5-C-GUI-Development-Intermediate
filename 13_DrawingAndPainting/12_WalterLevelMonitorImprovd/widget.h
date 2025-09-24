#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>

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
    void onWaterLevelChanged(int level);
    void onResetClicked();
    void onStartStopClicked();
    void setupControls();

private:
    Ui::Widget *ui;
    bool m_isSimulationRunning{false};
};
#endif // WIDGET_H
