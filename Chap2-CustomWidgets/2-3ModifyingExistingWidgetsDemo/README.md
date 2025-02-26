# Date and Time Widget in PySide6

This project demonstrates how to create a custom widget that displays the current date and time with automatic updates using PySide6.

## Project Overview

This application illustrates:
1. Creating a custom widget from scratch
2. Working with QDate and QTime classes
3. Using QTimer for periodic updates
4. Styling widgets with CSS-like stylesheets
5. Layout management with QVBoxLayout

## Project Structure

```
project/
├── main.py           # Application entry point
├── datetimewidget.py # Custom date and time display widget
├── ui_widget.py      # Generated UI code from widget.ui
├── widget.py         # Main window that hosts the datetime widget
└── widget.ui         # UI design file (XML)
```

## Key Concepts

### Custom Widget Creation

The `DateTimeWidget` is a custom widget that displays the current date and time:

```python
class DateTimeWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Create layout
        layout = QVBoxLayout(self)
        
        # Set font and size policy
        mFont = QFont("Consolas", 20, QFont.Bold)
        policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        
        # Initialize date and time labels
        # ...
```

### Working with Date and Time

The widget uses Qt's date and time classes:

```python
# Get current date as formatted string
self.dateString = QDate.currentDate().toString(Qt.TextDate)

# Get current time as string
self.timeString = QTime.currentTime().toString()
```

### Timer for Periodic Updates

The widget uses a QTimer to update the time display every second:

```python
# Set up timer
self.timer = QTimer(self)
self.timer.setInterval(1000)  # Update every second
self.timer.timeout.connect(self.updateTime)
self.timer.start()
```

### Time Update Logic

The `updateTime` method updates the time and, when necessary, the date:

```python
@Slot()
def updateTime(self):
    """Update the time display, and date if it has changed"""
    # Update time
    self.timeString = QTime.currentTime().toString()
    self.labelBottom.setText(self.timeString)
    
    # Check if date has changed
    current_date = QDate.currentDate().toString(Qt.TextDate)
    if self.dateString != current_date:
        self.dateString = current_date
        self.labelTop.setText(self.dateString)
```

### Widget Styling

The time display is styled using Qt stylesheets:

```python
# Set style for time label
css = "background-color: #00eff9; color: #fffff1"
self.labelBottom.setStyleSheet(css)
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

## Implementation Notes

### Font Configuration

The widget uses a monospaced font (Consolas) to ensure consistent display of the time:

```python
mFont = QFont("Consolas", 20, QFont.Bold)
```

### Size Policy

Size policies are used to control how the widget resizes:

```python
policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
```

This allows the widget to expand horizontally but stay at a fixed height.

### Text Alignment

The labels are centered to create a more visually appealing display:

```python
self.labelTop.setAlignment(Qt.AlignCenter)
```

### Widget Composition

The main widget loads a UI file and then adds the custom widget to it:

```python
# Create the datetime widget
self.datetimeWidget = DateTimeWidget(self)

# Add it to the layout from the UI file
self.ui.verticalLayout.addWidget(self.datetimeWidget)
```

## Exercise

1. **Customizable Format**: Add options to customize the date and time formats.

   ```python
   def setDateFormat(self, format):
       self.dateFormat = format
       self.dateString = QDate.currentDate().toString(self.dateFormat)
       self.labelTop.setText(self.dateString)
   
   def setTimeFormat(self, format):
       self.timeFormat = format
       self.timeString = QTime.currentTime().toString(self.timeFormat)
       self.labelBottom.setText(self.timeString)
   ```

2. **Timezone Support**: Add the ability to display time in different timezones.

3. **Theme Support**: Allow for different color themes or styles.

4. **Countdown/Stopwatch**: Extend the widget to include countdown or stopwatch functionality.
