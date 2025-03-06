# QSortFilterProxyModel in PySide6 - Implementation Guide

This guide demonstrates how to use `QSortFilterProxyModel` with views in PySide6 applications. The example application is a color filter that displays all available color names in a list view, allows filtering the list with a text search, and shows a preview of the selected color.

## Project Overview

This application demonstrates:
- Using a QStringListModel to display a list of items
- Adding a QSortFilterProxyModel to filter the data
- Implementing dynamic filtering based on user input
- Visualizing selected data (color names) in a preview panel

## Project Structure

```
qsortfilterproxymodel_demo/
│
├── main.py           # Application entry point
├── widget.py         # Main widget containing the views and models
└── ui_widget.py      # Generated UI code from widget.ui
```

## Building and Running the Project

1. Generate UI Python files:
   ```bash
   pyside6-uic widget.ui -o ui_widget.py
   ```

2. Run the application:
   ```bash
   python main.py
   ```

## Implementation Details

### Setting Up the Models and View

This implementation demonstrates the power of the proxy model pattern. The main components are:

1. **Source Model (QStringListModel)** - Contains the original data (color names)
2. **Proxy Model (QSortFilterProxyModel)** - Filters the source model
3. **View (QListView)** - Displays the filtered data from the proxy model

```python
class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # Get all available color names
        self.color_list = QColor.colorNames()
        
        # Create a string list model with the color names
        self.model = QStringListModel(self.color_list, self)
        
        # Create a proxy model for filtering
        self.proxy_model = QSortFilterProxyModel(self)
        self.proxy_model.setSourceModel(self.model)
        
        # Set the proxy model to the list view
        self.ui.listView.setModel(self.proxy_model)
        
        # Connect signals to slots
        self.ui.listView.clicked.connect(self.on_listView_clicked)
        self.ui.matchStringLineEdit.textChanged.connect(self.on_matchStringLineEdit_textChanged)
```

### Handling Item Selection

When selecting an item from the filtered list, we access the data through the proxy model:

```python
@Slot(QModelIndex)
def on_listView_clicked(self, index):
    """Handle list view item click to show the selected color"""
    # Get the color name from the proxy model
    color_name = self.proxy_model.data(index, role=0)  # DisplayRole is 0
    
    # Create a pixmap filled with the selected color
    pixmap = QPixmap(self.ui.label.size())
    pixmap.fill(QColor(color_name))
    
    # Set the pixmap to the label
    self.ui.label.setPixmap(pixmap)
```

### Implementing Dynamic Filtering

The filtering happens dynamically as the user types in the search field:

```python
@Slot(str)
def on_matchStringLineEdit_textChanged(self, text):
    """Filter the list view based on the entered text"""
    # Set the filter pattern on the proxy model
    self.proxy_model.setFilterRegularExpression(text)
```

## Key Concepts

### QSortFilterProxyModel

QSortFilterProxyModel is a proxy model that provides sorting and filtering capabilities for its source model. It doesn't store data itself, but provides a filtered/sorted view of the source model's data:

```python
# Creating a proxy model
proxy_model = QSortFilterProxyModel()
proxy_model.setSourceModel(source_model)

# Setting up filtering
proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
proxy_model.setFilterRegularExpression("blue")  # Filter items containing "blue"

# Setting up sorting
proxy_model.sort(0, Qt.AscendingOrder)  # Sort column 0 in ascending order
```

### Model-View-Proxy Architecture

The Model-View-Proxy pattern extends Qt's Model-View architecture:

1. **Model** (QStringListModel) - Stores and provides access to the data
2. **View** (QListView) - Displays the data and handles user interaction
3. **Proxy** (QSortFilterProxyModel) - Sits between the model and view, transforming the data

This architecture allows filtering and sorting without modifying the original data.

### Indexes and Mappings

When working with proxy models, it's important to understand the index mapping between the proxy model and the source model:

```python
# Getting the source model index from a proxy index
proxy_index = view.currentIndex()  # Index in the proxy model
source_index = proxy_model.mapToSource(proxy_index)  # Map to source model

# Getting data from the source model
source_data = source_model.data(source_index)

# Getting a proxy index from a source index
source_index = source_model.index(row, column)
proxy_index = proxy_model.mapFromSource(source_index)
```

### Filter Properties

QSortFilterProxyModel provides several properties to control filtering:

```python
# Basic filtering
proxy_model.setFilterRegularExpression("pattern")  # Set filter pattern
proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)  # Case insensitivity
proxy_model.setFilterKeyColumn(0)  # Only filter column 0 (default)

# Filter all columns
proxy_model.setFilterKeyColumn(-1)  # Check all columns

# Using wildcards
proxy_model.setFilterWildcard("bl*e")  # Match "blue", "blaze", etc.

# Using regular expressions
proxy_model.setFilterRegularExpression("[a-z]+")  # Match lowercase words
```

## Advanced Techniques

### Custom Filtering Logic

For more complex filtering, you can subclass QSortFilterProxyModel:

