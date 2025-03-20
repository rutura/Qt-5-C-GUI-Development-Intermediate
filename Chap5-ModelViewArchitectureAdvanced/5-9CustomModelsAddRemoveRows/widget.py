from PySide6.QtWidgets import QWidget, QInputDialog, QMessageBox, QLineEdit
from PySide6.QtCore import Slot, QModelIndex
from ui_widget import Ui_Widget
from personmodel import PersonModel
from person import Person

class Widget(QWidget):
    def __init__(self, model=None, controller=None, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # Store model and controller
        self._model = model
        self._controller = controller
        
        # If no model provided, create one for backward compatibility
        if not self._model:
            self._model = PersonModel(self)
        
        # Set the model for all three views
        self.ui.listView.setModel(self._model)
        self.ui.tableView.setModel(self._model)
        self.ui.treeView.setModel(self._model)
        
        # Share selection model between views
        # This ensures selecting in one view also selects in others
        self.ui.tableView.setSelectionModel(self.ui.listView.selectionModel())
        self.ui.treeView.setSelectionModel(self.ui.listView.selectionModel())
        
        # Connect buttons to slots
        if self._controller:
            self.ui.addPersonButton.clicked.connect(self._on_addPersonButton_clicked_with_controller)
            self.ui.removePersonButton.clicked.connect(self._on_removePersonButton_clicked_with_controller)
            
            # Connect listView selection to controller
            self.ui.listView.clicked.connect(self._on_listView_clicked)
        else:
            # Legacy connections
            self.ui.addPersonButton.clicked.connect(self._on_addPersonButton_clicked_legacy)
            self.ui.removePersonButton.clicked.connect(self._on_removePersonButton_clicked_legacy)
        
        # Set window title
        self.setWindowTitle("Advanced Custom Model Demo (Qt Widgets)")
    
    @Slot()
    def _on_addPersonButton_clicked_with_controller(self):
        """Handle Add Person button click using controller"""
        # Get name from user
        name, ok = QInputDialog.getText(
            self, 
            "Names",
            "Person name:", 
            QLineEdit.Normal,
            "Type in name"
        )
        
        if ok and name:
            # Get age from user
            age, ok = QInputDialog.getInt(
                self,
                "Person Age",
                "Age",
                20,  # Default value
                15,  # Min value
                120  # Max value
            )
            
            if ok and self._controller:
                # Add person through controller
                self._controller.addPerson(name, age)
        else:
            QMessageBox.information(
                self,
                "Failure", 
                "Must specify name and age"
            )
    
    @Slot()
    def _on_removePersonButton_clicked_with_controller(self):
        """Handle Remove Person button click using controller"""
        index = self.ui.listView.currentIndex()
        if index.isValid() and self._controller:
            self._controller.removePersonByIndex(index)
    
    @Slot(QModelIndex)
    def _on_listView_clicked(self, index):
        """Handle listView click with controller"""
        if self._controller:
            self._controller.selectPersonByIndex(index)
    
    # Legacy methods for backward compatibility
    
    @Slot()
    def _on_addPersonButton_clicked_legacy(self):
        """Legacy handler for Add Person button click"""
        # Get name from user
        name, ok = QInputDialog.getText(
            self, 
            "Names",
            "Person name:", 
            QLineEdit.Normal,
            "Type in name"
        )
        
        if ok and name:
            # Get age from user
            age, ok = QInputDialog.getInt(
                self,
                "Person Age",
                "Age",
                20,  # Default value
                15,  # Min value
                120  # Max value
            )
            
            if ok:
                # Create and add new person
                person = Person(name, "blue", age, self)
                self._model.addPerson(person)
        else:
            QMessageBox.information(
                self,
                "Failure", 
                "Must specify name and age"
            )
            
    @Slot()
    def _on_removePersonButton_clicked_legacy(self):
        """Legacy handler for Remove Person button click"""
        index = self.ui.listView.currentIndex()
        self._model.removePerson(index)