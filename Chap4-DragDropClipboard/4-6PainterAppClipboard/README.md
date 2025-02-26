# Paint Application with Clipboard Support in PySide6

This is a drawing application built with PySide6 that includes clipboard support for copying and pasting images. It provides various drawing tools, color options, and clipboard integration.

## Features

- **Drawing Tools**: Pen, Rectangle, Ellipse, and Eraser
- **Color Options**: Customizable pen and fill colors
- **Clipboard Integration**: Copy canvas content to clipboard and paste images from clipboard
- **Interactive UI**: Toolbar with drawing options and status bar feedback

## Project Structure

```
project/
├── main.py               # Application entry point
├── mainwindow.py         # Main window with toolbar and UI
├── paintcanvas.py        # Custom drawing canvas with tools and clipboard support
├── ui_mainwindow.py      # Generated UI code from mainwindow.ui
├── resource_rc.py        # Generated resource code from resource.qrc
└── images/               # Directory for tool icons
   ├── about.png
   ├── circle.png
   ├── close.png
   ├── eraser.png
   ├── open.png
   ├── pen.png
   ├── rectangle.png
   └── save.png
```

## Key Components

### PaintCanvas Widget

The `PaintCanvas` class is a custom widget that handles:
- Drawing operations with different tools
- Clipboard operations (copy/paste)
- Image management and rendering

```python
class PaintCanvas(QWidget):
    # Tool type enum
    Pen, Rect, Ellipse, Eraser = range(4)
    
    # Methods for drawing and clipboard operations
    def copy(self):
        # Copy canvas to clipboard
        
    def paste(self):
        # Paste image from clipboard
```

### Clipboard Integration

The application implements copy and paste operations using Qt's clipboard system:

```python
def copy(self):
    """Copy the canvas image to clipboard"""
    clipboard = QApplication.clipboard()
    mime_data = clipboard.mimeData()
    mime_data.setImageData(self.image)
    clipboard.setMimeData(mime_data)

def paste(self):
    """Paste image from clipboard to canvas"""
    # Get data from clipboard
    mime_data = QApplication.clipboard().mimeData()
    
    # Handle different clipboard data types
    if mime_data.hasUrls():
        # Handle image files
    elif mime_data.hasImage():
        # Handle direct image data
```

### Main Window

The `MainWindow` class creates the UI and connects the tools:

```python
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        # Create canvas
        self.canvas = PaintCanvas(self)
        self.setCentralWidget(self.canvas)
        
        # Create and connect toolbar controls
        # ...
```

## Drawing Tools

The application supports four drawing tools:

1. **Pen Tool**: Freeform drawing with the current pen color and width
2. **Rectangle Tool**: Draw rectangles with optional fill
3. **Ellipse Tool**: Draw ellipses with optional fill
4. **Eraser Tool**: Erase content in a rectangular area

## Clipboard Usage

The application supports the following clipboard operations:

- **Copy (Ctrl+C)**: Copy the entire canvas to the clipboard
- **Paste (Ctrl+V)**: 
  - Paste an image file from the clipboard (if a file was copied)
  - Paste an image directly from the clipboard (if image data was copied)

## Running the Application

1. Generate the UI Python file (if mainwindow.ui changes):
   ```
   pyside6-uic mainwindow.ui -o ui_mainwindow.py
   ```

2. Generate the resource Python file (if resources.qrc changes):
   ```
   pyside6-rcc resource.qrc -o resource_rc.py
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

1. **Drawing**: 
   - Select a tool from the toolbar
   - Choose pen width, colors, and fill options
   - Draw on the canvas using the mouse

2. **Clipboard Operations**:
   - Press Ctrl+C to copy the entire canvas to the clipboard
   - Press Ctrl+V to paste an image from the clipboard
   - You can copy images from other applications or files and paste them into the canvas

## Implementation Notes

### Event Handling

The application uses Qt's event system to handle keyboard shortcuts:

```python
def keyPressEvent(self, event):
    """Handle key press events for clipboard operations"""
    if event.matches(QKeySequence.Copy):
        self.copy()
        event.accept()
    elif event.matches(QKeySequence.Paste):
        self.paste()
        event.accept()
    else:
        super().keyPressEvent(event)
```

### Image Format Validation

When pasting from clipboard URLs, the application validates image formats:

```python
def isImage(self, file_path):
    """Check if a file is a supported image format"""
    _, ext = os.path.splitext(file_path)
    ext = ext.lower()
    return ext in [".png", ".jpg", ".jpeg"]
```

### QImage vs QPixmap

- `QImage` is used for the main canvas since it provides direct pixel access
- `QPixmap` is used for pasting operations since it's optimized for display

## Extending the Project

This project could be extended with:

1. **File Operations**: Add save and load functionality
2. **More Tools**: Add line, polygon, or text tools
3. **Selection Tool**: Add a tool to select and move parts of the drawing
4. **Layers**: Implement a layer system for more complex drawings
5. **Undo/Redo**: Add undo and redo capabilities
6. **More Clipboard Formats**: Support for other clipboard formats like SVG or text