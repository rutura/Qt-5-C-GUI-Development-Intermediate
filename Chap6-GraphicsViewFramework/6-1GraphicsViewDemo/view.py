from PySide6.QtWidgets import QGraphicsView, QGraphicsRectItem
from PySide6.QtCore import QPointF
from PySide6.QtGui import QMouseEvent, QBrush
from PySide6.QtCore import Qt

class View(QGraphicsView):
    """
    Custom QGraphicsView that handles mouse events to add rectangles
    where the user clicks
    """
    def __init__(self, parent=None):
        super().__init__(parent)

    def mousePressEvent(self, event: QMouseEvent):
        """
        Create a new rectangle at the position where the user clicked
        """
        # In PySide6, we need to handle both older and newer API styles
        try:
            # First try the newer API (PySide6)
            pos = event.position()
            print(f"Mouse pressed in view at position (View Coord): {pos}")
            scene_position = self.mapToScene(pos.toPoint())
        except AttributeError:
            # Fall back to older API (compatible with Qt5 style)
            pos = event.pos()
            print(f"Mouse pressed in view at position (View Coord): {pos}")
            scene_position = self.mapToScene(pos)

        print(f"Mouse pressed in view at position (Scene Coord): {scene_position}")

        # Create a new rectangle in the scene at the clicked position
        rect = self.scene().addRect(scene_position.x(), scene_position.y(), 50, 50)
        rect.setBrush(QBrush(Qt.blue))