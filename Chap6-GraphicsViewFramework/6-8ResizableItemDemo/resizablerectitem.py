from PySide6.QtWidgets import QGraphicsRectItem, QGraphicsItem
from PySide6.QtCore import QRectF, QPointF, QSize
from PySide6.QtGui import QPen, QBrush, QPainter, QColor

class ResizableRectItem(QGraphicsRectItem):
    """
    A rectangle item that can be resized using handles on its corners
    """
    def __init__(self):
        super().__init__()
        self.handles_added_to_scene = False
        self.handle_list = []
        
        # Initialize handle rects
        self.topleft_handle_rect = QRectF()
        self.topright_handle_rect = QRectF()
        self.bottomright_handle_rect = QRectF()
        self.bottomleft_handle_rect = QRectF()
    
    def selectorFrameBounds(self):
        """
        Get the bounds of the selector frame
        
        Returns:
            QRectF: The bounds rectangle
        """
        return self.rect()
    
    def setSelectorFrameBounds(self, bounds_rect):
        """
        Set the bounds of the selector frame
        
        Args:
            bounds_rect: QRectF with the new bounds
        """
        self.prepareGeometryChange()
        self.setRect(bounds_rect)
        self.update()
    
    def boundingRect(self):
        """
        Get the bounding rectangle of the item
        
        Returns:
            QRectF: The bounding rectangle
        """
        return self.selectorFrameBounds()
    
    def paint(self, painter, option, widget):
        """
        Paint the item
        
        Args:
            painter: QPainter
            option: QStyleOptionGraphicsItem
            widget: QWidget
        """
        painter.save()
        painter.setBrush(self.brush())
        painter.drawRect(self.rect())
        self.drawHandlesIfNecessary()
        painter.restore()
    
    def drawHandlesIfNecessary(self):
        """
        Draw handles if the item is selected, remove them otherwise
        """
        if self.isSelected():
            self.drawHandles()
            self.handles_added_to_scene = True
        else:
            # Remove the handles
            for handle_item in self.handle_list:
                self.scene().removeItem(handle_item)
            
            # Clear the list after removing handles
            self.handle_list.clear()
            self.handles_added_to_scene = False
    
    def drawHandles(self):
        """
        Draw the handles for resizing
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
        top_left_corner = self.boundingRect().topLeft() + QPointF(-12.0, -12.0)
        self.topleft_handle_rect = QRectF(top_left_corner, QSize(12, 12))
        self.handle_list[0].setRect(self.topleft_handle_rect)
        
        if len(self.handle_list) > 0 and not self.handles_added_to_scene:
            self.handle_list[0].setPen(pen)
            self.handle_list[0].setBrush(QBrush(QColor(128, 128, 128)))  # Qt::gray
            self.scene().addItem(self.handle_list[0])
            self.handle_list[0].setParentItem(self)
        
        # Top right handle
        top_right_corner = self.boundingRect().topRight() + QPointF(0, -12.0)
        self.topright_handle_rect = QRectF(top_right_corner, QSize(12, 12))
        self.handle_list[1].setRect(self.topright_handle_rect)
        
        if len(self.handle_list) > 0 and not self.handles_added_to_scene:
            self.handle_list[1].setPen(pen)
            self.handle_list[1].setBrush(QBrush(QColor(128, 128, 128)))  # Qt::gray
            self.scene().addItem(self.handle_list[1])
            self.handle_list[1].setParentItem(self)
        
        # Bottom right handle
        bottom_right_corner = self.boundingRect().bottomRight() + QPointF(0, 0)
        self.bottomright_handle_rect = QRectF(bottom_right_corner, QSize(12, 12))
        self.handle_list[2].setRect(self.bottomright_handle_rect)
        
        if len(self.handle_list) > 0 and not self.handles_added_to_scene:
            self.handle_list[2].setPen(pen)
            self.handle_list[2].setBrush(QBrush(QColor(128, 128, 128)))  # Qt::gray
            self.scene().addItem(self.handle_list[2])
            self.handle_list[2].setParentItem(self)
        
        # Bottom left handle
        bottom_left_corner = self.boundingRect().bottomLeft() + QPointF(-12, 0)
        self.bottomleft_handle_rect = QRectF(bottom_left_corner, QSize(12, 12))
        self.handle_list[3].setRect(self.bottomleft_handle_rect)
        
        if len(self.handle_list) > 0 and not self.handles_added_to_scene:
            self.handle_list[3].setPen(pen)
            self.handle_list[3].setBrush(QBrush(QColor(128, 128, 128)))  # Qt::gray
            self.scene().addItem(self.handle_list[3])
            self.handle_list[3].setParentItem(self)
        
        self.handles_added_to_scene = True