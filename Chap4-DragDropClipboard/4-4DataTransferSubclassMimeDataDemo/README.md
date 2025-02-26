# Custom MIME Data Drag and Drop Demo in PySide6

This project demonstrates how to implement advanced drag and drop functionality in PySide6 using a custom QMimeData subclass to provide enhanced data transfer capabilities.

## Project Overview

This application illustrates:
1. Creating a custom `QMimeData` subclass to store complex data
2. Implementing drag and drop with direct object references
3. Visual feedback during drag operations using semi-transparent overlays
4. Dragging and dropping between multiple container widgets
5. Distinguishing between move and copy operations
6. Providing additional data formats (HTML and plain text)

## Project Structure

```
project/
├── main.py            # Application entry point
├── widget.py          # Main application widget
├── container.py       # Custom container with drag and drop
├── pixmapmime.py      # Custom QMimeData subclass
├── ui_widget.py       # Generated UI code from widget.ui
├── resources.qrc      # Resource file for images
├── resource_rc.py     # Generated resource code
└── images/            # Directory for icon images
   ├── qt.png
   ├── cpp.png
   └── terminal.png
```

## Key Components

### Custom QMimeData Subclass

The `PixmapMime` class extends QMimeData to directly store a pixmap and offset information:

```python
class PixmapMime(QMimeData):
    def __init__(self, pix, offset, description):
        super().__init__()
        self.mPix = pix
        self.mOffset = offset
        self.description = description
        self.mimeFormats = ["text/html", "text/plain"]
    
    def pix(self):
        """Get the stored pixmap"""
        return self.mPix
    
    def offset(self):
        """Get the stored offset point"""
        return self.mOffset
    
    # Other methods for MIME data handling
```

This approach allows direct access to custom data without serialization/deserialization.

### Container Widget

The `Container` class implements the drag and drop functionality:

```python
def mouseMoveEvent(self, event: QMouseEvent):
    if event.buttons() & Qt.LeftButton:
        # Calculate distance moved
        distance = (event.position().toPoint() - self.startPos).manhattanLength()
        
        if distance >= QApplication.startDragDistance():
            # Start drag with custom MIME data
            child = self.childAt(event.position().toPoint())
            pixmap = child.pixmap()
            offset = event.position().toPoint() - child.pos()
            
            # Create custom mime data
            mime_data = PixmapMime(pixmap, offset, "Item icon")
            
            # Configure and execute the drag operation
            # ...
```

### Visual Feedback

The application provides visual feedback during drag operations:

```python
# Apply blur effect to original label during drag
temp_pixmap = QPixmap(pixmap)
painter = QPainter(temp_pixmap)
painter.fillRect(temp_pixmap.rect(), QColor(127, 127, 127, 127))
painter.end()
child.setPixmap(temp_pixmap)

# Execute drag operation
if drag.exec(Qt.MoveAction | Qt.CopyAction, Qt.CopyAction) == Qt.MoveAction:
    # Move operation - close the original widget
    child.close()
else:
    # Copy operation - restore the original pixmap
    child.setPixmap(pixmap)
```

### Type Checking

The application uses Python's `isinstance()` function to check the MIME data type:

```python
def dragEnterEvent(self, event: QDragEnterEvent):
    mime_data = event.mimeData()
    if isinstance(mime_data, PixmapMime):
        # Accept the drag operation
        # ...
    else:
        event.ignore()
```

## Multiple Data Formats

The custom MIME data provides data in multiple formats:

```python
def retrieveData(self, mimetype, preferredType):
    if mimetype == "text/plain":
        return self.description
    elif mimetype == "text/html":
        html_string = "<html><p>" + self.description + "</p></html>"
        return html_string
    else:
        return super().retrieveData(mimetype, preferredType)
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

## Using the Application

1. Run the application to see two container widgets side by side
2. Each container has three icons (Qt, C++, and Terminal)
3. Drag an icon within its container to move it
4. Drag an icon to the other container to copy it
5. Notice the semi-transparent effect applied to the original icon during dragging

## Implementation Notes

### Subclassing QMimeData

The key advantage of subclassing QMimeData is direct data access:

```python
# In dropEvent
mime_data = event.mimeData()
if isinstance(mime_data, PixmapMime):
    pixmap = mime_data.pix()  # Direct access to the pixmap
    offset = mime_data.offset()  # Direct access to the offset
    # ...
```

This approach:
- Avoids serialization/deserialization overhead
- Provides type-safe data access
- Allows for custom methods and properties

### Runtime Type Checking

In PySide6, we use Python's `isinstance()` function to check types:

```python
if isinstance(mime_data, PixmapMime):
    # It's our custom MIME data
```

This replaces the C++ `qobject_cast` used in the original code.

### Multiple MIME Types

The custom QMimeData subclass provides data in multiple formats:

1. Direct access to pixmap and offset via custom methods
2. Plain text description via "text/plain" MIME type
3. HTML formatted description via "text/html" MIME type

This demonstrates how to make drag and drop data compatible with different targets.

## Extending the Project

This project could be extended with:

1. **Additional Data Types**: Include more complex data structures in the custom MIME data
2. **Custom Rendering**: Implement custom rendering during drag operations
3. **Filtering**: Add criteria to control which targets accept drops
4. **Undo/Redo Support**: Track drag and drop operations for undo/redo functionality
5. **External Drop Support**: Enable dropping data from external applications