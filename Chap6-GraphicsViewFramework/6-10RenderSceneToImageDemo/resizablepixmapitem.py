from PySide6.QtWidgets import QGraphicsRectItem
from PySide6.QtCore import QRectF
from PySide6.QtGui import QPainter, QPixmap

from resizablehandlerect import ResizableHandleRect

class ResizablePixmapItem(QGraphicsRectItem, ResizableHandleRect):
    """
    A pixmap item that can be resized using handles on its corners.
    """
    def __init__(self, pixmap):
        """
        Initialize the resizable pixmap item with the given pixmap.
        
        Args:
            pixmap: QPixmap to display
        """
        QGraphicsRectItem.__init__(self)
        ResizableHandleRect.__init__(self)
        self.m_pixmap = pixmap
        self.setRect(QRectF(10, 10, 300, 300))
        self.setOwnerItem(self)
    
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
        painter.save()
        painter.drawPixmap(self.boundingRect(), self.m_pixmap, self.m_pixmap.rect())
        self.drawHandlesIfNecessary()
        painter.restore()
    
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
    
    def getPixmap(self):
        """
        Get the pixmap.
        
        Returns:
            QPixmap: The pixmap
        """
        return self.m_pixmap
    
    def setPixmap(self, pixmap):
        """
        Set the pixmap.
        
        Args:
            pixmap: QPixmap to display
        """
        self.m_pixmap = pixmap
        self.update()