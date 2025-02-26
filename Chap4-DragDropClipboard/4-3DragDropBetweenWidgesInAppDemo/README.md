# Custom Drag and Drop Demo in PySide6

This project demonstrates how to implement advanced drag and drop functionality in PySide6, including custom data serialization and inter-widget drag and drop operations.

## Project Overview

This application illustrates:
1. Creating custom drag and drop operations between container widgets
2. Serializing and deserializing custom data during drag and drop
3. Moving vs. copying items during drag operations
4. Using QDataStream for binary data serialization
5. Creating and managing dynamic widgets
6. Using Qt's resource system for loading images

## Project Structure

```
project/
├── main.py            # Application entry point
├── widget.py          # Main application widget
├── container.py       # Custom container with drag and drop
├── ui_widget.py       # Generated UI code from widget.ui
├── resources.qrc      # Resource file for images
├── resource_rc.py     # Generated resource code
└── images/            # Directory for icon images
   ├── qt.png
   ├── cpp.png
   └── terminal.png
```

## Key Components

### Container Widget

The `Container` class is a custom widget that implements drag and drop functionality:

```python
class Container(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(150, 150)
        self.setAcceptDrops(True)  # Enable drop acceptance
        self.startPos = QPoint()
        
        # Create initial icon labels
        # ...
```

### Drag Operations

The drag operation is implemented in the `mouseMoveEvent` method:

```python
def mouseMoveEvent(self, event: QMouseEvent):
    if event.buttons() & Qt.LeftButton:
        # Calculate distance moved
        distance = (event.position().toPoint() - self.startPos).manhattanLength()
        
        # Start drag if distance exceeds threshold
        if distance >= QApplication.startDragDistance():
            # Get child widget at position
            child = self.childAt(event.position().toPoint())
            
            # Serialize the drag data
            ba = QByteArray()
            data_stream = QDataStream(ba, QIODevice.WriteOnly)
            data_stream.writeQPixmap(pixmap)
            data_stream.writeQPoint(offset)
            
            # Create and execute drag operation
            # ...
```

### Data Serialization

The application serializes the dragged item's pixmap and position offset:

```python
# Serialization
ba = QByteArray()
data_stream = QDataStream(ba, QIODevice.WriteOnly)
data_stream.writeQPixmap(pixmap)
data_stream.writeQPoint(offset)

# Deserialization
ba = event.mimeData().data("application/x-qtcustomitem")
data_stream = QDataStream(ba, QIODevice.ReadOnly)
pixmap = QPixmap()
data_stream.readQPixmap(pixmap)
offset = QPoint()
data_stream.readQPoint(offset)
```

### Drop Handling

The application handles drops by creating new widgets with the deserialized data:

```python
def dropEvent(self, event: QDropEvent):
    if event.mimeData().hasFormat("application/x-qtcustomitem"):
        # Deserialize data
        # ...
        
        # Create new label with the deserialized pixmap
        new_label = QLabel(self)
        new_label.setPixmap(pixmap)
        new_label.move(event.position().toPoint() - offset)
        new_label.show()
        new_label.setAttribute(Qt.WA_DeleteOnClose)
        
        # Set drop action
        if event.source() == self:
            event.setDropAction(Qt.MoveAction)
            event.accept()
        else:
            event.acceptProposedAction()
```

## Resource System

The application uses Qt's resource system to load images:

```python
# In resources.qrc
<RCC>
    <qresource prefix="/">
        <file>images/qt.png</file>
        <file>images/cpp.png</file>
        <file>images/terminal.png</file>
    </qresource>
</RCC>

# In Python code
import resource_rc  # Import the compiled resource file
qtIcon.setPixmap(QPixmap(":/images/qt.png"))  # Use resource path
```

## Custom MIME Type

The application uses a custom MIME type to identify its drag and drop data:

```python
mime_data.setData("application/x-qtcustomitem", ba)
```

## Move vs. Copy Operations

The application supports both move and copy operations:

```python
if drag.exec(Qt.MoveAction | Qt.CopyAction, Qt.CopyAction) == Qt.MoveAction:
    # Move operation - close the original child widget
    child.close()
else:
    # Copy operation - keep the original
    pass
```

## Running the Application

1. Generate the resource Python file:
   ```
   pyside6-rcc resources.qrc -o resource_rc.py
   ```

2. Generate the UI Python file (if widget.ui changes):
   ```
   pyside6-uic widget.ui -o ui_widget.py
   ```

3. Ensure PySide6 is installed:
   ```
   pip install PySide6
   ```

4. Run the application:
   ```
   python main.py
   ```

## Troubleshooting Resources

If the icons don't appear:

1. Make sure the resource_rc.py file is generated correctly from the .qrc file
2. Verify that resource_rc.py is imported in both container.py and main.py
3. Check that the image paths in the .qrc file point to existing image files
4. Ensure the resource paths in the code match those in the .qrc file

## Using the Application

1. Run the application to see two container widgets side by side
2. Each container has multiple colored icons
3. Drag an icon within its container to move it
4. Drag an icon to the other container to copy it
5. Notice how the icon follows the mouse cursor during drag

## Implementation Notes

### QDataStream Version Compatibility

When using QDataStream for serialization, it's important to be aware of version compatibility:

```python
# For complete compatibility, you could set the version:
data_stream.setVersion(QDataStream.Qt_6_0)
```

### Event Acceptance

Proper event acceptance is crucial for drag and drop operations:

```python
def dragEnterEvent(self, event: QDragEnterEvent):
    if event.mimeData().hasFormat("application/x-qtcustomitem"):
        if event.source() == self:
            event.setDropAction(Qt.MoveAction)
            event.accept()
        else:
            event.acceptProposedAction()
    else:
        event.ignore()
```

### Widget Management

The application uses the `WA_DeleteOnClose` attribute to automatically manage memory:

```python
new_label.setAttribute(Qt.WA_DeleteOnClose)
```

## Extending the Project

This project could be extended with:

1. **Custom Icons**: Add more icon types and behaviors
2. **Drag Feedback**: Enhanced visual feedback during drag operations
3. **Layout Management**: Snap-to-grid or automatic layout of dropped items
4. **Edit Capabilities**: Add the ability to edit or customize dropped items
5. **Persistence**: Save and restore the state of the containers