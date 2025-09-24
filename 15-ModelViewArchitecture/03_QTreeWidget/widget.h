#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>
#include <QTreeWidgetItem>

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

private:
    QTreeWidgetItem *addRootOrganization(QString company, QString purpose);
    QTreeWidgetItem *addChildOrganization(QTreeWidgetItem *parent,QString branch,
                                          QString description);
    Ui::Widget *ui;
};
#endif // WIDGET_H
