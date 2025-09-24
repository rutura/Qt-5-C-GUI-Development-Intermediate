#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>

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
    void on_chooseDirButton_clicked();

    void on_createDirButton_clicked();

    void on_dirExistsButton_clicked();

    void on_dirOrFileButton_clicked();

    void on_folderContentsButton_clicked();

private:
    Ui::Widget *ui;
};

#endif // WIDGET_H
