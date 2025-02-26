# Double-Clickable Button in PySide6

This project demonstrates how to create a custom button in PySide6 that can detect and respond to double-click events.

## Project Overview

This application illustrates:
1. How to extend a standard widget (QPushButton) with custom behavior
2. Creating and emitting custom signals
3. Implementing custom event handlers
4. Connecting custom signals to slots

## Project Structure

```
project/
├── main.py                  # Application entry point
├── doubleclickablebutton.py # Custom button with double-click support
├── ui_widget.py             # Generated UI code from widget.ui
├── widget.py                # Main widget that uses the custom button
└── widget.ui                # UI design file (XML)
```

## Key Concepts

### Extending Standard Widgets

The `DoubleClickableButton` class demonstrates how to extend a standard QPushButton:

```python
class DoubleClickableButton(QPushButton):
    # Define the custom signal
    doubleClicked = Signal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
```

By inheriting from QPushButton, we get all the standard button functionality while being able to add our own behavior.

### Custom Signal Creation

The button defines a custom signal for double-click events:

```python
# Define the custom signal
doubleClicked = Signal()
```

This signal can be connected to any slot, just like built-in Qt signals.

### Overriding Event Handlers

The key to detecting double-clicks is overriding the `mouseDoubleClickEvent` method:

```python
def mouseDoubleClickEvent(self, event: QMouseEvent):
    """Handle mouse double click events"""
    # Emit our custom signal
    self.doubleClicked.emit()
    # Call the parent class implementation
    super().mouseDoubleClickEvent(event)
```

This allows us to:
1. Emit our custom signal when a double-click occurs
2. Call the parent class implementation to maintain default behavior

### Signal and Slot Connection

In the main widget, we connect the custom signal to a slot:

```python
# Connect the doubleClicked signal to our slot
self.button.doubleClicked.connect(self.onButtonDoubleClicked)

def onButtonDoubleClicked(self):
    """Handle double click on the button"""
    print("Button double clicked")
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

4. Interaction:
   - Double-click on the button
   - Observe the "Button double clicked" message in the console

## Implementation Notes

### Event Handling Chain

When overriding event handlers, it's important to call the parent class implementation:

```python
super().mouseDoubleClickEvent(event)
```

This ensures that the standard Qt event processing chain continues, maintaining expected widget behavior.

### Signal Declaration

In PySide6, signals are class attributes:

```python
doubleClicked = Signal()
```

This differs from C++ Qt, where signals are declared in a special section of the class.

### Widget Positioning

Since we're not using layouts in this simple example, we position the button explicitly:

```python
self.button.setGeometry(100, 100, 200, 50)  # Position the button
```

In a more complex application, you would typically use layouts for better responsiveness.

## Extended Applications

This pattern of extending standard widgets and adding custom events is widely applicable:

1. **Custom List Items**: Add special behaviors to list widget items
2. **Special Input Widgets**: Create text fields with validation or auto-completion
3. **Interactive Graphics Items**: Add custom interactions to graphics view items
4. **Specialized Controls**: Create domain-specific controls for your application
