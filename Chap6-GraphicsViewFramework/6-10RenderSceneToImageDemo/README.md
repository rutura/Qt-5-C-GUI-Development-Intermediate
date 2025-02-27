# PySide6 Resizable Graphics Items with Scene Export

This project demonstrates how to implement resizable items in a QGraphicsScene using PySide6 with the ability to export the scene to an image file. It shows how to create custom QGraphicsItem subclasses with resize handles using multiple inheritance and a shared base interface.

## Key Features

- Resizable items with corner handles
- Different item types (rectangle, ellipse, pixmap, star shape)
- Multiple inheritance approach with shared resize handle functionality
- Scene export to image (PNG, JPG, XPM)
- Clean separation of handle logic from item-specific drawing

## Project Structure

```
resizable_graphics_items/
│
├── main.py                   # Application entry point
├── widget.py                 # Main widget with scene setup and export functionality
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

#### Rectangle Item

The `ResizableRectItem` draws a simple rectangle:

```python
def paint(self, painter, option, widget):
    painter.setBrush(self.brush())
    painter.drawRect(self.rect())
    self.drawHandlesIfNecessary()
```

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

### Scene Export Functionality

The project adds the ability to export the entire scene to an image file:

```python
def on_renderScene_clicked(self):
    file_name, _ = QFileDialog.getSaveFileName(
        self, 
        "Save File",
        "untitled.png",
        "Images (*.png *.xpm *.jpg)"
    )
    
    if not file_name:
        return
        
    # Create an image with the size of the scene
    rect = self.scene.sceneRect().toAlignedRect()
    image = QImage(rect.size(), QImage.Format.Format_ARGB32)
    image.fill(Qt.transparent)
    
    # Create a painter to render the scene
    painter = QPainter(image)
    
    # Render the scene to the image
    self.scene.render(painter)
    
    # Save the image
    image.save(file_name)
    
    # Close the painter
    painter.end()
```

This method:
1. Shows a file dialog to get the save location
2. Creates a transparent image with the scene's dimensions
3. Uses a QPainter to render the scene onto the image
4. Saves the resulting image to the selected file

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

### Interface-Like Behavior with Abstract Methods

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

### Graphics Scene Rendering to Image

The project demonstrates how to render a QGraphicsScene to an image:

```python
# Create a transparent image
image = QImage(rect.size(), QImage.Format.Format_ARGB32)
image.fill(Qt.transparent)

# Render the scene
painter = QPainter(image)
self.scene.render(painter)
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

6. **Painter State Management**

   Properly save and restore the painter state:
   
   ```python
   def paint(self, painter, option, widget):
       painter.save()
       # Drawing code...
       painter.restore()
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

### Scene to Image Export

The technique used for exporting the scene to an image can be extended:

```python
# For anti-aliased rendering:
painter.setRenderHint(QPainter.Antialiasing)

# For higher resolution export:
image = QImage(rect.size() * 2, QImage.Format.Format_ARGB32)
painter.scale(2, 2)
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

4. **Group Operations**
   - Add group selection and group resize operations
   - Implement copy/paste functionality

5. **Scene Management**
   - Add layers support
   - Implement undo/redo functionality

6. **Enhanced Export Options**
   - Add support for more export formats (SVG, PDF)
   - Implement print functionality
   - Add options to control resolution and quality

## Conclusion

This project demonstrates how to implement resizable graphics items in PySide6 using multiple inheritance, along with scene export capabilities. By separating the handle functionality into a common base class, we achieve code reuse while allowing for specialized item types.

The multiple inheritance approach in Python provides a powerful way to extend Qt's Graphics View Framework with custom functionality. This technique can be applied to many other graphics applications that require interactive elements.

The architecture shown here provides a foundation for building sophisticated graphics editing applications with clean, maintainable code.