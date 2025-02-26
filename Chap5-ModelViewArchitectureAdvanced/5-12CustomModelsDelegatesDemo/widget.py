from PySide6.QtWidgets import QWidget, QInputDialog, QMessageBox, QLineEdit
from PySide6.QtCore import QObject
from ui_widget import Ui_Widget
from personmodel import PersonModel
from persondelegate import PersonDelegate
from person import Person

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # Create the custom delegate for color editing
        self.person_delegate = PersonDelegate(self)
        
        # Create the person model
        self.model = PersonModel(self)
        
        # Set the model for all views
        self.ui.listView.setModel(self.model)
        
        self.ui.tableView.setModel(self.model)
        # Set delegate for the color column only in table view
        self.ui.tableView.setItemDelegateForColumn(2, self.person_delegate)
        
        self.ui.treeView.setModel(self.model)
        # Set delegate for all columns in tree view
        self.ui.treeView.setItemDelegate(self.person_delegate)
        
        # Share selection model between views
        self.ui.tableView.setSelectionModel(self.ui.listView.selectionModel())
        self.ui.treeView.setSelectionModel(self.ui.listView.selectionModel())
        
        # Connect button signals
        self.ui.addPersonButton.clicked.connect(self.on_addPersonButton_clicked)
        self.ui.removePersonButton.clicked.connect(self.on_removePersonButton_clicked)
        
        # Set window title
        self.setWindowTitle("Person Model with Custom Delegate")
    
    def on_addPersonButton_clicked(self):
        """Handle Add Person button click"""
        # Get name from user
        name, ok = QInputDialog.getText(
            None, 
            "Names",
            "Person name:", 
            QLineEdit.Normal,
            "Type in name"
        )
        
        if ok and name:
            # Get age from user
            age, ok = QInputDialog.getInt(
                None,
                "Person Age",
                "Age",
                20,  # Default value
                15,  # Min value
                120  # Max value
            )
            
            if ok:
                # Create and add new person
                person = Person(name, "blue", age, self)
                self.model.addPerson(person)
        else:
            QMessageBox.information(
                None,
                "Failure", 
                "Must specify name and age"
            )
            
    def on_removePersonButton_clicked(self):
        """Handle Remove Person button click"""
        index = self.ui.listView.currentIndex()
        self.model.removePerson(index)