from PySide6.QtWidgets import QGraphicsRectItem
from PySide6.QtCore import QRectF, QPointF
from PySide6.QtGui import QPen, QBrush, QPainterPath, QPolygonF
from resizablehandlerect import ResizableHandleRect

class ResizableStarItem(QGraphicsRectItem, ResizableHandleRect):
    """Resizable star item with corner handles"""
    
    def __init__(self):
        QGraphicsRectItem.__init__(self)
        ResizableHandleRect.__init__(self)
        self.setRect(QRectF(10, 10, 300, 300))
        self.set_owner_item(self)
        self.setAcceptDrops(True)
    
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
        """Paint the star item"""
        painter.save()
        
        painter.setBrush(self.brush())
        painter.drawPath(self.star_from_rect(self.boundingRect()))
        
        self.draw_handles_if_necessary()
        
        painter.restore()
    
    def star_from_rect(self, m_rect_f):
        """Create a star path from the given rectangle"""
        poly = QPolygonF()
        
        # 1
        poly.append(m_rect_f.topLeft() + QPointF(m_rect_f.width()/2, 0.0))
        # 2
        poly.append(m_rect_f.topLeft() + QPointF(m_rect_f.width() * 0.7, m_rect_f.height() * 0.3))
        # 3
        poly.append(m_rect_f.topLeft() + QPointF(m_rect_f.width(), m_rect_f.height() * 0.5))
        # 4 : mirror 2
        poly.append(m_rect_f.topLeft() + QPointF(m_rect_f.width() * 0.7, m_rect_f.height() * 0.7))
        # 5
        poly.append(m_rect_f.topLeft() + QPointF(m_rect_f.width() * 0.75, m_rect_f.height()))
        # 6
        poly.append(m_rect_f.topLeft() + QPointF(m_rect_f.width() * 0.5, m_rect_f.height() * 0.75))
        # 7
        poly.append(m_rect_f.topLeft() + QPointF(m_rect_f.width() * 0.25, m_rect_f.height()))
        # 8
        poly.append(m_rect_f.topLeft() + QPointF(m_rect_f.width() * 0.3, m_rect_f.height() * 0.7))
        # 9
        poly.append(m_rect_f.topLeft() + QPointF(0, m_rect_f.height() * 0.5))
        # 10
        poly.append(m_rect_f.topLeft() + QPointF(m_rect_f.width() * 0.3, m_rect_f.height() * 0.3))
        # 1 again to close the path
        poly.append(m_rect_f.topLeft() + QPointF(m_rect_f.width()/2, 0.0))
        
        path = QPainterPath()
        path.addPolygon(poly)
        return path
    
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