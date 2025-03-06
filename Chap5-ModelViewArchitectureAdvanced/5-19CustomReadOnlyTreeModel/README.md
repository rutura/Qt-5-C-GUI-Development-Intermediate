# PySide6 Custom Hierarchical Tree Model

## Project Overview
This PySide6 application demonstrates a custom hierarchical tree model that reads a family tree from a text file, showcasing advanced Qt model/view programming techniques with nested data structures.

## Project Structure
- `main.py`: Application entry point
- `person.py`: Person class representing individual tree nodes
- `person_model.py`: Custom tree model implementation
- `widget.py`: Main widget implementation
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

### 2. Custom QAbstractItemModel Implementation
The `PersonModel` class demonstrates key model methods for hierarchical data:
- `index()`: Create model indexes for tree nodes
- `parent()`: Retrieve parent indexes
- `rowCount()`: Count child nodes
- `columnCount()`: Define number of columns
- `data()`: Provide data for different roles

### 3. Hierarchical Data Parsing
```python
def read_file(self):
    # Parse indentation-based hierarchical text file
    # Create nested Person objects based on indentation level
    last_indentation = 0
    last_parent = self.root_person
    last_person = None

    with open(self.filename, 'r') as file:
        for line in file:
            current_indentation = line.count('\t')
            names, profession = self.parse_line(line.strip())
            
            # Logic to determine correct parent based on indentation
            # Add new Person object to tree
```

### 4. Tree View Configuration
```python
# Set model for tree view
self.ui.treeView.setModel(self.person_model)
```

## Running the Application
```bash
python main.py
```

## Learning Highlights
- Hierarchical data modeling
- Custom model implementation
- Resource file usage
- Recursive data structure parsing

## Potential Improvements
- Add more advanced tree view interactions
- Implement sorting and filtering
- Create editable tree model

