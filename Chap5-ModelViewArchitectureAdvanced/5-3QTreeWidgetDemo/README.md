# QTreeWidget in PySide6 - Implementation Guide

This guide demonstrates how to implement and work with QTreeWidget in PySide6 applications. QTreeWidget is a powerful widget for displaying hierarchical data in a tree structure with expandable branches.

## Project Overview

This application displays a company organization structure using a tree widget. The demo shows:
- Creating a multi-column tree
- Adding parent and child nodes
- Handling item click events
- Organizing hierarchical data

The example creates a tree structure with Google as the parent company, regional branches as children, and city offices as grandchildren.

## Project Structure

```
qtreewidget_demo/
│
├── main.py           # Application entry point
├── widget.py         # Main widget containing the tree widget
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

### Main Widget Setup

The main widget class sets up the tree widget with columns and organization data:

```python
class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # Set column count and headers
        self.ui.treeWidget.setColumnCount(2)
        self.ui.treeWidget.setHeaderLabels(["Organization", "Description"])
        
        # Add tree nodes
        self.populate_tree()
        
        # Connect signals to slots
        self.ui.treeWidget.itemClicked.connect(self.on_treeWidget_itemClicked)
```

### Adding Tree Items

The code provides helper methods to add root and child items:

```python
def add_root_organization(self, company, purpose):
    """Add a root-level organization to the tree widget"""
    item = QTreeWidgetItem(self.ui.treeWidget)
    item.setText(0, company)
    item.setText(1, purpose)
    return item

def add_child_organization(self, parent, branch, description):
    """Add a child organization to a parent item"""
    item = QTreeWidgetItem()
    item.setText(0, branch)
    item.setText(1, description)
    parent.addChild(item)
    return item
```

### Handling Item Clicks

```python
@Slot(QTreeWidgetItem, int)
def on_treeWidget_itemClicked(self, item, column):
    """Handle item click events"""
    print(f"Clicked on: {item.text(0)}, column: {column}")
```

## Key Concepts

### QTreeWidgetItem

QTreeWidgetItem represents a single node in the tree structure. Each item can:
- Contain text, icons or widgets in each column
- Have child items (creating a hierarchy)
- Store custom data using Qt's role system

```python
# Basic item creation
item = QTreeWidgetItem()                # Create standalone item
item = QTreeWidgetItem(parent_item)     # Create as child of another item
item = QTreeWidgetItem(tree_widget)     # Create as top-level item

# Setting content
item.setText(column, text)              # Set text for a column
item.setIcon(column, icon)              # Set icon for a column

# Managing hierarchy
parent.addChild(child)                  # Add child to parent
parent.insertChild(index, child)        # Insert child at position
parent.removeChild(child)               # Remove child
parent.takeChild(index)                 # Remove and return child at index

# Working with item properties
item.childCount()                       # Get number of children
item.parent()                           # Get parent item
item.isExpanded()                       # Check if expanded
item.setExpanded(True)                  # Expand the item
```

### Column Headers

```python
# Set column count
tree_widget.setColumnCount(2)

# Set column headers
tree_widget.setHeaderLabels(["Column 1", "Column 2"])

# Resize columns to content
tree_widget.resizeColumnToContents(0)

# Hide header
tree_widget.header().setVisible(False)

# Set header mode
tree_widget.header().setSectionResizeMode(QHeaderView.Stretch)
tree_widget.header().setSectionResizeMode(0, QHeaderView.ResizeToContents)
```

### Traversing the Tree

```python
# Get top-level items
top_item_count = tree_widget.topLevelItemCount()
for i in range(top_item_count):
    top_item = tree_widget.topLevelItem(i)
    
# Traverse all items recursively
def traverse_items(item, level=0):
    # Process item
    print(f"{'  ' * level}{item.text(0)}")
    
    # Process children
    for i in range(item.childCount()):
        child = item.child(i)
        traverse_items(child, level + 1)

# Call for each top-level item
for i in range(tree_widget.topLevelItemCount()):
    traverse_items(tree_widget.topLevelItem(i))
```

### Selection

```python
# Set selection mode
tree_widget.setSelectionMode(QAbstractItemView.SingleSelection)
tree_widget.setSelectionMode(QAbstractItemView.MultiSelection)
tree_widget.setSelectionMode(QAbstractItemView.ExtendedSelection)

# Get selected items
selected_items = tree_widget.selectedItems()

# Set current item
tree_widget.setCurrentItem(item)
```

### Key Signals

```python
# Connect to signals
tree_widget.itemClicked.connect(self.on_item_clicked)
tree_widget.itemDoubleClicked.connect(self.on_item_double_clicked)
tree_widget.itemExpanded.connect(self.on_item_expanded)
tree_widget.itemCollapsed.connect(self.on_item_collapsed)
tree_widget.itemSelectionChanged.connect(self.on_selection_changed)

