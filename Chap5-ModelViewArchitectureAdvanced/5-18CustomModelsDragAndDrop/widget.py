from PySide6.QtWidgets import QWidget
from ui_widget import Ui_Widget
from personmodel import PersonModel

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Setup UI
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # Create and set model
        model = PersonModel(self)
        
        # Configure list view
        self.ui.listView.setModel(model)
        self.ui.listView.setDragEnabled(True)
        self.ui.listView.setAcceptDrops(True)
        
        # Configure table view
        self.ui.tableView.setModel(model)
        self.ui.tableView.setDragEnabled(True)
        self.ui.tableView.setAcceptDrops(True)
        
        # Configure tree view
        self.ui.treeView.setModel(model)
        self.ui.treeView.setDragEnabled(True)
        self.ui.treeView.setAcceptDrops(True)
        
        # Set window title
        self.setWindowTitle("Drag and Drop Model Views")