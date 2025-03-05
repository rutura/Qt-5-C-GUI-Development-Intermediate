from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QPoint, Qt, QMimeData
from PySide6.QtGui import QMouseEvent, QDrag, QPixmap, QColor

class DragButton(QPushButton):
    """Button that supports drag operations with color data"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.button_color = Qt.gray
        self.last_pos = QPoint()
    
    def get_button_color(self):
        """Get the button's current color"""
        return self.button_color
    
    def set_button_color(self, value):
        """Set the button's color"""
        self.button_color = value
    
    def mousePressEvent(self, event):
        """Handle mouse press events for starting drag operations"""
        if event.button() == Qt.MouseButton.LeftButton:
            self.last_pos = event.position().toPoint()
        super().mousePressEvent(event)
    
    def mouseMoveEvent(self, event):
        """Handle mouse move events for drag operations"""
        if event.buttons() & Qt.MouseButton.LeftButton:
            distance = (event.position().toPoint() - self.last_pos).manhattanLength()
            
            if distance >= 5:  # QApplication.startDragDistance()
                drag = QDrag(self)
                mime_data = QMimeData()
                mime_data.setColorData(self.button_color)
                pixmap = QPixmap(20, 20)
                pixmap.fill(self.button_color)
                drag.setPixmap(pixmap)
                drag.setMimeData(mime_data)
                drag.exec()
        
        super().mouseMoveEvent(event)