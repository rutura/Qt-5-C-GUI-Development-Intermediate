# Custom Roles in PySide6 Models - Implementation Guide

This guide demonstrates how to implement custom data roles in PySide6 models, which allow you to store and retrieve multiple pieces of data for each item in a model.

## Project Overview

This application demonstrates:
- Creating custom data roles to store different properties
- Implementing data() and setData() to handle multiple roles
- Defining roleNames() for QML integration
- Advanced implementation of add/remove operations

## Project Structure

```
custom_roles_model_demo/
│
├── main.py           # Application entry point
├── widget.py         # Main widget containing the views
├── person.py         # Person data class
├── personmodel.py    # Custom model with roles implementation
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

### Defining Custom Roles

Custom roles are defined as class attributes in the model:

```python
class PersonModel(QAbstractListModel):
    # Define custom roles
    NamesRole = Qt.UserRole + 1
    FavoriteColorRole = Qt.UserRole + 2
    AgeRole = Qt.UserRole + 3
```

Each role receives a unique integer ID, typically starting from `Qt.UserRole + 1`. These roles act as keys to access different properties of the data items.

### Implementing data() with Multiple Roles

The data() method returns different data depending on the requested role:

```python
def data(self, index, role=Qt.DisplayRole):
    """Return data for the specified index and role"""
    if not index.isValid() or index.row() < 0 or index.row() >= len(self.persons):
        return None
    
    person = self.persons[index.row()]
    
    if role == Qt.DisplayRole:
        return person.names()
    
    if role == Qt.EditRole:
        print("Data method called with edit role")
        return person.names()
    
    if role == self.NamesRole:
        return person.names()
    
    if role == self.FavoriteColorRole:
        return person.favoriteColor()
    
    if role == self.AgeRole:
        return person.age()
    
    # ... other roles ...
    
    return None
```

### Implementing setData() with Multiple Roles

Similarly, setData() handles different roles for modifying data:

```python
def setData(self, index, value, role=Qt.EditRole):
    """Set data for the specified index and role"""
    if not index.isValid():
        return False
    
    person = self.persons[index.row()]
    something_changed = False
    
    if role == Qt.EditRole:
        if person.names() != value:
            person.setNames(value)
            something_changed = True
    
    elif role == self.NamesRole:
        print(f"Names role changing names, index {index.row()}")
        if person.names() != value:
            person.setNames(value)
            something_changed = True
    
    elif role == self.AgeRole:
        if person.age() != value:
            person.setAge(value)
            something_changed = True
    
    elif role == self.FavoriteColorRole:
        if person.favoriteColor() != value:
            person.setFavoriteColor(value)
            something_changed = True
    
    if something_changed:
        self.dataChanged.emit(index, index)
        return True
    
    return False
```

### Defining Role Names for QML

For QML integration, the roleNames() method maps role IDs to role names:

```python
def roleNames(self):
    """Return role names for QML integration"""
    roles = {}
    roles[self.NamesRole] = QByteArray(b"names")
    roles[self.FavoriteColorRole] = QByteArray(b"favoritecolor")
    roles[self.AgeRole] = QByteArray(b"age")
    return roles
```

### Advanced Add Operation

This implementation demonstrates a more advanced add operation that uses insertRows() and setData():

```python
def addPerson(self, person):
    """Add a given person to the model using insertRows and setData"""
    self.insertRows(len(self.persons), 1)
    index = self.index(len(self.persons) - 1)
    self.setData(index, person.names(), self.NamesRole)
    self.setData(index, person.favoriteColor(), self.FavoriteColorRole)
    self.setData(index, person.age(), self.AgeRole)
```

## Key Concepts

### Data Roles in Qt's Model-View

Data roles separate different aspects of an item's data:

- **Qt.DisplayRole (0)**: The text to display
- **Qt.DecorationRole (1)**: The icon to display
- **Qt.EditRole (2)**: The text to edit
- **Qt.ToolTipRole (3)**: The tooltip text
- **Qt.StatusTipRole (4)**: The status bar text
- **Qt.UserRole (32+)**: Base value for custom roles

### Custom Roles vs. Multiple Columns

There are two main approaches to handling multiple properties in a model:

1. **Multiple columns**: Each property is a separate column
   - Good for tabular data
   - Naturally fits QTableView
   - Each column has a header

2. **Custom roles**: Each property is a different role
   - Good for complex or non-tabular data
   - Works well with QListView and custom delegates
   - Can be displayed in different ways without changing the model

This example uses custom roles for flexibility, showing how a single-column list model can store multiple properties per item.

### Role Names and QML

The roleNames() method is especially important for QML integration, as it maps role IDs to names that can be used in QML bindings:

```qml
ListView {
    model: personModel
    delegate: Text {
        // Access data through role names
        text: names + " (" + age + ")"
        color: favoritecolor
    }
}
```

## Advanced Techniques

### Custom Delegates with Multiple Roles

To display multiple roles in a single view, create a custom delegate:

```python
from PySide6.QtWidgets import QStyledItemDelegate, QStyle
from PySide6.QtGui import QColor, QPen, QBrush

class PersonDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        # Get data for different roles
        name = index.data(PersonModel.NamesRole)
        age = index.data(PersonModel.AgeRole)
        color = index.data(PersonModel.FavoriteColorRole)
        
        # Draw selection background
        if option.state & QStyle.State_Selected:
            painter.fillRect(option.rect, option.palette.highlight())
            
        # Set text color based on selection
        if option.state & QStyle.State_Selected:
            painter.setPen(QPen(option.palette.highlightedText().color()))
        else:
            painter.setPen(QPen(option.palette.text().color()))
            
        # Draw name and age
        text = f"{name} ({age})"
        painter.drawText(option.rect.adjusted(5, 5, -5, -5), 0, text)
        
        # Draw color indicator
        painter.fillRect(
            option.rect.right() - 20, option.rect.top() + 5, 
            15, 15, QColor(color)
        )
```

### Filtering and Sorting with Custom Roles

Use QSortFilterProxyModel with custom roles:

```python
from PySide6.QtCore import QSortFilterProxyModel

class AgeFilterModel(QSortFilterProxyModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.min_age = 0
        self.max_age = 999
        
    def setAgeRange(self, min_age, max_age):
        self.min_age = min_age
        self.max_age = max_age
        self.invalidateFilter()
        
    def filterAcceptsRow(self, source_row, source_parent):
        source_index = self.sourceModel().index(source_row, 0, source_parent)
        age = self.sourceModel().data(source_index, PersonModel.AgeRole)
        
        return self.min_age <= age <= self.max_age
```

### Using Custom Roles in Views

Standard views only use DisplayRole and DecorationRole by default. To show data from custom roles, use a custom delegate or subclass the view:

```python
class CustomListView(QListView):
    def __init__(self, parent=None):
        super().__init__(parent)
        
    def viewOptions(self):
        options = super().viewOptions()
        # Customize view options
        return options
```

### Multi-Property Editing with Custom Dialogs

For editing multiple properties at once, create a custom dialog:

```python
from PySide6.QtWidgets import QDialog, QFormLayout, QLineEdit, QSpinBox, QDialogButtonBox

class PersonEditDialog(QDialog):
    def __init__(self, person, parent=None):
        super().__init__(parent)
        self.person = person
        self.setWindowTitle("Edit Person")
        
        layout = QFormLayout(self)
        
        # Name field
        self.name_edit = QLineEdit(person.names())
        layout.addRow("Name:", self.name_edit)
        
        # Age field
        self.age_edit = QSpinBox()
        self.age_edit.setRange(0, 120)
        self.age_edit.setValue(person.age())
        layout.addRow("Age:", self.age_edit)
        
        # Color field
        # ... color selector ...
        
        # Buttons
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)
        
    def accept(self):
        # Update person with new values
        self.person.setNames(self.name_edit.text())
        self.person.setAge(self.age_edit.value())
        super().accept()
```

## Best Practices

1. **Define Clear Role Constants**

   Define role constants at the class level with clear names:
   
   ```python
   class MyModel(QAbstractListModel):
       NameRole = Qt.UserRole + 1
       AgeRole = Qt.UserRole + 2
       # ...
   ```

2. **Handle Missing or Invalid Data**

   Always check for invalid indices and handle missing data gracefully:
   
   ```python
   def data(self, index, role):
       if not index.isValid():
           return None
       # ...
   ```

3. **Use a Switch-Like Structure for Roles**

   Organize role handling in a clear way:
   
   ```python
   def setData(self, index, value, role):
       # ...
       if role == Qt.EditRole:
           # Handle edit role
       elif role == self.NameRole:
           # Handle name role
       elif role == self.AgeRole:
           # Handle age role
       # ...
   ```

4. **Emit dataChanged() When Appropriate**

   Only emit dataChanged() when data actually changes:
   
   ```python
   something_changed = False
   # ... change data ...
   if something_changed:
       self.dataChanged.emit(index, index)
       return True
   return False
   ```

5. **Consider Performance with Many Roles**

   If you have many roles, consider a more efficient way to store and retrieve data:
   
   ```python
   # Less efficient with many roles
   if role == self.Role1: return value1
   elif role == self.Role2: return value2
   # ...
   
   # More efficient
   role_mapping = {
       self.Role1: lambda obj: obj.value1(),
       self.Role2: lambda obj: obj.value2(),
       # ...
   }
   
   if role in role_mapping:
       return role_mapping[role](self.items[index.row()])
   ```

6. **Implement roleNames() for QML Integration**

   Always implement roleNames() for QML integration:
   
   ```python
   def roleNames(self):
       roles = {}
       roles[self.NameRole] = QByteArray(b"name")
       roles[self.AgeRole] = QByteArray(b"age")
       # ...
       return roles
   ```

## Conclusion

Custom roles provide a powerful way to store and retrieve multiple properties for items in Qt models. By using custom roles, you can create flexible models that work with different views and can be styled and filtered in various ways.

This implementation demonstrates how to define and use custom roles for a Person model, including adding and removing items, displaying and editing different properties, and integrating with QML. These techniques can be applied to more complex models with various data types and relationships.