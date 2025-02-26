# Car Drawing in PySide6

This project demonstrates how to create reusable drawing functions in PySide6 by implementing car drawing methods that can be used with different parameters and positions.

## Project Overview

This application illustrates:
1. Creating complex shapes using QPainter
2. Implementing reusable drawing functions
3. Using both absolute and relative coordinates for drawing
4. Parameterizing drawings to customize their appearance
5. Drawing multiple instances of the same shape with different properties

## Project Structure

```
project/
├── main.py      # Application entry point
├── ui_widget.py # Generated UI code from widget.ui
├── widget.py    # Main widget with car drawing functions
└── widget.ui    # UI design file (XML)
```

## Key Concepts

### Reusable Drawing Functions

The application defines two drawing functions:

1. **Basic drawing function** with hardcoded coordinates:
   ```python
   def drawCar(self, painter):
       """Draw a car with hardcoded coordinates"""
       # Drawing code here...
   ```

2. **Improved drawing function** with parametrized position and appearance:
   ```python
   def drawCarV2(self, painter, rect, tireColor):
       """Draw a car with relative coordinates based on a rect and custom tire color"""
       # Drawing code here with relative coordinates...
   ```

### Drawing with Absolute Coordinates

The first implementation uses absolute coordinates for all shapes:

```python
# Draw the upper roofs
painter.drawArc(QRectF(100, 100, 200, 200), startAngle, spanAngle)
painter.drawLine(197, 110, 197, 170)
```

This approach is simple but not reusable for drawing the same shape at different positions.

### Drawing with Relative Coordinates

The improved implementation uses relative coordinates based on a reference rectangle:

```python
# Use the provided rectangle as the base
outRect = QRectF(rect)

# Calculate inner rectangle based on the outer one
inRect = QRectF(
    outRect.topLeft().x() + 10, 
    outRect.topLeft().y() + 10,
    outRect.width() - 20, 
    outRect.height() - 20
)

# Draw lines relative to the top-left corner of the rectangle
painter.drawLine(
    outRect.topLeft() + QPointF(97, 10),
    outRect.topLeft() + QPointF(97, 70)
)
```

This makes the drawing function reusable for different positions.

### Customizing Appearance

The improved function also accepts a parameter for customizing the tire color:

```python
# Back Tire
painter.drawEllipse(QRectF(outRect.topLeft() + QPointF(0, 110), QSize(60, 60)))
painter.setBrush(tireColor)  # Use the provided color
```

### Drawing Multiple Instances

The `paintEvent` method demonstrates drawing multiple instances of the car:

```python
def paintEvent(self, event):
    painter = QPainter(self)
    
    # Draw the first car with hardcoded coordinates
    self.drawCar(painter)
    
    # Draw additional cars with different positions and tire colors
    self.drawCarV2(painter, QRectF(500, 100, 200, 200), Qt.red)
    self.drawCarV2(painter, QRectF(500, 300, 200, 200), Qt.green)
    self.drawCarV2(painter, QRectF(100, 300, 200, 200), Qt.blue)
```

## Implementation Details

### Car Components

The car drawing consists of several components:

1. **Upper Section**: The roof and cabin
   ```python
   # Draw the upper roofs
   painter.drawArc(outRect, startAngle, spanAngle)
   painter.drawArc(inRect, 20 * 16, 65 * 16)
   painter.drawArc(inRect, 92 * 16, 68 * 16)
   ```

2. **Back and Front Sections**: The hood and trunk
   ```python
   # Back Section
   painter.drawLine(
       outRect.topLeft() + QPointF(5, 74),
       outRect.topLeft() + QPointF(-50, 79)
   )
   
   # Front Section
   painter.drawLine(
       outRect.topLeft() + QPointF(200, 74),
       outRect.topLeft() + QPointF(290, 75)
   )
   ```

3. **Tires**: The wheels with frames and inner parts
   ```python
   # Back Tire
   painter.drawEllipse(QRectF(outRect.topLeft() + QPointF(0, 110), QSize(60, 60)))
   painter.setBrush(tireColor)
   painter.drawEllipse(QRectF(outRect.topLeft() + QPointF(10, 120), QSize(40, 40)))
   ```

### Arc Angles

In Qt, angles for arcs are specified in 16ths of a degree:
```python
startAngle = 15 * 16  # 15 degrees
spanAngle = 150 * 16  # 150 degrees
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
   - Four cars drawn on the screen
   - One with the basic drawing function (black tires)
   - Three with the improved function in different positions and with different tire colors (red, green, blue)

## Practical Applications

This approach to drawing is useful for:

1. **Game Development**: Drawing game characters or objects at different positions
2. **Custom UI Controls**: Creating reusable drawing functions for UI elements
3. **Data Visualization**: Drawing chart elements like bars or points based on data
4. **Technical Diagrams**: Creating components that can be positioned and customized
5. **Animations**: Moving elements around the screen by changing their position parameters

## Advanced Drawing Techniques

Building on this example, more advanced techniques could include:

1. **Parameterized Scaling**: Adding a scale factor to resize the car
   ```python
   def drawCarV3(self, painter, rect, tireColor, scale=1.0):
       # Apply scaling to all dimensions
   ```

2. **Rotation**: Adding rotation to the car
   ```python
   def drawCarV3(self, painter, rect, tireColor, angle=0):
       painter.save()
       painter.translate(rect.center())
       painter.rotate(angle)
       painter.translate(-rect.center())
       # Draw car
       painter.restore()
   ```

3. **Animation**: Updating positions over time for animation
   ```python
   def updateAnimation(self):
       self.carPosition.setX(self.carPosition.x() + 1)
       self.update()  # Trigger a repaint
   ```

4. **Clipping**: Using QClipPath to clip the drawing to a specific area
   ```python
   painter.setClipRect(QRectF(0, 0, width/2, height))
   ```