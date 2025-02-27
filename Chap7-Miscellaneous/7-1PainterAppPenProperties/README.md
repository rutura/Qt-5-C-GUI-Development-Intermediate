# Simple Drawing Application - PySide6 Port

The application allows users to create, manipulate, and style various shapes using an intuitive interface with drag-and-drop functionality.

## Project Overview

This drawing application demonstrates several important Qt concepts:

1. **Graphics Framework** - Using QGraphicsScene and QGraphicsView
2. **Custom Widgets** - Specialized widgets like DoubleclickButton and ColorPicker
3. **Drag and Drop** - Shape and color drag-and-drop functionality
4. **Resizable Graphics Items** - Interactive resizing with corner handles

## Application Structure

The application follows the Qt Creator pattern with proper separation of UI and logic:

### Core Files
- `main.py` - Application entry point
- `mainwindow.py` - Main window implementation
- `ui_mainwindow.py` - Generated UI code (from mainwindow.ui)
- `scene.py` - Custom graphics scene for drawing operations
- `view.py` - Custom graphics view with selection and grid functionality

### Widget Components
- `colorpicker.py` - Grid of color buttons for selecting colors
- `doubleclickbutton.py` - Button with double-click functionality
- `shapelist.py` - List of shape items with drag support
- `colorlistwidget.py` - List of colors with drag support

### Graphics Items
- `handleitem.py` - Corner handles for resizing items
- `resizablehandlerect.py` - Base class for resizable items
- `resizablerectitem.py` - Resizable rectangle implementation
- `resizableellipseitem.py` - Resizable ellipse implementation
- `resizablestaritem.py` - Resizable star shape implementation
- `resizablepixmapitem.py` - Resizable image implementation

## Key Implementation Concepts

### 1. Multiple Inheritance with ResizableHandleRect

The resizable graphics items use multiple inheritance, inheriting from both QGraphicsRectItem and ResizableHandleRect. This allows them to have both the standard graphics item functionality and the corner-handle resizing capability.

```python
class ResizableRectItem(QGraphicsRectItem, ResizableHandleRect):
    def __init__(self):
        QGraphicsRectItem.__init__(self)
        ResizableHandleRect.__init__(self)
        # Additional initialization
```

### 2. Drag and Drop Implementation

The application implements two types of drag-and-drop operations:

**Shape Dragging**: ShapeList items can be dragged onto the scene to create new shapes:
```python
def startDrag(self, supported_actions):
    """Start drag and drop operation with shape data"""
    items = self.selectedItems()
    if len(items) > 0:
        drag = QDrag(self)
        mime_data = QMimeData()
        
        item = items[0]
        key = item.data(Qt.ItemDataRole.UserRole)
        
        # Store the key as property
        mime_data.setProperty("Key", key)
        
        drag.setMimeData(mime_data)
        # Additional setup...
```

**Color Dragging**: Colors can be dragged onto shapes to change their fill:
```python
def dropEvent(self, event):
    """Handle drop events for color changes"""
    if event.mimeData().hasColor():
        color = event.mimeData().colorData()
        self.setBrush(QBrush(color))
        event.acceptProposedAction()
    else:
        super().dropEvent(event)
```

### 3. Tool-Based Drawing

The scene implements different drawing tools (pen, eraser, shape tools) with a state-machine-like approach:
```python
def mousePressEvent(self, event):
    if event.button() == Qt.MouseButton.LeftButton:
        if self.tool in [self.Pen, self.Eraser, self.Rect, self.Star, self.Ellipse]:
            self.starting_point = event.scenePos()
            self.drawing = True
        else:
            super().mousePressEvent(event)
```

### 4. Resizable Handle Implementation

The ResizableHandleRect base class provides corner handles for resizing:
```python
def draw_handles(self):
    """Draw handles at the corners of the item"""
    # Populate handles in list
    if len(self.handle_list) == 0:
        self.handle_list.append(HandleItem(HandleItem.TopLeft))
        self.handle_list.append(HandleItem(HandleItem.TopRight))
        # Additional handles...
    # Set up handles...
```

## Setting Up and Running the Project

### Required Files

1. Generate the UI file:
   ```bash
   pyside6-uic mainwindow.ui -o ui_mainwindow.py
   ```

2. Generate the resources file:
   ```bash
   pyside6-rcc resource.qrc -o resource_rc.py
   ```

### Dependencies

- Python 3.6+
- PySide6

### Running the Application

```bash
python main.py
```

## Usage Guide

1. **Selecting Tools**:
   - Use the toolbar buttons or Tools menu to select a drawing tool

2. **Drawing Shapes**:
   - Click and drag on the canvas to draw shapes directly
   - Alternatively, drag shapes from the shape list to the canvas

3. **Styling Shapes**:
   - Use the pen color button to change the outline color
   - Use the pen width spinbox to change the line thickness
   - Use the pen style combobox to change the line style
   - Drag colors from the color picker to shapes to change their fill

4. **Resizing Shapes**:
   - Select a shape and use the corner handles to resize it

5. **Adding Images**:
   - Use File > Add Image to add an image to the canvas

