#ifndef PRODUCTDETAILSWIDGET_H
#define PRODUCTDETAILSWIDGET_H

#include <QWidget>
#include <QLabel>
#include <QLineEdit>
#include <QSpinBox>
#include <QComboBox>
#include <QTextEdit>
#include <QPushButton>
#include "inventoryitem.h"

class ProductDetailsWidget : public QWidget
{
    Q_OBJECT

public:
    explicit ProductDetailsWidget(QWidget *parent = nullptr);
    void setItem(const InventoryItem &item);
    void clearDetails();

signals:
    void imageChanged(const QString &newPath);
    void descriptionChanged(const QString &newDescription);
    void detailsChanged();

private slots:
    void onChangeImage();
    void saveImageToDataFolder(const QString &sourcePath);

private:
    void setupUi();

    QLabel *imageLabel;
    QLabel *productNameLabel;
    QLabel *quantityLabel;
    QLabel *supplierLabel;
    QLabel *ratingLabel;
    QTextEdit *descriptionEdit;
    QPushButton *changeImageButton;
    QString currentImagePath;
};

#endif // PRODUCTDETAILSWIDGET_H
