from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QStandardItemModel, QStandardItem
from ui_widget import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # Create a standard item model
        self.model = QStandardItemModel(self)
        
        # Create item 0 - Can Drag, Can Drop
        item0 = QStandardItem()
        item0.setDragEnabled(True)
        item0.setDropEnabled(True)
        item0.setText("Item0 [CAN DRAG] [CAN DROP]")
        
        # Create item 1 - Can Drag, Can't Drop
        item1 = QStandardItem()
        item1.setDragEnabled(True)
        item1.setDropEnabled(False)
        item1.setText("Item1 [CAN DRAG] [CAN'T DROP]")
        
        # Create item 2 - Can't Drag, Can Drop
        item2 = QStandardItem()
        item2.setDragEnabled(False)
        item2.setDropEnabled(True)
        item2.setText("item2 [CAN'T DRAG] [CAN DROP]")
        
        # Create item 3 - Can't Drag, Can't Drop
        item3 = QStandardItem()
        item3.setDragEnabled(False)
        item3.setDropEnabled(False)
        item3.setText("item3 [CAN'T DRAG] [CAN'T DROP]")
        
        # Add items to the model
        self.model.appendRow(item0)
        self.model.appendRow(item1)
        self.model.appendRow(item2)
        self.model.appendRow(item3)
        
        # Configure ListView - Can Drag and Can Drop
        self.ui.listView.setAcceptDrops(True)
        self.ui.listView.setDragEnabled(True)
        self.ui.listView.setModel(self.model)
        
        # Configure TableView - Can Drag but Can't Drop
        self.ui.tableView.setAcceptDrops(False)
        self.ui.tableView.setDragEnabled(True)
        self.ui.tableView.setModel(self.model)
        
        # Configure TreeView - Can't Drag but Can Drop
        self.ui.treeView.setAcceptDrops(True)
        self.ui.treeView.setDragEnabled(False)
        self.ui.treeView.setModel(self.model)
        
        # Set window title
        self.setWindowTitle("Drag and Drop Demo")