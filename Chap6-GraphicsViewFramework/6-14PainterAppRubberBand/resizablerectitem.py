from PySide6.QtWidgets import QGraphicsRectItem
from PySide6.QtCore import QRectF
from PySide6.QtGui import QPen, QBrush
from resizablehandlerect import ResizableHandleRect

class ResizableRectItem(QGraphicsRectItem, ResizableHandleRect):
    """Resizable rectangle item with corner handles"""
    
    def __init__(self):
        QGraphicsRectItem.__init__(self)
        ResizableHandleRect.__init__(self)
        self.set_owner_item(self)
        self.setAcceptDrops(True)
    
    def boundingRect(self):
        """Return the bounding rectangle of the item"""
        return self.selector_frame_bounds()
    
    def paint(self, painter, option, widget):
        """Paint the rectangle item"""
        painter.setBrush(self.brush())
        painter.drawRect(self.rect())
        self.draw_handles_if_necessary()
    
    def selector_frame_bounds(self):
        """Return the bounds of the selector frame"""
        return self.rect()
    
    def set_selector_frame_bounds(self, bounds_rect):
        """Set the bounds of the selector frame"""
        self.prepareGeometryChange()
        self.setRect(bounds_rect)
        self.update()
    
    def dragEnterEvent(self, event):
        """Handle drag enter events for color drops"""
        if event.mimeData().hasColor():
            event.acceptProposedAction()
        else:
            super().dragEnterEvent(event)
    
    def dropEvent(self, event):
        """Handle drop events for color changes"""
        if event.mimeData().hasColor():
            color = event.mimeData().colorData()
            self.setBrush(QBrush(color))
            event.acceptProposedAction()
        else:
            super().dropEvent(event)