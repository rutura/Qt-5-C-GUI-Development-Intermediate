# PySide6 Draggable Shapes Application

This document explains how to implement a drawing application with Qt's Graphics View Framework that allows users to create, resize, and modify shapes with drag and drop functionality. The application demonstrates advanced graphics concepts in PySide6.

## Project Overview

This application demonstrates:
- Creating a custom graphics scene and view
- Using drag and drop for shape creation and color application
- Implementing resizable shapes with corner handles
- Multiple drawing tools (cursor, pen, various shapes, eraser)
- Color selection and application to shapes
- Adding and manipulating images

## Project Structure

```
draggable_shapes_app/
│
├── main.py                  # Application entry point
├── mainwindow.py            # Main window implementation
├── ui_mainwindow.py         # Generated UI from mainwindow.ui
├── scene.py                 # Custom graphics scene
├── handleitem.py            # Resize handles for shapes
├── resizablehandlerect.py   # Base class for resizable items
├── resizablerectitem.py     # Resizable rectangle implementation
├── resizableellipseitem.py  # Resizable ellipse implementation
├── resizablestaritem.py     # Resizable star implementation
├── resizablepixmapitem.py   # Resizable image implementation
├── shapelist.py             # List widget for shape selection
├── colorlistwidget.py       # List widget for color selection
├── resource.qrc             # Resource file for images
└── resource_rc.py           # Generated resource module
```

## Building and Running the Project

1. Generate UI Python files:
   ```bash
   pyside6-uic mainwindow.ui -o ui_mainwindow.py
   ```

2. Generate resource Python files:
   ```bash
   pyside6-rcc resource.qrc -o resource_rc.py
   ```

3. Run the application:
   ```bash
   python main.py
   ```

## Key Concepts

### 1. Multiple Inheritance with Qt Classes

The resizable items use multiple inheritance to combine Qt's graphics items with custom resize functionality:

```python
class ResizableRectItem(QGraphicsRectItem, ResizableHandleRect):
    def __init__(self):
        QGraphicsRectItem.__init__(self)
        ResizableHandleRect.__init__(self)
```

This design pattern allows reusing the resize functionality across different shape types.

### 2. Resizable Items Architecture

The application implements a flexible architecture for resizable items:

1. **Base Class**: `ResizableHandleRect` provides common functionality for all resizable items:
   - Drawing corner handles
   - Handling selection state
   - Defining the interface for bounds manipulation

2. **Handle Items**: `HandleItem` implements the corner handles that respond to mouse events to resize the parent item.

3. **Specific Shape Classes**: Each shape (rectangle, ellipse, star, pixmap) inherits from both `QGraphicsRectItem` and `ResizableHandleRect` to combine Qt's graphics capabilities with resizing functionality.

### 3. Drag and Drop System

The application implements two types of drag and drop operations:

1. **Shape Creation**: Dragging a shape from the shape list creates a new shape on the canvas.
2. **Color Application**: Dragging a color from the color list and dropping it on a shape changes the shape's color.

### 4. Drawing Tools

The scene implements multiple drawing tools:

1. **Cursor Tool**: For selecting and moving items
2. **Pen Tool**: For drawing freehand lines
3. **Shape Tools**: For drawing rectangles, ellipses, and stars
4. **Eraser Tool**: For erasing drawn elements

### 5. Custom Shape Implementation

The star shape demonstrates how to create custom shapes using QPainterPath:

```python
def star_from_rect(self, m_rect_f):
    """Create a star path from the given rectangle"""
    poly = QPolygonF()
    
    # Add points to form a star shape
    # ...
    
    path = QPainterPath()
    path.addPolygon(poly)
    return path
```

## Implementation Details

### Main Window

The main window sets up the UI, creates the scene and view, and connects the toolbar actions to the appropriate scene tools.

```python
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Create scene
        self.scene = Scene(self)
        
        # Create shape list and color list
        # ...
        
        # Connect toolbar actions
        self.ui.actionCursor.triggered.connect(self.on_action_cursor_triggered)
        # ...
```

### Scene

The scene manages drawing operations, tool selection, and object creation:

```python
class Scene(QGraphicsScene):
    # Tool type enumeration
    Cursor = 0
    Pen = 1
    Rect = 2
    Ellipse = 3
    Star = 4
    QtQuick = 5
    Eraser = 6
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.tool = self.Cursor
        # ...
```

### Resizable Handle Rectangle

The `ResizableHandleRect` class is a mixin that provides resizing functionality to shape items:

```python
class ResizableHandleRect:
    def __init__(self):
        self.handle_list = []
        self.handles_added_to_scene = False
        self.owner_item = None
        
    def draw_handles(self):
        # Create and position handles
        # ...
        
    def draw_handles_if_necessary(self):
        # Draw handles when selected, remove when not
        # ...
```

### Handle Item

The `HandleItem` class implements corner handles that can be dragged to resize their parent item:

```python
class HandleItem(QGraphicsRectItem):
    # Position enum
    TopLeft = 0
    TopRight = 1
    BottomRight = 2
    BottomLeft = 3
    
    def __init__(self, position):
        super().__init__()
        self.handle_position = position
        self.setFlag(QGraphicsRectItem.GraphicsItemFlag.ItemIsMovable)
    
    def mouseMoveEvent(self, event):
        # Resize parent based on handle position
        # ...
```

### Drag and Drop Lists

The application uses custom list widgets to support drag and drop operations:

```python
class ShapeList(QListWidget):
    def startDrag(self, supported_actions):
        items = self.selectedItems()
        if len(items) > 0:
            drag = QDrag(self)
            mime_data = QMimeData()
            
            # Set up drag data
            # ...
```

## Best Practices

1. **Separation of Concerns**

   The application separates different responsibilities into distinct classes:
   - `Scene`: Manages the drawing area and tools
   - `ResizableHandleRect`: Handles resizing behavior
   - Specific shape classes: Implement drawing and interaction for each shape type
   - List widgets: Handle selection and dragging of colors and shapes

2. **Reusable Components**

   The architecture allows for easy extension:
   - Adding new shape types by creating new resizable item classes
   - Adding new tools by extending the Scene class

3. **Event Handling**

   The application shows proper event handling techniques:
   - Using mouse events to implement drawing tools
   - Using drag and drop events for interacting between components
   - Using key events for operations like delete

4. **Memory Management**

   The application properly manages graphics items:
   - Removing temporary items when they're no longer needed
   - Deleting handles when deselecting items

## Usage Workflow

1. Select a drawing tool from the toolbar (cursor, pen, shape tools, eraser)
2. Create shapes by:
   - Dragging shapes from the shape list
   - Drawing shapes directly on the canvas
3. Select shapes with the cursor tool
4. Modify shapes:
   - Move by dragging
   - Resize using the corner handles
   - Change color by dragging a color from the color list
4. Add external images using the "Add Image" option
5. Delete selected items using the Delete key

## Conclusion

This application demonstrates advanced graphics techniques in PySide6, including custom graphics items, interactive drawing tools, and drag and drop operations. The architecture is designed to be extensible and maintainable through good separation of concerns and reusable components.