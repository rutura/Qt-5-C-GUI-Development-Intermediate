#include "widget.h"
#include "./ui_widget.h"
#include <QMessageBox>
#include <QInputDialog>
#include <QDir>
#include <QSplitter>

Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
{
    ui->setupUi(this);

    // Set up data directory
    QDir dataDir(QDir::current());
    if (!dataDir.exists("data")) {
        dataDir.mkdir("data");
    }
    if (!dataDir.exists("data/images")) {
        dataDir.mkdir("data/images");
    }
    dataFilePath = dataDir.filePath("data/inventory.json");

    setupModel();
    setupConnections();
    loadData();
    setupDelegates();
}

Widget::~Widget()
{
    saveData();
    delete ui;
}

void Widget::setupModel()
{
    model = new InventoryModel(this);
    ui->inventoryTableView->setModel(model);
    
    // Configure table view
    ui->inventoryTableView->horizontalHeader()->setSectionResizeMode(QHeaderView::Interactive);
    ui->inventoryTableView->verticalHeader()->setDefaultSectionSize(64); // For thumbnails
    ui->inventoryTableView->setSelectionBehavior(QAbstractItemView::SelectRows);
    ui->inventoryTableView->setSelectionMode(QAbstractItemView::SingleSelection);
    
    // Create splitter for master-detail view
    auto *splitter = new QSplitter(Qt::Horizontal, this);
    splitter->addWidget(ui->mainFrame); // Contains table and buttons
    
    detailsWidget = new ProductDetailsWidget(this);
    splitter->addWidget(detailsWidget);
    
    // Set initial sizes - 60% for table, 40% for details
    QList<int> sizes;
    sizes << 600 << 400;
    splitter->setSizes(sizes);
    
    // Update layout
    delete layout();
    auto *mainLayout = new QVBoxLayout(this);
    mainLayout->addWidget(splitter);
    setLayout(mainLayout);
}

void Widget::setupDelegates()
{
    imageDelegate = new ImageDelegate(this);
    ratingDelegate = new RatingDelegate(this);
    supplierDelegate = new SupplierDelegate(model->getSupplierList(), this);

    ui->inventoryTableView->setItemDelegateForColumn(InventoryModel::ProductImage, imageDelegate);
    ui->inventoryTableView->setItemDelegateForColumn(InventoryModel::Rating, ratingDelegate);
    ui->inventoryTableView->setItemDelegateForColumn(InventoryModel::Supplier, supplierDelegate);
}

void Widget::setupConnections()
{
    connect(ui->addButton, &QPushButton::clicked, this, &Widget::onAddItem);
    connect(ui->editButton, &QPushButton::clicked, this, &Widget::onEditItem);
    connect(ui->deleteButton, &QPushButton::clicked, this, &Widget::onDeleteItem);
    connect(ui->manageSuppliersButton, &QPushButton::clicked, this, &Widget::onManageSuppliers);
    connect(ui->searchLineEdit, &QLineEdit::textChanged, this, &Widget::onSearchTextChanged);
    
    // Connect selection changes to update details panel
    connect(ui->inventoryTableView->selectionModel(), &QItemSelectionModel::currentRowChanged,
            this, &Widget::onSelectionChanged);
    
    // Connect details panel signals
    connect(detailsWidget, &ProductDetailsWidget::imageChanged,
            this, &Widget::onImageChanged);
    connect(detailsWidget, &ProductDetailsWidget::descriptionChanged,
            this, &Widget::onDescriptionChanged);
}

void Widget::onSelectionChanged(const QModelIndex &current, const QModelIndex &previous)
{
    Q_UNUSED(previous);
    if (current.isValid()) {
        const InventoryItem &item = model->getItem(current.row());
        detailsWidget->setItem(item);
    } else {
        detailsWidget->clearDetails();
    }
}

void Widget::onImageChanged(const QString &newPath)
{
    QModelIndex index = ui->inventoryTableView->currentIndex();
    if (index.isValid()) {
        model->setData(model->index(index.row(), InventoryModel::ProductImage), newPath);
    }
}

void Widget::onDescriptionChanged(const QString &newDescription)
{
    QModelIndex index = ui->inventoryTableView->currentIndex();
    if (index.isValid()) {
        InventoryItem item = model->getItem(index.row());
        item.description = newDescription;
        item.lastUpdated = QDateTime::currentDateTime();
        model->updateItem(index.row(), item);
    }
}

void Widget::loadData()
{
    if (model->loadFromFile(dataFilePath)) {
        qDebug() << "Data loaded successfully from" << dataFilePath;
        if (ui->inventoryTableView->model()->rowCount() > 0) {
            ui->inventoryTableView->setCurrentIndex(model->index(0, 0));
        }
    }
}

void Widget::saveData()
{
    if (!model->saveToFile(dataFilePath)) {
        qDebug() << "Failed to save data to" << dataFilePath;
    }
}

void Widget::onAddItem()
{
    InventoryItem item;
    item.productName = QInputDialog::getText(this, tr("Add Item"), tr("Product Name:"));
    if (item.productName.isEmpty()) return;

    if (!model->isProductNameUnique(item.productName)) {
        QMessageBox::warning(this, tr("Error"), tr("A product with this name already exists."));
        return;
    }
    
    // Make sure supplier delegate has latest supplier list
    supplierDelegate->setSuppliers(model->getSupplierList());

    item.quantity = 0;
    item.supplier = model->getSupplierList().value(0); // Default to first supplier
    item.rating = 0;
    item.description = tr("Enter product description here...");

    if (model->addItem(item)) {
        int lastRow = model->rowCount() - 1;
        ui->inventoryTableView->setCurrentIndex(model->index(lastRow, 0));
    }
}

void Widget::onEditItem()
{
    QModelIndex index = ui->inventoryTableView->currentIndex();
    if (!index.isValid()) {
        QMessageBox::warning(this, tr("Error"), tr("Please select an item to edit."));
        return;
    }

    ui->inventoryTableView->edit(index);
}

void Widget::onDeleteItem()
{
    QModelIndex index = ui->inventoryTableView->currentIndex();
    if (!index.isValid()) {
        QMessageBox::warning(this, tr("Error"), tr("Please select an item to delete."));
        return;
    }

    if (QMessageBox::question(this, tr("Confirm Delete"), 
                            tr("Are you sure you want to delete this item?")) == QMessageBox::Yes) {
        model->removeItem(index.row());
        detailsWidget->clearDetails();
    }
}

void Widget::onManageSuppliers()
{
    bool ok;
    QString text = QInputDialog::getText(this, tr("Manage Suppliers"),
                                       tr("Enter supplier names (comma-separated):"),
                                       QLineEdit::Normal,
                                       model->getSupplierList().join(","), &ok);
    if (ok && !text.isEmpty()) {
        QStringList suppliers = text.split(",", Qt::SkipEmptyParts);
        for (QString &supplier : suppliers) {
            supplier = supplier.trimmed();
        }
        model->setSupplierList(suppliers);
        supplierDelegate->setSuppliers(suppliers);
    }
}

void Widget::onSearchTextChanged(const QString &text)
{
    for (int row = 0; row < model->rowCount(); ++row) {
        bool match = model->data(model->index(row, InventoryModel::ProductName)).toString()
                         .contains(text, Qt::CaseInsensitive);
        ui->inventoryTableView->setRowHidden(row, !match);
    }
}
