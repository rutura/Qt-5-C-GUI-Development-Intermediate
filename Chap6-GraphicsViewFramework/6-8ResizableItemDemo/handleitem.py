from PySide6.QtWidgets import QGraphicsRectItem
from PySide6.QtCore import QPointF, QRectF
from PySide6.QtGui import QPainter

class HandleItem(QGraphicsRectItem):
    """
    Handle item for resizing items in a graphics scene
    """
    # Enumeration for handle positions
    TopLeft = 0
    TopRight = 1
    BottomRight = 2
    BottomLeft = 3
    
    def __init__(self, position):
        """
        Initialize the handle item with a specified position
        
        Args:
            position: One of the position constants (TopLeft, TopRight, etc.)
        """
        super().__init__()
        self.handle_position = position
        self.setFlag(QGraphicsRectItem.ItemIsMovable)
    
    def mouseMoveEvent(self, event):
        """
        Handle the mouse move event to resize the parent item
        
        Args:
            event: QGraphicsSceneMouseEvent
        """
        if self.handle_position == HandleItem.TopLeft:
            # Try to cast the parent to the right type
            from resizablepixmapitem import ResizablePixmapItem
            rect_item = self.parentItem()
            
            if isinstance(rect_item, ResizablePixmapItem):
                bounding_frame_rect = rect_item.selectorFrameBounds()
                bounding_frame_rect.setTop(event.pos().y())
                bounding_frame_rect.setLeft(event.pos().x())
                rect_item.setSelectorFrameBounds(bounding_frame_rect)
        
        elif self.handle_position == HandleItem.TopRight:
            from resizablerectitem import ResizableRectItem
            rect_item = self.parentItem()
            
            if isinstance(rect_item, ResizableRectItem):
                bounding_frame_rect = rect_item.selectorFrameBounds()
                bounding_frame_rect.setTop(event.pos().y())
                bounding_frame_rect.setRight(event.pos().x())
                rect_item.setSelectorFrameBounds(bounding_frame_rect)
        
        elif self.handle_position == HandleItem.BottomRight:
            from resizablerectitem import ResizableRectItem
            rect_item = self.parentItem()
            
            if isinstance(rect_item, ResizableRectItem):
                bounding_frame_rect = rect_item.selectorFrameBounds()
                bounding_frame_rect.setRight(event.pos().x())
                bounding_frame_rect.setBottom(event.pos().y())
                rect_item.setSelectorFrameBounds(bounding_frame_rect)
        
        elif self.handle_position == HandleItem.BottomLeft:
            from resizablerectitem import ResizableRectItem
            rect_item = self.parentItem()
            
            if isinstance(rect_item, ResizableRectItem):
                bounding_frame_rect = rect_item.selectorFrameBounds()
                bounding_frame_rect.setBottom(event.pos().y())
                bounding_frame_rect.setLeft(event.pos().x())
                rect_item.setSelectorFrameBounds(bounding_frame_rect)