# PySide6 Draggable Shapes Application - Implementation Guide

This guide explains how to implement a drawing application with Qt's Graphics View Framework that allows users to create, resize, and modify shapes with drag and drop functionality. The application demonstrates advanced graphics concepts in PySide6.

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
├── mainwindow.py            # Main window implementation (if using QMainWindow)
├── widget.py                # Main widget implementation (if using QWidget directly)
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
├── resource_rc.py           # Generated resource module
└── ui_widget.py             # Generated UI file
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

### Resizable Items Architecture

The application implements a flexible architecture for resizable items:

1. **Base Class**: `ResizableHandleRect` provides common functionality for all resizable items:
   - Drawing corner handles
   - Handling selection state
   - Defining the interface for bounds manipulation

2. **Handle Items**: `HandleItem` implements the corner handles that respond to mouse events to resize the parent item.

3. **Specific Shape Classes**: Each shape (rectangle, ellipse, star, pixmap) inherits from both `QGraphicsRectItem` and `ResizableHandleRect` to combine Qt's graphics capabilities with resizing functionality.

```python
class ResizableHandleRect:
    """Base class for resizable items with handles at the corners"""
    
    def __init__(self):
        # Initialize handles and state
        
    def draw_handles(self):
        """Draw handles at the corners of the item"""
        
    def draw_handles_if_necessary(self):
        """Draw handles if the item is selected, remove them otherwise"""
        
    # Abstract methods
    def selector_frame_bounds(self):
        """Returns the bounds of the selector frame"""
        
    def set_selector_frame_bounds(self, bounds_rect):
        """Sets the bounds of the selector frame"""
```

### Drag and Drop System

The application implements two types of drag and drop operations:

1. **Shape Creation**: Dragging a shape from the shape list creates a new shape on the canvas.
   ```python
   class ShapeList(QListWidget):
       def startDrag(self, supported_actions):
           # Create drag with shape type data
   ```

2. **Color Application**: Dragging a color from the color list and dropping it on a shape changes the shape's color.
   ```python
   class ColorListWidget(QListWidget):
       def startDrag(self, supported_actions):
           # Create drag with color data
   ```

   The shapes accept the color drop with:
   ```python
   def dropEvent(self, event):
       """Handle drop events for color changes"""
       if event.mimeData().hasColor():
           # Apply the color to the shape
   ```

### Drawing Tools

The scene implements multiple drawing tools:

1. **Cursor Tool**: For selecting and moving items
2. **Pen Tool**: For drawing freehand lines
3. **Shape Tools**: For drawing rectangles, ellipses, and stars
4. **Eraser Tool**: For erasing drawn elements

The tool system is implemented with an enumeration and specialized event handling:

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
    
    def mousePressEvent(self, event):
        # Handle based on current tool
```

### Custom Shape Implementation

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

## Key Concepts

### Multiple Inheritance with Qt Classes

The resizable items use multiple inheritance to combine Qt's graphics items with custom resize functionality:

```python
class ResizableRectItem(QGraphicsRectItem, ResizableHandleRect):
    def __init__(self):
        QGraphicsRectItem.__init__(self)
        ResizableHandleRect.__init__(self)
```

This design pattern allows reusing the resize functionality across different shape types.

### Dynamic Object Creation and Management

The scene dynamically creates, tracks, and removes objects based on user actions:

1. **Temporary Objects**: When drawing a shape, a temporary object is shown during the drag operation:
   ```python
   def draw_shape_to(self, end_point):
       # Remove previous temporary item
       # Create new temporary item
   ```

2. **Finalized Objects**: When the mouse is released, the temporary object is replaced with a permanent one:
   ```python
   def mouseReleaseEvent(self, event):
       # Remove temporary item
       # Create permanent item
   ```

### MIME Data for Drag and Drop

The application uses QMimeData to transfer information during drag and drop operations:

1. **Custom Properties**: For shape creation
   ```python
   mime_data.setProperty("Key", key)
   ```

2. **Color Data**: For color application
   ```python
   mime_data.setColorData(color)
   ```

### Scene Coordinate System

The application uses a centered coordinate system for the scene:
```python
self.setSceneRect(-800, -400, 1600, 800)
```

This makes it easier to position items relative to the center of the view.

## Best Practices

1. **Separation of Concerns**

   The application separates different responsibilities into distinct classes:
   - `Scene`: Manages the drawing area and tools
   - `ResizableHandleRect`: Handles resizing behavior
   - Specific shape classes: Implement drawing and interaction for each shape type
   - List widgets: Handle selection and dragging of colors and shapes
