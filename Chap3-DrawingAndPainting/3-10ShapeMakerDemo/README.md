# Shape Drawing Application in PySide6

This project demonstrates a comprehensive shape drawing application in PySide6, allowing users to select different shapes, pen styles, and brush styles and see the results in real-time.

## Project Overview

This application illustrates:
1. Creating a custom drawing widget (ShapeCanvas)
2. Implementing various shape drawing operations
3. Working with pens and brushes with different styles
4. Applying transformations and antialiasing
5. Using gradients and textures for filling shapes
6. Interactive control over drawing parameters

## Project Structure

```
project/
├── main.py         # Application entry point
├── shapecanvas.py  # Custom drawing widget
├── widget.py       # Main application window with controls
├── ui_widget.py    # Generated UI code from widget.ui
└── widget.ui       # UI design file (XML)
└── images/         # Directory for images (optional)
   └── learnqt.png  # Sample image for texture pattern
```

## Key Components

### ShapeCanvas Widget

The `ShapeCanvas` class is a custom widget that handles the drawing operations:

```python
class ShapeCanvas(QWidget):
    # Shape enum
    Polygon, Rect, RoundedRect, Ellipse, Pie, Chord, Text, Pixmap = range(8)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        # Initialize properties
        self.shape = self.Polygon
        self.antialiased = False
        self.transformed = False
        # ...
```

It provides methods for setting the shape type, pen, brush, and other properties.

### Main Widget

The `Widget` class is the main application window that includes:
- UI controls for selecting shape properties
- Logic for updating the canvas based on user selections
- Methods for configuring pens and brushes

## Shape Types

The application supports drawing various shapes:

1. **Polygon**: A custom polygon defined by a set of points
2. **Rectangle**: A simple rectangular shape
3. **Rounded Rectangle**: A rectangle with rounded corners
4. **Ellipse**: An elliptical shape
5. **Pie**: A pie-shaped segment
6. **Chord**: A chord-shaped segment
7. **Text**: Rendered text ("Qt GUI")
8. **Pixmap**: A bitmap image

## Pen Configuration

Pens control the outline of shapes and can be configured with:

1. **Width**: The thickness of the line
2. **Style**: The pattern used for drawing lines (solid, dashed, etc.)
3. **Cap Style**: How line endpoints are drawn (flat, square, round)
4. **Join Style**: How line corners are drawn (miter, bevel, round)

```python
def penChanged(self):
    """Update the pen based on UI controls"""
    pen_width = self.ui.penWidthSpinbox.value()
    
    # Get the selected pen style
    style_index = self.ui.penStyleCombobox.currentIndex()
    style = self.ui.penStyleCombobox.itemData(style_index)
    
    # Get the selected pen cap
    cap_index = self.ui.penCapCombobox.currentIndex()
    cap = self.ui.penCapCombobox.itemData(cap_index)
    
    # Get the selected pen join
    join_index = self.ui.penJoinComboBox.currentIndex()
    join = self.ui.penJoinComboBox.itemData(join_index)
    
    # Create and configure the pen
    pen = QPen()
    pen.setWidth(pen_width)
    pen.setStyle(Qt.PenStyle(style))
    pen.setCapStyle(Qt.PenCapStyle(cap))
    pen.setJoinStyle(Qt.PenJoinStyle(join))
    
    # Update the canvas
    self.canvas.setPen(pen)
```

## Brush Configuration

Brushes control the fill of shapes and can be configured with various styles:

1. **Solid Pattern**: A solid color fill
2. **Gradient Patterns**: Linear, radial, or conical color gradients
3. **Texture Pattern**: An image-based fill
4. **Hatch Patterns**: Various line-based patterns
5. **Density Patterns**: Patterns with different dot densities

```python
def brushChanged(self):
    """Update the brush based on UI controls"""
    # Get the selected brush style
    style_index = self.ui.brushStyleCombobox.currentIndex()
    style = Qt.BrushStyle(self.ui.brushStyleCombobox.itemData(style_index))
    
    # Create and configure the brush based on the selected style
    if style == Qt.LinearGradientPattern:
        # Linear gradient brush
        linear_gradient = QLinearGradient(0, 0, 100, 100)
        linear_gradient.setColorAt(0.0, Qt.red)
        linear_gradient.setColorAt(0.2, Qt.green)
        linear_gradient.setColorAt(1.0, Qt.blue)
        self.canvas.setBrush(QBrush(linear_gradient))
        
    elif style == Qt.RadialGradientPattern:
        # Radial gradient brush
        # ...
```

## Additional Features

### Antialiasing

The application allows enabling or disabling antialiasing:

```python
def setAntialiased(self, value):
    self.antialiased = value
    self.update()
```

In the paint event:
```python
if self.antialiased:
    painter.setRenderHint(QPainter.Antialiasing, True)
```

### Transformations

The application can apply transformations to the shapes:

```python
if self.transformed:
    painter.translate(50, 50)
    painter.rotate(60.0)
    painter.scale(0.6, 0.9)
    painter.translate(-50, -50)
```

This demonstrates translation, rotation, and scaling.

## Running the Application

1. Generate the UI Python file (if widget.ui changes):
   ```
   pyside6-uic widget.ui -o ui_widget.py
   ```

2. Ensure PySide6 is installed:
   ```
   pip install PySide6
   ```

3. Create an `images` directory and add `learnqt.png` for texture brushes (optional)

4. Run the application:
   ```
   python main.py
   ```

5. Interaction:
   - Select a shape type from the dropdown
   - Adjust pen properties (width, style, cap, join)
   - Select a brush style
   - Toggle antialiasing and transformations
   - Observe the changes in the canvas

## Implementation Notes

### Adding Items to Combo Boxes

The application populates combo boxes with items and their associated data:

```python
self.ui.shapeCombo.addItem("Polygon", ShapeCanvas.Polygon)
self.ui.penStyleCombobox.addItem("Solid", int(Qt.SolidLine))
```

This allows retrieving the associated data when an item is selected:

```python
style = self.ui.penStyleCombobox.itemData(style_index)
```

### Drawing Grid

The canvas draws the selected shape in a grid pattern:

```python
# Loop to draw shapes in a grid pattern
for x in range(0, self.width(), 100):
    for y in range(0, self.height(), 100):
        # Draw at this position
```

This creates a repeating pattern that fills the canvas.

### Image Loading Fallback

The code includes fallback handling if the texture image can't be loaded:

```python
try:
    self.pixmap.load("images/learnqt.png")
    if self.pixmap.isNull():
        # Create a simple placeholder
        self.pixmap = QPixmap(50, 50)
        self.pixmap.fill(Qt.darkCyan)
except:
    # Create a simple placeholder
    self.pixmap = QPixmap(50, 50)
    self.pixmap.fill(Qt.darkCyan)
```

## Extending the Project

The project could be extended with:

1. **Color Selection**: Add controls for selecting pen and brush colors
2. **Saving/Loading**: Add functionality to save and load drawings
3. **Custom Patterns**: Allow creating custom brush patterns
4. **Layer Support**: Add support for multiple drawing layers
5. **Shape Editing**: Allow editing shapes after they are drawn