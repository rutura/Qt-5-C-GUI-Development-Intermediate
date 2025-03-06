from PySide6.QtWidgets import QGraphicsRectItem
from PySide6.QtCore import Qt
from PySide6.QtGui import QKeyEvent

class Rect(QGraphicsRectItem):
    """
    An interactive rectangle graphics item that can be moved with arrow keys
    """
    def __init__(self):
        super().__init__()

    def keyPressEvent(self, event: QKeyEvent):
        """
        Handle key press events to move the rectangle with arrow keys
        """
        print("Keypress event triggered for rect item")
        
        if event.key() == Qt.Key.Key_Left:
            # Move left
            self.moveBy(-20, 0)
        
        if event.key() == Qt.Key.Key_Right:
            # Move Right
            self.moveBy(20, 0)
        
        if event.key() == Qt.Key.Key_Up:
            # Move UP
            self.moveBy(0, -20)
        
        if event.key() == Qt.Key.Key_Down:
            # Move DOWN
            self.moveBy(0, 20)