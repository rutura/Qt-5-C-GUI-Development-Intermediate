from typing import Optional
from PySide6.QtWidgets import QPushButton, QLineEdit
from PySide6.QtGui import QMouseEvent, QKeyEvent

class ParentButton(QPushButton):
    """Base button class demonstrating event propagation."""
    
    def __init__(self, parent: Optional['QWidget'] = None) -> None:
        super().__init__(parent)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        print("ParentButton mousePressEvent Called")
        super().mousePressEvent(event)


class ParentLineEdit(QLineEdit):
    """Base line edit class demonstrating event propagation."""
    
    def __init__(self, parent: Optional['QWidget'] = None) -> None:
        super().__init__(parent)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        print("ParentLineEdit keyPressEvent")
        print(f"ParentLineEdit Accepted: {event.isAccepted()}")
        super().keyPressEvent(event)