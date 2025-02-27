# PySide6 Graphics View Event Propagation - Implementation Guide

This guide demonstrates how events propagate through the different layers of PySide6's Graphics View Framework. The project shows how keyboard and mouse events are handled at the View, Scene, and Item levels, illustrating the event propagation chain.

## Project Overview

This application demonstrates:
- How events flow through the Graphics View Framework
- Implementing event handlers at multiple levels (View, Scene, Item)
- The order of event propagation
- Proper event handling and passing to parent classes

## Project Structure

```
graphics_view_event_demo/
│
├── main.py           # Application entry point
├── widget.py         # Main widget containing the scene and view
├── view.py           # Custom view with event handling
├── scene.py          # Custom scene with event handling
├── rect.py           # Custom rectangle item with event handling
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

### Event Handling in Rect (Item Level)

The `Rect` class handles events at the item level:

```python
def keyPressEvent(self, event: QKeyEvent):
    print("Rect Item : Key press event")
    super().keyPressEvent(event)

def mousePressEvent(self, event: QGraphicsSceneMouseEvent):
    print(f"Rect Item : Mouse pressed at : {event.pos()}")
    super().mousePressEvent(event)
```

Note that items receive scene-specific mouse events (`QGraphicsSceneMouseEvent`), not the standard `QMouseEvent`.

### Event Handling in Scene

The `Scene` class handles events at the scene level:

```python
def keyPressEvent(self, event: QKeyEvent):
    print("Scene : KeypressEvent")
    super().keyPressEvent(event)

def mousePressEvent(self, event: QGraphicsSceneMouseEvent):
    print(f"Scene : MousePressEvent at : {event.scenePos()}")
    super().mousePressEvent(event)
```

### Event Handling in View

The `View` class handles events at the view level:

```python
def mousePressEvent(self, event: QMouseEvent):
    # Ensure compatibility with different PySide6 versions
    try:
        pos = event.position().toPoint()
    except AttributeError:
        pos = event.pos()
        
    print(f"View : MousePressEvent at : {pos}")
    super().mousePressEvent(event)

def keyPressEvent(self, event: QKeyEvent):
    print("View : KeyPressEvent")
    super().keyPressEvent(event)
```

Note that views receive standard `QMouseEvent` objects, which later get transformed into `QGraphicsSceneMouseEvent` objects for the scene and items.

### Setting Up the Main Widget

The main widget class connects everything together:

```python
# Create the custom graphics scene
self.scene = Scene(self)

# Create a rectangle item and add it to the scene
self.rect_item = Rect()
self.rect_item.setRect(10, 10, 200, 200)

self.scene.addItem(self.rect_item)

# Set the rectangle to be focusable and movable
self.rect_item.setFlag(QGraphicsItem.ItemIsFocusable)
self.rect_item.setFlag(QGraphicsItem.ItemIsMovable)
self.rect_item.setFocus()

# Create the custom view and set its scene
self.view = View(self)
self.view.setScene(self.scene)
```

## Key Concepts

### Event Propagation Path

In the Graphics View Framework, events typically follow this propagation path:

1. **View**: Events start at the `QGraphicsView` level
2. **Scene**: The view translates and forwards events to the `QGraphicsScene`
3. **Items**: The scene delivers events to the appropriate `QGraphicsItem`

### Different Event Types at Different Levels

Different classes in the framework receive different types of events:

- **View** receives standard Qt events (`QMouseEvent`, `QKeyEvent`)
- **Scene** receives scene-specific events (`QGraphicsSceneMouseEvent`)
- **Items** also receive scene-specific events

### Coordinate Transformations

As events move through the framework, their coordinates are transformed:

- **View coordinates**: Relative to the widget's top-left corner
- **Scene coordinates**: Relative to the scene's coordinate system
- **Item coordinates**: Relative to the item's coordinate system

### Forward vs. Backward Event Propagation

Event propagation can be:

- **Forward**: From parent to child (view → scene → item)
- **Backward**: From child to parent (item → scene → view)

Most events propagate forward, but some (like context menu events) can propagate backward if not handled.

## Event Handling Order

When clicking on an item in this application, you'll see events printed in this order:

```
View : MousePressEvent at : (X, Y)
Scene : MousePressEvent at : (X, Y)
Rect Item : Mouse pressed at : (X, Y)
```

For key presses (when the rect has focus):

```
View : KeyPressEvent
Scene : KeypressEvent
Rect Item : Key press event
```

## Best Practices

### 1. Always Call the Parent Implementation

When overriding event handlers, always call the parent class implementation to ensure proper event propagation:

```python
def mousePressEvent(self, event):
    # Handle the event
    print("Event handled")
    
    # Always call the parent implementation
    super().mousePressEvent(event)
```

### 2. Be Aware of Event Acceptance

Qt events have an "accepted" state. When an event is accepted, it typically stops propagation:

```python
def keyPressEvent(self, event):
    if event.key() == Qt.Key_Escape:
        # Handle the Escape key
        print("Escape pressed")
        event.accept()  # Mark as handled
    else:
        # Let parent handle other keys
        super().keyPressEvent(event)
```

### 3. Handle Coordinate Systems Correctly

When working with positions, be aware of which coordinate system you're in:

```python
# In a QGraphicsView mouse event handler
view_pos = event.pos()
scene_pos = self.mapToScene(view_pos)
```

### 4. Optimize for Performance

For complex scenes, avoid expensive operations in frequently called event handlers:

```python
def mouseMoveEvent(self, event):
    # Avoid expensive operations here
    super().mouseMoveEvent(event)
```

## Advanced Techniques

### Custom Event Filters

You can install event filters to intercept events before they reach their target:

```python
class MyFilter(QObject):
    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress:
            print(f"Filter caught key press: {event.key()}")
            return False  # Continue processing
        return super().eventFilter(obj, event)

# In your widget
filter = MyFilter(self)
view.installEventFilter(filter)
```

### Grabbing Mouse Input

Items can explicitly grab mouse input:

```python
def mousePressEvent(self, event):
    # Grab mouse - all further mouse events go to this item
    self.grabMouse()
    super().mousePressEvent(event)
    
def mouseReleaseEvent(self, event):
    # Release the grab
    self.ungrabMouse()
    super().mouseReleaseEvent(event)
```

### Handling Hover Events

To receive hover events, enable them for the item:

```python
rect_item.setAcceptHoverEvents(True)

# Then implement the hover handlers
def hoverEnterEvent(self, event):
    self.setBrush(QBrush(Qt.red))
    
def hoverLeaveEvent(self, event):
    self.setBrush(QBrush(Qt.green))
```

## Conclusion

The PySide6 Graphics View Framework provides a sophisticated event handling system that propagates events through multiple layers. Understanding this event flow is crucial for building interactive graphics applications.

This implementation demonstrates event handling at the View, Scene, and Item levels, showing how events propagate through the system. By observing the console output, you can see the exact path that each event takes through the framework.

These techniques can be used to build more complex interactive graphics applications where fine control over event handling is required.