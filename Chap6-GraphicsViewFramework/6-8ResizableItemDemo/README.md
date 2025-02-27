# PySide6 Resizable Graphics Items

This project demonstrates how to implement resizable items in a QGraphicsScene using PySide6. It shows how to create custom QGraphicsItem subclasses that can be resized by dragging handles at their corners.

## Key Features

- Resizable graphic items with corner handles
- Item selection with visual feedback
- Different item types (rectangle, pixmap, custom star shape)
- Draggable items that maintain their custom behavior

## Project Structure

```
resizable_graphics_items/
│
├── main.py                 # Application entry point
├── widget.py               # Main widget with scene setup
├── ui_widget.py            # Generated UI code from widget.ui
├── handleitem.py           # Corner handle implementation
├── resizablerectitem.py    # Resizable rectangle implementation
├── resizablepixmapitem.py  # Resizable pixmap implementation
├── resizablestaritem.py    # Resizable star shape implementation 
├── resources_rc.py         # Generated resources file
└── images/                 # Image resources
    └── Quick.png           # Sample image
```

## Building and Running the Project

1. Generate the UI Python file:
   ```bash
   pyside6-uic widget.ui -o ui_widget.py
   ```

2. Convert Qt resources to Python:
   ```bash
   pyside6-rcc resource.qrc -o resources_rc.py
   ```

3. Run the application:
   ```bash
   python main.py
   ```

## Implementation Details

### Handle Item for Resizing

The handle responds to mouse movements to resize its parent:

```python
def mouseMoveEvent(self, event):
    """
    Handle the mouse move event to resize the parent item
    """
    if self.handle_position == HandleItem.TopLeft:
        rect_item = self.parentItem()
        
        if isinstance(rect_item, ResizablePixmapItem):
            bounding_frame_rect = rect_item.selectorFrameBounds()
            bounding_frame_rect.setTop(event.pos().y())
            bounding_frame_rect.setLeft(event.pos().x())
            rect_item.setSelectorFrameBounds(bounding_frame_rect)
    
    elif self.handle_position == HandleItem.TopRight:
        rect_item = self.parentItem()
        
        if isinstance(rect_item, ResizableRectItem):
            bounding_frame_rect = rect_item.selectorFrameBounds()
            bounding_frame_rect.setTop(event.pos().y())
            bounding_frame_rect.setRight(event.pos().x())
            rect_item.setSelectorFrameBounds(bounding_frame_rect)
    
    # Similar implementations for other handle positions...
```

### Resizable Rectangle Item

The `ResizableRectItem` class implements a rectangle that can be resized using the corner handles:

```python
class ResizableRectItem(QGraphicsRectItem):
    def __init__(self):
        super().__init__()
        self.handles_added_to_scene = False
        self.handle_list = []
        
        # Initialize handle rects
        self.topleft_handle_rect = QRectF()
        self.topright_handle_rect = QRectF()
        self.bottomright_handle_rect = QRectF()
        self.bottomleft_handle_rect = QRectF()
```

The item provides a method to update its geometry when resized:

```python
def setSelectorFrameBounds(self, bounds_rect):
    """
    Set the bounds of the selector frame
    
    Args:
        bounds_rect: QRectF with the new bounds
    """
    self.prepareGeometryChange()
    self.setRect(bounds_rect)
    self.update()
```

### Handling Selection and Drawing Handles

When the item is selected, it displays handles at its corners:

```python
def drawHandlesIfNecessary(self):
    """
    Draw handles if the item is selected, remove them otherwise
    """
    if self.isSelected():
        self.drawHandles()
        self.handles_added_to_scene = True
    else:
        # Remove the handles
        for handle_item in self.handle_list:
            self.scene().removeItem(handle_item)
        
        # Clear the list after removing handles
        self.handle_list.clear()
        self.handles_added_to_scene = False
```

The `drawHandles` method creates and positions the corner handles:

```python
def drawHandles(self):
    """
    Draw the handles for resizing
    """
    # Populate handles in list if empty
    if len(self.handle_list) == 0:
        self.handle_list.append(HandleItem(HandleItem.TopLeft))
        self.handle_list.append(HandleItem(HandleItem.TopRight))
        self.handle_list.append(HandleItem(HandleItem.BottomRight))
        self.handle_list.append(HandleItem(HandleItem.BottomLeft))
    
    # Position and style each handle...
    
    # Top left handle
    top_left_corner = self.boundingRect().topLeft() + QPointF(-12.0, -12.0)
    self.topleft_handle_rect = QRectF(top_left_corner, QSize(12, 12))
    self.handle_list[0].setRect(self.topleft_handle_rect)
    
    if len(self.handle_list) > 0 and not self.handles_added_to_scene:
        self.handle_list[0].setPen(pen)
        self.handle_list[0].setBrush(QBrush(QColor(128, 128, 128)))  # Qt::gray
        self.scene().addItem(self.handle_list[0])
        self.handle_list[0].setParentItem(self)
    
    # Similar code for other handles...
```

### Resizable Pixmap Item

The `ResizablePixmapItem` class displays a QPixmap that can be resized:

```python
class ResizablePixmapItem(QGraphicsRectItem):
    def __init__(self, pixmap):
        super().__init__()
        self.m_pixmap = pixmap
        self.setRect(QRectF(10, 10, 300, 300))
        # Initialize handles...
```

It overrides the paint method to draw the pixmap:

