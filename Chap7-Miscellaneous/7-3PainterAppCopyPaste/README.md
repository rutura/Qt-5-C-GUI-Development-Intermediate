# PySide6 Drawing Application with Copy/Paste Functionality

This document explains the implementation of copy/paste features in the PySide6 drawing application. 

## Overview

The drawing application now includes copy, cut, and paste functionality for all graphics items. This allows users to:

1. Copy selected items to the clipboard
2. Cut selected items (copy and then remove them)
3. Paste items from the clipboard into the scene

## Implementation Details

### 1. New Files

- **`painterapptypes.py`**: Defines custom type constants for graphics items
- **`strokeitem.py`**: A dedicated class for handling stroke items (pen lines)

### 2. Core Copy/Paste Architecture

The copy/paste implementation uses Qt's clipboard system and custom data serialization:

1. **Copying**: Selected items are serialized to a data stream, which is then placed in the clipboard
2. **Cutting**: Similar to copying, but items are removed from the scene after copying
3. **Pasting**: Data from the clipboard is deserialized into new items, which are added to the scene

### 3. Serialization Process

To enable copy/paste, each graphics item type needed to implement:

- **Type identification**: Each item class now has a `type()` method returning a unique identifier
- **Data serialization**: Custom methods to write item properties to a data stream
- **Data deserialization**: Custom methods to read item properties from a data stream

### 4. MIME Type

The application uses a custom MIME type (`"application/com.blikoontech.painterapp"`) for its clipboard data, ensuring that:

1. Only compatible data can be pasted
2. Copy/paste works correctly between different instances of the application
3. The clipboard data won't interfere with other applications

## Key Methods in Scene Class

### Copy/Cut/Paste Methods

```python
def copy(self):
    """Copy selected items to clipboard"""
    # Serialize selected items to a data stream
    # Place data in clipboard

def cut(self):
    """Cut selected items to clipboard and remove them from scene"""
    # Call copy()
    # Remove selected items from scene

def paste(self):
    """Paste items from clipboard to scene"""
    # Get data from clipboard
    # Deserialize and create new items
    # Add items to scene
```

### Data Stream Methods

```python
def write_items_to_data_stream(self, data_stream, items):
    """Write multiple items to data stream"""
    # For each item, write its type and data

def read_items_from_data_stream(self, data_stream):
    """Read and create items from data stream"""
    # Read item type and create appropriate item
    # Configure item from stream data
    # Add item to scene
```

## Item-Specific Serialization

Each item type has specific serialization methods:

1. **Rectangle, Ellipse, Star**: Store bounds, position, brush color, pen properties
2. **Pixmap**: Store bounds, position, and the actual pixmap data
3. **Stroke**: Store position, lines, and pen properties

## Usage

To use copy/paste in the application:

1. **Copy**: Select one or more items and press Ctrl+C or use Edit → Copy
2. **Cut**: Select one or more items and press Ctrl+X or use Edit → Cut
3. **Paste**: Press Ctrl+V or use Edit → Paste

When pasting, items appear at the same position as the original but with a small offset (10,10) to make it clear that they are copies.

## Connection to UI

The copy/paste functionality is connected to the UI through action connections in the MainWindow class:

```python
# In MainWindow.__init__()
self.ui.actionCopy.triggered.connect(self.on_actionCopy_triggered)
self.ui.actionCut.triggered.connect(self.on_actionCut_triggered)
self.ui.actionPaste.triggered.connect(self.on_actionPaste_triggered)

# Action handlers
def on_actionCopy_triggered(self):
    self.scene.copy()

def on_actionCut_triggered(self):
    self.scene.cut()

def on_actionPaste_triggered(self):
    self.scene.paste()
```
