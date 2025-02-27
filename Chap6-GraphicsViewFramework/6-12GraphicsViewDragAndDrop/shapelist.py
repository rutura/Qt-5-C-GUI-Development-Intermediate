from PySide6.QtWidgets import QListWidget, QAbstractItemView, QListView
from PySide6.QtCore import Qt, QMimeData
from PySide6.QtGui import QDrag

class ShapeList(QListWidget):
    """
    Custom list widget for shapes that supports drag operations.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumWidth(200)
        self.setMaximumWidth(300)
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setViewMode(QListView.IconMode)
    
    def startDrag(self, supportedActions):
        """
        Override to start a drag operation when the user drags a shape.
        
        Args:
            supportedActions: The supported drag actions
        """
        items = self.selectedItems()
        if items:
            drag = QDrag(self)
            mime_data = QMimeData()
            
            item = items[0]
            key = item.data(Qt.UserRole)
            
            # In PySide6, we'll use text data to store the key value
            # Convert the key to a string and use a custom format
            mime_data.setText(f"SHAPE_KEY:{key}")
            
            drag.setMimeData(mime_data)
            pixmap = item.icon().pixmap(50, 50)
            drag.setPixmap(pixmap)
            
            drag.setHotSpot(pixmap.rect().center())
            
            if drag.exec() == Qt.IgnoreAction:
                print("Drag ignored")