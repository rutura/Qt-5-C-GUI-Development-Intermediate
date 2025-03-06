# Multiple Custom Delegates in PySide6

This project demonstrates how to implement and use multiple custom delegates in a single PySide6 application. The application displays a table of people with custom visualizations for both colors and star ratings.

## Project Overview

The application displays a table of people with four columns:
- Name
- Age
- Favorite Color (with color visualization)
- Social Score (with star rating visualization)

Two different custom delegates are used:
1. **PersonDelegate**: Renders favorite colors as colored rectangles with text
2. **StarDelegate**: Renders social scores as star ratings (0-5 stars)

Both delegates also provide custom editors for their respective columns.

## Project Structure

```
multiple_delegates/
│
├── main.py             # Application entry point
├── widget.py           # Main widget containing the views
├── ui_widget.py        # Generated UI code from widget.ui
├── person.py           # Person class with properties
├── personmodel.py      # Custom QAbstractTableModel implementation
├── persondelegate.py   # Custom delegate for color visualization/editing
├── stareditor.py       # Custom editor widget for star ratings
└── stardelegate.py     # Custom delegate for star visualization/editing
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

The `Person` class represents a person with properties for name, age, favorite color, and social score:

```python
class Person(QObject):
    # Signals for property changes
    namesChanged = Signal(str)
    favoriteColorChanged = Signal(str)
    ageChanged = Signal(int)
    
    def __init__(self, names="", favorite_color="", age=0, social_score=0, parent=None):
        super().__init__(parent)
        self._names = names
        self._favorite_color = favorite_color
        self._age = age
        self._social_score = social_score
```

### Custom Table Model

The `PersonModel` class is a custom implementation of `QAbstractTableModel` that manages a list of `Person` objects and exposes their data through multiple columns:

```python
class PersonModel(QAbstractTableModel):
    # Define custom roles
    NamesRole = Qt.UserRole + 1
    FavoriteColorRole = Qt.UserRole + 2
    AgeRole = Qt.UserRole + 3
    SocialScoreRole = Qt.UserRole + 4
    
    def columnCount(self, parent=QModelIndex()):
        """Return the number of columns in the model"""
        if parent.isValid():
            return 0
        return 4  # Name, Age, Favorite Color, Social Score
```

### Color Delegate

The `PersonDelegate` extends `QStyledItemDelegate` to provide custom rendering and editing for the favorite color column:

```python
def paint(self, painter, option, index):
    """Custom painting for favorite color column"""
    if index.column() == 2:  # Favorite color column
        # Highlight selected cell
        if option.state & QStyle.State_Selected:
            painter.fillRect(option.rect, option.palette.highlight())
        
        # Get favorite color
        fav_color = index.data(PersonModel.FavoriteColorRole)
        
        # Draw colored rectangle and text
        # ...
```

### Star Rating Editor

The `StarEditor` widget provides an interactive way to edit star ratings:

```python
def mouseMoveEvent(self, event):
    """Handle mouse move events to update the star rating"""
    rating = int(event.position().x() // 20)
    
    # Only update if the rating has changed and is valid
    if rating != self.starRating and rating < 6:
        self.starRating = rating
        self.update()  # Trigger a repaint
```

### Star Rating Delegate

The `StarDelegate` extends `QStyledItemDelegate` to provide custom rendering and editing for star ratings:

```python
def paint(self, painter, option, index):
    """Custom paint method to draw stars"""
    if index.column() == 3:  # Social score column
        rect = option.rect.adjusted(10, 10, -10, -10)
        star_number = index.data()
        
        # Draw stars based on rating
        # ...
```

### Main Widget Setup

The main widget configures the views, model, and both delegates:

```python
def __init__(self, parent=None):
    # Create the custom delegates
    self.person_delegate = PersonDelegate(self)
    self.star_delegate = StarDelegate(self)
    
    # Configure table view
    self.ui.tableView.setModel(self.model)
    self.ui.tableView.setItemDelegateForColumn(2, self.person_delegate)  # Color delegate
    self.ui.tableView.setItemDelegateForColumn(3, self.star_delegate)    # Star delegate
```

## Key Concepts

### Multiple Delegates in the Same View

This project shows how to use different delegates for different columns in the same view:

```python
# Column-specific delegates
self.ui.tableView.setItemDelegateForColumn(2, self.person_delegate)  # Color delegate
self.ui.tableView.setItemDelegateForColumn(3, self.star_delegate)    # Star delegate
```

### Delegate Mixing in Different Views

The project also demonstrates using different combinations of delegates in different views:

```python
# Table view - specific delegates per column
self.ui.tableView.setItemDelegateForColumn(2, self.person_delegate)
self.ui.tableView.setItemDelegateForColumn(3, self.star_delegate)

# Tree view - default delegate with one specific column override
self.ui.treeView.setItemDelegate(self.person_delegate)
self.ui.treeView.setItemDelegateForColumn(3, self.star_delegate)
```

### Custom Painting

Both delegates implement the `paint` method to provide custom visualization:

1. **PersonDelegate**: Draws a colored rectangle with the color name
2. **StarDelegate**: Draws a series of stars based on the rating

### Custom Editors

Both delegates also provide custom editors for interactive editing:

1. **PersonDelegate**: Uses a `QComboBox` with color swatches
2. **StarDelegate**: Uses a custom `StarEditor` widget

### Shared Selection

The project shares the selection model between views, so selecting in one view highlights the corresponding row in the others:

```python
self.ui.tableView.setSelectionModel(self.ui.listView.selectionModel())
self.ui.treeView.setSelectionModel(self.ui.listView.selectionModel())
```

## Advanced Techniques

### QPainter Usage

The project demonstrates several QPainter techniques:

1. **State Management**: Using `save()` and `restore()` to manage painter state
2. **Coordinate Transformations**: Using `translate()` and `scale()`
3. **Drawing Shapes**: Rectangles and polygons (stars)
4. **Text Rendering**: Centered text display

### Custom Editor Communication

The custom editors communicate back to their delegates using signals:

```python
# In StarDelegate
editor.editingFinished.connect(self.commitAndCloseEditor)

# The slot that handles the signal
@Slot()
def commitAndCloseEditor(self):
    editor = self.sender()
    self.commitData.emit(editor)
    self.closeEditor.emit(editor)
```

### Delegate Selection Logic

Both delegates check the column index before applying custom rendering or editing:

```python
def paint(self, painter, option, index):
    if index.column() == 3:  # Social score column
        # Custom painting
    else:
        # Default painting
        super().paint(painter, option, index)
```

## Best Practices

1. **Column-Specific Delegates**
   - Apply delegates only to relevant columns for better performance
   - Use `setItemDelegateForColumn()` for targeted delegation

2. **Data Role Separation**
   - Use custom roles to clearly separate different types of data
   - Keep role constants in the model for clarity

3. **Editor Simplicity**
   - Keep custom editors focused on a single editing task
   - Use signals to communicate when editing is complete

4. **Pointer Safety**
   - Use `qobject_cast<>` to safely convert from generic QWidget to specific editor types
   - Let Qt handle editor cleanup through the parent-child relationship

5. **Type Handling**
   - Handle different data types carefully, especially when converting between them
   - Provide fallbacks for invalid data conversions

## Conclusion

This project demonstrates the power and flexibility of Qt's Model-View-Delegate architecture. By using multiple custom delegates, you can create rich, interactive interfaces that provide specialized visualization and editing for different types of data.

The combination of a color delegate and a star rating delegate shows how different delegates can coexist in the same application, providing a cohesive user experience while handling different data types in their own specialized ways.