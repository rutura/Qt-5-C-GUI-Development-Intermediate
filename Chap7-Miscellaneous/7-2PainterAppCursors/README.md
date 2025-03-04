# PySide6 Drawing Application

A comprehensive vector drawing application built with PySide6 (Qt for Python) that demonstrates key Qt Graphics Framework concepts, drag-and-drop operations, and object-oriented design patterns.

*(Screenshot placeholder)*

## Project Overview

This application allows users to create and manipulate various shapes and drawings with an intuitive interface. It demonstrates several important Qt concepts:

1. **Graphics View Framework**: Uses QGraphicsScene and QGraphicsView for interactive graphics
2. **Drag and Drop**: Shapes can be dragged from a list to the canvas, and colors can be dragged onto shapes
3. **Resizable Graphics Items**: Shapes can be resized using corner handles
4. **Custom Widgets**: Specialized widgets like ShapeList and ColorListWidget

## Features

- **Multiple Drawing Tools**:
  - Selection cursor
  - Free-hand pen drawing
  - Rectangle, ellipse, and star shapes
  - Eraser tool
  
- **Item Manipulation**:
  - Move items by dragging
  - Resize items with corner handles
  - Delete items with Delete key
  
- **Image Support**:
  - Add images to the scene
  - Resize and position images
  
- **Color Handling**:
  - Drag colors from the color list onto shapes
  - Each shape has customizable fill
  
- **Visual Aids**:
  - Grid background
  - Guide lines
  - Selection rectangle

## Project Structure

The application follows the Qt Creator pattern with proper separation of UI and logic:

### Core Files
- `main.py`: Application entry point
- `mainwindow.py`: Main window implementation
- `ui_mainwindow.py`: Generated UI code (from mainwindow.ui)
- `scene.py`: Custom graphics scene for drawing operations
- `view.py`: Custom graphics view with selection rectangle and grid

### Widget Components
- `colorlistwidget.py`: List of colors with drag support
- `shapelist.py`: List of shape items with drag support
- `doubleclickbutton.py`: Button with double-click functionality

### Graphics Items
- `handleitem.py`: Corner handles for resizing items
- `resizablehandlerect.py`: Base class for resizable items
- `resizablerectitem.py`: Resizable rectangle implementation
- `resizableellipseitem.py`: Resizable ellipse implementation
- `resizablestaritem.py`: Resizable star shape implementation
- `resizablepixmapitem.py`: Resizable image implementation

### Resources
- `resource.qrc`: Qt Resource Collection file
- `resource_rc.py`: Generated resource file

## Key Implementation Concepts

### Multiple Inheritance

The resizable items use multiple inheritance to combine Qt's QGraphicsRectItem with our custom ResizableHandleRect:

```python
class ResizableRectItem(QGraphicsRectItem, ResizableHandleRect):
    def __init__(self):
        QGraphicsRectItem.__init__(self)
        ResizableHandleRect.__init__(self)
        # Additional setup...
```

### Drag and Drop

The application implements drag and drop operations for moving shapes onto the canvas and colors onto shapes:

```python
def dropEvent(self, event):
    if event.mimeData().hasColor():
        color = event.mimeData().colorData()
        self.setBrush(QBrush(color))
        event.acceptProposedAction()
    else:
        super().dropEvent(event)
```

### State-Based Drawing Tools

The scene implements a state-based approach for different drawing tools:

```python
def mousePressEvent(self, event):
    if event.button() == Qt.MouseButton.LeftButton:
        if self.tool in [self.Pen, self.Eraser, self.Rect, self.Star, self.Ellipse]:
            self.starting_point = event.scenePos()
            self.drawing = True
        else:
            super().mousePressEvent(event)
```

## Learning Opportunities

This application provides practical examples of:

1. **Object-Oriented Programming**: Inheritance, polymorphism, encapsulation
2. **Event-Driven Programming**: Qt's signal-slot mechanism, event handling
3. **Custom Widget Development**: Extending standard widgets
4. **Graphics Programming**: Vector graphics, transforms, custom painting
5. **UI Design Patterns**: Model-View-Controller, composition

## Setup and Running

### Requirements
- Python 3.6+
- PySide6

### Installation
```bash
pip install PySide6
```

### Generating UI and Resource Files
```bash
pyside6-uic mainwindow.ui -o ui_mainwindow.py
pyside6-rcc resource.qrc -o resource_rc.py
```

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

3. **Applying Colors**:
   - Drag colors from the color list onto shapes to change their fill color

4. **Resizing Shapes**:
   - Select a shape and use the corner handles to resize it

5. **Adding Images**:
   - Use File > Add Image to add an image to the canvas

## Extending the Application

