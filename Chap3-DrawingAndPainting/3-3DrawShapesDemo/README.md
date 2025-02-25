# QPainter Shapes in PySide6

This project demonstrates the variety of shapes and drawing operations available with QPainter in PySide6.

## Project Overview

This application illustrates:
1. Drawing basic shapes (rectangles, ellipses, lines)
2. Creating complex shapes (polygons, arcs, chords, pies)
3. Rendering text with custom fonts
4. Drawing images (pixmaps)
5. Customizing drawing with pens and brushes

## Project Structure

```
project/
├── main.py      # Application entry point
├── ui_widget.py # Generated UI code from widget.ui
├── widget.py    # Main widget with custom painting
└── widget.ui    # UI design file (XML)
└── images/      # Directory containing images (optional)
   └── LearnQt.png # Sample image
```

## Key Concepts

### Basic Drawing Setup

QPainter requires a paint device (like a widget) and configuration for its pen and brush:

```python
painter = QPainter(self)  # 'self' is the widget to paint on
mPen = QPen()
mPen.setColor(Qt.black)
mPen.setWidth(5)
painter.setPen(mPen)
```

### Basic Shapes

QPainter can draw several basic shapes:

#### Rectangles
```python
painter.setBrush(Qt.red)
painter.drawRect(10, 10, 100, 100)
```

#### Ellipses
```python
painter.setBrush(Qt.green)
painter.drawEllipse(120, 10, 200, 100)
```

#### Rounded Rectangles
```python
painter.setBrush(Qt.gray)
painter.drawRoundedRect(330, 10, 200, 100, 20, 20)
```

### Lines

Lines can be drawn individually or in groups:

#### Individual Lines
```python
painter.drawLine(550, 30, 650, 30)
```

#### Multiple Lines
```python
pointVec = [
    QPointF(660, 30), QPointF(760, 30),
    QPointF(660, 50), QPointF(760, 50)
]
painter.drawLines(pointVec)
```

### Complex Shapes

Complex shapes can be created with specific APIs:

#### Polygons
```python
# Create a polygon from a list of points
polygon = QPolygonF([
    QPointF(240.0, 150.0),
    QPointF(10.0, 150.0),
    QPointF(60.0, 200.0),
    QPointF(30.0, 250.0),
    QPointF(120.0, 250.0)
])
painter.drawPolygon(polygon)
```

#### Arcs
Arcs are segments of an ellipse's outline:
```python
rectangle = QRectF(250.0, 150.0, 150.0, 150.0)
startAngle = 30 * 16  # Qt uses 16th of a degree for angles
spanAngle = 240 * 16
painter.drawArc(rectangle, startAngle, spanAngle)
```

#### Chords
Chords are arcs with a straight line connecting the endpoints:
```python
chordRect = QRectF(450.0, 150.0, 150.0, 150.0)
painter.drawChord(chordRect, startAngle, spanAngle)
```

#### Pies
Pies are arcs with lines from the center to the endpoints:
```python
pieRect = QRectF(650.0, 150.0, 150.0, 150.0)
painter.drawPie(pieRect, startAngle, spanAngle)
```

### Text and Images

QPainter also handles text and images:

#### Text
```python
painter.setFont(QFont("Times", 40, QFont.Bold))
painter.drawText(50.0, 400.0, "I'm loving Qt")
```

#### Images (Pixmaps)
```python
target = QRectF(520.0, 350.0, 200.0, 200.0)
mPix = QPixmap("images/LearnQt.png")
mSourceRect = mPix.rect()
painter.drawPixmap(target, mPix, mSourceRect)
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

3. Create an `images` directory and add an image named `LearnQt.png` (optional)

4. Run the application:
   ```
   python main.py
   ```

5. Observe the variety of shapes, text, and images drawn on the widget

## Implementation Notes

### The `paintEvent` Method

The painting is done in the `paintEvent` method, which is called whenever the widget needs to be redrawn:

```python
def paintEvent(self, event):
    painter = QPainter(self)
    # Drawing operations...
```

### Angles in Qt

Qt uses 16ths of a degree for angle measurements:
- 360 degrees = 5760 units (360 × 16)
- 90 degrees = 1440 units (90 × 16)
- 45 degrees = 720 units (45 × 16)

### Pens and Brushes

- **Pen**: Controls the outline properties (color, width, style)
- **Brush**: Controls the fill properties (color, pattern, gradient)

```python
mPen = QPen()
mPen.setColor(Qt.black)
mPen.setWidth(5)
painter.setPen(mPen)

painter.setBrush(Qt.red)  # Solid red fill
```

### Coordinate System

QPainter uses a Cartesian coordinate system where:
- The origin (0,0) is at the top-left corner
- X-coordinates increase to the right
- Y-coordinates increase downward

### Error Handling for Images

The code includes error handling for image loading:

```python
try:
    mPix = QPixmap("images/LearnQt.png")
    if mPix.isNull():
        # Create a placeholder if image not found
        mPix = QPixmap(200, 200)
        mPix.fill(Qt.darkCyan)
        # ... draw placeholder text ...
except Exception as e:
    print(f"Error drawing pixmap: {e}")
```


## Advanced Techniques

QPainter supports many more advanced features not shown in this example:

1. **Gradients**: Linear, radial, and conical gradients using QLinearGradient, QRadialGradient, and QConicalGradient

2. **Path Drawing**: Complex paths using QPainterPath

3. **Transformations**: Rotating, scaling, and shearing using QTransform

4. **Clipping**: Restricting drawing to specific regions

5. **Composition Modes**: Controlling how new drawing combines with existing content

6. **Anti-aliasing**: Smoother edges with painter.setRenderHint(QPainter.Antialiasing)