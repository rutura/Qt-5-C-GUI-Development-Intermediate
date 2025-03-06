from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Signal

class DoubleclickButton(QPushButton):
    """Button that emits a double click signal when double-clicked"""
    
    # Define the doubleClicked signal
    doubleClicked = Signal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
    
    def mouseDoubleClickEvent(self, event):
        """Handle mouse double click events"""
        self.doubleClicked.emit()
        super().mouseDoubleClickEvent(event)