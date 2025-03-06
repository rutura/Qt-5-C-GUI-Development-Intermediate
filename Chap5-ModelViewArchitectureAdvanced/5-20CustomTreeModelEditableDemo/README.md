# PySide6 Editable Hierarchical Tree Model

## Project Overview
This PySide6 application demonstrates an editable hierarchical tree model with dynamic row and column manipulation, showcasing advanced Qt model/view programming techniques.

## Project Structure
- `main.py`: Application entry point
- `person.py`: Person class representing tree nodes
- `person_model.py`: Custom editable tree model implementation
- `widget.py`: Main widget with tree view and interaction buttons
- `ui_widget.py`: Generated UI file from Qt Designer
- `widget.ui`: UI design file
- `resources_rc.py`: Resource file for loading data
- `data/familytree1.txt`: Family tree data file

## Key Qt/PySide6 Concepts Demonstrated

### 1. UI File Generation
Generate the UI Python file using the following command:
```bash
pyside6-uic widget.ui -o ui_widget.py
```

### 2. Custom Editable QAbstractItemModel Implementation
The `PersonModel` class demonstrates advanced model methods:
- Dynamic row and column insertion/removal
- Hierarchical data representation
- Editable data handling

#### Key Model Methods
```python
def insertRows(self, position, rows, parent=QModelIndex()):
    # Insert new rows at a specific position
    person_parent = self.get_person_from_index(parent)
    success = person_parent.insert_children(position, rows, self.root_person.column_count())
    return success

def removeRows(self, position, rows, parent=QModelIndex()):
    # Remove rows from a specific position
    person_parent = self.get_person_from_index(parent)
    success = person_parent.remove_children(position, rows)
    return success

def setData(self, index, value, role=Qt.EditRole):
    # Edit data for a specific index
    if role == Qt.EditRole:
        person = index.internalPointer()
        result = person.set_data(index.column(), value)
        if result:
            self.dataChanged.emit(index, index, [role])
        return result
```

### 3. Tree View Interaction
Buttons for manipulating the tree model:
- Add Row
- Remove Row
- Add Column
- Remove Column
- Add Child

```python
def on_add_row_button_clicked(self):
    # Add a new row at the current index
    index = self.ui.treeView.selectionModel().currentIndex()
    model = self.ui.treeView.model()
    
    if model.insertRow(index.row() + 1, index.parent()):
        for column in range(model.columnCount(index.parent())):
            child_index = model.index(index.row() + 1, column, index.parent())
            model.setData(child_index, "[Empty Cell]", Qt.EditRole)
```

## Running the Application
```bash
python main.py
```

## Learning Highlights
- Hierarchical data modeling
- Dynamic model manipulation
- Custom tree model implementation
- Model/view programming patterns

## Potential Improvements
- Add undo/redo functionality
- Implement drag and drop
- Create more advanced data validation
