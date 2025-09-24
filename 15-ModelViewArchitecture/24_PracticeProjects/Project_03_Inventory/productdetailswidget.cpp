#include "productdetailswidget.h"
#include <QVBoxLayout>
#include <QFormLayout>
#include <QFileDialog>
#include <QMessageBox>
#include <QDir>
#include <QFile>
#include <QFileInfo>
#include <QStandardPaths>

ProductDetailsWidget::ProductDetailsWidget(QWidget *parent)
    : QWidget(parent)
{
    setupUi();
}

void ProductDetailsWidget::setupUi()
{
    auto *mainLayout = new QVBoxLayout(this);
    
    // Image section
    imageLabel = new QLabel(this);
    imageLabel->setMinimumSize(300, 300);
    imageLabel->setAlignment(Qt::AlignCenter);
    imageLabel->setStyleSheet("QLabel { background-color: #f0f0f0; border: 1px solid #ddd; }");
    mainLayout->addWidget(imageLabel);

    changeImageButton = new QPushButton(tr("Change Image"), this);
    mainLayout->addWidget(changeImageButton);

    // Details section
    auto *formLayout = new QFormLayout;
    productNameLabel = new QLabel(this);
    quantityLabel = new QLabel(this);
    supplierLabel = new QLabel(this);
    ratingLabel = new QLabel(this);
    
    formLayout->addRow(tr("Product:"), productNameLabel);
    formLayout->addRow(tr("Quantity:"), quantityLabel);
    formLayout->addRow(tr("Supplier:"), supplierLabel);
    formLayout->addRow(tr("Rating:"), ratingLabel);

    mainLayout->addLayout(formLayout);

    // Description section
    mainLayout->addWidget(new QLabel(tr("Description:"), this));
    descriptionEdit = new QTextEdit(this);
    mainLayout->addWidget(descriptionEdit);

    // Connect signals
    connect(changeImageButton, &QPushButton::clicked, this, &ProductDetailsWidget::onChangeImage);
    connect(descriptionEdit, &QTextEdit::textChanged, this, [this]() {
        emit descriptionChanged(descriptionEdit->toPlainText());
    });
}

void ProductDetailsWidget::setItem(const InventoryItem &item)
{
    productNameLabel->setText(item.productName);
    quantityLabel->setText(QString::number(item.quantity));
    supplierLabel->setText(item.supplier);
    
    QString ratingText;
    for (int i = 0; i < 5; ++i) {
        ratingText += i < item.rating ? "★" : "☆";
    }
    ratingLabel->setText(ratingText);
    
    if (!item.image.isNull()) {
        QPixmap scaled = item.image.scaled(300, 300, Qt::KeepAspectRatio, Qt::SmoothTransformation);
        imageLabel->setPixmap(scaled);
    } else {
        imageLabel->setText(tr("No Image"));
    }
    
    currentImagePath = item.imagePath;
    descriptionEdit->setText(item.description);
}

void ProductDetailsWidget::clearDetails()
{
    imageLabel->clear();
    imageLabel->setText(tr("No Item Selected"));
    productNameLabel->clear();
    quantityLabel->clear();
    supplierLabel->clear();
    ratingLabel->clear();
    descriptionEdit->clear();
    currentImagePath.clear();
}

void ProductDetailsWidget::onChangeImage()
{
    QString fileName = QFileDialog::getOpenFileName(this,
        tr("Select Image"), QString(), tr("Images (*.png *.jpg *.jpeg)"));
    
    if (!fileName.isEmpty()) {
        saveImageToDataFolder(fileName);
    }
}

void ProductDetailsWidget::saveImageToDataFolder(const QString &sourcePath)
{
    QDir dataDir(QDir::current());
    if (!dataDir.exists("data/images")) {
        dataDir.mkpath("data/images");
    }

    QFileInfo sourceFile(sourcePath);
    QString newFileName = QDateTime::currentDateTime().toString("yyyyMMddhhmmss_") + 
                         sourceFile.fileName();
    QString newPath = dataDir.filePath("data/images/" + newFileName);

    if (QFile::copy(sourcePath, newPath)) {
        QPixmap newImage(newPath);
        if (!newImage.isNull()) {
            QPixmap scaled = newImage.scaled(300, 300, Qt::KeepAspectRatio, Qt::SmoothTransformation);
            imageLabel->setPixmap(scaled);
            emit imageChanged(newPath);
        }
    } else {
        QMessageBox::warning(this, tr("Error"), tr("Failed to save image."));
    }
}