```python
from PySide6.QtCore import QSortFilterProxyModel, QModelIndex, Qt

class CustomFilterProxyModel(QSortFilterProxyModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.min_length = 0
    
    def setMinimumLength(self, length):
        self.min_length = length
        self.invalidateFilter()  # Reapply the filter
    
    def filterAcceptsRow(self, source_row, source_parent):
        # Get the index for the item in column 0
        index = self.sourceModel().index(source_row, 0, source_parent)
        
        # Get the text
        text = self.sourceModel().data(index, Qt.DisplayRole)
        
        # Apply custom filtering logic
        if len(text) < self.min_length:
            return False
            
        # Also apply the standard filter
        return super().filterAcceptsRow(source_row, source_parent)
```

Usage:
```python
custom_proxy = CustomFilterProxyModel()
custom_proxy.setSourceModel(model)
custom_proxy.setMinimumLength(5)  # Only show items with 5+ characters
```

### Combining Filtering and Sorting

QSortFilterProxyModel can both filter and sort simultaneously:

```python
# Enable sorting
proxy_model.sort(0, Qt.AscendingOrder)  # Sort by column 0

# Dynamic sorting from the view
list_view.setSortingEnabled(True)
```

### Cascading Proxy Models

For complex transformations, you can chain multiple proxy models:

```python
source_model = QStringListModel(data)

# First proxy for filtering
filter_proxy = QSortFilterProxyModel()
filter_proxy.setSourceModel(source_model)
filter_proxy.setFilterRegularExpression("blue")

# Second proxy for sorting
sort_proxy = QSortFilterProxyModel()
sort_proxy.setSourceModel(filter_proxy)
sort_proxy.setSortCaseSensitivity(Qt.CaseInsensitive)
sort_proxy.sort(0, Qt.AscendingOrder)

# Connect the view to the final proxy
view.setModel(sort_proxy)
```

### Filtering with Multiple Criteria

To filter based on multiple criteria, customize the `filterAcceptsRow` method:

```python
class MultiCriteriaProxyModel(QSortFilterProxyModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.length_filter = 0
        self.prefix_filter = ""
    
    def filterAcceptsRow(self, source_row, source_parent):
        # Get source model index for the row
        index = self.sourceModel().index(source_row, 0, source_parent)
        
        # Get text from the model
        text = self.sourceModel().data(index, Qt.DisplayRole)
        
        # Apply length filter
        if len(text) < self.length_filter:
            return False
        
        # Apply prefix filter
        if self.prefix_filter and not text.startswith(self.prefix_filter):
            return False
        
        # Apply regular expression filter (from base class)
        return super().filterAcceptsRow(source_row, source_parent)
```

## Best Practices

1. **Connect the Proxy to the View, Not the Source Model**

   Always set the proxy model as the view's model:
   ```python
   # Correct
   view.setModel(proxy_model)
   
   # Incorrect
   view.setModel(source_model)  # Bypasses the proxy
   ```

2. **Remember to Map Indexes**

   When working with both source and proxy models, map the indexes properly:
   ```python
   # Getting data from source model
   proxy_index = view.currentIndex()
   source_index = proxy_model.mapToSource(proxy_index)
   source_data = source_model.data(source_index)
   ```

3. **Optimize Filter Performance**

   For large datasets, consider optimizing filter performance:
   ```python
   # Disable dynamic filtering during bulk operations
   proxy_model.setDynamicSortFilter(False)
   # Make changes...
   proxy_model.setDynamicSortFilter(True)
   
   # Or use a timer to delay filtering during typing
   self.filter_timer = QTimer()
   self.filter_timer.setSingleShot(True)
   self.filter_timer.timeout.connect(self.apply_filter)
   
   def on_text_changed(self, text):
       self.filter_text = text
       self.filter_timer.start(200)  # Wait 200ms before filtering
   
   def apply_filter(self):
       self.proxy_model.setFilterRegularExpression(self.filter_text)
   ```

4. **Provide Visual Feedback During Filtering**

   For large datasets, filtering may take time. Consider showing busy indicators:
   ```python
   def on_filter_start(self):
       self.busy_indicator.show()
   
   def on_filter_end(self):
       self.busy_indicator.hide()
       self.status_label.setText(f"{self.proxy_model.rowCount()} items found")
   ```

5. **Use Case Insensitive Filtering by Default**

   For better user experience, use case-insensitive filtering by default:
   ```python
   proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
   ```

## Conclusion

QSortFilterProxyModel is a powerful tool in Qt's Model-View architecture, allowing you to add filtering and sorting capabilities to your applications without modifying the underlying data model. By placing a proxy model between your data source and views, you can provide dynamic filtering and improve the user experience with minimal code.

This implementation demonstrates the basic usage of QSortFilterProxyModel with a QStringListModel, but the same principles apply to any model type, including custom models. For more complex scenarios, consider subclassing QSortFilterProxyModel to implement custom filtering and sorting logic.