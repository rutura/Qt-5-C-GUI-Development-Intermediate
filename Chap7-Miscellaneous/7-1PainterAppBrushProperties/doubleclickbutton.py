from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QMouseEvent

class DoubleclickButton(QPushButton):
    """Button that emits a double click signal when double-clicked"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
    
    def mouseDoubleClickEvent(self, event):
        """Handle mouse double click events"""
        self.doubleClicked.emit()
        super().mouseDoubleClickEvent(event)
    
    # Define the doubleClicked signal
    from PySide6.QtCore import Signal
    doubleClicked = Signal()