from PySide6.QtWidgets import QWidget
from ui_widget import Ui_Widget
from personmodel import PersonModel

class Widget(QWidget):
    def __init__(self, parent=None):
        """
        Initialize the widget with a tree view model
        
        :param parent: Parent widget
        """
        super().__init__(parent)
        
        # Setup UI
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # Create and set model
        self.person_model = PersonModel(self)
        
        # Configure tree view
        self.ui.treeView.setModel(self.person_model)
        
        # Expand the first level of the tree
        for row in range(self.person_model.rowCount()):
            index = self.person_model.index(row, 0)
            self.ui.treeView.expand(index)
        
        # Set window title
        self.setWindowTitle("Family Tree Hierarchical Model")