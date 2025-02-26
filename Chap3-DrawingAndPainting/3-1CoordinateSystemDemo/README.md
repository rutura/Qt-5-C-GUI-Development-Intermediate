# QPainter Coordinate Systems in PySide6

This project demonstrates how QPainter's coordinate systems work in PySide6, showing the difference between logical and physical coordinates.

## Project Overview

This application illustrates:
1. Basic usage of QPainter for custom drawing
2. How to manipulate logical coordinates using `setWindow()`
3. How to manipulate physical coordinates using `setViewport()`
4. The effect of these transformations on drawing operations
5. How to save and restore painter states

## Project Structure

```
project/
├── main.py      # Application entry point
├── ui_widget.py # Generated UI code from widget.ui
├── widget.py    # Main widget with custom painting
└── widget.ui    # UI design file (XML)
```

## Key Concepts

### QPainter Coordinate Systems

QPainter has two coordinate systems:

1. **Logical Coordinates (Window)**: The coordinate system used by your drawing code
2. **Physical Coordinates (Viewport)**: The actual pixels on the screen/device

By default, these are mapped 1:1, but you can change this mapping to:
- Scale your drawing
- Translate (move) your drawing
- Create device-independent drawing code
- Implement zooming functionality

### Basic Drawing

The application starts by drawing a red rectangle with the default coordinate mapping:

```python
# Draw a red rectangle using default coordinates
painter.drawRect(50, 50, 100, 100)
```

### Manipulating Logical Coordinates

The green rectangle is drawn after changing the logical coordinate system:

```python
# Change the logical coordinates, keep physical coords the same
painter.save()  # Save the current state

painter.setWindow(0, 0, 300, 200)
mPen.setColor(Qt.green)
painter.setPen(mPen)

# Draw a green rectangle with modified logical coordinates
painter.drawRect(50, 50, 100, 100)

painter.restore()  # Restore the previous state
```

By changing the logical coordinate system, the same drawing code produces a different result because the coordinates are interpreted differently.

### Manipulating Physical Coordinates

The blue rectangle is drawn after changing the physical coordinate system:

```python
# Change physical coordinates, keep logical the same
painter.save()

mPen.setColor(Qt.blue)
painter.setPen(mPen)
painter.setViewport(0, 0, 300, 200)

# Draw a blue rectangle with modified physical coordinates
painter.drawRect(50, 50, 100, 100)

painter.restore()
```

This affects how the logical coordinates are mapped to physical pixels on the screen.

### Save and Restore

The `save()` and `restore()` methods are used to manage the painter state:

```python
painter.save()    # Save the current state
# Make changes to the painter
painter.restore() # Restore the previous state
```

This prevents changes from affecting subsequent drawing operations.

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
   - A red rectangle drawn with default coordinates
   - A green rectangle drawn with modified logical coordinates
   - A blue rectangle drawn with modified physical coordinates
   - Coordinate information printed to the console

## Understanding the Results

When you run the application, you should see:

1. **Red Rectangle**: The reference rectangle using the default coordinate mapping
2. **Green Rectangle**: Appears smaller and in a different position because the logical coordinate system has been changed to a 300×200 window
3. **Blue Rectangle**: Appears larger because the physical coordinate system has been reduced to a 300×200 viewport

The console output shows the default window and viewport settings.

## Practical Applications

Understanding coordinate systems in QPainter is useful for:

1. **Responsive UI**: Adapting drawings to different screen sizes
2. **Zoom Functionality**: Implementing zoom in/out features
3. **Scrollable Views**: Creating large, scrollable canvases
4. **Custom Controls**: Building controls that scale appropriately
5. **Device-Independent Drawing**: Creating drawings that look consistent across devices


## Exercise

Beyond what this example demonstrates, QPainter's coordinate systems can be further manipulated with:

1. **Matrix Transformations**: Using `setWorldTransform()` for rotations, scaling, and shearing
2. **Custom Viewports**: Creating multiple viewports within a single widget
3. **High DPI Support**: Handling different screen densities
4. **Painter Paths**: Creating complex shapes that transform with the coordinate system