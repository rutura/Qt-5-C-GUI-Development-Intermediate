# Event Handling in PySide6

This project demonstrates various event handling mechanisms in a PySide6 widget. It showcases how to override different event handlers to respond to user interactions and system events.

## Project Overview

This application illustrates:
1. How to override mouse event handlers (press, release, move)
2. How to handle keyboard input with modifier detection
3. How to create context menus
4. How to handle widget lifecycle events (resize, paint, close)
5. How to detect mouse enter/leave events
6. How to process wheel events for scrolling

## Project Structure

```
project/
├── main.py          # Application entry point
├── ui_widget.py     # Generated UI code from widget.ui
└── widget.py        # Widget class with event handler overrides
```

## Key Event Handling Concepts

### Mouse Events
The widget overrides three primary mouse event handlers:
- `mousePressEvent`: Called when mouse button is pressed
- `mouseReleaseEvent`: Called when mouse button is released
- `mouseMoveEvent`: Called when mouse is moved within the widget

### Keyboard Events
The `keyPressEvent` handler demonstrates:
- How to detect modifier keys (Ctrl, Alt, Shift)
- How to detect specific key combinations (Shift+A)

### Context Menu
The `contextMenuEvent` handler shows:
- How to create a custom context menu
- How to position it at the click location
- How to retrieve event coordinates and context

### Widget Lifecycle
The widget implements handlers for:
- `resizeEvent`: Called when widget is resized
- `paintEvent`: Called when widget needs repainting
- `closeEvent`: Called when widget is closed

### Mouse Enter/Leave
The widget tracks mouse entry and exit with:
- `enterEvent`: Called when mouse enters widget
- `leaveEvent`: Called when mouse leaves widget

### Wheel Events
The `wheelEvent` handler demonstrates:
- How to retrieve scroll delta
- How to get pixel and angle delta information
- How to get the wheel event position

## Running the Application

1. Ensure PySide6 is installed:
   ```
   pip install PySide6
   ```

2. Run the application:
   ```
   python main.py
   ```

3. Interact with the widget to see different events triggered:
   - Move the mouse around the widget
   - Click and release the mouse button
   - Press keyboard keys with modifiers
   - Right-click to invoke context menu
   - Resize the window
   - Use the mouse wheel
   - Move mouse in and out of the widget

## Event Handling Best Practices

1. **Always Call Base Class Implementation**  
   For events where you want default behavior to continue.

2. **Use Event Accept/Ignore**  
   When you want to control event propagation.

3. **Keep Event Handlers Focused**  
   Each handler should only handle its specific event type.

4. **Use Qt's Signal-Slot Mechanism**  
   For higher-level event handling in complex applications.

5. **Be Mindful of Performance**  
   Events like mouseMoveEvent can fire frequently, so keep handlers efficient.