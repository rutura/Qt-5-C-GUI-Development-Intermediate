# Advanced Custom Models in PySide6 - Implementation Guide

This guide demonstrates how to implement advanced custom models in PySide6. Building on the basic editable model implementation, we'll add row insertion and removal, and synchronize the selection between multiple views.

## Project Overview

This application demonstrates:
- Creating a custom data class (Person)
- Implementing an editable custom model that supports adding and removing items
- Sharing a selection model between multiple view types
- Collecting user input via dialogs for adding new items
- Using QListView, QTableView, and QTreeView with the same model

## Project Structure

```
advanced_custom_model_demo/
│
├── main.py           # Application entry point
├── widget.py         # Main widget containing the views
├── person.py         # Person data class
├── personmodel.py    # Advanced custom model implementation
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

### The Person Data Class

A data class with properties and change notifications:

```python
class Person(QObject):
    namesChanged = Signal(str)
    favoriteColorChanged = Signal(str)
    ageChanged = Signal(int)
    
    def __init__(self, names="", favorite_color="", age=0, parent=None):
        super().__init__(parent)
        self._names = names
        self._favorite_color = favorite_color
        self._age = age
    
    # Getters and setters with change notifications
    def names(self):
        return self._names
    
    def setNames(self, names):
        if self._names == names:
            return
        
        self._names = names
        self.namesChanged.emit(self._names)
```

### Advanced Model Features

The PersonModel class implements all the methods needed for an editable, mutable model:

```python
class PersonModel(QAbstractListModel):
    # ... basic model methods ...
    
    def addPerson(self, person):
        """Add a given person to the model"""
        index = len(self.persons)
        self.beginInsertRows(QModelIndex(), index, index)
        self.persons.append(person)
        self.endInsertRows()
    
    def removePerson(self, index):
        """Remove a person at the given index"""
        if not index.isValid() or index.row() >= len(self.persons):
            return
            
        self.beginRemoveRows(QModelIndex(), index.row(), index.row())
        self.persons.pop(index.row())
        self.endRemoveRows()
```

### Sharing Selection Models

The widget implementation shows how to share a selection model between views:

```python
# Set the model for all three views
self.ui.listView.setModel(self.model)
self.ui.tableView.setModel(self.model)
self.ui.treeView.setModel(self.model)

# Share selection model between views
# This ensures selecting in one view also selects in others
self.ui.tableView.setSelectionModel(self.ui.listView.selectionModel())
self.ui.treeView.setSelectionModel(self.ui.listView.selectionModel())
```

### User Interaction with the Model

The widget implements methods to add and remove items with user input:

```python
def on_addPersonButton_clicked(self):
    """Handle Add Person button click"""
    # Get name from user
    name, ok = QInputDialog.getText(
        self, 
        "Names",
        "Person name:", 
        QLineEdit.Normal,
        "Type in name"
    )
    
    if ok and name:
        # Get age from user
        age, ok = QInputDialog.getInt(
            self,
            "Person Age",
            "Age",
            20,  # Default value
            15,  # Min value
            120  # Max value
        )
        
        if ok:
            # Create and add new person
            person = Person(name, "blue", age, self)
            self.model.addPerson(person)
```

## Key Concepts

### Row Insertion and Removal

When inserting or removing rows, the model must notify its views about the changes:

```python
# When inserting rows:
self.beginInsertRows(QModelIndex(), row, row + count - 1)
# Insert the rows...
self.endInsertRows()

# When removing rows:
self.beginRemoveRows(QModelIndex(), row, row + count - 1)
# Remove the rows...
self.endRemoveRows()
```

The `beginInsertRows()` and `beginRemoveRows()` calls tell the views that the model is about to change, allowing them to update their internal state. The `endInsertRows()` and `endRemoveRows()` calls signal that the changes are complete.

### Shared Selection Models

In Qt's Model-View architecture, you can share a selection model between multiple views showing the same data:

```python
view2.setSelectionModel(view1.selectionModel())
```

This makes selections consistent across views. When a user selects an item in one view, it appears selected in all views that share the same selection model.

### Model Indices and Row Management

The QModelIndex class represents a location in a model. It contains a row, column, and parent index:

```python
# Check if an index is valid
if not index.isValid():
    return False

# Get the row from an index
row = index.row()

# Create a new QModelIndex
newIndex = self.createIndex(row, column, parent)
```

### Resource Management

Since Person objects are QObjects, they need to be properly cleaned up:

```python
def __del__(self):
    # Clean up Person objects
    for person in self.persons:
        person.deleteLater()
```

### Standard Model Methods

A QAbstractListModel subclass must implement at least:
- `rowCount()`: Returns the number of rows
- `data()`: Returns data for a given index and role

For editable models, additional methods are required:
- `setData()`: To handle editing
- `flags()`: To enable the proper item flags

To support row operations, these methods are useful:
- `insertRows()`: For adding rows
- `removeRows()`: For removing rows
- Custom methods like `addPerson()` and `removePerson()` that call the above

## Advanced Techniques

### Implementing CRUD Operations

CRUD (Create, Read, Update, Delete) operations should be implemented consistently:

```python
# CREATE: Add new items
def addItem(self, item):
    self.beginInsertRows(QModelIndex(), len(self.items), len(self.items))
    self.items.append(item)
    self.endInsertRows()

