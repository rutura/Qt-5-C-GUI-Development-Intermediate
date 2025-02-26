# QPainter Transformations in PySide6

This project demonstrates how to use transformations with QPainter in PySide6, including rotation, scaling, shearing, and translation.

## Project Overview

This application illustrates:
1. Translating the coordinate system (moving the origin)
2. Rotating drawing operations
3. Scaling drawing operations
4. Shearing drawing operations
5. Resetting transformations
6. Combining multiple transformations

## Project Structure

```
project/
├── main.py      # Application entry point
├── ui_widget.py # Generated UI code from widget.ui
├── widget.py    # Main widget with transformation demonstrations
└── widget.ui    # UI design file (XML)
```

## Key Concepts

### Coordinate System Transformations

QPainter allows you to transform the coordinate system before drawing operations:

```python
# The default coordinate system has (0,0) at the top-left corner
# with x increasing to the right and y increasing downward
```

### Translation

Translation moves the origin of the coordinate system:

```python
# Move the origin 200 pixels right and 200 pixels down
painter.translate(200, 200)
```

This affects all subsequent drawing operations until another transformation is applied or until the transformation is reset.

### Rotation

Rotation turns the coordinate system around its origin:

```python
# Rotate the coordinate system by 45 degrees clockwise
painter.rotate(45)
```

The angle is specified in degrees, with positive values rotating clockwise.

### Scaling

Scaling stretches or shrinks the coordinate system:

```python
# Make everything 60% of its original size
painter.scale(0.6, 0.6)
```

The x and y scale factors can be different, allowing for non-uniform scaling.

### Shearing

Shearing skews the coordinate system:

```python
# Apply shearing transformation
painter.shear(0.6, 0.6)
```

The shear factors specify how much the x coordinates shift based on the y value, and how much the y coordinates shift based on the x value.

### Resetting Transformations

You can reset the coordinate system to its default state:

```python
# Reset to the default transformation
painter.resetTransform()
```

This removes all applied transformations.

## Transformation Order and Combining Transformations

The order of transformations matters:

```python
# Center a rotation around point (200, 200)
painter.translate(200, 200)  # Step 1: Move origin to (200, 200)
painter.rotate(45)           # Step 2: Rotate around the new origin
painter.translate(-200, -200)  # Step 3: Move origin back
```

This sequence rotates the coordinate system around the point (200, 200) rather than the default origin (0, 0).

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
   - The original black rectangle
   - A rotated green rectangle
   - A scaled blue rectangle
   - A red rectangle showing the original position after resetTransform()
   - A sheared yellow rectangle

## Implementation Notes

### Transformation Stack

Transformations are cumulative. Each new transformation is applied relative to the current state:

```python
painter.translate(100, 0)  # Move 100 pixels right
painter.translate(0, 100)  # Move 100 pixels down (now at (100, 100))
```

### Save and Restore

For complex transformations, you can save and restore the state:

```python
painter.save()      # Save the current transformation state
# Apply transformations
painter.restore()   # Restore the saved state
```

This approach allows you to apply transformations for specific drawing operations without affecting others.

### Center of Rotation

To rotate around a specific point, you need to:
1. Translate to the desired center
2. Apply the rotation
3. Translate back

```python
painter.translate(centerX, centerY)
painter.rotate(angle)
painter.translate(-centerX, -centerY)
```

### Transformation Matrix

Under the hood, QPainter uses a transformation matrix for all transformations:

```python
# Alternatively, you can set the transformation matrix directly
transform = QTransform()
transform.translate(200, 200)
transform.rotate(45)
transform.translate(-200, -200)
painter.setTransform(transform)
```

## Practical Applications

Transformations are essential for:

1. **Custom Controls**: Creating rotated text or components
2. **Data Visualization**: Implementing zoom, pan, and rotation in charts and graphs
3. **Graphics Applications**: Creating effects, animations, and manipulations
4. **Games**: Implementing camera systems and object transformations
5. **Technical Drawing**: Creating different views and projections

## Advanced Transformation Techniques

### World vs. Logical vs. Device Transformations

QPainter has different types of transformations:

```python
# Combine all transformations (default behavior)
painter.setWorldTransform(transform)

# Only transform logical coordinates
painter.setWorldMatrixEnabled(False)
```

### Transforming Points

You can transform individual points:

```python
point = QPointF(10, 10)
transform = painter.transform()
transformedPoint = transform.map(point)
```

### Custom Transformation Matrices

For complex transformations, create custom matrices:

```python
transform = QTransform()
transform.rotate(45)
transform.scale(2, 1)
painter.setTransform(transform)
```

### Non-Affine Transformations

Using QTransform, you can also create perspective transformations:

```python
transform = QTransform()
transform.rotate(45)
# Add perspective effect
transform.setMatrix(transform.m11(), transform.m12(), 0.001,
                   transform.m21(), transform.m22(), 0.001,
                   transform.m31(), transform.m32(), 1)
painter.setTransform(transform)
```