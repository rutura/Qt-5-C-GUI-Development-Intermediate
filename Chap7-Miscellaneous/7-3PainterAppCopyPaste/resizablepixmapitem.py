from PySide6.QtWidgets import QGraphicsRectItem
from PySide6.QtCore import QRectF
from PySide6.QtGui import QPen, QBrush
from resizablehandlerect import ResizableHandleRect

class ResizablePixmapItem(QGraphicsRectItem, ResizableHandleRect):
    """Resizable pixmap item with corner handles"""
    
    def __init__(self, pixmap):
        QGraphicsRectItem.__init__(self)
        ResizableHandleRect.__init__(self)
        self.m_pixmap = pixmap
        self.setRect(QRectF(10, 10, 300, 300))
        self.set_owner_item(self)
    
    def selector_frame_bounds(self):
        """Return the bounds of the selector frame"""
        return self.rect()
    
    def set_selector_frame_bounds(self, bounds_rect):
        """Set the bounds of the selector frame"""
        self.prepareGeometryChange()
        self.setRect(bounds_rect)
        self.update()
    
    def boundingRect(self):
        """Return the bounding rectangle of the item"""
        return self.selector_frame_bounds()
    
    def paint(self, painter, option, widget):
        """Paint the pixmap item"""
        painter.save()
        
        painter.drawPixmap(self.boundingRect(), self.m_pixmap, self.m_pixmap.rect())
        
        self.draw_handles_if_necessary()
        
        painter.restore()
    
    def get_pixmap(self):
        """Get the pixmap"""
        return self.m_pixmap
    
    def set_pixmap(self, value):
        """Set the pixmap"""
        self.m_pixmap = value
    
    def type(self):
        """Return the custom item type for this item"""
        from painterapptypes import ResizablePixmapType
        return ResizablePixmapType