# Signal handlers
@Slot(QTreeWidgetItem, int)
def on_item_clicked(self, item, column):
    # Handle click
    pass
    
@Slot(QTreeWidgetItem)
def on_item_expanded(self, item):
    # Handle expansion
    pass
```

## Advanced Techniques

### Custom Item Delegate

For custom rendering or editing of tree items:

```python
from PySide6.QtWidgets import QStyledItemDelegate
from PySide6.QtCore import QSize, Qt

class TreeItemDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        # Custom painting logic
        super().paint(painter, option, index)
    
    def sizeHint(self, option, index):
        # Custom size hint
        return QSize(100, 30)
```

Usage:
```python
delegate = TreeItemDelegate()
self.ui.treeWidget.setItemDelegate(delegate)
```

### Checkable Items

Create a tree with checkable items:

```python
# Make items checkable
item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
item.setCheckState(0, Qt.Unchecked)

# Handle state changes
@Slot(QTreeWidgetItem, int)
def on_item_changed(self, item, column):
    if column == 0:
        check_state = item.checkState(column)
        if check_state == Qt.Checked:
            print(f"{item.text(0)} is checked")
        else:
            print(f"{item.text(0)} is unchecked")
```

### Drag and Drop

Enable drag and drop for tree items:

```python
# Enable drag and drop
tree_widget.setDragEnabled(True)
tree_widget.setAcceptDrops(True)
tree_widget.setDragDropMode(QAbstractItemView.InternalMove)  # Move within the tree
```

### Custom Context Menu

```python
from PySide6.QtWidgets import QMenu

# Setup
tree_widget.setContextMenuPolicy(Qt.CustomContextMenu)
tree_widget.customContextMenuRequested.connect(self.show_context_menu)

def show_context_menu(self, position):
    # Get the item at the position
    item = tree_widget.itemAt(position)
    if not item:
        return
        
    # Create context menu
    menu = QMenu()
    add_action = menu.addAction("Add Child")
    delete_action = menu.addAction("Delete")
    
    # Show menu and handle action
    action = menu.exec_(tree_widget.mapToGlobal(position))
    
    if action == delete_action:
        parent = item.parent()
        if parent:
            parent.removeChild(item)
        else:
            index = tree_widget.indexOfTopLevelItem(item)
            tree_widget.takeTopLevelItem(index)
    elif action == add_action:
        self.add_child_organization(item, "New Child", "Description")
```

### Filtering and Searching

Implementing a filter to show only matching items:

```python
def filter_tree(self, search_text):
    """Filter tree items to show only those matching search_text"""
    # Process all top-level items
    for i in range(self.ui.treeWidget.topLevelItemCount()):
        item = self.ui.treeWidget.topLevelItem(i)
        self._filter_item(item, search_text.lower())

def _filter_item(self, item, search_text):
    """Recursively filter a tree item and its children"""
    # Default visibility
    item_visible = False
    
    # Check if item matches
    if search_text in item.text(0).lower() or search_text in item.text(1).lower():
        item_visible = True
    
    # Process children
    child_count = item.childCount()
    for i in range(child_count):
        child = item.child(i)
        # If any child is visible, parent should be visible
        if self._filter_item(child, search_text):
            item_visible = True
    
    # Set item visibility
    item.setHidden(not item_visible)
    
    return item_visible
```

## Best Practices

1. **Use Helper Methods for Item Creation**
   Create reusable methods like `add_root_organization()` and `add_child_organization()` to make your code cleaner and more consistent.

2. **Consider Performance with Large Trees**
   - Disable sorting when building the tree and enable it when finished.
   - Use `setUniformRowHeights(True)` if all rows have the same height for better performance.
   - Consider loading children on-demand when parent items are expanded.

3. **Properly Handle Item Deletion**
   When deleting items, check if it's a top-level item or a child item:
   ```python
   def delete_item(self, item):
       if item.parent():
           # It's a child item
           item.parent().removeChild(item)
       else:
           # It's a top-level item
           index = self.ui.treeWidget.indexOfTopLevelItem(item)
           self.ui.treeWidget.takeTopLevelItem(index)
   ```

4. **Use setExpanded() Instead of expandItem()**
   The `setExpanded()` method is more versatile and consistent:
   ```python
   # Expand an item and all its children
   def expand_all(self, item):
       item.setExpanded(True)
       for i in range(item.childCount()):
           self.expand_all(item.child(i))
   ```

5. **Consider Using QTreeView with Models for Complex Cases**
   For very complex tree structures or large datasets, consider using QTreeView with a custom model instead of QTreeWidget.

## Conclusion

QTreeWidget is a powerful tool for displaying hierarchical data in PySide6 applications. By understanding how to create, manipulate, and traverse the tree structure, you can create rich, interactive tree-based interfaces.

Whether you're building file browsers, organization charts, or any other hierarchical data display, QTreeWidget provides a convenient and feature-rich solution.