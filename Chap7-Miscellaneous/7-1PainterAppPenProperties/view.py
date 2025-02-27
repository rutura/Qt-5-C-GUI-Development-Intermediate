from PySide6.QtWidgets import QGraphicsView, QGraphicsRectItem
from PySide6.QtCore import Qt, QPoint, QRect, QRectF
from PySide6.QtGui import QPainter, QPainterPath, QBrush, QColor

class View(QGraphicsView):
    """Custom view with selection rectangle and grid background"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.drawing_selection = False
        self.last_rect = None
        self.draw_grid_lines = True
        self.select_top_left = QPoint()
    
    def mousePressEvent(self, event):
        """Handle mouse press events for selection rectangle"""
        current_scene = self.scene()
        
        # Check if we're using the cursor tool
        from scene import Scene
        if hasattr(current_scene, 'get_tool') and (current_scene.get_tool() == Scene.Cursor):
            scene_item = self.scene().itemAt(self.mapToScene(event.position().toPoint()), self.transform())
            if not scene_item:
                self.select_top_left = event.position().toPoint()
                self.drawing_selection = True
        
        super().mousePressEvent(event)
    
    def mouseMoveEvent(self, event):
        """Handle mouse move events for selection rectangle"""
        current_scene = self.scene()
        
        # Check if we're using the cursor tool
        from scene import Scene
        if hasattr(current_scene, 'get_tool') and (current_scene.get_tool() == Scene.Cursor):
            if self.drawing_selection:
                # Selection region
                select_region = QRect(self.select_top_left, event.position().toPoint())
                
                path = QPainterPath()
                path.addRect(select_region)
                
                self.scene().setSelectionArea(self.mapToScene(path))
                
                # Draw visual feedback for the user
                item_to_remove = self.last_rect
                
                if item_to_remove:
                    self.scene().removeItem(item_to_remove)
                
                self.last_rect = self.scene().addRect(
                    QRectF(
                        self.mapToScene(self.select_top_left),
                        self.mapToScene(event.position().toPoint())
                    ).normalized()
                )
                self.last_rect.setBrush(QBrush(QColor(255, 0, 0, 50)))
                
                if item_to_remove:
                    del item_to_remove
        
        super().mouseMoveEvent(event)
    
    def mouseReleaseEvent(self, event):
        """Handle mouse release events for selection rectangle"""
        current_scene = self.scene()
        
        # Check if we're using the cursor tool
        from scene import Scene
        if hasattr(current_scene, 'get_tool') and (current_scene.get_tool() == Scene.Cursor):
            if self.drawing_selection:
                item_to_remove = self.last_rect
                if item_to_remove:
                    self.scene().removeItem(item_to_remove)
                    del item_to_remove
                    self.last_rect = None
            
            self.drawing_selection = False
        
        super().mouseReleaseEvent(event)
    
    def drawBackground(self, painter, rect):
        """Draw custom background"""
        painter.save()
        painter.setBrush(QBrush(Qt.yellow))
        painter.drawRect(-800, -600, 1600, 1200)
        painter.restore()
    
    def drawForeground(self, painter, rect):
        """Draw grid lines if enabled"""
        if self.draw_grid_lines:
            painter.save()
            # -800,-600,1600,1200
            painter.setPen(QColor(100, 44, 18, 30))
            
            # Vertical lines
            for i in range(32):
                painter.drawLine(-800 + (50 * i), -600, -800 + (50 * i), 600)
            
            # Horizontal lines
            for i in range(24):
                painter.drawLine(-800, -600 + (i * 50), 800, -600 + (i * 50))
            
            painter.restore()
        else:
            super().drawForeground(painter, rect)
    
    def get_draw_grid_lines(self):
        """Get grid lines drawing state"""
        return self.draw_grid_lines
    
    def set_draw_grid_lines(self, value):
        """Set grid lines drawing state"""
        if self.draw_grid_lines != value:
            self.draw_grid_lines = value
            self.scene().update()