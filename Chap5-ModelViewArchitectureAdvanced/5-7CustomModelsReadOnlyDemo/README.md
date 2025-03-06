# Custom Models in PySide6 - Implementation Guide

This guide demonstrates how to create and use custom models in PySide6 applications. The example application implements a custom data model for Person objects and displays it in multiple views.

## Project Overview

This application demonstrates:
- Creating a custom data class (Person)
- Implementing a custom model by subclassing QAbstractListModel
- Using the same model with different view types (ListView, TableView, TreeView)
- Working with Qt's Model-View architecture

## Project Structure

```
custom_model_demo/
│
├── main.py           # Application entry point
├── widget.py         # Main widget containing the views
├── person.py         # Person data class
├── personmodel.py    # Custom list model implementation
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

First, we define a data class that represents a person with properties and signals for change notification:

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
    
    def names(self):
        """Get the person's name"""
        return self._names
    
    # Additional getters and setters...
```

The Person class uses Qt's property system with getter and setter methods, along with signals that are emitted when properties change.

### The Custom Model

The custom model inherits from QAbstractListModel and implements the required methods:

```python
class PersonModel(QAbstractListModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # List to store Person objects
        self.persons = []
        
        # Populate with initial data
        self.persons.append(Person("Jamie Lannister", "red", 33))
        # Additional persons...
    
    def rowCount(self, parent=None):
        """Return the number of rows in the model"""
        return len(self.persons)
    
    def data(self, index, role=Qt.DisplayRole):
        """Return data for the specified index and role"""
        if not index.isValid() or index.row() < 0 or index.row() >= len(self.persons):
            return QVariant()
        
        person = self.persons[index.row()]
        
        if role == Qt.DisplayRole:
            return f"{person.names()} {person.age()} {person.favoriteColor()}"
        
        if role == Qt.ToolTipRole:
            return f"{person.names()} {index.row()}"
            
        return QVariant()
```

### Using the Model with Views

Finally, we connect the model to different view types:

```python
def __init__(self, parent=None):
    super().__init__(parent)
    self.ui = Ui_Widget()
    self.ui.setupUi(self)
    
    # Create the person model
    self.model = PersonModel(self)
    
    # Set the model for all three views
    self.ui.listView.setModel(self.model)
    self.ui.tableView.setModel(self.model)
    self.ui.treeView.setModel(self.model)
```

## Key Concepts

### Qt's Model-View Architecture

Qt's Model-View architecture separates data (Model) from presentation (View):

1. **Model**: Manages the data and provides an interface for views to access it
2. **View**: Displays the data and handles user interaction
3. **Delegate**: Handles rendering and editing of individual items (optional)

This separation allows the same data to be displayed in multiple ways without duplicating the data.

### Model Types

Qt provides several abstract model classes for different data structures:

- **QAbstractListModel**: For simple list-based data
- **QAbstractTableModel**: For tabular data with rows and columns
- **QAbstractItemModel**: For hierarchical tree-structured data

For this example, we use QAbstractListModel since our data is a simple list of Person objects.

### Model Methods

When implementing a custom model, you must implement certain methods:

- **rowCount()**: Returns the number of rows (items) in the model
- **data()**: Returns the data for a specific model index and role

For editable models, you would also implement:

- **setData()**: Sets data for a specific index
- **flags()**: Returns item flags (e.g., Qt.ItemIsEditable)

For table or tree models, additional methods are required:

- **columnCount()**: Returns the number of columns (for table models)
- **headerData()**: Returns header data for rows and columns
- **index()** and **parent()**: Establish the hierarchy (for tree models)

### Data Roles

Qt uses roles to request different aspects of the data:

- **Qt.DisplayRole (0)**: Data to be displayed as text
- **Qt.DecorationRole (1)**: Data to be displayed as an icon
- **Qt.EditRole (2)**: Data to be edited
- **Qt.ToolTipRole (3)**: Data for tooltips
- **Qt.StatusTipRole (4)**: Data for status bar tips
- **Qt.UserRole (32+)**: Base value for custom roles

In our example, we implement DisplayRole and ToolTipRole.

## Advanced Techniques

### Implementing a Table Model

To extend our example to a proper table model with multiple columns:

```python
class PersonTableModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.persons = []  # List of Person objects
        # Populate data...
    
    def rowCount(self, parent=None):
        """Return the number of rows"""
        return len(self.persons)
    
    def columnCount(self, parent=None):
        """Return the number of columns"""
        return 3  # Name, Age, Favorite Color
    
    def data(self, index, role=Qt.DisplayRole):
        """Return data for the requested index and role"""
        if not index.isValid():
            return QVariant()
        
        if index.row() >= len(self.persons):
            return QVariant()
        
        person = self.persons[index.row()]
        
        if role == Qt.DisplayRole:
            if index.column() == 0:
                return person.names()
            elif index.column() == 1:
                return person.age()
            elif index.column() == 2:
                return person.favoriteColor()
        
        return QVariant()
    
    def headerData(self, section, orientation, role=Qt.DisplayRole):
        """Return header data for the model"""
        if role != Qt.DisplayRole:
            return QVariant()
        
        if orientation == Qt.Horizontal:
            if section == 0:
                return "Name"
            elif section == 1:
                return "Age"
            elif section == 2:
                return "Favorite Color"
        
        return QVariant()
```

### Making the Model Editable

To allow editing of data in the model:

