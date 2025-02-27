from PySide6.QtWidgets import QGraphicsView
from PySide6.QtCore import Qt
from PySide6.QtGui import QKeyEvent, QMouseEvent

class View(QGraphicsView):
    """
    A custom graphics view that demonstrates event handling
    """
    def __init__(self, parent=None):
        super().__init__(parent)

    def mousePressEvent(self, event: QMouseEvent):
        """
        Handle mouse press events and pass them to the parent class
        """
        # Ensure compatibility with different PySide6 versions
        try:
            pos = event.position().toPoint()
        except AttributeError:
            pos = event.pos()
            
        print(f"View : MousePressEvent at : {pos}")
        super().mousePressEvent(event)

    def keyPressEvent(self, event: QKeyEvent):
        """
        Handle key press events and pass them to the parent class
        """
        print("View : KeyPressEvent")
        super().keyPressEvent(event)