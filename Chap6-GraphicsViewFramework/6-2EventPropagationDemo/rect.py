from PySide6.QtWidgets import QGraphicsRectItem
from PySide6.QtCore import Qt
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QGraphicsSceneMouseEvent

class Rect(QGraphicsRectItem):
    """
    A rectangle graphics item that demonstrates event handling
    """
    def __init__(self):
        super().__init__()

    def keyPressEvent(self, event: QKeyEvent):
        """
        Handle key press events and pass them to the parent class
        """
        print("Rect Item : Key press event")
        super().keyPressEvent(event)

    def mousePressEvent(self, event: QGraphicsSceneMouseEvent):
        """
        Handle mouse press events and pass them to the parent class
        """
        print(f"Rect Item : Mouse pressed at : {event.pos()}")
        super().mousePressEvent(event)