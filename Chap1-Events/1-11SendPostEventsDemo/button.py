from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QMouseEvent

class Button(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
    
    def mousePressEvent(self, event: QMouseEvent):
        print(f"Button: Mouse press at {event.pos()}")
        super().mousePressEvent(event)
    
    def mouseReleaseEvent(self, event: QMouseEvent):
        print(f"Button: Mouse release at {event.pos()}")
        super().mouseReleaseEvent(event)
    
    def mouseMoveEvent(self, event: QMouseEvent):
        print(f"Button: Mouse move at {event.pos()}")
        super().mouseMoveEvent(event)