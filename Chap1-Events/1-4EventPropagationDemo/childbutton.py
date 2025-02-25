from parentbutton import ParentButton
from PySide6.QtGui import QMouseEvent

class ChildButton(ParentButton):
    def __init__(self, parent=None):
        super().__init__(parent)
    
    def mousePressEvent(self, event: QMouseEvent):
        print("ChildButton mousePressEvent called")
        super().mousePressEvent(event)