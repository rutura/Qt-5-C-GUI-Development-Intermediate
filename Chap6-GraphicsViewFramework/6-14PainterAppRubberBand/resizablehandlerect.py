from PySide6.QtCore import QRectF, QSize, QPointF
from PySide6.QtGui import QPen, QBrush
from PySide6.QtWidgets import QGraphicsItem
from PySide6.QtCore import Qt

class ResizableHandleRect:
    """Base class for resizable items with handles at the corners"""
    
    def __init__(self):
        self.topleft_handle_rect = QRectF()
        self.top_right_handle_rect = QRectF()
        self.bottom_right_handle_rect = QRectF()
        self.bottom_left_handle_rect = QRectF()
        
        self.handle_list = []
        self.handles_added_to_scene = False
        self.owner_item = None
    
    def draw_handles(self):
        """Draw handles at the corners of the item"""
        from handleitem import HandleItem
        
        # Populate handles in list
        if len(self.handle_list) == 0:
            self.handle_list.append(HandleItem(HandleItem.TopLeft))
            self.handle_list.append(HandleItem(HandleItem.TopRight))
            self.handle_list.append(HandleItem(HandleItem.BottomRight))
            self.handle_list.append(HandleItem(HandleItem.BottomLeft))
        
        # Set up pen
        m_pen = QPen()
        m_pen.setWidth(2)
        m_pen.setColor(Qt.black)
        
        # Top left handle
        top_left_corner = self.selector_frame_bounds().topLeft() + QPointF(-12.0, -12.0)
        self.topleft_handle_rect = QRectF(top_left_corner, QSize(12, 12))
        self.handle_list[0].setRect(self.topleft_handle_rect)
        
        if len(self.handle_list) > 0 and not self.handles_added_to_scene:
            self.handle_list[0].setPen(m_pen)
            self.handle_list[0].setBrush(QBrush(Qt.gray))
            self.owner_item.scene().addItem(self.handle_list[0])
            self.handle_list[0].setParentItem(self.owner_item)
        
        # Top right
        top_right_corner = self.selector_frame_bounds().topRight() + QPointF(0, -12.0)
        self.top_right_handle_rect = QRectF(top_right_corner, QSize(12, 12))
        self.handle_list[1].setRect(self.top_right_handle_rect)
        
        if len(self.handle_list) > 0 and not self.handles_added_to_scene:
            self.handle_list[1].setPen(m_pen)
            self.handle_list[1].setBrush(QBrush(Qt.gray))
            self.owner_item.scene().addItem(self.handle_list[1])
            self.handle_list[1].setParentItem(self.owner_item)
        
        # Bottom right
        bottom_right_corner = self.selector_frame_bounds().bottomRight() + QPointF(0, 0)
        self.bottom_right_handle_rect = QRectF(bottom_right_corner, QSize(12, 12))
        self.handle_list[2].setRect(self.bottom_right_handle_rect)
        
        if len(self.handle_list) > 0 and not self.handles_added_to_scene:
            self.handle_list[2].setPen(m_pen)
            self.handle_list[2].setBrush(QBrush(Qt.gray))
            self.owner_item.scene().addItem(self.handle_list[2])
            self.handle_list[2].setParentItem(self.owner_item)
        
        # Bottom left
        bottom_left_corner = self.selector_frame_bounds().bottomLeft() + QPointF(-12, 0)
        self.bottom_left_handle_rect = QRectF(bottom_left_corner, QSize(12, 12))
        self.handle_list[3].setRect(self.bottom_left_handle_rect)
        
        if len(self.handle_list) > 0 and not self.handles_added_to_scene:
            self.handle_list[3].setPen(m_pen)
            self.handle_list[3].setBrush(QBrush(Qt.gray))
            self.owner_item.scene().addItem(self.handle_list[3])
            self.handle_list[3].setParentItem(self.owner_item)
        
        self.handles_added_to_scene = True
    
    def set_owner_item(self, item):
        """Set the owner item of this resizable handle"""
        self.owner_item = item
    
    def draw_handles_if_necessary(self):
        """Draw handles if the item is selected, remove them otherwise"""
        if not self.owner_item:
            import warnings
            warnings.warn("ResizableHandleRect: No ownerItem set. Not drawing any handle. "
                         "Please call set_owner_item on your ResizableHandleRect subclass")
            return
        
        if self.owner_item.isSelected():
            self.draw_handles()
            self.handles_added_to_scene = True
        else:
            # Remove the handles
            for handle_item in self.handle_list:
                self.owner_item.scene().removeItem(handle_item)
            
            # Clean up handles
            self.handle_list.clear()
            self.handles_added_to_scene = False
    
    # Abstract methods to be implemented by subclasses
    def selector_frame_bounds(self):
        """Returns the bounds of the selector frame"""
        raise NotImplementedError("Subclasses must implement selector_frame_bounds")
    
    def set_selector_frame_bounds(self, bounds_rect):
        """Sets the bounds of the selector frame"""
        raise NotImplementedError("Subclasses must implement set_selector_frame_bounds")