```python
def paint(self, painter, option, widget):
    painter.save()
    painter.drawPixmap(self.boundingRect(), self.m_pixmap, self.m_pixmap.rect())
    self.drawHandlesIfNecessary()
    painter.restore()
```

### Resizable Star Item

The `ResizableStarItem` class demonstrates a custom shape that can be resized:

```python
class ResizableStarItem(QGraphicsRectItem):
    def __init__(self):
        super().__init__()
        self.setRect(QRectF(10, 10, 300, 300))
        # Initialize handles...
```

It defines a method to create a star shape from a rectangle:

```python
def starFromRect(self, rect):
    """
    Create a star shape from a rectangle
    
    Args:
        rect: QRectF to create the star in
    
    Returns:
        QPainterPath: Path defining the star shape
    """
    poly = QPolygonF()
    
    # Define the star points...
    poly.append(rect.topLeft() + QPointF(rect.width()/2, 0.0))
    poly.append(rect.topLeft() + QPointF(rect.width() * 0.7, rect.height() * 0.3))
    # More points...
    
    path = QPainterPath()
    path.addPolygon(poly)
    return path
```

### Main Widget

The `Widget` class sets up the scene and creates the resizable items:

```python
class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # Create the graphics scene
        self.scene = QGraphicsScene(self)
        
        # Create a resizable rectangle item
        rect_item = ResizableRectItem()
        rect_item.setRect(-50, -50, 100, 100)
        rect_item.setBrush(QBrush(Qt.green))
        rect_item.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)
        self.scene.addItem(rect_item)
        
        # Create other items...
        
        # Create the view and set its scene
        self.view = QGraphicsView(self)
        self.view.setScene(self.scene)
        
        # Add the view to the layout
        self.ui.verticalLayout.addWidget(self.view)
```

## Key Concepts

### Graphics Item Coordinates

The Graphics View Framework operates with different coordinate systems:

1. **Item Coordinates**: Local coordinates relative to each QGraphicsItem
2. **Scene Coordinates**: Logical coordinates in the QGraphicsScene
3. **View Coordinates**: Window coordinates relative to the QGraphicsView widget

### Parent-Child Relationships

In this project, the handle items are children of the resizable items:

```python
handle_item.setParentItem(self)
```

This means:
- Handles move with their parent items
- Handles are automatically removed when the parent is removed
- Transformations of the parent apply to the children

### Dynamic Casting in PySide6

In C++, `dynamic_cast` is used to safely cast between related types. In PySide6, we use `isinstance()`:

```python
# C++ version:
// ResizablePixmapItem * rectItem = dynamic_cast<ResizablePixmapItem *>(parentItem());

# Python version:
if isinstance(rect_item, ResizablePixmapItem):
    # It's a ResizablePixmapItem
```

## Best Practices

1. **Prepare for Geometry Changes**

   Call `prepareGeometryChange()` before changing an item's geometry:
   
   ```python
   def setSelectorFrameBounds(self, bounds_rect):
       self.prepareGeometryChange()
       self.setRect(bounds_rect)
       self.update()
   ```

2. **Memory Management**

   Clean up objects that you create:
   
   ```python
   # Remove handles when they're no longer needed
   for handle_item in self.handle_list:
       self.scene().removeItem(handle_item)
   
   # Clear the list
   self.handle_list.clear()
   ```

3. **Separation of Functionality**

   Create specialized classes for different item types rather than using a single complex class:
   
   ```python
   # Separate classes for different item types
   class ResizableRectItem(QGraphicsRectItem):
       # Rectangle-specific implementation
   
   class ResizablePixmapItem(QGraphicsRectItem):
       # Pixmap-specific implementation
   
   class ResizableStarItem(QGraphicsRectItem):
       # Star-specific implementation
   ```

4. **Use Custom Paint Methods**

   Override the `paint()` method to customize how items are drawn:
   
   ```python
   def paint(self, painter, option, widget):
       painter.save()
       # Custom drawing code
       painter.restore()
   ```

## Advanced Techniques

### Custom Shapes with QPainterPath

For more complex shapes, QPainterPath provides powerful drawing capabilities:

```python
def starFromRect(self, rect):
    poly = QPolygonF()
    
    # Define the star points
    poly.append(rect.topLeft() + QPointF(rect.width()/2, 0.0))
    # More points...
    
    path = QPainterPath()
    path.addPolygon(poly)
    return path
```

### Item Selection Feedback

You can provide visual feedback when items are selected:

```python
def drawHandlesIfNecessary(self):
    if self.isSelected():
        self.drawHandles()
    else:
        # Remove handles
```

### Resource Management

Use Qt's resource system to bundle images and other resources with your application:

```python
# resource.qrc defines resources
<RCC>
    <qresource prefix="/">
        <file>images/Quick.png</file>
    </qresource>
</RCC>

# In Python, access resources with the : prefix
pixmap = QPixmap(":/images/Quick.png")
```

## Conclusion

This project demonstrates how to create custom, resizable graphics items using PySide6's Graphics View Framework. By extending `QGraphicsRectItem` and implementing custom handles, we can create interactive items that users can resize and move.

The techniques shown here can be applied to a wide range of applications, including:
- Diagram editors
- Image manipulation tools
- CAD applications
- User interface designers
- Interactive presentations

The modular design makes it easy to add more item types or enhance the existing ones with additional functionality.