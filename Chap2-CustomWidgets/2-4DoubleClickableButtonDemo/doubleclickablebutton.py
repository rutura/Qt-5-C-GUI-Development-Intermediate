from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QMouseEvent
from PySide6.QtCore import Signal

class DoubleClickableButton(QPushButton):
    # Define the custom signal
    doubleClicked = Signal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
    
    def mouseDoubleClickEvent(self, event: QMouseEvent):
        """Handle mouse double click events"""
        # Emit our custom signal
        self.doubleClicked.emit()
        # Call the parent class implementation
        super().mouseDoubleClickEvent(event)