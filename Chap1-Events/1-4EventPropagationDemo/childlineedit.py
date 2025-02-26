from parentlineedit import ParentLineEdit
from PySide6.QtGui import QKeyEvent
from PySide6.QtCore import Qt

class ChildLineEdit(ParentLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
    
    def keyPressEvent(self, event: QKeyEvent):
        print(f"ChildLineEdit Accepted: {event.isAccepted()}")
        
        event.ignore()
        
        if event.key() == Qt.Key.Key_Delete:
            print("Pressed the Delete Key")
            self.clear()
        else:
            super().keyPressEvent(event)