from typing import Optional
from PySide6.QtCore import Qt
from PySide6.QtGui import QMouseEvent, QKeyEvent
from base_widgets import ParentButton, ParentLineEdit

class ChildButton(ParentButton):
    """Child button demonstrating event propagation."""
    
    def __init__(self, parent: Optional['QWidget'] = None) -> None:
        super().__init__(parent)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        print("ChildButton mousePressEvent called")
        super().mousePressEvent(event)


class ChildLineEdit(ParentLineEdit):
    """Child line edit demonstrating event propagation."""
    
    def __init__(self, parent: Optional['QWidget'] = None) -> None:
        super().__init__(parent)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        print(f"ChildLineEdit Accepted: {event.isAccepted()}")
        
        # Demonstrate event handling and propagation
        event.ignore()
        
        if event.key() == Qt.Key.Key_Delete:
            print("Pressed the Delete Key")
            self.clear()
        else:
            super().keyPressEvent(event)