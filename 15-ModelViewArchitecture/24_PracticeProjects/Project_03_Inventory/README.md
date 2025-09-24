# Inventory Management System with Qt6/C++

This project is a comprehensive desktop application built with Qt6 and C++ that demonstrates the Model-View-Delegate pattern along with practical implementations of data persistence, custom widgets, and modern C++ practices. It serves as an educational resource for understanding Qt's powerful MVC architecture.

## Architecture Overview

### Model-View-Delegate Pattern Implementation

The application implements Qt's Model-View-Delegate pattern with three distinct layers:

1. **Model Layer** (`InventoryModel`):
   - Inherits from `QAbstractTableModel`
   - Manages data storage and business logic
   - Implements required virtual functions:
     ```cpp
     virtual int rowCount(const QModelIndex &parent) const override;
     virtual int columnCount(const QModelIndex &parent) const override;
     virtual QVariant data(const QModelIndex &index, int role) const override;
     virtual bool setData(const QModelIndex &index, const QVariant &value, int role) override;
     ```
   - Handles data persistence through JSON serialization
   - Provides CRUD operations for inventory items

2. **View Layer**:
   - Main window (`Widget`) with split layout
   - Table view for item listing
   - Detail panel (`ProductDetailsWidget`) for item editing
   - Search and filtering capabilities

3. **Delegate Layer** (`InventoryDelegates`):
   - Custom rendering and editing of table cells
   - Specialized delegates for:
     - Images (`ImageDelegate`)
     - Star ratings (`RatingDelegate`)
     - Supplier selection (`SupplierDelegate`)

## Features

- **Master-Detail View**: Split interface showing a table of items and detailed information
- **Product Management**:
  - Add, edit, and delete inventory items
  - Track product name, quantity, supplier, and rating
  - Add and manage product images
  - Add detailed product descriptions
- **Data Persistence**: Automatically saves data to JSON format
- **Search Functionality**: Real-time search through inventory items
- **Supplier Management**: Manage list of suppliers through a simple interface
- **Rating System**: Visual star-rating system for products
- **Image Support**: Add and manage product images with thumbnail display

## Project Structure

- `main.cpp`: Application entry point
- `widget.h/cpp`: Main window implementation
- `inventorymodel.h/cpp`: Data model implementation (MVC pattern)
- `inventoryitem.h`: Product item data structure
- `inventorydelegates.h/cpp`: Custom delegates for table view rendering
- `productdetailswidget.h/cpp`: Detail view implementation

## Technical Implementation

### Data Model
- Uses `QAbstractTableModel` for implementing the MVC pattern
- Data stored in JSON format (`data/inventory.json`)
- Images stored in `data/images/` directory

### User Interface
- Table view with custom delegates for:
  - Image thumbnails
  - Star ratings
  - Supplier selection
- Split view interface using `QSplitter`
- Detail panel showing comprehensive item information

### Key Components in Detail

#### 1. Inventory Model (`inventorymodel.h/cpp`)
```cpp
class InventoryModel : public QAbstractTableModel {
    enum Column {
        ProductName = 0,
        Quantity,
        Supplier,
        ProductImage,
        Rating,
        ColumnCount
    };
    // ... methods for CRUD operations
    private:
        QVector<InventoryItem> items;
        QStringList supplierList;
};
```
- Implements table model interface
- Manages data persistence
- Handles item validation and unique constraints
- Provides search and filter capabilities

#### 2. Item Structure (`inventoryitem.h`)
```cpp
class InventoryItem {
public:
    QString productName;
    int quantity;
    QString supplier;
    QString imagePath;
    QPixmap image;
    int rating;
    QString description;
    QDateTime lastUpdated;
};
```
- Represents individual inventory items
- Contains all item properties
- Used for data transfer and storage

#### 3. Custom Delegates (`inventorydelegates.h/cpp`)
- **ImageDelegate**: 
  - Displays thumbnails in table
  - Handles image file selection
  - Manages image scaling and caching
- **RatingDelegate**:
  - Shows interactive star rating
  - Provides click-to-rate functionality
