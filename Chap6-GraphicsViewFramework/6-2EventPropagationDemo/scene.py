from PySide6.QtWidgets import QGraphicsScene
from PySide6.QtCore import QObject
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QGraphicsSceneMouseEvent

class Scene(QGraphicsScene):
    """
    A custom graphics scene that demonstrates event handling
    """
    def __init__(self, parent=None):
        super().__init__(parent)

    def keyPressEvent(self, event: QKeyEvent):
        """
        Handle key press events and pass them to the parent class
        """
        print("Scene : KeypressEvent")
        super().keyPressEvent(event)

    def mousePressEvent(self, event: QGraphicsSceneMouseEvent):
        """
        Handle mouse press events and pass them to the parent class
        """
        print(f"Scene : MousePressEvent at : {event.scenePos()}")
        super().mousePressEvent(event)