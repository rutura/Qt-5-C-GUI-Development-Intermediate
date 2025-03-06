from PySide6.QtWidgets import QListWidget, QListView, QAbstractItemView
from PySide6.QtCore import Qt
from PySide6.QtGui import QDrag, QPixmap, QColor, QMimeData

class ColorListWidget(QListWidget):
    """List widget for selecting colors with drag and drop capability"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setMinimumWidth(200)
        self.setMaximumWidth(300)
        self.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.setViewMode(QListView.ViewMode.IconMode)
    
    def startDrag(self, supported_actions):
        """Start drag and drop operation with color data"""
        items = self.selectedItems()
        if len(items) > 0:
            drag = QDrag(self)
            mime_data = QMimeData()
            
            color = QColor(items[0].text())
            mime_data.setColorData(color)
            
            pixmap = QPixmap(20, 20)
            pixmap.fill(color)
            drag.setPixmap(pixmap)
            drag.setMimeData(mime_data)
            drag.exec(supported_actions)