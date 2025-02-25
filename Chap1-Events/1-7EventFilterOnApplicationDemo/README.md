# Event Filtering in PySide6

This project demonstrates how to use event filters in PySide6 to intercept events before they reach their intended target.

## Project Overview

This application illustrates:
1. How to create an event filter by subclassing QObject and overriding eventFilter()
2. How to install an event filter at the application level
3. How events can be intercepted and optionally blocked from reaching their targets
4. The event processing pipeline in Qt/PySide6

## Project Structure

```
project/
├── filter.py       # Event filter implementation
├── main.py         # Application entry point
├── ui_widget.py    # Generated UI code from widget.ui
└── widget.py       # Widget with a button
```

## Event Filtering Explained

Event filtering is a powerful mechanism in Qt/PySide6 that allows an object to intercept events destined for other objects. Key concepts:

1. **Event Filter Creation**
   - Subclass QObject
   - Override eventFilter(watched, event)
   - Return True to stop event propagation, False to allow it to continue

2. **Event Filter Installation**
   - Object-specific: `object.installEventFilter(filter)`
   - Application-wide: `app.installEventFilter(filter)`

3. **Event Processing Pipeline**
   - Application receives event
   - App-level event filters process events (in order of installation)
   - If not filtered, QApplication::notify() delivers to target object
   - Object-level event filters process events
   - If not filtered, the object's event() method processes the event

## Use Cases for Event Filters

Event filters are useful for:
- Adding behaviors to existing widgets without subclassing
- Debugging events (logging)
- Implementing global shortcut handlers
- Intercepting events across multiple widgets
- Creating custom input behavior without modifying widget classes

## Running the Application

1. Ensure PySide6 is installed:
   ```
   pip install PySide6
   ```

2. Run the application:
   ```
   python main.py
   ```

3. Interact with the application and observe:
   - Mouse clicks are detected by the event filter
   - "Event hijacked in filter" message appears in the console
   - The button still receives clicks because the filter returns False
   - If you change the filter to return True, the button won't respond to clicks

## How This Example Works

1. The application creates a Filter object
2. The filter is installed on the QApplication using installEventFilter()
3. When you click on the button:
   - The filter's eventFilter method is called first
   - It detects mouse press events and prints a message
   - It returns False, allowing the event to continue
   - The button receives the click and triggers its clicked signal
   - The Widget's on_pushButton_clicked slot is called

If you change the filter to return True for mouse events, the button will no longer respond to clicks because the events are consumed by the filter.