from PySide6.QtWidgets import QGraphicsScene, QGraphicsItem
from PySide6.QtCore import QObject, QPointF
from PySide6.QtGui import QBrush, QColor, QPen

class Scene(QGraphicsScene):
    """
    Custom scene that handles shape drag and drop operations.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
    
    def dragMoveEvent(self, event):
        """
        Handle drag move events - accept if it's one of our shapes.
        
        Args:
            event: QGraphicsSceneDragDropEvent
        """
        # Check if the mime data has our custom format
        if event.mimeData().hasText() and event.mimeData().text().startswith("SHAPE_KEY:"):
            event.acceptProposedAction()
        else:
            super().dragMoveEvent(event)
    
    def dropEvent(self, event):
        """
        Handle drop events - create the appropriate shape.
        
        Args:
            event: QGraphicsSceneDragDropEvent
        """
        # Check if the mime data has our custom format
        if event.mimeData().hasText() and event.mimeData().text().startswith("SHAPE_KEY:"):
            # Extract the key from the custom format
            key_str = event.mimeData().text().split(":", 1)[1]
            key = int(key_str)
            
            # Import here to avoid circular imports
            from resizableellipseitem import ResizableEllipseItem
            from resizablepixmapitem import ResizablePixmapItem
            from resizablerectitem import ResizableRectItem
            from resizablestaritem import ResizableStarItem
            
            from PySide6.QtGui import QPixmap
            
            # Using QColor for gray instead of Qt.gray
            gray_brush = QBrush(QColor("gray"))
            
            if key == 10:  # Ellipse
                ellipse = ResizableEllipseItem()
                ellipse.setRect(0, 0, 80, 50)
                ellipse.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)
                ellipse.setBrush(gray_brush)
                self.addItem(ellipse)
                
                # Center on drop position
                ellipse.setPos(event.scenePos() - QPointF(ellipse.boundingRect().width()/2, 
                                                         ellipse.boundingRect().height()/2))
                
            elif key == 20:  # Qt Quick Image
                pix_item = ResizablePixmapItem(QPixmap(":/images/quick.png"))
                pix_item.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)
                self.addItem(pix_item)
                
                # Center on drop position
                pix_item.setPos(event.scenePos() - QPointF(pix_item.boundingRect().width()/2, 
                                                          pix_item.boundingRect().height()/2))
                
            elif key == 30:  # Rectangle
                rect_item = ResizableRectItem()
                rect_item.setRect(0, 0, 80, 50)
                rect_item.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable | 
                                 QGraphicsItem.ItemIsFocusable)
                rect_item.setBrush(gray_brush)
                self.addItem(rect_item)
                
                # Center on drop position
                rect_item.setPos(event.scenePos() - QPointF(rect_item.boundingRect().width()/2, 
                                                          rect_item.boundingRect().height()/2))
                
            elif key == 40:  # Star
                star_item = ResizableStarItem()
                star_item.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)
                star_item.setBrush(gray_brush)
                self.addItem(star_item)
                
                # Center on drop position
                star_item.setPos(event.scenePos() - QPointF(star_item.boundingRect().width()/2, 
                                                          star_item.boundingRect().height()/2))
            
            event.acceptProposedAction()
        else:
            super().dropEvent(event)