The modular architecture makes it easy to extend the application. Some ideas:

1. **New Shape Types**: Create a new class inheriting from QGraphicsItem and ResizableHandleRect
2. **Additional Tools**: Add new tools by extending the Scene.ToolType enum
3. **Layer Support**: Implement a layer system for organizing shapes
4. **Export/Import**: Add support for saving/loading drawings in various formats
5. **Text Support**: Implement text items with formatting options

# PySide6 Drawing Application

This document explains the implementation of a drawing application ported from Qt6 C++ to PySide6 Python. The application demonstrates various Qt concepts including graphics view framework, drag and drop, custom widgets, and event handling.

## Project Structure

The drawing application consists of several components:

1. **MainWindow** - The main application window with toolbars, menus, and property panels.
2. **Scene** - Custom QGraphicsScene implementation that handles drawing operations.
3. **View** - Custom QGraphicsView implementation for displaying the scene.
4. **Resizable Items** - Various graphics items that can be resized and modified.
5. **Helper Widgets** - Custom widgets like ColorPicker, ShapeList, and DoubleclickButton.

## Key Concepts Demonstrated

### 1. Graphics View Framework

The application uses Qt's Graphics View Framework which provides a surface for managing and interacting with a large number of custom 2D graphical items. The key classes are:

- `QGraphicsScene` - Manages items in a 2D space.
- `QGraphicsView` - Widget for viewing the scene.
- `QGraphicsItem` - Base class for all graphics items.

### 2. Custom Graphics Items

The application implements several custom graphics items:

- `ResizableRectItem` - A rectangle that can be resized with handles.
- `ResizableEllipseItem` - An ellipse that can be resized with handles.
- `ResizableStarItem` - A star shape that can be resized with handles.
- `ResizablePixmapItem` - An image that can be resized with handles.

These items use a common base class (`ResizableHandleRect`) that provides functionality for resizing handles.

### 3. Drag and Drop

The application demonstrates two drag and drop features:

- **Shape Dragging**: Dragging shapes from a list widget to the canvas.
- **Color Dragging**: Dragging colors onto shapes to change their fill color.

### 4. Custom Events

The application implements custom event handling for:

- Mouse events for drawing shapes
- Keyboard events for deleting items
- Drag and drop events
- Double-click events for the DoubleclickButton

### 5. Signals and Slots

The application demonstrates signal/slot connections for:

- Connecting UI actions to functionality
- Communicating between different components
- Updating properties when values change

## Implementation Details

### Graphics Items Hierarchy

The application implements a hierarchy of graphics items:

```
QGraphicsRectItem
└── ResizableHandleRect (mixin)
    ├── ResizableRectItem
    ├── ResizableEllipseItem
    ├── ResizableStarItem
    └── ResizablePixmapItem
```

### File Generation

To build the UI for the application, you need to generate Python files from Qt Designer files:

```bash
pyside6-uic mainwindow.ui -o ui_mainwindow.py
```

### Resource Handling

The application includes various resources (icons, cursors, etc.) which are loaded through a Qt resource file. To generate the Python resource file from the QRC file:

```bash
pyside6-rcc resource.qrc -o resource_rc.py
```

## Class Details

### MainWindow

The MainWindow class sets up the UI, connects signals/slots, and manages the overall application structure. It includes:

- Tool selection (cursor, pen, shapes, eraser)
- Property panels for pen and brush
- Menu and toolbar setup

### Scene

The Scene class manages drawing operations and maintains the state of the drawing. It handles:

- Drawing tools implementation (pen, rectangle, ellipse, star, eraser)
- Drag and drop of shapes
- Selection of items
- Property management (pen color, width, style, fill color)

### View

The View class customizes how the scene is displayed and interacted with. It includes:

- Grid drawing in the background
- Selection rectangle drawing
- Custom background color

### Resizable Items

All resizable items share common functionality through the ResizableHandleRect mixin:

- Corner handles for resizing
- Selection state visualization
- Maintaining aspect ratio (optional)

### Helper Widgets

- **DoubleclickButton**: A button that emits a signal when double-clicked
- **ColorPicker**: A grid of color buttons for selecting colors
- **ShapeList**: A list widget that allows shapes to be dragged onto the canvas
- **ColorListWidget**: A list widget that allows colors to be dragged onto shapes

## Running the Application

To run the application, execute the `main.py` file:

```bash
python main.py
```

## Usage

1. Select a tool from the toolbar (cursor, pen, shape, eraser)
2. Draw on the canvas by clicking and dragging
3. Modify properties using the panels on the left
4. Add shapes by dragging from the shape list
5. Add images using the menu option
6. Change colors by clicking the color buttons or using the color picker
