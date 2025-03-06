# Custom List Model Demo in PySide6

This project demonstrates implementing a custom `QAbstractListModel` in PySide6, showing how the same model can be used with multiple views.

## Project Overview

The application displays a list of people with their properties (name, age, favorite color) in three different view types:

1. **ListView**: Shows the names in a simple list format
2. **TableView**: Shows all data in a table format
3. **TreeView**: Shows the data in a hierarchical structure

All three views use the same model instance, with a shared selection model so selecting an item in one view also selects it in the others.

## Project Structure

```
custom_list_model/
│
├── main.py         # Application entry point
├── widget.py       # Main widget containing the views and buttons
├── ui_widget.py    # Generated UI code from widget.ui
├── person.py       # Person class with properties and signals
└── personmodel.py  # Custom QAbstractListModel implementation
```

## Building and Running the Project

1. Generate the UI Python file from the widget.ui file:
   ```bash
   pyside6-uic widget.ui -o ui_widget.py
   ```

2. Run the application:
   ```bash
   python main.py
   ```

## Implementation Details

### Person Class

The `Person` class represents a person with properties for name, age, and favorite color:

```python
class Person(QObject):
    # Signals for property changes
    namesChanged = Signal(str)
    favoriteColorChanged = Signal(str)
    ageChanged = Signal(int)
    
    def __init__(self, names="", favorite_color="", age=0, parent=None):
        super().__init__(parent)
        self._names = names
        self._favorite_color = favorite_color
        self._age = age
    
    # Getter and setter methods
    def names(self):
        return self._names
    
    def setNames(self, names):
        if self._names == names:
            return
        
        self._names = names
        self.namesChanged.emit(self._names)
```

### Custom List Model

The `PersonModel` class is a custom implementation of `QAbstractListModel` that manages a list of `Person` objects:

```python
class PersonModel(QAbstractListModel):
    # Define custom roles
    NamesRole = Qt.UserRole + 1
    FavoriteColorRole = Qt.UserRole + 2
    AgeRole = Qt.UserRole + 3
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # List to store Person objects
        self.persons = []
        
        # Populate with initial data
        self.persons.append(Person("Jamie Lannister", "red", 33, self))
        self.persons.append(Person("Marry Lane", "cyan", 26, self))
        # Additional persons...
```

### Implementing Model-View Requirements

The model implements the following required methods for `QAbstractListModel`:

- `rowCount()`: Returns the number of rows (persons) in the model
- `data()`: Returns data for different roles (display, edit, custom roles)
- `setData()`: Updates the data in the model based on the role
- `flags()`: Returns item flags (editable, selectable, etc.)
- `headerData()`: Provides header information for the views
- `insertRows()`: Adds new rows to the model
- `removeRows()`: Removes rows from the model

### Custom Roles

Custom roles are defined to access specific person properties:

```python
# Define custom roles
NamesRole = Qt.UserRole + 1
FavoriteColorRole = Qt.UserRole + 2
AgeRole = Qt.UserRole + 3
```

These are used both when setting and retrieving data:

```python
def data(self, index, role=Qt.DisplayRole):
    # ...
    if role == self.NamesRole:
        return person.names()
    
    if role == self.FavoriteColorRole:
        return person.favoriteColor()
    
    if role == self.AgeRole:
        return person.age()
```

### Main Widget

The main widget sets up the UI and connects the model to the three different views:

```python
def __init__(self, parent=None):
    # ...
    
    # Create the person model
    self.model = PersonModel(self)
    
    # Set the model for all three views
    self.ui.listView.setModel(self.model)
    self.ui.tableView.setModel(self.model)
    self.ui.treeView.setModel(self.model)
    
    # Share selection model between views
    self.ui.tableView.setSelectionModel(self.ui.listView.selectionModel())
    self.ui.treeView.setSelectionModel(self.ui.listView.selectionModel())
```

It also handles adding and removing persons through dialog interactions:

```python
def on_addPersonButton_clicked(self):
    # Get name from user
    name, ok = QInputDialog.getText(
        None, 
        "Names",
        "Person name:", 
        QLineEdit.Normal,
        "Type in name"
    )
    
    if ok and name:
        # Get age from user
        age = QInputDialog.getInt(
            None,
            "Person Age",
            "Age",
            20,  # Default value
            15,  # Min value
            120  # Max value
        )
        
        # Create and add new person
        person = Person(name, "blue", age[0], self)
        self.model.addPerson(person)
```

## Key Concepts

### Model-View Architecture

The Qt Model-View architecture separates data handling (model) from data visualization (views):

1. **Model**: Manages data and provides an interface for views to access it
2. **View**: Displays the data and handles user interaction
3. **Delegate**: (Optional) Handles rendering and editing of items

### QAbstractListModel vs. Other Model Types

- **QAbstractListModel**: For simple list-based data structures
- **QAbstractTableModel**: For two-dimensional table data
- **QAbstractItemModel**: For hierarchical tree-structured data

Although this example uses `QAbstractListModel`, the data is still displayed effectively in TableView and TreeView.

### Sharing Selection Models

By sharing the selection model between views, selecting an item in one view automatically selects the corresponding item in the other views:

```python
self.ui.tableView.setSelectionModel(self.ui.listView.selectionModel())
self.ui.treeView.setSelectionModel(self.ui.listView.selectionModel())
```

This creates a more integrated user experience across multiple views.

## Best Practices

1. **Use proper beginInsertRows/endInsertRows pairs**
   ```python
   self.beginInsertRows(QModelIndex(), row, row + count - 1)
   # Insert rows here
   self.endInsertRows()
   ```

2. **Emit dataChanged when data changes**
   ```python
   if something_changed:
       self.dataChanged.emit(index, index)
       return True
   ```

3. **Clean up resources in __del__**
   ```python
   def __del__(self):
       for person in self.persons:
           person.deleteLater()
   ```

4. **Use appropriate roles for data access**
   - `Qt.DisplayRole`: For text to display
   - `Qt.EditRole`: For editing data
   - Custom roles: For specific data types

5. **Check index validity**
   Always verify that an index is valid before using it:
   ```python
   if not index.isValid() or index.row() < 0 or index.row() >= len(self.persons):
       return None
   ```

## Conclusion

This project demonstrates how to create a custom list model that works with multiple view types in PySide6. Understanding the Model-View architecture is crucial for developing scalable and maintainable Qt/PySide6 applications, especially when dealing with complex data relationships.

By separating the data management (model) from the visual representation (views), you can create more flexible and reusable code that can adapt to different UI requirements.