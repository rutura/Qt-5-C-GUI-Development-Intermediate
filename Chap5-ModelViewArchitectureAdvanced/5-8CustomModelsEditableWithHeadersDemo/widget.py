from PySide6.QtWidgets import QWidget
from ui_widget import Ui_Widget
from personmodel import PersonModel

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # Create the person model
        self.model = PersonModel(self)
        
        # Set the model for all three views
        self.ui.listView.setModel(self.model)
        self.ui.tableView.setModel(self.model)
        self.ui.treeView.setModel(self.model)
        
        # Set window title
        self.setWindowTitle("Editable Custom Model Demo")