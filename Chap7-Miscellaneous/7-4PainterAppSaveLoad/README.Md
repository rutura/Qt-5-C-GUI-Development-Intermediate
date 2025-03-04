# PySide6 Drawing Application with Save/Load Functionality

This document explains the implementation of save/load features in the PySide6 drawing application.

## Overview

The drawing application now includes save and load functionality, allowing users to:

1. Save their drawings to a file (.pa format)
2. Load previously saved drawings from a file
3. Maintain all properties of shapes, strokes, and images

## Implementation Details

### 1. Core Save/Load Architecture

The save/load implementation uses Qt's file system and data stream mechanisms:

1. **Saving**: 
   - The entire scene (all items) is serialized to a data stream
   - The data stream is written to a file with a .pa extension
   - Each item's type, position, size, and style properties are saved

2. **Loading**:
   - Data from a file is read into a data stream
   - Items are deserialized from the stream and added to the scene
   - All properties (colors, styles, sizes) are preserved exactly as saved

### 2. File Format

The application uses a custom binary file format (.pa extension) that contains:
- A sequence of serialized items
- Each item prefixed with its type identifier
- Full property information for each item

### 3. Integration with Copy/Paste System

The save/load functionality builds on the existing copy/paste architecture:
- The same serialization/deserialization methods are used
- A parameter determines whether items should be offset (for paste) or placed exactly (for load)

## Key Methods in Scene Class

### Save/Load Methods

```python
def save_scene(self, filename):
    """Save the scene to a file"""
    # Open file for writing
    # Serialize all scene items to the file
    # Close file

def load_scene(self, filename):
    """Load the scene from a file"""
    # Open file for reading
    # Deserialize items and add them to scene
    # Close file
```

### Updated ItemsFromDataStream Method

```python
def read_items_from_data_stream(self, data_stream, copy_paste=True):
    """Read items from data stream for pasting or loading"""
    # Read item type
    # Create appropriate item
    # Configure item from stream data
    # Add item to scene
    # If copy_paste is True, offset the item position and select it
```

## Connection to UI

The save/load functionality is connected to the UI through action connections in the MainWindow class:

```python
# In MainWindow.__init__()
self.ui.actionSave.triggered.connect(self.on_actionSave_triggered)
self.ui.actionLoad.triggered.connect(self.on_actionLoad_triggered)

# Action handlers
def on_actionSave_triggered(self):
    # Show save file dialog
    # Call scene.save_scene() with selected filename

def on_actionLoad_triggered(self):
    # Show open file dialog
    # Call scene.load_scene() with selected filename
```

## Usage

To use the save/load feature in the application:

1. **Save**:
   - Create a drawing with any tools available
   - Click File → Save or press the Save button in the toolbar
   - Choose a location and filename for your drawing
   - The file will be saved with a .pa extension

2. **Load**:
   - Click File → Load or press the Load button in the toolbar
   - Navigate to a previously saved .pa file and select it
   - The drawing will be loaded into the scene, replacing any current content

## Technical Notes

1. The save operation saves the entire scene, not just selected items
2. Loaded items maintain their exact positions, unlike pasted items which are offset
3. All item properties are preserved, including:
   - Size and position
   - Fill color and brush style
   - Pen color, width and style
   - For pixmap items, the actual image data

## Future Enhancements

Possible future enhancements to the save/load functionality:
1. Save/load of view settings (grid visibility, background color)
2. Support for merging loaded content with existing content
3. Support for different file formats (SVG, PNG, etc.)
4. Implementation of auto-save functionality