```python
def flags(self, index):
    """Return item flags"""
    if not index.isValid():
        return Qt.NoItemFlags
    
    return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

def setData(self, index, value, role=Qt.EditRole):
    """Set data for the specified index"""
    if not index.isValid() or role != Qt.EditRole:
        return False
    
    if index.row() >= len(self.persons):
        return False
    
    person = self.persons[index.row()]
    
    if index.column() == 0:
        person.setNames(value)
    elif index.column() == 1:
        try:
            person.setAge(int(value))
        except ValueError:
            return False
    elif index.column() == 2:
        person.setFavoriteColor(value)
    else:
        return False
    
    # Notify views that data has changed
    self.dataChanged.emit(index, index, [role])
    return True
```

### Adding and Removing Items

To add or remove items from the model:

```python
def addPerson(self, person):
    """Add a new person to the model"""
    # Notify views that rows will be inserted
    self.beginInsertRows(QModelIndex(), len(self.persons), len(self.persons))
    
    # Add the person
    self.persons.append(person)
    
    # Notify views that rows have been inserted
    self.endInsertRows()
    return True

def removePerson(self, row):
    """Remove a person from the model"""
    if row < 0 or row >= len(self.persons):
        return False
    
    # Notify views that rows will be removed
    self.beginRemoveRows(QModelIndex(), row, row)
    
    # Remove the person
    del self.persons[row]
    
    # Notify views that rows have been removed
    self.endRemoveRows()
    return True
```

### Implementing Custom Roles

To add custom roles:

```python
# Define custom roles
class PersonRoles:
    NamesRole = Qt.UserRole + 1
    AgeRole = Qt.UserRole + 2
    FavoriteColorRole = Qt.UserRole + 3

def data(self, index, role=Qt.DisplayRole):
    # Handle standard roles...
    
    # Handle custom roles
    if role == PersonRoles.NamesRole:
        return person.names()
    elif role == PersonRoles.AgeRole:
        return person.age()
    elif role == PersonRoles.FavoriteColorRole:
        return person.favoriteColor()
    
    return QVariant()
```

### Using Custom Delegates

To customize the appearance or editing of items:

```python
from PySide6.QtWidgets import QStyledItemDelegate, QLineEdit, QSpinBox, QComboBox

class PersonDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        """Create an editor for editing the data"""
        if index.column() == 0:
            # Name editor
            editor = QLineEdit(parent)
            return editor
        elif index.column() == 1:
            # Age editor
            editor = QSpinBox(parent)
            editor.setMinimum(0)
            editor.setMaximum(120)
            return editor
        elif index.column() == 2:
            # Color editor
            editor = QComboBox(parent)
            editor.addItems(QColor.colorNames())
            return editor
        
        return super().createEditor(parent, option, index)
    
    def setEditorData(self, editor, index):
        """Set the editor data"""
        value = index.model().data(index, Qt.EditRole)
        
        if index.column() == 0:
            editor.setText(value)
        elif index.column() == 1:
            editor.setValue(int(value))
        elif index.column() == 2:
            colorNames = QColor.colorNames()
            colorIndex = colorNames.index(value) if value in colorNames else 0
            editor.setCurrentIndex(colorIndex)
        else:
            super().setEditorData(editor, index)
    
    def setModelData(self, editor, model, index):
        """Set the model data"""
        if index.column() == 0:
            model.setData(index, editor.text(), Qt.EditRole)
        elif index.column() == 1:
            model.setData(index, editor.value(), Qt.EditRole)
        elif index.column() == 2:
            model.setData(index, editor.currentText(), Qt.EditRole)
        else:
            super().setModelData(editor, model, index)
```

To use the delegate:

```python
delegate = PersonDelegate()
tableView.setItemDelegate(delegate)
```

## Best Practices

1. **Keep the Model Simple and Focused**

   A model should focus on providing data to views without any UI logic:
   
   ```python
   # Good - Model only manages data
   def data(self, index, role):
       return self.persons[index.row()].names()
   
   # Bad - Model contains UI logic
   def data(self, index, role):
       name = self.persons[index.row()].names()
       return f"<b>{name}</b>"  # HTML formatting should be in a delegate
   ```

2. **Use beginInsertRows() / endInsertRows() for Adding Items**

   Always notify views about changes to the model structure:
   
   ```python
   # Correct way to add items
   def addPerson(self, person):
       self.beginInsertRows(QModelIndex(), rowCount(), rowCount())
       self.persons.append(person)
       self.endInsertRows()
   ```

3. **Emit dataChanged() Signal When Data Changes**

   Notify views when data changes:
   
   ```python
   def updatePerson(self, row, person):
       if row < 0 or row >= len(self.persons):
           return False
           
       self.persons[row] = person
       index = self.index(row, 0)
       self.dataChanged.emit(index, index)
       return True
   ```

4. **Check Index Validity**

   Always check if indices are valid before accessing data:
   
   ```python
   def data(self, index, role):
       if not index.isValid() or index.row() >= len(self.persons):
           return QVariant()
       # Process valid index...
   ```

5. **Implement Invalid Return Values Correctly**

   Return an invalid QVariant for invalid indices or unsupported roles:
   
   ```python
   def data(self, index, role):
       if not supported_role:
           return QVariant()  # Invalid QVariant
   ```

6. **Consider Performance**

   For large datasets, implement techniques to improve performance:
   
   ```python
   # Lazy loading
   def fetchMore(self, parent):
       # Load additional data when needed
   
   def canFetchMore(self, parent):
       # Return True if more data is available
   ```

## Conclusion

Creating custom models in PySide6 gives you complete control over how your data is presented to views. By understanding the Model-View architecture and implementing the required interfaces correctly, you can create flexible, reusable models that work with Qt's standard views and your own custom views.

This implementation demonstrates the basics of custom model creation using QAbstractListModel. For more complex data structures, consider using QAbstractTableModel or QAbstractItemModel, and implement additional methods as needed to fully support the Model-View architecture.