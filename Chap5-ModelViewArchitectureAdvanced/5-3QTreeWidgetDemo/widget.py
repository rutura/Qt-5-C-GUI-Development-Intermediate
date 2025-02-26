from PySide6.QtWidgets import QWidget, QTreeWidgetItem
from PySide6.QtCore import Slot
from ui_widget import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # Set column count for the tree widget
        self.ui.treeWidget.setColumnCount(2)
        
        # Set column headers
        headers = ["Organization", "Description"]
        self.ui.treeWidget.setHeaderLabels(headers)
        
        # Add Google root organization
        google_root = self.add_root_organization("Google Inc", "Head Quarters")
        
        # Add India branch
        google_india = self.add_child_organization(google_root, "Google India", "Google India Branch")
        self.add_child_organization(google_india, "Mumbai", "AI Research")
        self.add_child_organization(google_india, "Bangalore", "Sales")
        
        # Add Ghana branch
        google_ghana = self.add_child_organization(google_root, "Google Ghana", "Ghana Branch")
        self.add_child_organization(google_ghana, "Akra", "AI")
        
        # Connect the itemClicked signal to our slot
        self.ui.treeWidget.itemClicked.connect(self.on_treeWidget_itemClicked)
        
        # Set window title
        self.setWindowTitle("QTreeWidget Demo")
    
    def add_root_organization(self, company, purpose):
        """Add a root-level organization to the tree widget"""
        item = QTreeWidgetItem(self.ui.treeWidget)
        item.setText(0, company)
        item.setText(1, purpose)
        return item
    
    def add_child_organization(self, parent, branch, description):
        """Add a child organization to a parent item"""
        item = QTreeWidgetItem()
        item.setText(0, branch)
        item.setText(1, description)
        parent.addChild(item)
        return item
    
    @Slot(QTreeWidgetItem, int)
    def on_treeWidget_itemClicked(self, item, column):
        """Handle item click events"""
        print(f"Clicked on: {item.text(0)}, column: {column}")