from PySide6.QtWidgets import QListWidget, QListView, QAbstractItemView
from PySide6.QtCore import Qt, QMimeData
from PySide6.QtGui import QDrag, QPixmap

class ShapeList(QListWidget):
    """List widget for selecting shapes with drag and drop capability"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setMinimumWidth(200)
        self.setMaximumWidth(300)
        self.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.setViewMode(QListView.ViewMode.IconMode)
    
    def startDrag(self, supported_actions):
        """Start drag and drop operation with shape data"""
        items = self.selectedItems()
        if len(items) > 0:
            drag = QDrag(self)
            mime_data = QMimeData()
            
            item = items[0]
            key = item.data(Qt.ItemDataRole.UserRole)
            
            # Store the key as property
            mime_data.setProperty("Key", key)
            
            drag.setMimeData(mime_data)
            pixmap = item.icon().pixmap(50, 50)
            drag.setPixmap(pixmap)
            
            # Set hotspot to center of the pixmap
            drag.setHotSpot(pixmap.rect().center())
            
            if drag.exec() == Qt.DropAction.IgnoreAction:
                print("Drag ignored")