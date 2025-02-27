# PySide6 Graphics View Framework - Implementation Guide

This guide demonstrates how to use PySide6's Graphics View Framework to create interactive 2D graphics applications. The project shows the basics of creating custom graphics items, handling keyboard and mouse events, and implementing a scene-view architecture.

## Project Overview

This application demonstrates:
- Creating a QGraphicsScene with coordinate axes
- Adding an interactive QGraphicsRectItem that responds to keyboard input
- Implementing a custom QGraphicsView that adds items on mouse click
- Proper event handling in a 2D graphics environment

## Project Structure

```
graphics_view_demo/
│
├── main.py           # Application entry point
├── widget.py         # Main widget containing the scene and view
├── rect.py           # Custom rectangle item with keyboard controls
├── view.py           # Custom view with mouse event handling
└── ui_widget.py      # Generated UI code from widget.ui
```

## Building and Running the Project

1. Generate UI Python files:
   ```bash
   pyside6-uic widget.ui -o ui_widget.py
   ```

2. Run the application:
   ```bash
   python main.py
   ```

## Implementation Details

### Creating a Custom Graphics Item

The `Rect` class extends `QGraphicsRectItem` to create a rectangle that can be moved with arrow keys:

```python
class Rect(QGraphicsRectItem):
    def __init__(self):
        super().__init__()

    def keyPressEvent(self, event: QKeyEvent):
        print("Keypress event triggered for rect item")
        
        if event.key() == Qt.Key.Key_Left:
            self.moveBy(-20, 0)
        
        if event.key() == Qt.Key.Key_Right:
            self.moveBy(20, 0)
        
        if event.key() == Qt.Key.Key_Up:
            self.moveBy(0, -20)
        
        if event.key() == Qt.Key.Key_Down:
            self.moveBy(0, 20)
```

To make this item receive keyboard events, we need to enable focus:

```python
rect_item.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsFocusable)
rect_item.setFocus()
```

### Creating a Custom Graphics View

The `View` class extends `QGraphicsView` to handle mouse events and create new rectangles:

```python
class View(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)

    def mousePressEvent(self, event: QMouseEvent):
        print(f"Mouse pressed in view at position (View Coord): {event.position()}")

        scene_position = self.mapToScene(event.position().toPoint())
        print(f"Mouse pressed in view at position (Scene Coord): {scene_position}")

        rect = self.scene().addRect(scene_position.x(), scene_position.y(), 50, 50)
        rect.setBrush(QBrush(Qt.blue))
```

This demonstrates the important concept of mapping from view coordinates to scene coordinates.

### Setting Up the Graphics Scene

The main widget sets up the scene with a yellow background, axes, and an initial rectangle:

```python
# Create the graphics scene
self.scene = QGraphicsScene(self)
self.scene.setBackgroundBrush(QBrush(QColor(Qt.yellow)))
self.scene.setSceneRect(-300, -300, 600, 600)

# Add coordinate axes
self.scene.addLine(-300, 0, 300, 0)  # Horizontal line
self.scene.addLine(0, -300, 0, 300)  # Vertical line
```

## Key Concepts

### Scene-View Architecture

The Graphics View Framework uses a scene-view architecture:

- **QGraphicsScene**: Manages all the graphics items, coordinates, and the scene state
- **QGraphicsView**: Provides a viewport into the scene, handles rendering and user interaction
- **QGraphicsItem**: Base class for all items that can be placed in a scene

This separation allows for multiple views of the same scene and provides a natural coordinate system.

### Coordinate Systems

The framework uses two coordinate systems:

1. **Scene Coordinates**: A logical coordinate system used by the scene and items
2. **View Coordinates**: The pixel coordinates in the viewport

When handling events, you often need to convert between these coordinate systems using methods like `mapToScene()` and `mapFromScene()`.

### Event Handling in Graphics Items

Graphics items can handle their own events by overriding methods like:

- `keyPressEvent()`: For keyboard input
- `mousePressEvent()`: For mouse clicks
- `mouseReleaseEvent()`: For when mouse buttons are released
- `mouseMoveEvent()`: For mouse movement

For an item to receive keyboard events, it must have the `ItemIsFocusable` flag set and have focus.

### Graphics Item Flags

Common flags for graphics items include:

- `ItemIsMovable`: Makes the item movable by mouse
- `ItemIsSelectable`: Makes the item selectable
- `ItemIsFocusable`: Allows the item to receive keyboard focus
- `ItemClipsToShape`: Makes the item clip to its shape
- `ItemClipsChildrenToShape`: Makes children clip to the parent's shape

Example:
```python
item.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
item.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
```

### Advanced Techniques

#### Transformation and Zoom

To implement zoom functionality in a view:

```python
def wheelEvent(self, event):
    zoom_factor = 1.15
    
    if event.angleDelta().y() > 0:
        # Zoom in
        self.scale(zoom_factor, zoom_factor)
    else:
        # Zoom out
        self.scale(1 / zoom_factor, 1 / zoom_factor)
```

#### Drag and Drop

To implement drag and drop in a custom item:

```python
def mousePressEvent(self, event):
    self.setCursor(Qt.ClosedHandCursor)
    super().mousePressEvent(event)

def mouseReleaseEvent(self, event):
    self.setCursor(Qt.OpenHandCursor)
    super().mouseReleaseEvent(event)

def mouseMoveEvent(self, event):
    super().mouseMoveEvent(event)
    # Add any custom drag behavior here
```

#### Custom Item Shapes

For complex shapes, override the `shape()` method:

```python
def shape(self):
    path = QPainterPath()
    path.addRect(self.rect())
    return path
```

#### Item Groups

You can group items together using `QGraphicsItemGroup`:

```python
group = self.scene.createItemGroup([item1, item2, item3])
# Move all items together
group.moveBy(100, 100)
# To ungroup
self.scene.destroyItemGroup(group)
```

## Best Practices

1. **Separate Item Logic from View Logic**

   Keep the item behavior (like in the `Rect` class) separate from the view behavior (like in the `View` class).

2. **Use the Scene Rect Appropriately**

   Set the scene rect to define the logical boundaries of your scene:
   
   ```python
   scene.setSceneRect(-300, -300, 600, 600)
   ```

3. **Optimize Performance for Complex Scenes**

   For scenes with many items, consider:
   - Using `QGraphicsScene.itemAt()` instead of searching all items
   - Setting the view's viewport update mode
   - Using `QGraphicsItem.cacheMode` for complex items

4. **Handle Coordinate Transformations Correctly**

   Always remember to convert between view and scene coordinates when handling events:
   
   ```python
   scene_pos = view.mapToScene(view_pos)
   view_pos = view.mapFromScene(scene_pos)
   ```

5. **Use the Painter Correctly**

   When implementing custom painting in a graphics item:
   
   ```python
   def paint(self, painter, option, widget):
       # Set rendering hints for better quality
       painter.setRenderHint(QPainter.Antialiasing)
       
       # Draw the item
       painter.setPen(self.pen)
       painter.setBrush(self.brush)
       painter.drawRect(self.rect())
   ```

## Conclusion

The PySide6 Graphics View Framework provides a powerful way to create interactive 2D graphics applications. It separates the logical scene from the views that display it, and provides a natural way to handle user interaction through events.

This implementation demonstrates the basics of creating a scene with custom items and views, handling keyboard and mouse input, and setting up a basic coordinate system. These techniques can be extended to create more complex graphics applications, such as diagramming tools, simple games, or visualization applications.