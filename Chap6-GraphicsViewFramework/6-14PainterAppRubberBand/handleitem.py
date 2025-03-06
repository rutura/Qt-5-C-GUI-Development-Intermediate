from PySide6.QtWidgets import QGraphicsRectItem
from PySide6.QtCore import QRectF

class HandleItem(QGraphicsRectItem):
    """Handle item for resizing graphics items"""
    
    # Position enum
    TopLeft = 0
    TopRight = 1
    BottomRight = 2
    BottomLeft = 3
    
    def __init__(self, position):
        """Initialize with the specified handle position"""
        super().__init__()
        self.handle_position = position
        self.setFlag(QGraphicsRectItem.GraphicsItemFlag.ItemIsMovable)
    
    def mouseMoveEvent(self, event):
        """Handle mouse movement for resizing the parent item"""
        
        if self.handle_position == self.TopLeft:
            # Get parent item that should be a ResizableHandleRect
            rect_item = self.parentItem()
            if hasattr(rect_item, 'set_selector_frame_bounds') and hasattr(rect_item, 'selector_frame_bounds'):
                bounding_frame_rect = rect_item.selector_frame_bounds()
                bounding_frame_rect.setTop(event.pos().y() + 6)
                bounding_frame_rect.setLeft(event.pos().x() + 6)
                rect_item.set_selector_frame_bounds(bounding_frame_rect.normalized())
        
        elif self.handle_position == self.TopRight:
            rect_item = self.parentItem()
            if hasattr(rect_item, 'set_selector_frame_bounds') and hasattr(rect_item, 'selector_frame_bounds'):
                bounding_frame_rect = rect_item.selector_frame_bounds()
                bounding_frame_rect.setTop(event.pos().y() + 6)
                bounding_frame_rect.setRight(event.pos().x() - 6)
                rect_item.set_selector_frame_bounds(bounding_frame_rect.normalized())
        
        elif self.handle_position == self.BottomRight:
            rect_item = self.parentItem()
            if hasattr(rect_item, 'set_selector_frame_bounds') and hasattr(rect_item, 'selector_frame_bounds'):
                bounding_frame_rect = rect_item.selector_frame_bounds()
                bounding_frame_rect.setRight(event.pos().x() - 6)
                bounding_frame_rect.setBottom(event.pos().y() - 6)
                rect_item.set_selector_frame_bounds(bounding_frame_rect.normalized())
        
        elif self.handle_position == self.BottomLeft:
            rect_item = self.parentItem()
            if hasattr(rect_item, 'set_selector_frame_bounds') and hasattr(rect_item, 'selector_frame_bounds'):
                bounding_frame_rect = rect_item.selector_frame_bounds()
                bounding_frame_rect.setBottom(event.pos().y() - 6)
                bounding_frame_rect.setLeft(event.pos().x() + 6)
                rect_item.set_selector_frame_bounds(bounding_frame_rect.normalized())