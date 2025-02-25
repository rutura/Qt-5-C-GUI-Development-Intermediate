# Widget-Specific Event Filtering in PySide6

This project demonstrates how to create and apply an event filter to a specific widget in a PySide6 application. It shows how to filter out numeric key inputs from a QLineEdit.

## Project Overview

This application illustrates:
1. How to create a keyboard event filter that blocks numeric input
2. How to apply an event filter to a specific widget (not application-wide)
3. How to dynamically remove an event filter at runtime

## Project Structure

```
project/
├── keyboardfilter.py  # Event filter implementation for keyboard events
├── main.py            # Application entry point
├── ui_widget.py       # Generated UI code from widget.ui
└── widget.py          # Main widget that sets up the filter
```

## Key Concepts

### Widget-Specific Event Filtering

Unlike application-wide event filters, widget-specific filters only intercept events for the widgets they're installed on. This project demonstrates:

1. **Creating an Event Filter**
   - Create a class inheriting from QObject
   - Override the eventFilter method
   - Check for specific event types (QEvent.KeyPress)
   - Return True to block the event, False to let it pass

2. **Installing on a Widget**
   - Call `widget.installEventFilter(filter)` to apply the filter
   - Call `widget.removeEventFilter(filter)` to remove it

3. **Dynamic Filter Management**
   - The "Remove Filter" button demonstrates removing a filter at runtime
   - This allows toggling filtering behavior on and off

## How It Works

In this application:
1. A KeyboardFilter is created that checks for numeric key presses
2. The filter is installed on a QLineEdit
3. When you type in the line edit:
   - Non-numeric keys pass through normally
   - Numeric keys (0-9) are blocked and never reach the line edit
4. Clicking the "Remove Filter" button removes the filter
5. After removal, all keys (including numbers) work normally

## Running the Application

1. Ensure PySide6 is installed:
   ```
   pip install PySide6
   ```

2. Run the application:
   ```
   python main.py
   ```

3. Try typing in the line edit:
   - Notice that numbers (0-9) don't appear
   - Letters and symbols work normally
   - Click "Remove Filter" and numbers will now work

## Use Cases for Widget-Specific Filters

Widget-specific event filters are useful for:
- Implementing custom input validation
- Adding custom behavior to standard widgets
- Blocking certain types of input
- Intercepting events before widgets process them
- Adding behaviors to widgets without subclassing

## Implementation Notes

In the Python implementation:

1. **No Type Casting Needed**
   - Unlike C++, Python doesn't require static_cast to convert the event
   - We can directly use the event object's methods

2. **String Membership Testing**
   - Instead of using indexOf, we use Python's `in` operator for more readable code

3. **Event Propagation**
   - As in C++, returning True stops event propagation
   - Returning False lets the event continue to its destination