# READ: Get existing items
def getItem(self, index):
    if not index.isValid() or index.row() >= len(self.items):
        return None
    return self.items[index.row()]

# UPDATE: Modify existing items
def updateItem(self, index, newItem):
    if not index.isValid() or index.row() >= len(self.items):
        return False
    self.items[index.row()] = newItem
    self.dataChanged.emit(index, index)
    return True

# DELETE: Remove items
def deleteItem(self, index):
    if not index.isValid() or index.row() >= len(self.items):
        return False
    self.beginRemoveRows(QModelIndex(), index.row(), index.row())
    del self.items[index.row()]
    self.endRemoveRows()
    return True
```

### Multiple Columns in List Models

Although QAbstractListModel is designed for single-column data, you can still return different data for different roles:

```python
def data(self, index, role=Qt.DisplayRole):
    person = self.persons[index.row()]
    
    if role == Qt.DisplayRole:
        return person.names()
    elif role == Qt.UserRole:
        return person.age()
    elif role == Qt.UserRole + 1:
        return person.favoriteColor()
    
    return None
```

### Custom Roles

Define custom roles for different data types:

```python
class PersonRoles:
    NamesRole = Qt.UserRole + 1
    AgeRole = Qt.UserRole + 2
    ColorRole = Qt.UserRole + 3

def data(self, index, role):
    person = self.persons[index.row()]
    
    if role == PersonRoles.NamesRole:
        return person.names()
    elif role == PersonRoles.AgeRole:
        return person.age()
    elif role == PersonRoles.ColorRole:
        return person.favoriteColor()
    
    return None
```

### Custom Sorting and Filtering

To add sorting and filtering, use QSortFilterProxyModel:

```python
from PySide6.QtCore import QSortFilterProxyModel

# Create the source model
sourceModel = PersonModel()

# Create a proxy model for sorting and filtering
proxyModel = QSortFilterProxyModel()
proxyModel.setSourceModel(sourceModel)

# Set up filtering
proxyModel.setFilterCaseSensitivity(Qt.CaseInsensitive)
proxyModel.setFilterRole(PersonRoles.NamesRole)
proxyModel.setFilterRegularExpression("John")

# Set up sorting
proxyModel.sort(0, Qt.AscendingOrder)

# Connect to view
view.setModel(proxyModel)
```

### Drag and Drop Support

Enable drag and drop by implementing additional methods:

```python
def supportedDropActions(self):
    return Qt.MoveAction | Qt.CopyAction

def mimeTypes(self):
    return ["application/x-personmodel-item"]

def mimeData(self, indexes):
    mimeData = QMimeData()
    encodedData = QByteArray()
    stream = QDataStream(encodedData, QIODevice.WriteOnly)
    
    for index in indexes:
        if index.isValid():
            # Serialize the person data
            person = self.persons[index.row()]
            stream << person.names()
            stream << person.age()
            stream << person.favoriteColor()
    
    mimeData.setData("application/x-personmodel-item", encodedData)
    return mimeData

def dropMimeData(self, data, action, row, column, parent):
    if not data.hasFormat("application/x-personmodel-item"):
        return False
    
    if action == Qt.IgnoreAction:
        return True
    
    # Process the dropped data
    # ...
    
    return True
```

## Best Practices

1. **Use beginInsertRows() and endInsertRows()**

   Always use these methods when modifying the model structure:
   
   ```python
   self.beginInsertRows(QModelIndex(), startRow, endRow)
   # Insert rows...
   self.endInsertRows()
   ```

2. **Properly Clean Up Resources**

   Since Person objects are QObjects, make sure to clean them up:
   
   ```python
   def __del__(self):
       for person in self.persons:
           person.deleteLater()
   ```

3. **Validate Indices**

   Always check if an index is valid before using it:
   
   ```python
   if not index.isValid() or index.row() >= len(self.persons):
       return None
   ```

4. **Properly Signal Data Changes**

   When data changes, emit the dataChanged signal:
   
   ```python
   self.dataChanged.emit(topLeft, bottomRight)
   ```

5. **Manage Parent Indices in List Models**

   For list models, handle parent indices correctly:
   
   ```python
   def rowCount(self, parent=None):
       # Return 0 for valid parent indices, since lists don't have children
       if parent and parent.isValid():
           return 0
       return len(self.persons)
   ```

6. **Use Custom Model Methods**

   Create convenience methods for common operations:
   
   ```python
   def addPerson(self, person):
       # Implementation...
   
   def removePerson(self, index):
       # Implementation...
   ```

7. **Share Selection Models for Consistent UX**

   When multiple views show the same data, share selection models:
   
   ```python
   view2.setSelectionModel(view1.selectionModel())
   view3.setSelectionModel(view1.selectionModel())
   ```

## Conclusion

Advanced custom models in PySide6 offer powerful capabilities for representing and manipulating complex data structures. By implementing row insertion and removal, supporting editing, and coordinating multiple views, you can create sophisticated applications that provide a consistent and intuitive user experience.

This implementation demonstrates the key components needed for advanced models, including proper resource management, user interaction, and selection synchronization. These techniques can be expanded and adapted for more complex scenarios, including hierarchical data, multi-column tables, and specialized interaction patterns.