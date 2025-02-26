# Event Inheritance in PySide6

This project demonstrates how event handling is inherited through a widget hierarchy in PySide6. It showcases the event propagation mechanism and how to override event handlers in derived classes.

## Project Overview

This application illustrates:
1. How event handlers are inherited and called through a widget inheritance chain
2. How to override specific event handlers like `mousePressEvent` and `keyPressEvent`
3. How to control event propagation using `event.accept()` and `event.ignore()`
4. How to implement custom event handling in widget subclasses

## Project Structure

```
project/
├── parentbutton.py      # Base button class with mousePressEvent override
├── childbutton.py       # Derived button class with its own mousePressEvent
├── parentlineedit.py    # Base line edit class with keyPressEvent override
├── childlineedit.py     # Derived line edit with custom key handling
├── main.py              # Application entry point
├── ui_widget.py         # Generated UI code from widget.ui
├── widget.py            # Main widget that uses the UI
└── widget.ui            # UI file created with Qt Designer
```

## Key Concepts

### Event Inheritance Chain

When an event occurs in Qt/PySide6, it follows a specific inheritance chain:

1. The event is first delivered to the target widget
2. The widget's specific event handler (e.g., `mousePressEvent`) is called
3. If the widget is a derived class, its implementation is called first
4. The derived class typically calls the base class implementation
5. This continues up the inheritance chain until the base Qt widget is reached

This project demonstrates this chain with both buttons and line edits:
- `ChildButton` → `ParentButton` → `QPushButton`
- `ChildLineEdit` → `ParentLineEdit` → `QLineEdit`

### Event Acceptance and Propagation

The project also demonstrates how to control event propagation using:

- `event.accept()`: Marks the event as handled, preventing further processing
- `event.ignore()`: Allows the event to be processed by parent widgets

The `ChildLineEdit` shows how to implement custom behavior for specific keys (Delete)
while delegating other keys to the parent class.

## Running the Application

1. Make sure you have PySide6 installed:
   ```
   pip install PySide6
   ```

2. Generate the UI Python file (already done in this project):
   ```
   pyside6-uic widget.ui -o ui_widget.py
   ```

3. Run the application:
   ```
   python main.py
   ```

## What to Learn From This Example

- How events propagate through widget inheritance hierarchies
- How to override specific event handlers in PySide6
- How to implement custom event handling while preserving base class behavior
- How to control event propagation using acceptance/ignorance mechanisms
- Best practices for organizing widget classes in a PySide6 application