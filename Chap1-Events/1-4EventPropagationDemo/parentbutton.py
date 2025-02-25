from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QMouseEvent

class ParentButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
    
    def mousePressEvent(self, event: QMouseEvent):
        print("ParentButton mousePressEvent Called")
        super().mousePressEvent(event)