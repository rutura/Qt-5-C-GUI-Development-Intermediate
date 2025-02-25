# Sending Synthetic Events in PySide6

This project demonstrates how to programmatically create and send synthetic mouse events to widgets in a PySide6 application.

## Project Overview

This application illustrates:
1. How to create custom mouse events programmatically
2. How to send events to widgets using `QApplication.postEvent()` and `QApplication.sendEvent()`
3. How to handle mouse events in a custom button class
4. The difference between synchronous and asynchronous event delivery

## Project Structure

```
project/
├── button.py       # Custom button with mouse event handlers
├── main.py         # Application entry point
├── ui_widget.py    # Generated UI code from widget.ui
└── widget.py       # Main widget that creates synthetic events
```

## Key Concepts

### Creating Synthetic Events

The application demonstrates how to create synthetic mouse events:

```python
mouse_event = QMouseEvent(
    QEvent.MouseButtonPress,  # Type
    QPointF(10, 10),          # Local position
    QPointF(10, 10),          # Screen position 
    Qt.LeftButton,            # Button
    Qt.LeftButton,            # Buttons
    Qt.NoModifier             # Modifiers
)
```

### Event Delivery Methods

There are two ways to deliver events to widgets:

1. **Synchronous Delivery (sendEvent)**
   ```python
   if QApplication.sendEvent(widget, event):
       print("Event accepted")
   else:
       print("Event not accepted")
   ```
   - Processes the event immediately
   - Returns whether the event was accepted
   - Runs in the current thread

2. **Asynchronous Delivery (postEvent)**
   ```python
   QApplication.postEvent(widget, event)
   ```
   - Queues the event for later processing
   - Returns immediately without waiting
   - Safer for cross-thread event delivery

### Custom Event Handling

The `Button` class demonstrates how to handle mouse events:

```python
def mousePressEvent(self, event: QMouseEvent):
    print(f"Button: Mouse press at {event.pos()}")
    super().mousePressEvent(event)
```

## Running the Application

1. Ensure PySide6 is installed:
   ```
   pip install PySide6
   ```

2. Run the application:
   ```
   python main.py
   ```

3. Interact with the application:
   - Click "Button2" to send a synthetic mouse press event to the custom button
   - Observe the console output showing the event was received and handled

## Use Cases for Synthetic Events

Synthetic events are useful for:
- Automated testing of UI components
- Simulating user interaction programmatically
- Creating custom interactions between widgets
- Implementing macros or recorded actions
- Forwarding events between different parts of an application

## Implementation Notes

- The example uses `postEvent` by default, which is generally safer
- For immediate processing, uncomment the `sendEvent` code
- The custom button logs all mouse events to show which ones are triggered
- Event creation requires careful attention to parameter types and values