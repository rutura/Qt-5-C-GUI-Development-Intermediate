from PySide6.QtCore import QRectF, QSize, QPointF
from PySide6.QtGui import QPen, QBrush, QColor
import warnings

class ResizableHandleRect:
    """
    A mixin class that provides resizable handle functionality for QGraphicsItem subclasses.
    This should be used through multiple inheritance alongside a QGraphicsItem class.
    """
    def __init__(self):
        self.handle_list = []
        self.handles_added_to_scene = False
        self.owner_item = None
        
        # Initialize handle rects
        self.topleft_handle_rect = QRectF()
        self.topright_handle_rect = QRectF()
        self.bottomright_handle_rect = QRectF()
        self.bottomleft_handle_rect = QRectF()
    
    def __del__(self):
        """
        Clean up resources when the object is destroyed.
        """
        pass
    
    def selectorFrameBounds(self):
        """
        Get the bounds of the selector frame - must be implemented by subclasses.
        
        Returns:
            QRectF: The bounds rectangle
        """
        raise NotImplementedError("Subclasses must implement selectorFrameBounds")
    
    def setSelectorFrameBounds(self, bounds_rect):
        """
        Set the bounds of the selector frame - must be implemented by subclasses.
        
        Args:
            bounds_rect: QRectF with the new bounds
        """
        raise NotImplementedError("Subclasses must implement setSelectorFrameBounds")
    
    def setOwnerItem(self, item):
        """
        Set the owner item for this resizable handle rectangle.
        
        Args:
            item: QGraphicsItem that will own these handles
        """
        self.owner_item = item
    
    def drawHandlesIfNecessary(self):
        """
        Draw handles if the item is selected, remove them otherwise.
        """
        if not self.owner_item:
            warnings.warn("ResizableHandleRect: No ownerItem set. Not drawing any "
                       "handle. Please call setOwnerItem on your ResizableHandleRect subclass")
            return
        
        if self.owner_item.isSelected():
            self.drawHandles()
            self.handles_added_to_scene = True
        else:
            # Remove the handles
            for handle_item in self.handle_list:
                self.owner_item.scene().removeItem(handle_item)
            
            # Clear the handle list
            for item in self.handle_list:
                del item
            self.handle_list.clear()
            self.handles_added_to_scene = False
    
    def drawHandles(self):
        """
        Draw the handles for resizing.
        """
        from handleitem import HandleItem
        
        # Populate handles in list if empty
        if len(self.handle_list) == 0:
            self.handle_list.append(HandleItem(HandleItem.TopLeft))
            self.handle_list.append(HandleItem(HandleItem.TopRight))
            self.handle_list.append(HandleItem(HandleItem.BottomRight))
            self.handle_list.append(HandleItem(HandleItem.BottomLeft))
        
        # Set up pen
        pen = QPen()
        pen.setWidth(2)
        pen.setColor(QColor(0, 0, 0))  # Qt::black
        
        # Top left handle
        top_left_corner = self.selectorFrameBounds().topLeft() + QPointF(-12.0, -12.0)
        self.topleft_handle_rect = QRectF(top_left_corner, QSize(12, 12))
        self.handle_list[0].setRect(self.topleft_handle_rect)
        
        if self.handle_list and not self.handles_added_to_scene:
            self.handle_list[0].setPen(pen)
            self.handle_list[0].setBrush(QBrush(QColor(128, 128, 128)))  # Qt::gray
            self.owner_item.scene().addItem(self.handle_list[0])
            self.handle_list[0].setParentItem(self.owner_item)
        
        # Top right handle
        top_right_corner = self.selectorFrameBounds().topRight() + QPointF(0, -12.0)
        self.topright_handle_rect = QRectF(top_right_corner, QSize(12, 12))
        self.handle_list[1].setRect(self.topright_handle_rect)
        
        if self.handle_list and not self.handles_added_to_scene:
            self.handle_list[1].setPen(pen)
            self.handle_list[1].setBrush(QBrush(QColor(128, 128, 128)))  # Qt::gray
            self.owner_item.scene().addItem(self.handle_list[1])
            self.handle_list[1].setParentItem(self.owner_item)
        
        # Bottom right handle
        bottom_right_corner = self.selectorFrameBounds().bottomRight() + QPointF(0, 0)
        self.bottomright_handle_rect = QRectF(bottom_right_corner, QSize(12, 12))
        self.handle_list[2].setRect(self.bottomright_handle_rect)
        
        if self.handle_list and not self.handles_added_to_scene:
            self.handle_list[2].setPen(pen)
            self.handle_list[2].setBrush(QBrush(QColor(128, 128, 128)))  # Qt::gray
            self.owner_item.scene().addItem(self.handle_list[2])
            self.handle_list[2].setParentItem(self.owner_item)
        
        # Bottom left handle
        bottom_left_corner = self.selectorFrameBounds().bottomLeft() + QPointF(-12, 0)
        self.bottomleft_handle_rect = QRectF(bottom_left_corner, QSize(12, 12))
        self.handle_list[3].setRect(self.bottomleft_handle_rect)
        
        if self.handle_list and not self.handles_added_to_scene:
            self.handle_list[3].setPen(pen)
            self.handle_list[3].setBrush(QBrush(QColor(128, 128, 128)))  # Qt::gray
            self.owner_item.scene().addItem(self.handle_list[3])
            self.handle_list[3].setParentItem(self.owner_item)
        
        self.handles_added_to_scene = True