from PySide6.QtWidgets import QWidget, QInputDialog, QMessageBox, QLineEdit
from ui_widget import Ui_Widget
from personmodel import PersonModel
from persondelegate import PersonDelegate
from stardelegate import StarDelegate
from person import Person

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # Create the custom delegates
        self.person_delegate = PersonDelegate(self)
        self.star_delegate = StarDelegate(self)
        
        # Create the person model
        self.model = PersonModel(self)
        
        # Set the model for all views
        self.ui.listView.setModel(self.model)
        
        # Configure table view
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.setItemDelegateForColumn(2, self.person_delegate)  # Color delegate
        self.ui.tableView.setItemDelegateForColumn(3, self.star_delegate)    # Star delegate
        
        # Configure tree view
        self.ui.treeView.setModel(self.model)
        self.ui.treeView.setItemDelegate(self.person_delegate)               # Default delegate
        self.ui.treeView.setItemDelegateForColumn(3, self.star_delegate)     # Star delegate
        
        # Share selection model between views
        self.ui.tableView.setSelectionModel(self.ui.listView.selectionModel())
        self.ui.treeView.setSelectionModel(self.ui.listView.selectionModel())
        
        # Connect button signals
        self.ui.addPersonButton.clicked.connect(self.on_addPersonButton_clicked)
        self.ui.removePersonButton.clicked.connect(self.on_removePersonButton_clicked)
        
        # Set window title
        self.setWindowTitle("Multiple Custom Delegates Demo")
    
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
            age, age_ok = QInputDialog.getInt(
                None,
                "Person Age",
                "Age",
                20,  # Default value
                15,  # Min value
                120  # Max value
            )
            
            if age_ok:
                # Create and add new person with default social score of 3
                person = Person(name, "blue", age, 3, self)
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