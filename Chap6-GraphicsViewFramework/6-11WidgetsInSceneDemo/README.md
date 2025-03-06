# PySide6 Graphics View with Embedded Widgets

This project demonstrates how to use the QGraphicsProxyWidget class to embed standard Qt widgets inside a QGraphicsScene. It showcases how to create interactive elements within a graphics scene that can manipulate other graphical items.

## Key Features

- Embedding a QDial widget in a QGraphicsScene using QGraphicsProxyWidget
- Interactive control of a QGraphicsRectItem's rotation using the dial
- Basic setup of a Graphics View Framework application

## Project Structure

```
graphics_proxy_widget/
│
├── main.py           # Application entry point
├── widget.py         # Main widget with scene and view setup
└── ui_widget.py      # Generated UI code from widget.ui
```

## Building and Running the Project

1. Generate the UI Python file:
   ```bash
   pyside6-uic widget.ui -o ui_widget.py
   ```

2. Run the application:
   ```bash
   python main.py
   ```

## Implementation Details

### Main Application Widget

The `Widget` class sets up the graphics scene, view, and embedded dial:

```python
def __init__(self, parent=None):
    super().__init__(parent)
    self.ui = Ui_Widget()
    self.ui.setupUi(self)
    
    # Create the graphics scene
    self.scene = QGraphicsScene(self)
    
    # Add coordinate grid lines
    self.scene.addLine(-400, 0, 400, 0, QPen(Qt.blue))
    self.scene.addLine(0, -400, 0, 400, QPen(Qt.blue))
    self.scene.setSceneRect(-800, -400, 1600, 800)
    
    # Add rectangle item
    self.rect = self.scene.addRect(-200, -100, 200, 70)
    self.rect.setBrush(QBrush(Qt.red))
    
    # Create a dial widget
    self.dial = QDial()
    self.dial.setMinimum(0)
    self.dial.setMaximum(360)
```

### Embedding a Widget in the Scene

The key aspect of this project is using QGraphicsProxyWidget to embed a standard Qt widget (QDial) in the graphics scene:

```python
# Create a proxy widget to embed the dial in the scene
proxy_widget = QGraphicsProxyWidget()
proxy_widget.setWidget(self.dial)
proxy_widget.setPos(100, -300)

# Add the proxy widget to the scene
self.scene.addItem(proxy_widget)
```

### Connecting Widget Signals to Scene Items

The dial's value changes are connected to control the rectangle's rotation:

```python
# Connect dial's value changes to rectangle rotation
self.dial.valueChanged.connect(self.on_dial_value_changed)

def on_dial_value_changed(self, value):
    """
    Handle dial value changes by rotating the rectangle.
    
    Args:
        value: The new value of the dial
    """
    print(f"Dial value changed to: {value}")
    self.rect.setRotation(value)
```

## Key Concepts

### QGraphicsProxyWidget

QGraphicsProxyWidget is a bridge between the widget system and the graphics view framework. It allows you to embed any QWidget subclass into a QGraphicsScene.

Key features of QGraphicsProxyWidget:
- It automatically forwards events to the embedded widget
- It adjusts its size to match the embedded widget
- It supports all standard widget features (input focus, tab focus, etc.)

### Item Transformation

In this example, we demonstrate how to rotate a graphics item:

```python
self.rect.setRotation(value)
```

QGraphicsItem supports various transformations:
- Rotation (setRotation)
- Scaling (setScale)
- Translation (setPos)
- Custom transformations (setTransform)

### Event Propagation

Events flow from the QGraphicsView to the QGraphicsScene to the QGraphicsItems within the scene. When using QGraphicsProxyWidget, events are further propagated to the embedded widget when appropriate.

## Extending the Project

Here are some ways you could extend this project:

1. **Add More Controls**
   - Add sliders to control the rectangle's position or scale
   - Add color pickers to change the rectangle's color

2. **Multiple Proxy Widgets**
   - Add several widgets to control different aspects of the scene
   - Create a control panel with multiple widgets

3. **Complex Interactions**
   - Implement drag-and-drop between widgets and graphics items
   - Allow graphics items to be selected and modified by the widgets

4. **Animation**
   - Use a QTimeLine or QPropertyAnimation to animate graphics items
   - Control animation parameters with embedded widgets

## Best Practices

1. **Memory Management**

   In Qt/PySide6, when a QGraphicsScene is destroyed, it automatically destroys all of its items, including proxy widgets and their embedded widgets. However, when replacing a widget in a proxy or removing a proxy from a scene, you should handle memory management carefully:
   
   ```python
   # Removing a proxy widget from the scene
   self.scene.removeItem(proxy_widget)
   
   # If necessary, explicitly delete the widget
   self.dial.deleteLater()
   ```

2. **Widget Interaction**

   Remember that embedded widgets receive events through the proxy. If you need to directly interact with the widget from your code, you can access it via:
   
   ```python
   widget = proxy_widget.widget()
   ```

3. **Coordinate Systems**

   Be aware of the different coordinate systems:
   - Scene coordinates (logical coordinates in the graphics scene)
   - View coordinates (coordinates in the viewport widget)
   - Item coordinates (local coordinates relative to each graphics item)
   
   The proxy widget's position is in scene coordinates.

## Conclusion

QGraphicsProxyWidget provides a powerful way to combine the flexibility of the Graphics View Framework with the rich set of standard Qt widgets. This integration allows you to create more interactive and dynamic graphics applications with familiar UI controls.

This project demonstrates a simple use case, but the technique can be extended to create complex graphical editors, interactive diagrams, or custom visualization tools with embedded controls.