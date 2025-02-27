from PySide6.QtWidgets import QGraphicsView, QGraphicsRectItem, QGraphicsItem
from PySide6.QtCore import QObject, QPoint, QRect, QRectF, Qt
from PySide6.QtGui import QPainter, QPainterPath, QBrush, QColor, QPen

class View(QGraphicsView):
    """
    Custom QGraphicsView that implements custom selection and grid drawing
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.drawing_selection = False
        self.last_rect = None
        self.draw_grid_lines = True
        self.select_top_left = QPoint()
    
    def mousePressEvent(self, event):
        """
        Handle mouse press event:
        - If clicking on an empty area, start drawing selection
        - Otherwise, pass the event to the base class
        """
        print(f"View mouse pressed at: {event.pos()}")
        scene_item = self.scene().itemAt(self.mapToScene(event.pos()), self.transform())
        
        if not scene_item:
            self.select_top_left = event.pos()
            self.drawing_selection = True
        
        super().mousePressEvent(event)
    
    def mouseMoveEvent(self, event):
        """
        Handle mouse move event:
        - If drawing selection, update the selection area
        - Otherwise, pass the event to the base class
        """
        print(f"View mouse moved at: {event.pos()}")
        
        if self.drawing_selection:
            # Selection region
            select_region = QRect(self.select_top_left, event.pos())
            
            # Create selection path
            path = QPainterPath()
            path.addRect(select_region)
            
            # Set the selection area in the scene
            self.scene().setSelectionArea(self.mapToScene(path))
            
            # Draw visual feedback for the user
            item_to_remove = self.last_rect
            
            if item_to_remove:
                self.scene().removeItem(item_to_remove)
            
            # Create a new selection rectangle
            self.last_rect = self.scene().addRect(
                QRectF(self.mapToScene(self.select_top_left),
                      self.mapToScene(event.pos())).normalized()
            )
            self.last_rect.setBrush(QBrush(QColor(255, 0, 0, 50)))  # Semi-transparent red
            
            # Clean up the old rectangle
            if item_to_remove:
                del item_to_remove
        
        super().mouseMoveEvent(event)
    
    def mouseReleaseEvent(self, event):
        """
        Handle mouse release event:
        - If drawing selection, finish the selection and remove the visual feedback
        - Otherwise, pass the event to the base class
        """
        if self.drawing_selection:
            item_to_remove = self.last_rect
            if item_to_remove:
                self.scene().removeItem(item_to_remove)
                del item_to_remove
                self.last_rect = None
        
        self.drawing_selection = False
        super().mouseReleaseEvent(event)
    
    def drawBackground(self, painter, rect):
        """
        Draw a custom background for the view
        """
        painter.save()
        
        painter.setBrush(QBrush(Qt.yellow))
        painter.drawRect(-800, -400, 1600, 800)
        
        painter.restore()
        
        # We don't call the base class implementation
        # super().drawBackground(painter, rect)
    
    def drawForeground(self, painter, rect):
        """
        Draw grid lines in the foreground if enabled
        """
        if self.draw_grid_lines:
            painter.save()
            
            # Set a semi-transparent pen for grid lines
            painter.setPen(QColor(100, 44, 18, 30))
            
            # Draw vertical lines
            for i in range(32):
                painter.drawLine(-800 + (50 * i), -400, -800 + (50 * i), 400)
            
            # Draw horizontal lines
            for i in range(16):
                painter.drawLine(-800, -400 + (i * 50), 800, -400 + (i * 50))
            
            painter.restore()
        else:
            super().drawForeground(painter, rect)
    
    def getDrawGridLines(self):
        """
        Get the current grid lines visibility state
        """
        return self.draw_grid_lines
    
    def setDrawGridLines(self, value):
        """
        Set the grid lines visibility state
        """
        if self.draw_grid_lines != value:
            self.draw_grid_lines = value
            self.scene().update()