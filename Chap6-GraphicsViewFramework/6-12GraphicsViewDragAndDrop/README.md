# PySide6 Graphics Editor with Drag-and-Drop

This project demonstrates how to create a graphics editor application with drag-and-drop functionality using PySide6. The application allows users to drag shapes from a palette onto a canvas and customize them by dragging colors onto them.

## Key Features

- Drag-and-drop shape creation from a shape palette
- Drag-and-drop color application to shapes
- Resizable graphics items with handles at corners
- Multiple shape types (rectangle, ellipse, star, image)
- Custom scene for handling drag-and-drop operations

## Project Structure

```
graphics_editor/
│
├── main.py                   # Application entry point
├── widget.py                 # Main widget and application setup
├── ui_widget.py              # Generated UI code from widget.ui
├── shapelist.py              # Custom list widget for shapes
├── colorlistwidget.py        # Custom list widget for colors
├── scene.py                  # Custom scene for handling drops
├── handleitem.py             # Corner handle implementation
├── resizablehandlerect.py    # Base class for handle functionality
├── resizablerectitem.py      # Resizable rectangle implementation
├── resizableellipseitem.py   # Resizable ellipse implementation
├── resizablepixmapitem.py    # Resizable pixmap implementation
├── resizablestaritem.py      # Resizable star shape implementation 
├── resources_rc.py           # Generated resources file
└── images/                   # Image resources
    ├── ellipse.png           # Ellipse icon
    ├── rectangle.png         # Rectangle icon
    ├── star.png              # Star icon
    └── quick.png             # Qt Quick logo image
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

### Main Application Structure

The application consists of three main components:
1. A shape palette (custom QListWidget)
2. A color palette (custom QListWidget)
3. A graphics scene (custom QGraphicsScene)

### Custom List Widgets for Drag Operations

#### Shape List

The `ShapeList` class extends `QListWidget` to provide drag functionality for shapes:

```python
def startDrag(self, supportedActions):
    items = self.selectedItems()
    if items:
        drag = QDrag(self)
        mime_data = QMimeData()
        
        item = items[0]
        key = item.data(Qt.UserRole)
        
        mime_data.setProperty("Key", QVariant(key))
        
        drag.setMimeData(mime_data)
        pixmap = item.icon().pixmap(50, 50)
        drag.setPixmap(pixmap)
        
        drag.setHotSpot(pixmap.rect().center())
        
        if drag.exec() == Qt.IgnoreAction:
            print("Drag ignored")
```

#### Color List

The `ColorListWidget` class provides drag functionality for colors:

```python
def startDrag(self, supportedActions):
    items = self.selectedItems()
    if items:
        drag = QDrag(self)
        mime_data = QMimeData()
        
        color = QColor(items[0].text())
        mime_data.setColorData(color)
        
        pixmap = QPixmap(20, 20)
        pixmap.fill(color)
        drag.setPixmap(pixmap)
        drag.setMimeData(mime_data)
        drag.exec(supportedActions)
```

### Custom Scene for Drop Handling

The `Scene` class extends `QGraphicsScene` to handle drops from the shape list:

```python
def dropEvent(self, event):
    if event.mimeData().property("Key").canConvert(QMetaType.Int):
        key = event.mimeData().property("Key").toInt()
        
        if key == 10:  # Ellipse
            ellipse = ResizableEllipseItem()
            ellipse.setRect(0, 0, 80, 50)
            ellipse.setFlags(QGraphicsScene.ItemIsMovable | QGraphicsScene.ItemIsSelectable)
            ellipse.setBrush(QBrush(Qt.gray))
            self.addItem(ellipse)
            
            # Center on drop position
            ellipse.setPos(event.scenePos() - QPointF(ellipse.boundingRect().width()/2, 
                                                     ellipse.boundingRect().height()/2))
