#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>
#include "inventorymodel.h"
#include "inventorydelegates.h"
#include "productdetailswidget.h"

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
    void onAddItem();
    void onEditItem();
    void onDeleteItem();
    void onManageSuppliers();
    void onSearchTextChanged(const QString &text);
    void onSelectionChanged(const QModelIndex &current, const QModelIndex &previous);
    void onImageChanged(const QString &newPath);
    void onDescriptionChanged(const QString &newDescription);

private:
    void setupModel();
    void setupDelegates();
    void setupConnections();
    void loadData();
    void saveData();
    void updateSelectedItemDetails();

    Ui::Widget *ui;
    InventoryModel *model;
    ImageDelegate *imageDelegate;
    RatingDelegate *ratingDelegate;
    SupplierDelegate *supplierDelegate;
    ProductDetailsWidget *detailsWidget;
    QString dataFilePath;
};

#endif // WIDGET_H
