# Person Model with Custom Delegate in PySide6

This project demonstrates implementing a custom `QAbstractTableModel` with a `QStyledItemDelegate` in PySide6, showcasing advanced Model-View-Delegate architecture with custom visualization.

## Project Overview

The application displays a list of people with their properties (name, age, favorite color) in three different view types:

1. **ListView**: Shows the names in a simple list format
2. **TableView**: Shows all data in a table format with a custom color editor and visualization for the favorite color column
3. **TreeView**: Shows the data in a hierarchical structure with custom editing and visualization for all columns

Key features:
- Custom table model with multiple columns
- Custom delegate for color selection with a visual color picker
- Custom painting for visualizing the selected color in the view
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
└── persondelegate.py  # Custom QStyledItemDelegate for color editing and visualization
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

### Custom Delegate for Color Editing and Visualization

The `PersonDelegate` extends `QStyledItemDelegate` to provide both a custom editor for color selection and custom visualization of the color in the view:

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

The custom `paint` method provides visual representation of the favorite color:

```python
def paint(self, painter, option, index):
    """Custom painting for favorite color column"""
    if index.column() == 2:  # Favorite color column
        # Highlight selected cell
        if option.state & QStyle.State_Selected:
            painter.fillRect(option.rect, option.palette.highlight())
        
        # Get favorite color
        fav_color = index.data(PersonModel.FavoriteColorRole)
        
        painter.save()
        
        # Set brush to favorite color
        painter.setBrush(QBrush(QColor(fav_color)))
        
        # Draw colored rectangle
        painter.drawRect(option.rect.adjusted(3, 3, -3, -3))
        
        # Draw white rectangle with text in the center
        # ...
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

### Custom Painting in Delegates

The `paint` method allows the delegate to completely control how items are rendered. This project uses custom painting to:

1. Draw a colored rectangle representing the favorite color
2. Draw a white rectangle for text visibility
3. Display the color name in the center

```python
def paint(self, painter, option, index):
    """Custom painting for favorite color column"""
    if index.column() == 2:
        # Custom painting for color column
        # ...
    else:
        # Default painting for other columns
        super().paint(painter, option, index)
```

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

### QPainter Basics

The custom painting uses various QPainter methods:

- `save()` / `restore()`: Save and restore painter state
- `setBrush()`: Set the fill color for shapes
- `drawRect()`: Draw rectangles
- `drawText()`: Draw text with alignment
- `fillRect()`: Fill an area with a color

### Delegate Paint Method

The paint method follows this general workflow:

1. Check if we need custom painting (column check)
2. Paint selection highlight if item is selected
3. Get data from the model
4. Save the painter state
5. Paint custom elements (colored rectangle, text, etc.)
6. Restore the painter state

### Working with Multiple View Types

The same model and delegate can be used with different view types, each providing a different visualization:

- **ListView**: Simple list showing just the first column
- **TableView**: Grid showing all columns with custom column delegates
- **TreeView**: Hierarchical tree structure with a delegate for all columns

### Shared Selection Model

Sharing a selection model between views keeps selections synchronized:

```python
self.ui.tableView.setSelectionModel(self.ui.listView.selectionModel())
self.ui.treeView.setSelectionModel(self.ui.listView.selectionModel())
```

## Best Practices

1. **Separate Display Logic from Data Logic**
   - Keep painting and editing code in delegates
   - Keep data management in the model

2. **Use Custom Roles for Data Access**
   - Define custom roles for specific data types
   - Access data consistently through these roles

3. **Optimize Painting**
   - Only do custom painting when needed (column check)
   - Use `save()` and `restore()` to manage painter state
   - Consider the cost of painting operations

4. **Validate User Input**
   - Ensure data is valid before updating the model
   - Use appropriate editors for different data types

5. **Handle Editor Cleanup**
   - Qt automatically manages editor widget lifecycle
   - Focus on creating appropriate editors and transferring data

## Conclusion

This project demonstrates the power of Qt's Model-View-Delegate architecture for creating rich, interactive interfaces with custom data visualization and editing capabilities. The combination of a custom model and a delegate with custom painting provides a polished user experience that intuitively represents the data being edited.

Custom painting in delegates allows for rich visualizations that go far beyond standard cell rendering, enabling applications to provide immediate visual feedback about the data they contain. These techniques are essential for developing professional-grade Qt/PySide6 applications.