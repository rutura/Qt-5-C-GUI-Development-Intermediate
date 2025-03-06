# PySide6 Graphics View Shapes - Implementation Guide

This guide demonstrates how to create various graphics items in PySide6's Graphics View Framework. The project shows how to create and manipulate different shapes, paths, and images in a graphics scene.

## Project Overview

This application demonstrates:
- Creating different types of graphics items (line, ellipse, path, image)
- Making items movable by using parent-child relationships
- Using QPainterPath to create custom shapes
- Loading images from resources
- Organizing items with bounding rectangles

## Project Structure

```
graphics_view_shapes_demo/
│
├── main.py           # Application entry point
├── widget.py         # Main widget containing the shapes implementation
├── resource.qrc      # Qt Resource Collection file
├── resource_rc.py    # Generated resource code
└── ui_widget.py      # Generated UI code from widget.ui
```

## Building and Running the Project

1. Generate UI Python files:
   ```bash
   pyside6-uic widget.ui -o ui_widget.py
   ```

2. Generate resource Python files:
   ```bash
   pyside6-rcc resource.qrc -o resource_rc.py
   ```

3. Run the application:
   ```bash
   python main.py
   ```

## Implementation Details

### Setting Up the Scene and View

The application creates a QGraphicsScene with coordinate axes and a QGraphicsView to display it:

```python
# Create the graphics scene
self.scene = QGraphicsScene(self)
self.scene.setSceneRect(QRectF(-400, -400, 800, 800))

# Add coordinate axes
self.scene.addLine(-400, 0, 400, 0)  # Horizontal line
self.scene.addLine(0, -400, 0, 400)  # Vertical line

# Create the graphics view and set its scene
self.view = QGraphicsView(self)
self.view.setScene(self.scene)
```

This sets up a scene with a coordinate system centered at (0, 0) and extending 400 units in each direction.

### Creating Simple Shapes

The application demonstrates creating basic shapes like lines and ellipses:

```python
# Creating a line
line = QGraphicsLineItem(QPointF(10, 10), QPointF(90, 90))
line.setPen(QPen(Qt.red, 3))

# Creating an ellipse
rect = QRectF(10, 10, 80, 60)
ellipse = QGraphicsEllipseItem(rect)
ellipse.setBrush(QBrush(Qt.green))
```

### Creating Paths

For more complex shapes, the application uses QPainterPath:

```python
# Creating a compound path with an ellipse and rectangle
path = QPainterPath()
path.addEllipse(QRectF(10, 10, 90, 60))
path.addRect(QRectF(20, 20, 50, 50))

path_item = QGraphicsPathItem(path)
path_item.setPen(QPen(Qt.black, 5))
path_item.setBrush(Qt.green)
```

### Creating a Pie Shape

The application demonstrates how to create a pie shape using QPainterPath:

```python
path = QPainterPath(QPointF(60, 60))
path.arcTo(QRectF(10, 10, 80, 80), 30, 170)
path.lineTo(QPointF(60, 60))
```

This creates a path that starts at the center point (60, 60), draws an arc, and then draws a line back to the center.

### Creating a Star Shape

The application shows how to create a star shape using a polygon:

```python
poly = QPolygon()
poly.append(QPoint(0, 85))
poly.append(QPoint(75, 75))
# ... more points ...
poly.append(QPoint(0, 85))

path = QPainterPath()
path.addPolygon(poly)
```

### Working with Images

The application loads and displays an image from Qt resources:

```python
pixmap = QPixmap(":/images/LearnQt.png")
pixmap_item = QGraphicsPixmapItem(pixmap.scaled(110, 110))
```

### Making Items Movable

A key technique in this application is making items movable by using parent-child relationships:

```python
# Create a movable bounding rectangle
bound_rect = QGraphicsRectItem()
bound_rect.setRect(shape_item.boundingRect().adjusted(-10, -10, 10, 10))
bound_rect.setFlag(QGraphicsRectItem.GraphicsItemFlag.ItemIsMovable)
shape_item.setParentItem(bound_rect)

self.scene.addItem(bound_rect)
```

