# PySide6 Resizable Graphics Items with Multiple Inheritance

This project demonstrates how to implement resizable items in a QGraphicsScene using PySide6. It shows how to create custom QGraphicsItem subclasses with resize handles using multiple inheritance and a shared base interface.

## Key Features

- Resizable items with corner handles
- Different item types (rectangle, ellipse, pixmap, star shape)
- Multiple inheritance approach with shared resize handle functionality
- Clean separation of handle logic from item-specific drawing

## Project Structure

```
resizable_graphics_items/
│
├── main.py                   # Application entry point
├── widget.py                 # Main widget with scene setup
├── ui_widget.py              # Generated UI code from widget.ui
├── handleitem.py             # Corner handle implementation
├── resizablehandlerect.py    # Base class for handle functionality
├── resizablerectitem.py      # Resizable rectangle implementation
├── resizableellipseitem.py   # Resizable ellipse implementation
├── resizablepixmapitem.py    # Resizable pixmap implementation
├── resizablestaritem.py      # Resizable star shape implementation 
├── resources_rc.py           # Generated resources file
└── images/                   # Image resources
    └── Quick.png             # Sample image
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

### Multiple Inheritance Approach

This project uses multiple inheritance to provide resizable handle functionality to different graphics items:

```python
class ResizableRectItem(QGraphicsRectItem, ResizableHandleRect):
    def __init__(self):
        QGraphicsRectItem.__init__(self)
        ResizableHandleRect.__init__(self)
        self.setOwnerItem(self)
```

The `ResizableHandleRect` class provides the common handle functionality, while each specific item class handles its own drawing.

### The ResizableHandleRect Base Class

The `ResizableHandleRect` class serves as a mixin to provide handle functionality:

```python
class ResizableHandleRect:
    def __init__(self):
        self.handle_list = []
        self.handles_added_to_scene = False
        self.owner_item = None
        
    def drawHandlesIfNecessary(self):
        if self.owner_item.isSelected():
            self.drawHandles()
            self.handles_added_to_scene = True
        else:
            # Remove the handles
            for handle_item in self.handle_list:
                self.owner_item.scene().removeItem(handle_item)
            
            # Clean up the handle list
            self.handle_list.clear()
            self.handles_added_to_scene = False
```

Subclasses must implement two abstract methods:
- `selectorFrameBounds()`: Returns the current item bounds
- `setSelectorFrameBounds(rect)`: Updates the item's geometry

### Handle Items for Resizing

The `HandleItem` class implements a draggable corner handle:

```python
class HandleItem(QGraphicsRectItem):
    # Handle position enum
    TopLeft = 0
    TopRight = 1 
    BottomRight = 2
    BottomLeft = 3
    
    def __init__(self, position):
        super().__init__()
        self.handle_position = position
        self.setFlag(QGraphicsRectItem.ItemIsMovable)
```

The `mouseMoveEvent` method resizes the parent item:

```python
def mouseMoveEvent(self, event):
    parent = self.parentItem()
    
    if isinstance(parent, ResizableHandleRect):
        bounding_frame_rect = parent.selectorFrameBounds()
        
        if self.handle_position == HandleItem.TopLeft:
            bounding_frame_rect.setTop(event.pos().y() + 6)
            bounding_frame_rect.setLeft(event.pos().x() + 6)
            parent.setSelectorFrameBounds(bounding_frame_rect.normalized())
```

### Different Item Types 

#### Ellipse Item

The `ResizableEllipseItem` draws an ellipse within its bounding rectangle:

```python
def paint(self, painter, option, widget):
    painter.save()
    painter.setBrush(self.brush())
    painter.drawEllipse(self.rect())
    self.drawHandlesIfNecessary()
    painter.restore()
```

#### Pixmap Item

The `ResizablePixmapItem` displays an image that can be resized:

```python
def __init__(self, pixmap):
    QGraphicsRectItem.__init__(self)
    ResizableHandleRect.__init__(self)
    self.m_pixmap = pixmap
    self.setRect(QRectF(10, 10, 300, 300))
    self.setOwnerItem(self)

def paint(self, painter, option, widget):
    painter.save()
    painter.drawPixmap(self.boundingRect(), self.m_pixmap, self.m_pixmap.rect())
    self.drawHandlesIfNecessary()
    painter.restore()
```

#### Star Item

The `ResizableStarItem` creates a custom star shape:

```python
def paint(self, painter, option, widget):
    painter.save()
    painter.setBrush(self.brush())
    painter.drawPath(self.starFromRect(self.boundingRect()))
    self.drawHandlesIfNecessary()
    painter.restore()
