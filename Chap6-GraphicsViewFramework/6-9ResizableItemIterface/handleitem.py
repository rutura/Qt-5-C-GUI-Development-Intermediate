from PySide6.QtWidgets import QGraphicsRectItem
from PySide6.QtCore import QRectF, QPointF

class HandleItem(QGraphicsRectItem):
    """
    Handle item for resizing items in a graphics scene.
    """
    # Handle position enum
    TopLeft = 0
    TopRight = 1 
    BottomRight = 2
    BottomLeft = 3
    
    def __init__(self, position):
        """
        Initialize the handle item with a specified position.
        
        Args:
            position: One of HandleItem position constants (TopLeft, TopRight, etc.)
        """
        super().__init__()
        self.handle_position = position
        self.setFlag(QGraphicsRectItem.ItemIsMovable)
    
    def mouseMoveEvent(self, event):
        """
        Handle mouse move events to resize the parent item.
        
        Args:
            event: QGraphicsSceneMouseEvent
        """
        from resizablehandlerect import ResizableHandleRect
        
        # Try to get the parent item's ResizableHandleRect interface
        parent = self.parentItem()
        
        # We need to check if the parent implements the ResizableHandleRect interface
        if isinstance(parent, ResizableHandleRect):
            bounding_frame_rect = parent.selectorFrameBounds()
            
            if self.handle_position == HandleItem.TopLeft:
                bounding_frame_rect.setTop(event.pos().y() + 6)
                bounding_frame_rect.setLeft(event.pos().x() + 6)
                parent.setSelectorFrameBounds(bounding_frame_rect.normalized())
                
            elif self.handle_position == HandleItem.TopRight:
                bounding_frame_rect.setTop(event.pos().y() + 6)
                bounding_frame_rect.setRight(event.pos().x() - 6)
                parent.setSelectorFrameBounds(bounding_frame_rect.normalized())
                
            elif self.handle_position == HandleItem.BottomRight:
                bounding_frame_rect.setRight(event.pos().x() - 6)
                bounding_frame_rect.setBottom(event.pos().y() - 6)
                parent.setSelectorFrameBounds(bounding_frame_rect.normalized())
                
            elif self.handle_position == HandleItem.BottomLeft:
                bounding_frame_rect.setBottom(event.pos().y() - 6)
                bounding_frame_rect.setLeft(event.pos().x() + 6)
                parent.setSelectorFrameBounds(bounding_frame_rect.normalized())