Instead of making each shape movable directly, the application:
1. Creates a transparent bounding rectangle slightly larger than the shape
2. Makes the rectangle movable
3. Makes the shape a child of the rectangle
4. Adds only the rectangle to the scene

This approach creates a "handle" around each shape that users can click and drag.

## Key Concepts

### Graphics Items Hierarchy

Qt's Graphics View Framework provides a hierarchy of item classes:

- **QGraphicsItem**: The base abstract class for all graphics items
- **QGraphicsLineItem**: For line segments
- **QGraphicsRectItem**: For rectangles
- **QGraphicsEllipseItem**: For ellipses and circles
- **QGraphicsPathItem**: For arbitrary paths
- **QGraphicsPixmapItem**: For images
- **QGraphicsPolygonItem**: For polygons
- **QGraphicsTextItem**: For text
- **QGraphicsItemGroup**: For grouping items

### QPainterPath

QPainterPath is a powerful class for creating complex shapes:

- **Path Operations**: Move to a point, draw lines, arcs, curves
- **Compound Shapes**: Add ellipses, rectangles, text, or polygons
- **Boolean Operations**: Unite, intersect, subtract, or XOR paths
- **Fill Rules**: Choose between odd-even or winding fill rules

Example of creating a simple path:

```python
path = QPainterPath()
path.moveTo(10, 10)
path.lineTo(100, 10)
path.arcTo(100, 10, 50, 50, 90, 180)
path.lineTo(10, 60)
path.closeSubpath()
```

### Styling Graphics Items

Items can be styled with pens and brushes:

```python
# Set the outline (pen)
item.setPen(QPen(Qt.black, 5, Qt.DashLine, Qt.RoundCap, Qt.RoundJoin))

# Set the fill (brush)
item.setBrush(QBrush(Qt.red, Qt.DiagonalPattern))
```

Pens control the outline:
- Color
- Width
- Line style (solid, dash, dot, etc.)
- Cap style (flat, square, round)
- Join style (miter, bevel, round)

Brushes control the fill:
- Color
- Pattern (solid, horizontal, vertical, cross, etc.)
- Texture (from an image)
- Gradient (linear, radial, conical)

### Coordinate Systems

The Graphics View Framework uses three coordinate systems:

1. **View Coordinates**: Pixel coordinates in the view widget
2. **Scene Coordinates**: Logical coordinates in the scene
3. **Item Coordinates**: Local coordinates for each item

The application uses scene coordinates centered at (0, 0) with axes to help visualize the coordinate system.

## Advanced Techniques

### Custom Graphics Items

For more complex items, you can create custom subclasses:

```python
class StarItem(QGraphicsItem):
    def __init__(self, points=5, inner_radius=40, outer_radius=80):
        super().__init__()
        self.points = points
        self.inner_radius = inner_radius
        self.outer_radius = outer_radius
        self.setFlag(QGraphicsItem.ItemIsMovable)
        
    def boundingRect(self):
        return QRectF(-self.outer_radius, -self.outer_radius,
                     2 * self.outer_radius, 2 * self.outer_radius)
    
    def paint(self, painter, option, widget):
        painter.setPen(QPen(Qt.black, 2))
        painter.setBrush(QBrush(Qt.yellow))
        
        # Create a path for a star
        path = QPainterPath()
        
        angle_step = 360 / (2 * self.points)
        
        for i in range(2 * self.points):
            angle = i * angle_step
            radius = self.outer_radius if i % 2 == 0 else self.inner_radius
            x = radius * math.cos(math.radians(angle))
            y = radius * math.sin(math.radians(angle))
            
            if i == 0:
                path.moveTo(x, y)
            else:
                path.lineTo(x, y)
        
        path.closeSubpath()
        painter.drawPath(path)
```

### Implementing Interaction

To add interaction to custom items, override event handlers:

