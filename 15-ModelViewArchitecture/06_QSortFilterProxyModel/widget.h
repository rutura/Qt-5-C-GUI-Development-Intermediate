#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>
#include <QStringListModel>
#include <QSortFilterProxyModel>

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
    void on_listView_clicked(const QModelIndex &index);

    void on_lineEdit_textChanged(const QString &arg1);

private:
    Ui::Widget *ui;
    QStringListModel * model;
    QStringList colorList;
    QSortFilterProxyModel * proxyModel;
};
#endif // WIDGET_H
