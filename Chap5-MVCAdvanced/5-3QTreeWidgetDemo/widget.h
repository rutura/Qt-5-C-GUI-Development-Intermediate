#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>
#include <QTreeWidgetItem>

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
    void on_treeWidget_itemClicked(QTreeWidgetItem *item, int column);

private:
    QTreeWidgetItem *addRootOrganization(QString company, QString purpose);
    QTreeWidgetItem *addChildOrganization(QTreeWidgetItem *parent,QString branch,
                                          QString description);
    Ui::Widget *ui;
};

#endif // WIDGET_H
