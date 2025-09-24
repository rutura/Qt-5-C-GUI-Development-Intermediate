#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>
#include <QList>
#include <QColor>
#include <QPushButton>

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
    void on_button1_clicked();

    void on_button2_clicked();

    void on_button3_clicked();

    void on_button4_clicked();

    void on_button5_clicked();

    void on_button6_clicked();

    void on_button7_clicked();

    void on_button8_clicked();

    void on_button9_clicked();

    void on_loadPushButton_clicked();

    void on_savePushButton_clicked();

private:
    Ui::Widget *ui;
    QList<QColor> colorList;

    void saveColor( QString key, QColor color);
    QColor loadColor(QString key);

    void setLoadedColor( QString key, int index, QPushButton * button);
};

#endif // WIDGET_H