```

### Resizable Graphics Items

All shape items inherit from both a QGraphicsItem class and a `ResizableHandleRect` mixin class:

```python
class ResizableRectItem(QGraphicsRectItem, ResizableHandleRect):
    def __init__(self):
        QGraphicsRectItem.__init__(self)
        ResizableHandleRect.__init__(self)
        self.setOwnerItem(self)
        self.setAcceptDrops(True)
```

Each item implements color drop handling:

```python
def dragEnterEvent(self, event):
    if event.mimeData().hasColor():
        event.acceptProposedAction()
    else:
        super().dragEnterEvent(event)

def dropEvent(self, event):
    if event.mimeData().hasColor():
        color = event.mimeData().colorData()
        self.setBrush(QBrush(color))
        event.acceptProposedAction()
    else:
        super().dropEvent(event)
```

### Handle Items for Resizing

The `HandleItem` class provides corner handles for resizing items:

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

## Key Concepts

### Multiple Inheritance for Object Composition

This project uses multiple inheritance to combine QGraphicsItem functionality with resize handle functionality:

```python
class ResizableStarItem(QGraphicsRectItem, ResizableHandleRect):
```

### Custom Shapes with QPainterPath

The star shape is created using a custom QPainterPath:

```python
def starFromRect(self, rect):
    poly = QPolygonF()
    
    # Add points to create star shape
    poly.append(rect.topLeft() + QPointF(rect.width()/2, 0.0))
    # More points...
    
    path = QPainterPath()
    path.addPolygon(poly)
    return path
```

### Drag and Drop with MIME Data

The application uses MIME data to transfer information during drag and drop:

- For shapes: A custom property "Key" is used to identify the shape type
- For colors: The standard `setColorData()` and `colorData()` methods are used

### Parent-Child Relationships

Resize handles are children of the items they resize:

```python
handle.setParentItem(self.owner_item)
```

This ensures that:
- Handles move with their parent items
- Handles are automatically removed when the parent is removed
- Transformations of the parent apply to the children

## Usage Guide

1. **Adding Shapes**: 
   - Drag a shape from the shape palette on the left and drop it onto the canvas.
   - The shape will appear centered at the drop location.

2. **Changing Colors**:
   - Drag a color from the color palette and drop it onto a shape.
   - The shape will change to that color.

3. **Resizing Shapes**:
   - Click on a shape to select it.
   - When selected, handles will appear at the corners.
   - Drag the handles to resize the shape.

4. **Moving Shapes**:
   - Click and drag on a shape to move it around the canvas.

## Best Practices Demonstrated

1. **Separation of Concerns**:
   - Shape dragging logic is in `ShapeList`
   - Color dragging logic is in `ColorListWidget`
   - Drop handling for shapes is in `Scene`
   - Drop handling for colors is in each item class

2. **Code Reuse Through Mixins**:
   - Resize handle functionality is implemented once in `ResizableHandleRect`
   - All shape classes inherit this functionality

3. **Custom Graphics Items**:
   - Each shape type has its own class
   - Common functionality is shared through inheritance

4. **Clean Drag and Drop**:
   - Visual feedback is provided during dragging
   - Drop targets indicate when they can accept drops

## Extending the Project

Here are some ways you could extend this project:

1. **Additional Shape Types**:
   - Add more shape types like triangle, hexagon, arrow, etc.
   - Implement text items that can be edited

2. **Layer Management**:
   - Add a layer panel to control stacking order
   - Implement grouping of items

3. **Property Editor**:
   - Add a property panel to edit item properties
   - Control stroke width, style, etc.

4. **Import/Export**:
   - Save designs to files
   - Export as images

5. **Undo/Redo**:
   - Implement command pattern for operations
   - Add undo/redo functionality

## Conclusion

This project demonstrates how to create a graphics editor with drag-and-drop functionality using PySide6. It shows how to use QListWidgets for palette elements, how to implement custom graphics items with resize handles, and how to handle drag-and-drop operations between different parts of the application.

The architecture shown here provides a solid foundation for building more sophisticated graphics editing applications while maintaining a clean and extensible code structure.