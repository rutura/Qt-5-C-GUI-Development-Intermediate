# Gradient Brushes in PySide6

This project demonstrates how to use the three types of gradient brushes available in PySide6: linear, radial, and conical.

## Project Overview

This application illustrates:
1. Creating and configuring linear gradients
2. Creating and configuring radial gradients
3. Creating and configuring conical gradients
4. Setting gradient color stops
5. Applying different spread methods
6. Using gradients with brushes for shape filling

## Project Structure

```
project/
├── main.py      # Application entry point
├── ui_widget.py # Generated UI code from widget.ui
├── widget.py    # Main widget with gradient demonstrations
└── widget.ui    # UI design file (XML)
```

## Key Concepts

### Linear Gradients

Linear gradients transition colors along a line from a start point to an end point:

```python
# Create a linear gradient from (70,20) to (70,170)
linearGradient = QLinearGradient(QPointF(70, 20), QPointF(70, 170))

# Set color stops
linearGradient.setColorAt(0, "red")     # Start color
linearGradient.setColorAt(0.5, "gray")  # Middle color
linearGradient.setColorAt(1, "yellow")  # End color

# Set spread method
linearGradient.setSpread(QGradient.ReflectSpread)

# Use the gradient with a brush
mBrush = QBrush(linearGradient)
painter.setBrush(mBrush)
```

The gradient line direction determines how colors transition across the shape. In this example, the vertical line creates a top-to-bottom gradient.

### Radial Gradients

Radial gradients transition colors outward from a center point to a radius:

```python
# Create a radial gradient with center at (280,170) and radius 75
radialGradient = QRadialGradient(QPointF(280, 170), 75)

# Set color stops
radialGradient.setColorAt(0, "blue")    # Center color
radialGradient.setColorAt(1, "yellow")  # Edge color

# Set spread method
radialGradient.setSpread(QGradient.RepeatSpread)
```

The gradient radiates outward from the center point, creating a circular transition of colors.

### Conical Gradients

Conical gradients transition colors around a center point:

```python
# Create a conical gradient with center at (600,170) and starting angle 90 degrees
conicalGradient = QConicalGradient(QPointF(600, 170), 90)

# Set color stops
conicalGradient.setColorAt(0, "blue")   # Start angle color
conicalGradient.setColorAt(1, "yellow") # End angle color (360 degrees from start)
```

The gradient sweeps around the center point, creating a circular pattern that transitions between colors based on the angle.

### Spread Methods

Spread methods determine how gradients fill space beyond their defined boundaries:

1. **PadSpread** (default): Extends the edge colors
   ```python
   gradient.setSpread(QGradient.PadSpread)
   ```

2. **RepeatSpread**: Repeats the gradient pattern
   ```python
   gradient.setSpread(QGradient.RepeatSpread)
   ```

3. **ReflectSpread**: Reflects the gradient pattern
   ```python
   gradient.setSpread(QGradient.ReflectSpread)
   ```

### Using Gradients with Shapes

Once a gradient is configured, it's applied using a QBrush:

```python
painter.setBrush(QBrush(gradient))
painter.drawRect(20, 20, 100, 300)  # For a linear gradient
painter.drawRect(130, 20, 300, 300) # For a radial gradient
painter.drawEllipse(450, 20, 300, 300) # For a conical gradient
```

## Running the Application

1. Generate the UI Python file (if widget.ui changes):
   ```
   pyside6-uic widget.ui -o ui_widget.py
   ```

2. Ensure PySide6 is installed:
   ```
   pip install PySide6
   ```

3. Run the application:
   ```
   python main.py
   ```

4. Observe:
   - A rectangle with a vertical linear gradient (red-gray-yellow) with reflection
   - A rectangle with a radial gradient (blue-yellow) with repetition
   - An ellipse with a conical gradient (blue-yellow)

## Implementation Notes

### Color Specification

Colors can be specified in multiple ways:

```python
# Named colors
gradient.setColorAt(0, "red")

# Qt color constants
gradient.setColorAt(0, Qt.red)

# RGB/RGBA values
gradient.setColorAt(0, QColor(255, 0, 0))
gradient.setColorAt(0, QColor(255, 0, 0, 128))  # Semi-transparent

# Hex values
gradient.setColorAt(0, QColor("#FF0000"))
```

### Gradient Coordinates

Gradient coordinates are defined in the local coordinate system of the painted shape. This means:

- For a linear gradient, you specify start and end points
- For a radial gradient, you specify center point and radius
- For a conical gradient, you specify center point and start angle

### Rendering Performance

Gradients can be performance-intensive, especially for large areas or complex gradients. For static gradients, consider:

1. Pre-rendering to a QPixmap
2. Caching the result
3. Using simpler gradients for frequently redrawn areas


## Practical Applications

Gradients are useful for:

1. **UI Design**: Creating attractive buttons, backgrounds, and panels
2. **Data Visualization**: Representing data intensity or transitions
3. **Graphics & Illustrations**: Creating realistic lighting and shadows
4. **Charts**: Making visually appealing chart areas and bars
5. **Progress Indicators**: Visual feedback that's more interesting than solid colors

## Advanced Gradient Techniques

### Gradient Transformations

You can apply transformations to gradients:

```python
transform = QTransform()
transform.rotate(45)
gradient.setCoordinateMode(QGradient.ObjectMode)
gradient.setTransform(transform)
```

### Coordinate Modes

Gradients have different coordinate modes:

```python
# Logical coordinates (relative to the shape)
gradient.setCoordinateMode(QGradient.LogicalMode)

# Physical coordinates (relative to the device)
gradient.setCoordinateMode(QGradient.ObjectMode)

# Absolute coordinates (in the painting system)
gradient.setCoordinateMode(QGradient.StretchToDeviceMode)
```

### Multiple Color Stops

Complex gradients can use many color stops:

```python
# Rainbow gradient
for i in range(7):
    gradient.setColorAt(i/6, QColor.fromHsv(i*60, 255, 255))
```

### Interpolation Mode

Control how colors blend:

```python
# Component-wise RGB interpolation (default)
gradient.setInterpolationMode(QGradient.ComponentInterpolation)

# Color space interpolation
gradient.setInterpolationMode(QGradient.ColorInterpolation)
```