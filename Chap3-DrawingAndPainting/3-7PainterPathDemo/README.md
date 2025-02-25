# QPainterPath in PySide6

This project demonstrates how to use QPainterPath in PySide6 to create complex shapes and paths for drawing.

## Project Overview

This application illustrates:
1. Creating QPainterPath objects
2. Adding shapes (rectangles, ellipses) to paths
3. Drawing lines and arcs within paths
4. Combining shapes into complex paths
5. Transforming paths
6. Rendering paths with different fill settings

## Project Structure

```
project/
├── main.py      # Application entry point
├── ui_widget.py # Generated UI code from widget.ui
├── widget.py    # Main widget with path demonstrations
└── widget.ui    # UI design file (XML)
```

## Key Concepts

### Creating Paths

A QPainterPath is an object that can store and manipulate a sequence of drawing commands:

```python
# Create a new path
path = QPainterPath()
```

### Adding Shapes to Paths

Shapes can be added to a path as complete entities:

```python
# Add a rectangle
path.addRect(100, 100, 100, 100)

# Add an ellipse
path.addEllipse(100, 220, 100, 100)
```

### Combining Paths with Lines and Arcs

Paths can include lines and arcs that connect shapes:

```python
# Move to a specific point
path.moveTo(150, 150)

# Draw a line to another point
path.lineTo(150, 50)

# Draw an arc (center x, y, width, height, startAngle, sweepLength)
path.arcTo(50, 50, 200, 200, 90, 90)

# Complete the shape by connecting back to the start
path.lineTo(150, 150)
```

### Drawing Paths

Once a path is created, it can be drawn using QPainter:

```python
# Set fill color
painter.setBrush(Qt.green)

# Draw the path with current pen and brush
painter.drawPath(path)
```

### Transforming Paths

Paths can be transformed using various operations:

```python
# Translate a path
path.translate(150, 150)  # Move 150 pixels right and 150 pixels down

# Other transformations available:
# path.rotate(angle)
# path.scale(sx, sy)
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
   - A green filled path that combines a rectangle, line, and arc
   - Two unfilled paths showing connected ellipses:
     - One in the original position
     - A second copy translated 150 pixels right and down

## Implementation Notes

### Path Creation Process

The typical process for creating a path involves:
1. Creating a new QPainterPath
2. Adding shapes, lines, and arcs
3. Setting up the painter's pen and brush
4. Drawing the path

### Path Components

A path can contain several types of elements:
- **MoveTo**: Position the "pen" without drawing
- **LineTo**: Draw a straight line
- **ArcTo**: Draw an arc of an ellipse
- **CubicTo/QuadTo**: Draw Bezier curves
- **AddRect/AddEllipse**: Add complete shapes

### Arc Angles

In QPainterPath, angles for arcs are specified in degrees multiplied by 16:
```python
# Draw a 90-degree arc starting at 90 degrees
path.arcTo(50, 50, 200, 200, 90, 90)
```

### Connecting vs. Adding Shapes

There are two main ways to include shapes in a path:
1. **Adding**: Using `addRect()`, `addEllipse()`, etc. - These create separate sub-paths
2. **Connecting**: Using `moveTo()`, `lineTo()`, `arcTo()` - These create connected segments

### Filling Behavior

When a path is filled:
- Closed sub-paths are filled according to their winding rule
- Connected segments that form a closed shape are filled
- Open sub-paths are not filled (just stroked)

## From C++ to PySide6

This project has been ported from Qt/C++ to PySide6. Key translations include:

1. **Brush Specification**:
   - C++: `painter.setBrush(Qt::green);`
   - Python: `painter.setBrush(Qt.green)`

2. **Path Creation**:
   - C++: Same API structure as Python
   - Python: Same functions, different syntax

3. **Transparency**:
   - C++: Often not explicitly set
   - Python: `painter.setBrush(Qt.transparent)` for clarity

## Practical Applications

QPainterPath is useful for:

1. **Custom UI Controls**: Creating unique-shaped controls
2. **Vector Graphics**: Creating scalable graphics and icons
3. **Game Development**: Creating complex collision shapes
4. **Technical Drawing**: Creating diagrams with precise shapes
5. **Charts and Graphs**: Creating custom visualization elements

## Advanced Techniques

Beyond the basics shown here, QPainterPath offers more advanced capabilities:

### Path Operations

Combine paths with boolean operations:

```python
result = path1.united(path2)         # Union
result = path1.subtracted(path2)     # Difference
result = path1.intersected(path2)    # Intersection
```

### Text in Paths

Convert text to paths for special effects:

```python
font = QFont("Arial", 50)
path = QPainterPath()
path.addText(100, 100, font, "Hello")
```

### Clipping with Paths

Use paths as complex clipping regions:

```python
painter.setClipPath(path)
# Drawing operations are now clipped to the path
```

### Checking Point Containment

Test if a point is inside a path:

```python
if path.contains(QPointF(x, y)):
    # Point is inside the path
```

### Creating Stroked Outlines

Convert a path's outline to another path:

```python
pen = QPen(Qt.black, 5)
strokedPath = QPainterPath()
strokedPath.addPath(QPainterPathStroker(pen).createStroke(path))
```