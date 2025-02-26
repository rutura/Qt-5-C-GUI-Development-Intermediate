# Water Tank Monitor in PySide6

This project demonstrates a water tank monitoring system with custom painted widgets in PySide6. It features a water tank display that communicates with a traffic light indicator to show warning states.

## Project Overview

This application illustrates several important concepts:

1. Custom painted widgets using QPainter
2. Signal and slot communication between widgets
3. Timer-based animation
4. Custom event handling (wheel events)
5. Using QT Designer-generated UI with custom widgets
6. Interactive simulation of a monitoring system

## Project Structure

```
project/
├── main.py         # Application entry point
├── indicator.py    # Traffic light indicator widget
├── watertank.py    # Water tank display widget
├── ui_widget.py    # Generated UI code from widget.ui
├── widget.py       # Main widget that connects components
└── widget.ui       # UI design file (XML)
```

## Key Concepts

### Custom Painted Widgets

Both the WaterTank and Indicator classes use custom painting to render their visuals:

```python
def paintEvent(self, event: QPaintEvent):
    """Custom paint event to draw the water tank"""
    # Set up painter and pen
    mPen = QPen()
    mPen.setColor(Qt.black)
    mPen.setWidth(3)
    
    painter = QPainter(self)
    painter.setPen(mPen)
    
    # Draw the tank walls
    painter.drawLine(10, 10, 10, 300)      # Left
    painter.drawLine(10, 300, 300, 300)    # Bottom
    painter.drawLine(300, 300, 300, 10)    # Right
    
    # Draw the water
    painter.setBrush(Qt.blue)
    painter.drawRect(10, 300 - self.waterHeight, 290, self.waterHeight)
```

### Signal and Slot Communication

The WaterTank widget emits signals based on the water level, which are connected to slots in the Indicator widget:

```python
# In watertank.py
normal = Signal()   # Green - normal water level
warning = Signal()  # Yellow - warning water level
danger = Signal()   # Red - danger water level

# In widget.py
self.ui.waterTank.normal.connect(self.ui.indicator.activateNormal)
self.ui.waterTank.warning.connect(self.ui.indicator.activateWarning)
self.ui.waterTank.danger.connect(self.ui.indicator.activateDanger)
```

### Timer-Based Animation

Both widgets use QTimer for animation:

```python
# In watertank.py (for water level simulation)
self.timer = QTimer(self)
self.timer.setInterval(1000)
self.timer.timeout.connect(self.updateWaterLevel)
self.timer.start()

# In indicator.py (for light blinking)
self.timer = QTimer(self)
self.timer.setInterval(300)
self.timer.timeout.connect(self.toggleLights)
self.timer.start()
```

### Custom Event Handling

The WaterTank widget handles wheel events to allow user interaction:

```python
def wheelEvent(self, event: QWheelEvent):
    """Handle mouse wheel events to decrease water level"""
    # Check for backward wheel movement and if water height is greater than minimum
    if event.angleDelta().y() < 0 and self.waterHeight > 10:
        self.waterHeight -= 10
        self.update()
        
        # Emit signals based on updated water level
        # ...
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
   - Watch as the water level rises and the indicator changes from green to yellow to red
   - Use the mouse wheel to lower the water level (scroll down)
   - Observe how the indicator changes based on the water level

## Widget Details

### WaterTank Widget

The WaterTank widget simulates a filling water tank:

- A timer increases the water level at regular intervals
- The water level determines which signal is emitted (normal, warning, or danger)
- The user can decrease the water level using the mouse wheel
- The tank is drawn using simple lines and rectangles with QPainter

### Indicator Widget

The Indicator widget displays a traffic light-style status indicator:

- Red light indicates danger (high water level)
- Yellow light indicates warning (moderate water level)
- Green light indicates normal status (low water level)
- The active light blinks using a timer
- The indicator responds to signals from the WaterTank

## Implementation Notes

### Size Hints

Both custom widgets implement `sizeHint()` to suggest appropriate sizes:

```python
def sizeHint(self) -> QSize:
    """Suggested size for the widget"""
    return QSize(120, 350)  # For Indicator
```

### State Management

The Indicator widget manages its state with boolean flags:

```python
def activateNormal(self):
    """Activate the green light (normal state)"""
    self.greenActive = True
    self.yellowActive = self.redActive = False
    self.update()
```

### UI Integration

The custom widgets are integrated into the UI file and loaded through the UI file generation system:

```xml
<customwidget>
  <class>WaterTank</class>
  <extends>QWidget</extends>
  <header>watertank.h</header>
  <container>1</container>
</customwidget>
```

## From C++ to PySide6

This project has been ported from Qt/C++ to PySide6. Key translations include:

1. **Signal Declaration**:
   - C++: `signals: void normal();`
   - Python: `normal = Signal()`

2. **Lambda Expressions**:
   - C++: `connect(timer, &QTimer::timeout, [=](){ toggleLights(); });`
   - Python: `self.timer.timeout.connect(self.toggleLights)`

3. **Paint Events**:
   - C++: `void paintEvent(QPaintEvent *event) override;`
   - Python: `def paintEvent(self, event: QPaintEvent):`

4. **Enum Usage**:
   - C++: `Qt::black`
   - Python: `Qt.black`

5. **Type Annotations**:
   - Python adds type hints like `event: QPaintEvent` which aren't present in C++

## Extending the Application

This application could be extended in various ways:

1. **Add Controls**: Add buttons or sliders to control the water level or simulation speed
2. **Add Logging**: Create a log panel that records state changes
3. **Add Alarms**: Play sounds when danger state is reached
4. **Multiple Tanks**: Monitor multiple tanks simultaneously
5. **Data Visualization**: Add graphs to track water level over time