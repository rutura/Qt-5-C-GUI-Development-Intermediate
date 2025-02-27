from PySide6.QtWidgets import QGraphicsRectItem
from PySide6.QtCore import QRectF
from PySide6.QtGui import QPainter, QBrush

from resizablehandlerect import ResizableHandleRect

class ResizableRectItem(QGraphicsRectItem, ResizableHandleRect):
    """
    A rectangle item that can be resized using handles on its corners
    and can accept color drag-and-drop.
    """
    def __init__(self):
        """
        Initialize the resizable rectangle item.
        """
        QGraphicsRectItem.__init__(self)
        ResizableHandleRect.__init__(self)
        self.setOwnerItem(self)
        self.setAcceptDrops(True)
    
    def boundingRect(self):
        """
        Get the bounding rectangle of the item.
        
        Returns:
            QRectF: The bounding rectangle
        """
        return self.selectorFrameBounds()
    
    def paint(self, painter, option, widget):
        """
        Paint the item.
        
        Args:
            painter: QPainter
            option: QStyleOptionGraphicsItem
            widget: QWidget
        """
        painter.setBrush(self.brush())
        painter.drawRect(self.rect())
        self.drawHandlesIfNecessary()
    
    def selectorFrameBounds(self):
        """
        Get the bounds of the selector frame.
        
        Returns:
            QRectF: The bounds rectangle
        """
        return self.rect()
    
    def setSelectorFrameBounds(self, bounds_rect):
        """
        Set the bounds of the selector frame.
        
        Args:
            bounds_rect: QRectF with the new bounds
        """
        self.prepareGeometryChange()
        self.setRect(bounds_rect)
        self.update()
    
    def dragEnterEvent(self, event):
        """
        Handle drag enter events - accept if the dragged item is a color.
        
        Args:
            event: QGraphicsSceneDragDropEvent
        """
        if event.mimeData().hasColor():
            event.acceptProposedAction()
        else:
            super().dragEnterEvent(event)
    
    def dropEvent(self, event):
        """
        Handle drop events - change the brush color if a color was dropped.
        
        Args:
            event: QGraphicsSceneDragDropEvent
        """
        if event.mimeData().hasColor():
            color = event.mimeData().colorData()
            self.setBrush(QBrush(color))
            event.acceptProposedAction()
        else:
            super().dropEvent(event)