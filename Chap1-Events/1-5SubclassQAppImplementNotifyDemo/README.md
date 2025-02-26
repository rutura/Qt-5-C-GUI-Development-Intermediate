# PySide6 Application Event Handling

This project demonstrates how to override the global event handling system in a PySide6 application by subclassing QApplication and implementing the `notify()` method.

## Project Overview

This application shows:
1. How to create a custom Application class by inheriting from QApplication
2. How to override the `notify()` method to intercept events at the application level
3. How to integrate a UI file created with Qt Designer with PySide6 code
4. How type checking works in Python vs. C++ (using `isinstance()` instead of `dynamic_cast`)

## Project Structure

```
project/
├── application.py   # Custom application class with notify override
├── main.py          # Application entry point
├── ui_widget.py     # Generated UI code from widget.ui
├── widget.py        # Main widget that uses the UI
└── widget.ui        # UI file created with Qt Designer
```

## Key Concepts

### Application Level Event Handling

In Qt/PySide6, the event system has a specific flow:
1. Events are first processed by `QApplication::notify()`
2. Then passed to the destination object's `event()` method
3. Finally dispatched to specific event handlers (e.g., `mousePressEvent()`)

By overriding `notify()`, we can intercept all events before they reach any objects, allowing for:
- Global event filtering
- Debugging and logging
- Custom event handling across the entire application
- Preventing specific events from reaching their targets

### UI Loading in PySide6

This project uses the recommended pattern for PySide6 UI integration:
1. Generate Python code from the .ui file using pyside6-uic
2. Import the generated Ui_Widget class
3. Create an instance of this class in our widget
4. Call setupUi() to configure the widget

### Type Checking

In Qt C++, we would use `dynamic_cast` to check if an object is of a specific type. In Python, we use the simpler `isinstance()` function, which makes the code cleaner and more readable.

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

- How the Qt/PySide6 event system works at the application level
- How to intercept events globally
- How type checking works in Python vs. C++
- How to integrate UI files with custom application logic