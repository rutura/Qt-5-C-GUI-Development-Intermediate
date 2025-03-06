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

