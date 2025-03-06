from PySide6.QtWidgets import QListWidget, QAbstractItemView, QListView
from PySide6.QtCore import Qt, QMimeData
from PySide6.QtGui import QDrag, QColor, QPixmap

class ColorListWidget(QListWidget):
    """
    Custom list widget for colors that supports drag operations.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumWidth(200)
        self.setMaximumWidth(300)
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setViewMode(QListView.IconMode)
    
    def startDrag(self, supportedActions):
        """
        Override to start a drag operation when the user drags a color.
        
        Args:
            supportedActions: The supported drag actions
        """
        items = self.selectedItems()
        if items:
            drag = QDrag(self)
            mime_data = QMimeData()
            
            color = QColor(items[0].text())
            mime_data.setColorData(color)
            
            pixmap = QPixmap(20, 20)
            pixmap.fill(color)
            drag.setPixmap(pixmap)
            drag.setMimeData(mime_data)
            drag.exec(supportedActions)