```python
def mousePressEvent(self, event):
    self.setCursor(Qt.ClosedHandCursor)
    super().mousePressEvent(event)
    
def mouseReleaseEvent(self, event):
    self.setCursor(Qt.OpenHandCursor)
    super().mouseReleaseEvent(event)
    
def hoverEnterEvent(self, event):
    self.setCursor(Qt.OpenHandCursor)
    super().hoverEnterEvent(event)
    
def hoverLeaveEvent(self, event):
    self.setCursor(Qt.ArrowCursor)
    super().hoverLeaveEvent(event)
```

### Advanced Path Techniques

QPainterPath can be used for more advanced operations:

```python
# Create two paths
path1 = QPainterPath()
path1.addEllipse(QRectF(0, 0, 100, 100))

path2 = QPainterPath()
path2.addEllipse(QRectF(50, 50, 100, 100))

# Combine paths
united_path = path1.united(path2)        # Union
intersected_path = path1.intersected(path2)  # Intersection
subtracted_path = path1.subtracted(path2)    # Subtraction
```

### Transformations

Items can be transformed in various ways:

```python
# Scaling
item.setScale(2.0)  # Double the size

# Rotation
item.setRotation(45.0)  # Rotate 45 degrees

# Translation
item.setPos(100, 100)  # Move to (100, 100)

# Custom transformation
transform = QTransform()
transform.translate(100, 100)
transform.rotate(45)
transform.scale(2, 1)  # Stretch horizontally
item.setTransform(transform)
```

## Best Practices

1. **Use the Right Item Class**

   Choose the appropriate item class for your needs:
   
   ```python
   # For simple shapes, use specific classes
   line_item = QGraphicsLineItem(0, 0, 100, 100)
   rect_item = QGraphicsRectItem(0, 0, 100, 80)
   
   # For complex shapes, use QGraphicsPathItem
   path = QPainterPath()
   # ... create path ...
   path_item = QGraphicsPathItem(path)
   ```

2. **Optimize Performance**

   For scenes with many items:
   
   ```python
   # Turn off item indexing when adding many items
   scene.setItemIndexMethod(QGraphicsScene.NoIndex)
   
   # Add items
   for i in range(1000):
       scene.addItem(item)
   
   # Restore indexing
   scene.setItemIndexMethod(QGraphicsScene.BspTreeIndex)
   ```

3. **Use Item Flags Appropriately**

   Set flags based on the behavior you want:
   
   ```python
   # For an item that can be moved, selected, and focused
   item.setFlag(QGraphicsItem.ItemIsMovable)
   item.setFlag(QGraphicsItem.ItemIsSelectable)
   item.setFlag(QGraphicsItem.ItemIsFocusable)
   
   # Or set multiple flags at once
   item.setFlags(QGraphicsItem.ItemIsMovable | 
                QGraphicsItem.ItemIsSelectable)
   ```

4. **Structure Complex Items with Parent-Child Relationships**

   Group related items together:
   
   ```python
   # Create a car with body and wheels
   body = QGraphicsRectItem(0, 0, 100, 30)
   wheel1 = QGraphicsEllipseItem(10, 25, 20, 20)
   wheel2 = QGraphicsEllipseItem(70, 25, 20, 20)
   
   # Make wheels children of body
   wheel1.setParentItem(body)
   wheel2.setParentItem(body)
   
   # Now you only need to add the body to the scene
   scene.addItem(body)
   ```

5. **Use Resource System for Images**

   Package images with your application:
   
   ```python
   # Load from resource instead of file system
   pixmap = QPixmap(":/images/my_image.png")
   ```

## Conclusion

The PySide6 Graphics View Framework provides a powerful way to create and manipulate various shapes, paths, and images in interactive graphics applications. By understanding the different item types and how to use QPainterPath for complex shapes, you can create sophisticated visualizations and user interfaces.

This implementation demonstrates the creation of different types of graphics items, including lines, ellipses, paths, pie shapes, star shapes, and images. The project also shows how to make items movable by using parent-child relationships, setting up a bounding rectangle as a "handle" for each shape.

These techniques can be applied to create more complex graphics applications like diagrams, charts, editors, or games.