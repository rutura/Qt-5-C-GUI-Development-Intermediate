# Paint Application in PySide6

This project demonstrates a simple paint application built with PySide6, featuring multiple drawing tools, color selection, and other paint options.

## Project Overview

This application illustrates:
1. Creating a custom drawing canvas
2. Implementing various drawing tools (pen, rectangle, ellipse, eraser)
3. Working with QImage for drawing operations
4. Using QToolBar to create a drawing toolbar
5. Handling mouse events for drawing
6. Supporting color selection, fill options, and pen width

## Project Structure

```
project/
├── main.py         # Application entry point
├── mainwindow.py   # Main window with toolbar and canvas
├── paintcanvas.py  # Custom drawing canvas
├── ui_mainwindow.py # Generated UI code from mainwindow.ui
└── images/         # Directory for tool icons (optional)
   ├── pen.png
   ├── rectangle.png
   ├── circle.png
   └── eraser.png
```

## Key Components

### PaintCanvas Widget

The `PaintCanvas` class is a custom widget that handles drawing operations:

```python
class PaintCanvas(QWidget):
    # Tool type enum
    Pen, Rect, Ellipse, Eraser = range(4)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Initialize properties
        self.tool = self.Pen
        self.fill = False
        self.penWidth = 3
        # ...
```

It provides methods for different drawing operations:
- `drawLineTo()`: Draw a line for the pen tool
- `drawRectTo()`: Draw rectangles or ellipses
- `eraseUnder()`: Erase content under the eraser

### Main Window

The `MainWindow` class creates the UI and connects controls to drawing operations:

```python
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Create and set the canvas as central widget
        self.canvas = PaintCanvas(self)
        self.setCentralWidget(self.canvas)
        
        # Create toolbar controls
        # ...
```

## Drawing Tools

The application supports four drawing tools:

1. **Pen Tool**: Freeform drawing with the current pen color and width
   ```python
   def drawLineTo(self, endPoint):
       painter = QPainter(self.image)
       painter.setPen(QPen(self.penColor, self.penWidth, Qt.SolidLine, 
                          Qt.RoundCap, Qt.RoundJoin))
       painter.setRenderHint(QPainter.Antialiasing, True)
       painter.drawLine(self.lastPoint, endPoint)
       # ...
   ```

2. **Rectangle Tool**: Draw rectangles with optional fill
   ```python
   def drawRectTo(self, endPoint, ellipse=False):
       # ...
       if not ellipse:
           painter.drawRect(QRect(self.lastPoint, endPoint))
       # ...
   ```

3. **Ellipse Tool**: Draw ellipses with optional fill
   ```python
   def drawRectTo(self, endPoint, ellipse=False):
       # ...
       if ellipse:
           painter.drawEllipse(QRect(self.lastPoint, endPoint))
       # ...
   ```

4. **Eraser Tool**: Erase content in a rectangular area
   ```python
   def eraseUnder(self, topLeft):
       painter = QPainter(self.image)
       # Erase content by drawing white
       painter.setBrush(Qt.white)
       painter.setPen(Qt.white)
       # ...
   ```

## Drawing Options

The application provides several drawing options:

1. **Pen Width**: Control the thickness of drawn lines
   ```python
   def penWidthChanged(self, width):
       self.canvas.setPenWidth(width)
   ```

2. **Pen Color**: Select the color for drawing outlines
   ```python
   def changePenColor(self):
       color = QColorDialog.getColor(self.canvas.getPenColor())
       if color.isValid():
           self.canvas.setPenColor(color)
           # ...
   ```

3. **Fill Color**: Select the color for filling shapes
   ```python
   def changeFillColor(self):
       color = QColorDialog.getColor(self.canvas.getFillColor())
       if color.isValid():
           self.canvas.setFillColor(color)
           # ...
   ```

4. **Fill Option**: Toggle whether shapes are filled
   ```python
   def changeFillProperty(self):
       self.canvas.setFill(self.fillCheckBox.isChecked())
   ```

## Mouse Event Handling

Drawing is implemented through mouse event handling:

```python
def mousePressEvent(self, event):
    """Handle mouse press events"""
    if event.button() == Qt.LeftButton:
        self.lastPoint = event.position().toPoint()
        self.drawing = True

def mouseMoveEvent(self, event):
    """Handle mouse move events"""
    if (event.buttons() & Qt.LeftButton) and self.drawing:
        pos = event.position().toPoint()
        
        if self.tool == self.Pen:
            self.drawLineTo(pos)
        # ...
```

## Image Handling

The canvas uses QImage for drawing operations:

```python
# Create a white image to paint on
self.image = QImage(self.size(), QImage.Format_RGB32)
self.image.fill(Qt.white)
```

The image is automatically resized when the widget resizes:

```python
def resizeEvent(self, event):
    if self.width() > self.image.width() or self.height() > self.image.height():
        newWidth = max(self.width() + 128, self.image.width())
        newHeight = max(self.height() + 128, self.image.height())
        self.image = self.resizeImage(self.image, QSize(newWidth, newHeight))
        self.update()
```

## Running the Application

1. Generate the UI Python file (if mainwindow.ui changes):
   ```
   pyside6-uic mainwindow.ui -o ui_mainwindow.py
   ```

2. Ensure PySide6 is installed:
   ```
   pip install PySide6
   ```

3. If you want icons, create an `images` directory and add icon files:
   - pen.png
   - rectangle.png
   - circle.png
   - eraser.png

4. Run the application:
   ```
   python main.py
   ```

5. Drawing:
   - Select a tool from the toolbar
   - Choose pen width, colors, and fill options
   - Draw on the canvas using the mouse

## Implementation Notes

### Tool Selection

Tools are implemented as enum values, with the current tool stored in a variable:

```python
# Tool type enum
Pen, Rect, Ellipse, Eraser = range(4)

# Set current tool
def setTool(self, tool):
    self.canvas.setTool(tool)
```

### Live Drawing Preview

For rectangle and ellipse tools, the application provides a live preview while drawing:

```python
if self.drawing:
    # Erase the last preview shape
    painter.setPen(QPen(Qt.white, self.penWidth+2, Qt.SolidLine, 
                       Qt.RoundCap, Qt.RoundJoin))
    
    if self.fill:
        painter.setBrush(Qt.white)
    else:
        painter.setBrush(Qt.NoBrush)
    
    if not ellipse:
        painter.drawRect(self.lastRect)
    else:
        painter.drawEllipse(self.lastRect)
    
    # Reset and draw the new preview
    # ...
```

### Toolbar Creation

The toolbar is created by adding widgets programmatically:

```python
# Add widgets to toolbar
self.ui.mainToolBar.addWidget(penWidthLabel)
self.ui.mainToolBar.addWidget(penWidthSpinBox)
# ...
```

### Icon Fallback

The code includes fallback handling if icons are not found:

```python
try:
    rectButton.setIcon(QIcon("images/rectangle.png"))
except:
    rectButton.setText("Rect")
```

## Extending the Project

The project could be extended with:

1. **Additional Tools**: Add more drawing tools like lines, polygons, or text
2. **Save/Load**: Add functionality to save and load drawings
3. **Undo/Redo**: Implement an undo/redo system
4. **Layer Support**: Add support for multiple drawing layers
5. **Image Import**: Allow importing images to draw on