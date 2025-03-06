# PySide6 Custom List Model with Drag and Drop

## Project Overview
This PySide6 application demonstrates a custom list model with drag and drop functionality across multiple views (ListView, TableView, TreeView), showcasing advanced Qt model/view programming techniques.

## Project Structure
- `main.py`: Application entry point
- `person_model.py`: Custom list model implementation
- `widget.py`: Main widget implementation
- `ui_widget.py`: Generated UI file from Qt Designer
- `widget.ui`: UI design file

## Key Qt/PySide6 Concepts Demonstrated

### 1. UI File Generation
Generate the UI Python file using the following command:
```bash
pyside6-uic widget.ui -o ui_widget.py
```

### 2. Custom QAbstractListModel Implementation
The `PersonModel` class demonstrates key model methods:
- `rowCount()`: Return number of items
- `data()`: Provide data for different roles
- `setData()`: Update model data
- `insertRows()` and `removeRows()`: Modify model structure
- `mimeTypes()`, `mimeData()`, `dropMimeData()`: Enable drag and drop

#### Key Drag and Drop Methods
```python
def mimeTypes(self):
    # Define MIME types supported by the model
    return super().mimeTypes() + ["plain/text"]

def mimeData(self, indexes):
    # Create MIME data for dragged items
    mime_data = super().mimeData(indexes)
    text_data = ",".join(index.data() for index in indexes)
    mime_data.setText(text_data)
    return mime_data

def dropMimeData(self, data, action, row, column, parent):
    # Handle drop actions
    if data.hasText():
        if parent.isValid():
            # Overwrite existing item
            self.setData(parent, data.text())
        else:
            # Add new item
            self.insertRows(self.rowCount(), 1)
            self.setData(self.index(self.rowCount() - 1), data.text())
        return True
    return False
```

### 3. View Configuration
```python
# Enable drag and drop for different views
self.listView.setDragEnabled(True)
self.listView.setAcceptDrops(True)

self.tableView.setDragEnabled(True)
self.tableView.setAcceptDrops(True)

self.treeView.setDragEnabled(True)
self.treeView.setAcceptDrops(True)
```

## Running the Application
```bash
python main.py
```

## Learning Highlights
- Custom model implementation
- Drag and drop between views
- MIME data handling
- Model/View programming pattern

## Potential Improvements
- Add more complex data structures
- Implement undo/redo functionality
- Add custom drag and drop styling
