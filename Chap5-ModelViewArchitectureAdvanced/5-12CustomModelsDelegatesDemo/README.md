# Person Model with Custom Delegate in PySide6

This project demonstrates implementing a custom `QAbstractTableModel` with a `QStyledItemDelegate` in PySide6, showcasing advanced Model-View-Delegate architecture.

## Project Overview

The application displays a list of people with their properties (name, age, favorite color) in three different view types:

1. **ListView**: Shows the names in a simple list format
2. **TableView**: Shows all data in a table format with a custom color editor for the favorite color column
3. **TreeView**: Shows the data in a hierarchical structure with custom editing for all columns

Key features:
- Custom table model with multiple columns
- Custom delegate for color selection with a visual color picker
- Shared selection model across multiple views
- Add/remove person functionality

## Project Structure

```
person_model_delegate/
│
├── main.py            # Application entry point
├── widget.py          # Main widget containing the views and buttons
├── ui_widget.py       # Generated UI code from widget.ui
├── person.py          # Person class with properties and signals
├── personmodel.py     # Custom QAbstractTableModel implementation
└── persondelegate.py  # Custom QStyledItemDelegate for color editing
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

The `Person` class represents a person with properties for name, age, and favorite color, with proper signal emission when values change:

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
```

### Custom Table Model

The `PersonModel` class is a custom implementation of `QAbstractTableModel` that manages a list of `Person` objects and displays data in multiple columns:

```python
class PersonModel(QAbstractTableModel):
    # Define custom roles
    NamesRole = Qt.UserRole + 1
    FavoriteColorRole = Qt.UserRole + 2
    AgeRole = Qt.UserRole + 3
    
    def columnCount(self, parent=QModelIndex()):
        """Return the number of columns in the model"""
        if parent.isValid():
            return 0
        return 3
```

### Custom Delegate for Color Editing

The `PersonDelegate` extends `QStyledItemDelegate` to provide a custom editor for color selection:

```python
def createEditor(self, parent, option, index):
    """Create editor widget for editing data"""
    if index.column() == 2:  # Favorite color column
        editor = QComboBox(parent)
        
        # Add all color names with color swatches as icons
        for color in QColor.colorNames():
            pixmap = QPixmap(50, 50)
            pixmap.fill(QColor(color))
            editor.addItem(QIcon(pixmap), color)
        
        return editor
    else:
        # For other columns, use default editor
        return super().createEditor(parent, option, index)
```

### Main Widget Setup

The main widget configures the views, model, and delegates:

```python
def __init__(self, parent=None):
    # Create the custom delegate for color editing
    self.person_delegate = PersonDelegate(self)
    
    # Create the person model
    self.model = PersonModel(self)
    
    # Set the model for all views
    self.ui.listView.setModel(self.model)
    
    self.ui.tableView.setModel(self.model)
    # Set delegate for the color column only in table view
    self.ui.tableView.setItemDelegateForColumn(2, self.person_delegate)
    
    self.ui.treeView.setModel(self.model)
    # Set delegate for all columns in tree view
    self.ui.treeView.setItemDelegate(self.person_delegate)
```

## Key Concepts

### Model-View-Delegate Architecture

The Qt Model-View-Delegate architecture separates responsibilities:

1. **Model**: Manages data and provides an interface (PersonModel)
2. **View**: Displays the data and handles user interaction (ListView, TableView, TreeView)
3. **Delegate**: Handles rendering and editing of items (PersonDelegate)

### Custom Delegates

Delegates in Qt/PySide6 control how items are rendered and edited. The custom delegate in this project provides:

1. A specialized editor (QComboBox with color icons)
2. Custom handling of editor geometry and layout
3. Control over how data transfers between the model and editor

### Different Uses of Delegates

The project demonstrates two ways to apply delegates:

1. **Column-specific delegation**: `setItemDelegateForColumn()` applies a delegate to a specific column
   ```python
   self.ui.tableView.setItemDelegateForColumn(2, self.person_delegate)
   ```

2. **View-wide delegation**: `setItemDelegate()` applies a delegate to an entire view
   ```python
   self.ui.treeView.setItemDelegate(self.person_delegate)
   ```

### QComboBox with Icons as Editor

The delegate uses a QComboBox with color icons for a visual color picker:

```python
editor = QComboBox(parent)
for color in QColor.colorNames():
    pixmap = QPixmap(50, 50)
    pixmap.fill(QColor(color))
    editor.addItem(QIcon(pixmap), color)
```

## Advanced Techniques

### Delegate Editor Lifecycle

The delegate editor lifecycle follows this sequence:

1. **createEditor()**: Creates the editor widget
2. **setEditorData()**: Populates the editor with model data
3. **updateEditorGeometry()**: Positions the editor
4. (User edits the data)
5. **setModelData()**: Updates the model with editor data

### Delegate Size Hints

Custom size hints ensure the delegate renders appropriately:

```python
def sizeHint(self, option, index):
    """Provide size hint for items"""
    default_size = super().sizeHint(option, index)
    return default_size.expandedTo(QSize(64, option.fontMetrics.height() + 10))
```

### Working with Multiple View Types

The same model can be used with different view types, each providing a different visualization of the data:

- **ListView**: Simple list showing just the first column
- **TableView**: Grid showing all columns
- **TreeView**: Hierarchical tree structure

### Shared Selection Model

Sharing a selection model between views keeps selections synchronized:

```python
self.ui.tableView.setSelectionModel(self.ui.listView.selectionModel())
self.ui.treeView.setSelectionModel(self.ui.listView.selectionModel())
```

## Best Practices

1. **Separate Concerns**
   - Keep model, view, and delegate responsibilities distinct
   - Delegate should only control rendering and editing

2. **Use Column-Specific Delegates**
   - Apply delegates only where needed to improve performance
   - Use `setItemDelegateForColumn()` for targeted delegation

3. **Proper Editor Cleanup**
   - Editor widgets are automatically deleted after use
   - No need to manually delete editor widgets

4. **Validate Data**
   - Validate data in `setModelData()` before updating the model
   - Return false from `setData()` if validation fails

5. **Handle Editor Geometry**
   - Properly implement `updateEditorGeometry()` for proper editor placement
   - Consider using option.rect to position the editor

## Conclusion

This project demonstrates the power of Qt's Model-View-Delegate architecture for creating rich, interactive interfaces with custom data visualization and editing capabilities. By understanding how to implement custom models and delegates, you can create sophisticated applications that provide intuitive user interfaces for complex data.