```

The star shape is created with a custom method:

```python
def starFromRect(self, rect):
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

### Multiple Inheritance in Python

This project demonstrates how to use multiple inheritance to add functionality to QGraphicsItem subclasses:

```python
class ResizableEllipseItem(QGraphicsRectItem, ResizableHandleRect):
```

Key points about multiple inheritance:
- The class inherits both from a QGraphicsItem subclass and our ResizableHandleRect mixin
- Both parent constructors must be called explicitly
- Method resolution follows Python's Method Resolution Order (MRO)

### Interface-Like Behavior with Python's ABC

While Python doesn't have formal interfaces, the `ResizableHandleRect` class works like an interface by requiring subclasses to implement specific methods:

```python
def selectorFrameBounds(self):
    """
    Get the bounds of the selector frame - must be implemented by subclasses.
    """
    raise NotImplementedError("Subclasses must implement selectorFrameBounds")
```

### Parent-Child Relationships

In this project, the handle items are children of the resizable items:

```python
self.handle_list[0].setParentItem(self.owner_item)
```

This means:
- Handles move with their parent items
- Handles are automatically removed when the parent is removed
- Transformations of the parent apply to the children

### Dynamic Type Checking

In PySide6, we use `isinstance()` for type checking:

```python
if isinstance(parent, ResizableHandleRect):
    # It's a ResizableHandleRect
```

## Best Practices

1. **Separate Interface from Implementation**

   The project separates the resizing handle interface (`ResizableHandleRect`) from specific item implementations:
   
   ```python
   # Interface class
   class ResizableHandleRect:
       # Common functionality...
   
   # Implementation classes
   class ResizableRectItem(QGraphicsRectItem, ResizableHandleRect):
       # Rectangle-specific implementation
   ```

2. **Proper Initialization with Multiple Inheritance**

   Always explicitly call all parent class initializers:
   
   ```python
   def __init__(self):
       QGraphicsRectItem.__init__(self)
       ResizableHandleRect.__init__(self)
   ```

3. **Prepare for Geometry Changes**

   Call `prepareGeometryChange()` before changing an item's geometry:
   
   ```python
   def setSelectorFrameBounds(self, bounds_rect):
       self.prepareGeometryChange()
       self.setRect(bounds_rect)
       self.update()
   ```

4. **Clean Up Resources**

   Clean up objects that you create:
   
   ```python
   # Remove handles when they're no longer needed
   for handle_item in self.handle_list:
       self.owner_item.scene().removeItem(handle_item)
   
   # Clear the list
   self.handle_list.clear()
   ```

5. **Normalize Rectangles**

   When creating rectangles from arbitrary points, normalize them to ensure positive width and height:
   
   ```python
   parent.setSelectorFrameBounds(bounding_frame_rect.normalized())
   ```

## Advanced Techniques

### Custom Shapes with QPainterPath

For more complex shapes, QPainterPath provides powerful drawing capabilities:

```python
def starFromRect(self, rect):
    poly = QPolygonF()
    # Define points...
    path = QPainterPath()
    path.addPolygon(poly)
    return path
```

### Painter State Management

Properly save and restore the painter state to prevent side effects:

```python
def paint(self, painter, option, widget):
    painter.save()
    # Custom drawing code
    painter.restore()
```

### Resource Management

Use Qt's resource system to bundle images and other resources with your application:

```python
# In widget.py
pix_item = ResizablePixmapItem(QPixmap(":/images/Quick.png"))

# In main.py
import resources_rc
```

## Extending the Project

Here are some ways you could extend this project:

1. **Add More Handle Types**
   - Add handles at the midpoints of each side for resizing in just one dimension
   - Add rotation handles

2. **Support Item Transformation**
   - Implement rotation support
   - Add skewing or shearing capabilities

3. **Enhanced Visual Feedback**
   - Show dimensions while resizing
   - Add snapping to grid or to other items

4. **Group Resizing**
   - Implement a group item that can be resized, moving/resizing its children
   - Add aspect ratio lock when resizing

## Conclusion

This project demonstrates how to implement resizable graphics items in PySide6 using multiple inheritance. By separating the handle functionality into a common base class, we achieve code reuse while allowing for specialized item types.

The multiple inheritance approach in Python provides a powerful way to extend Qt's Graphics View Framework with custom functionality. This technique can be applied to many other graphics applications that require interactive elements.

The architecture shown here provides a foundation for building sophisticated graphics editing applications with clean, maintainable code.