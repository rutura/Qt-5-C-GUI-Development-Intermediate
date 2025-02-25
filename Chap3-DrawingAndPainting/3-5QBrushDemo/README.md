# QBrush Styles in PySide6

This project demonstrates the various brush styles (fill patterns) available in QPainter in PySide6.

## Project Overview

This application illustrates:
1. Different brush patterns for filling shapes
2. Density patterns with varying densities
3. Line-based patterns (horizontal, vertical, diagonal)
4. Image-based texture patterns
5. Configuring brush color and style

## Project Structure

```
project/
├── main.py       # Application entry point
├── ui_widget.py  # Generated UI code from widget.ui
├── widget.py     # Main widget with custom painting
├── widget.ui     # UI design file (XML)
└── images/       # Directory containing images (optional)
   └── LearnQt.png # Sample image for texture pattern
```

## Key Concepts

### Brush Configuration

QBrush can be configured with different styles that affect how shapes are filled:

```python
# Configure a brush with color and style
mBrush = QBrush()
mBrush.setColor(Qt.red)
mBrush.setStyle(Qt.SolidPattern)
painter.setBrush(mBrush)
```

### Available Brush Styles

#### Density Patterns

These patterns fill the shape with dots of varying density:

1. **Qt.SolidPattern**: Completely filled
   ```python
   mBrush.setStyle(Qt.SolidPattern)
   ```

2. **Qt.Dense1Pattern** through **Qt.Dense7Pattern**: Dots with different densities
   ```python
   mBrush.setStyle(Qt.Dense1Pattern)  # Most dense
   # ...through...
   mBrush.setStyle(Qt.Dense7Pattern)  # Least dense
   ```

#### Line Patterns

These patterns fill the shape with lines in different orientations:

1. **Qt.HorPattern**: Horizontal lines
   ```python
   mBrush.setStyle(Qt.HorPattern)
   ```

2. **Qt.VerPattern**: Vertical lines
   ```python
   mBrush.setStyle(Qt.VerPattern)
   ```

3. **Qt.CrossPattern**: Crossing horizontal and vertical lines
   ```python
   mBrush.setStyle(Qt.CrossPattern)
   ```

4. **Qt.BDiagPattern**: Backward diagonal lines (top-right to bottom-left)
   ```python
   mBrush.setStyle(Qt.BDiagPattern)
   ```

5. **Qt.FDiagPattern**: Forward diagonal lines (top-left to bottom-right)
   ```python
   mBrush.setStyle(Qt.FDiagPattern)
   ```

6. **Qt.DiagCrossPattern**: Crossing diagonal lines
   ```python
   mBrush.setStyle(Qt.DiagCrossPattern)
   ```

#### Texture Pattern

This pattern fills the shape with a repeating image:

```python
mPix = QPixmap("images/LearnQt.png")
mBrush.setTexture(mPix.scaled(50, 50))
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

5. Observe the variety of brush patterns displayed as filled rectangles

## Implementation Notes

### The `paintEvent` Method

The painting is done in the `paintEvent` method, which is called whenever the widget needs to be redrawn:

```python
def paintEvent(self, event):
    painter = QPainter(self)
    mBrush = QBrush()
    # ... configure brush and draw shapes ...
```

### Brush Color

The color of the brush affects the pattern color:

```python
mBrush.setColor(Qt.blue)
```

### Fallback for Missing Images

The code includes a fallback for when the texture image is not found:

```python
try:
    mPix = QPixmap("images/LearnQt.png")
    if mPix.isNull():
        # Create a placeholder pixmap with a simple pattern
        mPix = QPixmap(50, 50)
        mPix.fill(Qt.darkCyan)
        tempPainter = QPainter(mPix)
        tempPainter.setPen(Qt.white)
        tempPainter.drawLine(0, 0, 50, 50)
        tempPainter.drawLine(0, 50, 50, 0)
        tempPainter.end()
except Exception as e:
    print(f"Error setting texture: {e}")
```

## From C++ to PySide6

This project has been ported from Qt/C++ to PySide6. Key translations include:

1. **Resource System**:
   - C++: `QPixmap mPix("://images/LearnQt.png");` (using Qt resource system)
   - Python: Direct file path `QPixmap("images/LearnQt.png")`

2. **Error Handling**:
   - C++: Generally minimal in example code
   - Python: Added try/except block for image loading

3. **Pixmap Manipulation**:
   - C++: Similar approach
   - Python: Added more robust placeholder generation if image is missing

## Practical Applications

Understanding brush styles is essential for:

1. **Data Visualization**: Creating distinguishable fills for charts and graphs
2. **Technical Drawing**: Representing different materials or states
3. **UI Design**: Creating textured backgrounds or filled components
4. **Maps and Diagrams**: Representing different areas or zones
5. **Accessibility**: Using patterns to distinguish areas when color alone is insufficient

## Advanced Brush Techniques

Beyond the basic styles shown here, QBrush offers more advanced features:

1. **Gradient Fills**:
   ```python
   gradient = QLinearGradient(0, 0, 100, 100)
   gradient.setColorAt(0, Qt.red)
   gradient.setColorAt(1, Qt.blue)
   mBrush = QBrush(gradient)
   ```

2. **Custom Patterns**:
   Create completely custom patterns with QImage and setTextureImage()
   ```python
   image = QImage(2, 2, QImage.Format_ARGB32)
   image.setPixel(0, 0, QColor(Qt.red).rgba())
   image.setPixel(1, 1, QColor(Qt.red).rgba())
   image.setPixel(0, 1, QColor(Qt.blue).rgba())
   image.setPixel(1, 0, QColor(Qt.blue).rgba())
   mBrush.setTextureImage(image)
   ```

3. **Transformed Brushes**:
   Apply transformations to brushes to rotate, scale, or shear the pattern
   ```python
   transform = QTransform()
   transform.rotate(45)
   mBrush.setTransform(transform)
   ```

4. **Alpha Blending**:
   Use semi-transparent colors for more subtle effects
   ```python
   mBrush.setColor(QColor(0, 0, 255, 128))  # Semi-transparent blue
   ```

## Comparison of Brush Styles

The application shows a visual comparison of all the standard brush styles:

1. **First Row**: Various density patterns from solid to sparse
2. **Second Row**: Line-based patterns and texture

This visual reference helps developers choose the appropriate pattern for their needs.