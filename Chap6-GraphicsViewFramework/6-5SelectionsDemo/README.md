# PySide6 Graphics View Drawing Tool - Implementation Guide

This guide demonstrates how to implement a drawing tool application using PySide6's Graphics View Framework. The project shows how to create an interactive application where users can select different drawing tools, create shapes, and modify their appearance.

## Project Overview

This application demonstrates:
- Creating a custom QGraphicsView for handling drawing operations
- Implementing different drawing tools (cursor, line, ellipse, path, pie, image, star)
- Adding movable and selectable graphics items to a scene
- Changing the color of selected items
- Organizing graphics items with parent-child relationships

## Project Structure

```
graphics_view_drawing_tool/
│
├── main.py           # Application entry point
├── widget.py         # Main widget containing the UI and controls
├── view.py           # Custom view with tool handling implementation
├── resource.qrc      # Qt Resource Collection file
├── resource_rc.py    # Generated resource code
└── ui_widget.py      # Generated UI code from widget.ui
```

## Building and Running the Project

1. Generate UI Python files:
   ```bash
   pyside6-uic widget.ui -o ui_widget.py
   ```

2. Generate resource Python files:
   ```bash
   pyside6-rcc resource.qrc -o resource_rc.py
   ```

3. Run the application:
   ```bash
   python main.py
   ```

## Implementation Details

### Custom Graphics View

The `View` class extends `QGraphicsView` to handle different drawing tools:

```python
class View(QGraphicsView):
    # Enum for different drawing tools
    Cursor = 0
    Line = 1
    Ellipse = 2
    Path = 3
    Pie = 4
    Image = 5
    Star = 6
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.current_tool = self.Cursor
```

The view overrides `mousePressEvent` to handle different drawing operations based on the current tool:

```python
def mousePressEvent(self, event):
    """Handle mouse press events based on the current tool"""
    if self.current_tool == self.Cursor:
        super().mousePressEvent(event)
    elif self.current_tool == self.Line:
        self.addLine(self.mapToScene(event.pos()))
    elif self.current_tool == self.Ellipse:
        self.addEllipse(self.mapToScene(event.pos()))
    # ... other tools ...
```

### Adding Items to the Scene

Each drawing tool has a corresponding method to create and add the appropriate item to the scene:

```python
def addLine(self, pos):
    """Add a line item at the specified position"""
    line = QGraphicsLineItem(10, 10, 90, 90)
    line.setPen(QPen(Qt.red, 3))
    
    bound_rect = QGraphicsRectItem()
    bound_rect.setRect(line.boundingRect().adjusted(-10, -10, 10, 10))
    bound_rect.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsMovable | 
                       QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
    line.setParentItem(bound_rect)
    
    bound_rect.setPos(pos)
    self.scene().addItem(bound_rect)
```

This pattern is repeated for each shape type, with appropriate adjustments for the specific shape.

### Main Widget Implementation

The main `Widget` class sets up the UI, connects signals to slots, and implements the color changing functionality:

```python
def __init__(self, parent=None):
    super().__init__(parent)
    self.ui = Ui_Widget()
    self.ui.setupUi(self)
    
    # Initialize current color
    self.current_color = QColor(Qt.white)
    
    # Create the graphics scene
    self.scene = QGraphicsScene(self)
    # ... scene setup ...
    
    # Create custom view and set its scene
    self.view = View(self)
    # ... view setup ...
    
    # Connect buttons to their slots
    self.ui.cursorButton.clicked.connect(self.on_cursorButton_clicked)
    # ... other connections ...
```

### Changing Item Colors

The application allows changing the color of selected items:

```python
def setSelectItemColor(self, color):
    """Set the color of selected items"""
    if not self.scene.selectedItems():
        return
    
    # Loop through the selected items
    for item in self.scene.selectedItems():
        # Loop to find children
        for child_item in item.childItems():
            # Check item type and set color accordingly
            # ...
```

## Key Concepts

### Tool-Based Drawing Approach

The application uses a tool-based approach to drawing:

1. **Tool Selection**: The user selects a drawing tool from the UI
2. **Tool Activation**: Clicking on the scene activates the selected tool
3. **Item Creation**: Based on the active tool, a new item is created at the click position
4. **Item Manipulation**: Items can be selected and moved (when using the cursor tool)

This approach is common in drawing applications and separates the selection of what to draw from the action of drawing.

### Parent-Child Relationships for Item Manipulation

Each drawing item is created with a bounding rectangle as its parent:

