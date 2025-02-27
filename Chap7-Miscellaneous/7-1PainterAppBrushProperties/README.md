# PySide6 Advanced Drawing Application

This document explains how to implement an advanced drawing application with Qt's Graphics View Framework that allows users to create, resize, and modify shapes with drag and drop functionality, custom pen and brush styles, and a color picker.

## Project Overview

This application demonstrates:
- Creating a custom graphics scene and view
- Using drag and drop for shape creation and color application
- Implementing resizable shapes with corner handles
- Multiple drawing tools (cursor, pen, various shapes, eraser)
- Color selection through a color picker widget
- Custom pen and brush style controls
- Customizable grid background
- Selection rectangle functionality

## Project Structure

```
drawing_app/
│
├── main.py                  # Application entry point
├── mainwindow.py            # Main window implementation
├── ui_mainwindow.py         # Generated UI from mainwindow.ui
├── scene.py                 # Custom graphics scene
├── view.py                  # Custom graphics view
├── handleitem.py            # Resize handles for shapes
├── resizablehandlerect.py   # Base class for resizable items
├── resizablerectitem.py     # Resizable rectangle implementation
├── resizableellipseitem.py  # Resizable ellipse implementation
├── resizablestaritem.py     # Resizable star implementation
├── resizablepixmapitem.py   # Resizable image implementation
├── shapelist.py             # List widget for shape selection
├── colorpicker.py           # Color picker widget
├── doubleclickbutton.py     # Button with double-click capability
├── dragbutton.py            # Button with drag capability
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

### 1. Enhanced Pen and Brush Controls

The application provides detailed control over drawing properties:

```python
# In the Scene class
self.pen_color = QColor(Qt.black)
self.pen_width = 2
self.pen_style = Qt.PenStyle.SolidLine
self.fill_color = QColor(Qt.gray)
self.brush_style = Qt.BrushStyle.SolidPattern
```

Users can change these properties through UI controls:
- Pen color button
- Pen width spinbox
- Pen style combobox
- Brush color button
- Brush style combobox

### 2. Color Picker Widget

A custom color picker widget is implemented with a grid of color buttons:

```python
class ColorPicker(QWidget):
    # Signal emitted when a color is selected
    colorChanged = Signal(QColor)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.colors = []
        self.populate_colors()
        # ...
```

Each button in the color picker:
- Shows a color
- Changes the current pen color when clicked
- Opens a color dialog when double-clicked

### 3. Custom Buttons

Two custom button classes enhance the application:

```python
class DoubleclickButton(QPushButton):
    """Button that emits a double click signal when double-clicked"""
    # ...
    doubleClicked = Signal()
```

```python
class DragButton(QPushButton):
    """Button that supports drag operations with color data"""
    # ...
```

The drag button allows users to drag a color directly to a shape to change its fill.

### 4. Custom View Implementation

The view class provides a customized canvas with grid lines and selection functionality:

```python
def drawBackground(self, painter, rect):
    """Draw custom background"""
    painter.save()
    painter.setBrush(QBrush(Qt.yellow))
    painter.drawRect(-800, -600, 1600, 1200)
    painter.restore()

def drawForeground(self, painter, rect):
    """Draw grid lines if enabled"""
    if self.draw_grid_lines:
        # Draw vertical and horizontal grid lines
        # ...
```

### 5. Enhanced Shape Drawing

Shapes can now be drawn with different pen and brush styles:

```python
def draw_shape_to(self, end_point):
    # ...
    # Create pen and brush with current properties
    m_pen = QPen()
    m_pen.setColor(self.pen_color)
    m_pen.setWidth(self.pen_width)
    m_pen.setStyle(self.pen_style)
    
    m_brush = QBrush()
    m_brush.setColor(self.fill_color)
    m_brush.setStyle(self.brush_style)
    # ...
```

## Implementation Details

### Main Window

The main window sets up the UI, creates the scene and view, and connects the toolbar actions and property controls to the appropriate scene methods.

### Scene

The scene manages drawing operations, tool selection, and object creation with enhanced pen and brush properties.

### View

The view provides custom rendering of background, grid lines, and selection rectangles.

### Color Picker

The color picker provides a grid of color buttons that can be clicked to select a color or double-clicked to change a color.

### Drag Button

The drag button allows dragging a color directly onto shapes to change their fill color.

## Best Practices

1. **Separation of Concerns**

   The application separates different responsibilities into distinct classes:
   - `Scene`: Manages the drawing area, tools, and drawing properties
   - `View`: Handles display of the scene and selection functionality
   - `ColorPicker`: Manages color selection
   - `DoubleclickButton` and `DragButton`: Provide specialized button behaviors

2. **Signal-Slot Connections**

   The application uses Qt's signal-slot mechanism to connect UI elements to scene properties:

   ```python
   color_picker.colorChanged.connect(self.on_colorpicker_color_changed)
   self.ui.penWidthSpinbox.valueChanged.connect(self.on_pen_width_spinbox_value_changed)
   ```

3. **Custom Widgets**

   Custom widgets like DoubleclickButton and DragButton enhance the user interface with specialized behaviors.

4. **Property Getters and Setters**

   The scene class provides getter and setter methods for all drawing properties:

   ```python
   def get_pen_color(self):
       """Get the current pen color"""
       return self.pen_color
   
   def set_pen_color(self, value):
       """Set the current pen color"""
       self.pen_color = value
   ```

## Usage Workflow

1. Select a drawing tool from the toolbar (cursor, pen, shape tools, eraser)
2. Set pen properties (color, width, style) and brush properties (color, style)
3. Create shapes by:
   - Dragging shapes from the shape list
   - Drawing shapes directly on the canvas
4. Select a color from the color picker to set the pen color
5. Select shapes with the cursor tool:
   - Individual shapes by clicking on them
   - Multiple shapes by dragging a selection rectangle
6. Modify shapes:
   - Move by dragging
   - Resize using the corner handles
   - Change color by dragging a color from the color button
7. Draw free-form lines with the pen tool
8. Erase elements with the eraser tool
9. Add external images using the "Add Image" option
10. Delete selected items using the Delete key

## Conclusion

This advanced drawing application demonstrates sophisticated graphics techniques in PySide6, including custom color handling, specialized buttons, enhanced drawing properties, and interactive UI elements. The architecture is designed to be extensible and maintainable through good separation of concerns and reusable components.