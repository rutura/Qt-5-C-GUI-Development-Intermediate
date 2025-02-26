# Custom Button Event Handling in PySide6

This project demonstrates how to create a custom button class that overrides the default event handling in a PySide6 application.

## Project Overview

This application shows:
1. How to create a custom button class by inheriting from QPushButton
2. How to override the `event()` method to intercept events before they're processed by default handlers
3. How to integrate a UI file created with Qt Designer with PySide6 code
4. How to programmatically add widgets to layouts defined in the UI file

## Project Structure

```
project/
├── button.py        # Custom button class with event override
├── main.py          # Application entry point
├── ui_widget.py     # Generated UI code from widget.ui
├── widget.py        # Main widget that uses the UI
└── widget.ui        # UI file created with Qt Designer
```

## Key Concepts

### Event Handling

In Qt/PySide6, the event system has several layers:

1. **QApplication::notify()** - First chance to handle events at the application level
2. **QObject::event()** - Object-specific event handler (what we override in this example)
3. **Specific event handlers** - Like mousePressEvent(), keyPressEvent(), etc.

By overriding `event()`, we can intercept events before they get dispatched to specific handlers.

### UI Loading

This project uses the recommended pattern for PySide6 UI integration:

1. Generate Python code from the .ui file using pyside6-uic
2. Import the generated Ui_Widget class
3. Create an instance of this class in our widget
4. Call setupUi() to configure the widget

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

- How to intercept and handle events in PySide6
- How to create custom widget classes
- How to properly integrate UI files with your code
- How to connect signals to slots
- How to programmatically add widgets to layouts