- **SupplierDelegate**:
  - Implements dropdown selection
  - Manages supplier list synchronization

#### 4. Data Persistence System
- JSON-based storage:
  ```cpp
  // Saving example (simplified)
  QJsonObject itemToJson(const InventoryItem &item) {
      QJsonObject obj;
      obj["productName"] = item.productName;
      obj["quantity"] = item.quantity;
      obj["supplier"] = item.supplier;
      // ... other properties
      return obj;
  }
  ```
- Automatic save/load functionality
- Image file management
- Data validation and error handling

## Building and Running the Project

### Prerequisites
- Qt 6.x
- C++ compiler with C++11 support
- CMake 3.x

### Build Steps
1. Open the project in Qt Creator
2. Configure the project for your Qt kit
3. Build and run the project

The application will create necessary data directories on first run.

## Usage

1. **Adding Items**:
   - Click "Add" button
   - Enter product name
   - Fill in details in the detail panel

2. **Editing Items**:
   - Select an item in the table
   - Click "Edit" or directly edit cells
   - Modify details in the detail panel

3. **Managing Suppliers**:
   - Click "Manage Suppliers"
   - Enter comma-separated supplier names

4. **Search**:
   - Type in the search box to filter items

5. **Images**:
   - Click "Change Image" in detail panel
   - Select an image file (supports PNG, JPG)

## Data Storage

- All data is automatically saved when the application closes
- Images are copied to the data directory
- Data can be found in:
  - `data/inventory.json`: Item data
  - `data/images/`: Product images

## Implementation Details for Students

### Signal-Slot Connections
Example from `widget.cpp`:
```cpp
void Widget::setupConnections()
{
    // Button connections
    connect(ui->addButton, &QPushButton::clicked, this, &Widget::onAddItem);
    connect(ui->editButton, &QPushButton::clicked, this, &Widget::onEditItem);
    
    // Selection change handling
    connect(ui->inventoryTableView->selectionModel(), 
            &QItemSelectionModel::currentRowChanged,
            this, &Widget::onSelectionChanged);
    
    // Detail panel updates
    connect(detailsWidget, &ProductDetailsWidget::imageChanged,
            this, &Widget::onImageChanged);
}
```

### Data Loading Process
1. Application startup flow:
   ```cpp
   Widget::Widget(QWidget *parent)
   {
       // Create data directories
       QDir dataDir(QDir::current());
       if (!dataDir.exists("data")) {
           dataDir.mkdir("data");
       }
       if (!dataDir.exists("data/images")) {
           dataDir.mkdir("data/images");
       }
       
       // Setup components
       setupModel();
       setupConnections();
       loadData();
       setupDelegates();
   }
   ```

2. JSON handling:
   ```cpp
   bool InventoryModel::loadFromFile(const QString &filename)
   {
       QFile file(filename);
       if (!file.open(QIODevice::ReadOnly)) {
           return false;
       }
       
       QJsonDocument doc = QJsonDocument::fromJson(file.readAll());
       QJsonArray itemsArray = doc.object()["items"].toArray();
       
       // Process each item
       for (const QJsonValue &value : itemsArray) {
           QJsonObject obj = value.toObject();
           // Convert JSON to InventoryItem
           // Add to model
       }
   }
   ```

### Key Learning Points
1. **Model-View-Delegate Pattern**
   - Separation of concerns
   - Data management vs. presentation
   - Custom rendering and editing

2. **Qt Best Practices**
   - Signal-slot mechanism for loose coupling
   - Resource management and cleanup
   - Event handling patterns

3. **Modern C++ Features Used**
   - Smart pointers for memory management
   - Range-based for loops
   - Lambda expressions
   - Auto type deduction

4. **Data Persistence Patterns**
   - JSON serialization/deserialization
   - File I/O operations
   - Error handling and validation

5. **UI Design Patterns**
   - Master-detail views
   - Custom delegates
   - Dynamic updates
   - Search and filtering

This project serves as a comprehensive example of professional Qt/C++ development practices. Study the implementation details to understand how various components work together in a real-world application.
