# Image Viewer with Drag and Drop in PySide6

This is a simple image viewer application built with PySide6 that allows users to drag and drop image files onto the application window to view them.

## Project Overview

This application demonstrates:
1. Implementing drag and drop functionality in a Qt application
2. Handling image files dropped onto a widget
3. Displaying and scaling images to fit a QLabel
4. Validating file types

## Project Structure

```
project/
├── main.py         # Application entry point
├── widget.py       # Main application widget
├── ui_widget.py    # Generated UI code from widget.ui
└── widget.ui       # UI design file
```

## Key Components

### Widget Class

The `Widget` class is the main application window that handles drag and drop operations:

```python
class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.setAcceptDrops(True)  # Enable drag and drop
```

### Drag and Drop Events

The application implements four key event handlers for drag and drop:

1. **dragEnterEvent**: Called when a drag operation enters the widget
2. **dragMoveEvent**: Called when a drag operation moves within the widget
3. **dragLeaveEvent**: Called when a drag operation leaves the widget
4. **dropEvent**: Called when the content is dropped onto the widget

```python
def dropEvent(self, event: QDropEvent):
    """Handle drop events, loading image files"""
    if event.mimeData().hasUrls():
        urls = event.mimeData().urls()
        if len(urls) > 1:
            return
        
        file_path = urls[0].toLocalFile()
        if self.isImage(file_path):
            pixmap = QPixmap()
            if pixmap.load(file_path):
                # Scale the pixmap to fit the label
                self.ui.label.setPixmap(pixmap.scaled(
                    self.ui.label.size(), 
                    Qt.AspectRatioMode.KeepAspectRatio, 
                    Qt.TransformationMode.SmoothTransformation
                ))
```

### Image Handling

The application checks if the dropped file is a supported image format:

```python
def isImage(self, file_path):
    """Check if the file is a supported image format"""
    _, ext = os.path.splitext(file_path)
    ext = ext.lower()
    return ext in [".png", ".jpg", ".jpeg"]
```

## Responsive Image Scaling

The application scales images to fit the widget while preserving their aspect ratio:

```python
def resizeEvent(self, event):
    """Handle resize events to scale the image"""
    if self.ui.label.pixmap():
        # Get the original pixmap stored as a property
        original_pixmap = getattr(self, '_original_pixmap', None)
        if original_pixmap:
            # Scale the original pixmap to the new size
            self.ui.label.setPixmap(original_pixmap.scaled(
                self.ui.label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            ))
    super().resizeEvent(event)
```

## Enabling Drag and Drop

To enable drag and drop in a Qt application, two key steps are needed:

1. Call `setAcceptDrops(True)` on the widget
2. Implement the necessary event handlers

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

4. Use the application:
   - Drag and drop an image file (PNG, JPG, JPEG) onto the application window
   - The image will be displayed and scaled to fit the window
   - Resize the window to see the image scaled accordingly

## Implementation Notes

### File Path Handling

When processing URLs from the MIME data, we need to convert them to local file paths:

```python
file_path = urls[0].toLocalFile()
```

### Image Scaling

For better visual quality, we use smooth transformation when scaling images:

```python
pixmap.scaled(
    self.ui.label.size(),
    Qt.AspectRatioMode.KeepAspectRatio,
    Qt.TransformationMode.SmoothTransformation
)
```

### Extending the Project

This project could be extended with:

1. **Multiple Image Support**: Allow dropping multiple images and provide navigation
2. **Additional Formats**: Add support for more image formats (GIF, WebP, etc.)
3. **Image Information**: Display details about the image (dimensions, file size, etc.)
4. **Edit Capabilities**: Add basic image editing functions
5. **Save/Export**: Add the ability to save or export viewed images