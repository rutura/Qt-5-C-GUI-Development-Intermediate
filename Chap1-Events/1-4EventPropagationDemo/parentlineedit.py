from PySide6.QtWidgets import QLineEdit
from PySide6.QtGui import QKeyEvent

class ParentLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
    
    def keyPressEvent(self, event: QKeyEvent):
        print("ParentLineEdit keyPressEvent")
        print(f"ParentLineEdit Accepted: {event.isAccepted()}")
        super().keyPressEvent(event)