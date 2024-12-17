#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>
#include <QStringListModel>
#include <QSortFilterProxyModel>

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
    void on_listView_clicked(const QModelIndex &index);

    void on_matchStringLineEdit_textChanged(const QString &arg1);

private:
    Ui::Widget *ui;
    QStringListModel * model;
    QStringList colorList;
    QSortFilterProxyModel * proxyModel;
};

#endif // WIDGET_H