```python
# Create the shape item
shape_item = QGraphicsPathItem(path)

# Create a bounding rectangle
bound_rect = QGraphicsRectItem()
bound_rect.setRect(shape_item.boundingRect().adjusted(-10, -10, 10, 10))
bound_rect.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsMovable | 
                   QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)

# Make the shape a child of the rectangle
shape_item.setParentItem(bound_rect)

# Add only the rectangle to the scene
scene.addItem(bound_rect)
```

This design provides several benefits:
1. The bounding rectangle serves as a "handle" for moving and selecting the shape
2. The shape moves along with its parent rectangle
3. The bounding rectangle provides visual feedback when the shape is selected

### Type Casting in Python vs C++

In the original C++ code, `qgraphicsitem_cast` is used to cast items to specific types:

```cpp
QGraphicsRectItem* mItem = qgraphicsitem_cast<QGraphicsRectItem*>(childItem);
```

In Python, we can use `isinstance()` for the same purpose:

```python
if isinstance(child_item, QGraphicsRectItem):
    # It's a rectangle
```

For compatibility with the original code structure, we implement helper methods:

```python
def qgraphicsitem_cast_rect(self, item):
    """Cast item to QGraphicsRectItem if possible"""
    if isinstance(item, QGraphicsRectItem):
        return item
    return None
```

### Color Selection and Application

The application provides two ways to change the color of items:

1. **Color Dialog**: Click "Choose Color" to open a dialog and select a color
2. **Direct Application**: Once a color is selected, click the color button to apply it to selected items

The selected color is stored and applied to selected items using `setBrush()`:

```python
item.setBrush(QBrush(color))
```

## Advanced Techniques

### Creating Custom Paths

The application demonstrates creating complex shapes using `QPainterPath`:

```python
# Create a pie shape
path = QPainterPath(QPointF(60, 60))
path.arcTo(QRectF(10, 10, 80, 80), 30, 170)
path.lineTo(QPointF(60, 60))

# Create a star shape
poly = QPolygon()
poly.append(QPoint(0, 85))
# ... more points ...
path = QPainterPath()
path.addPolygon(poly)
```

### Selection Handling

The application uses `QGraphicsView.RubberBandDrag` to allow selecting multiple items by dragging:

```python
self.view.setDragMode(View.RubberBandDrag)
```

This enables users to select multiple items by dragging a selection rectangle around them.

### Resource Integration

The application loads images from Qt resources:

```python
pixmap = QPixmap(":/images/LearnQt.png")
```

This demonstrates integrating resources into the application using Qt's resource system.

## Best Practices

1. **Separate View Logic from UI Logic**

   The application separates the drawing logic (in the `View` class) from the UI and control logic (in the `Widget` class):
   
   ```python
   # View class handles drawing operations
   class View(QGraphicsView):
       def mousePressEvent(self, event):
           # Drawing logic
   
   # Widget class handles UI and controls
   class Widget(QWidget):
       def on_lineButton_clicked(self):
           # UI logic
   ```

2. **Make Items Both Movable and Selectable**

   Items are made both movable and selectable using flags:
   
   ```python
   item.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsMovable | 
                QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
   ```

   This allows users to both select items (for changing properties) and move them around the scene.

3. **Use Parent-Child Relationships for Item Groups**

   Instead of manually grouping items, the application uses parent-child relationships:
   
   ```python
   shape_item.setParentItem(bound_rect)
   ```

   This simplifies moving and selecting related items together.

4. **Handle Tool States Explicitly**

   The application uses explicit tool states rather than boolean flags:
   
   ```python
   # Using an enum-like approach
   class View(QGraphicsView):
       Cursor = 0
       Line = 1
       # ...
   ```

   This makes it easier to add new tools without adding more boolean variables.

5. **Provide Visual Feedback**

   The application provides visual feedback through:
   - Selectable items with visible selection indicators
   - A color button that shows the current color
   - A bounding rectangle around each shape

## Conclusion

The PySide6 Graphics View Drawing Tool demonstrates how to create an interactive drawing application using the Graphics View Framework. By implementing different drawing tools, item selection, and property editing (color changing), it shows the flexibility and power of the framework.

This implementation exemplifies how to structure a drawing application with a clear separation between drawing tools, items, and UI controls. The use of parent-child relationships for item manipulation and the custom view for handling tool operations provide a solid foundation for more complex drawing applications.

The techniques demonstrated in this project can be extended to create more sophisticated drawing and diagramming tools, CAD applications, or any software that requires interactive graphical manipulation.