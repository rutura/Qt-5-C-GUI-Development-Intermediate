from PySide6.QtWidgets import QGraphicsRectItem
from PySide6.QtCore import QRectF, QPointF
from PySide6.QtGui import QPainter, QPainterPath, QPolygonF, QBrush

from resizablehandlerect import ResizableHandleRect

class ResizableStarItem(QGraphicsRectItem, ResizableHandleRect):
    """
    A star-shaped item that can be resized using handles on its corners
    and can accept color drag-and-drop.
    """
    def __init__(self):
        """
        Initialize the resizable star item.
        """
        QGraphicsRectItem.__init__(self)
        ResizableHandleRect.__init__(self)
        self.setRect(QRectF(10, 10, 300, 300))
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
        painter.save()
        painter.setBrush(self.brush())
        painter.drawPath(self.starFromRect(self.boundingRect()))
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
    
    def starFromRect(self, rect):
        """
        Create a star shape from a rectangle.
        
        Args:
            rect: QRectF to create the star in
        
        Returns:
            QPainterPath: Path defining the star shape
        """
        poly = QPolygonF()
        
        # 1 - Top point
        poly.append(rect.topLeft() + QPointF(rect.width()/2, 0.0))
        # 2
        poly.append(rect.topLeft() + QPointF(rect.width() * 0.7, rect.height() * 0.3))
        # 3
        poly.append(rect.topLeft() + QPointF(rect.width(), rect.height() * 0.5))
        # 4 : mirror 2
        poly.append(rect.topLeft() + QPointF(rect.width() * 0.7, rect.height() * 0.7))
        # 5
        poly.append(rect.topLeft() + QPointF(rect.width() * 0.75, rect.height()))
        # 6
        poly.append(rect.topLeft() + QPointF(rect.width() * 0.5, rect.height() * 0.75))
        # 7
        poly.append(rect.topLeft() + QPointF(rect.width() * 0.25, rect.height()))
        # 8
        poly.append(rect.topLeft() + QPointF(rect.width() * 0.3, rect.height() * 0.7))
        # 9
        poly.append(rect.topLeft() + QPointF(0, rect.height() * 0.5))
        # 10
        poly.append(rect.topLeft() + QPointF(rect.width() * 0.3, rect.height() * 0.3))
        # 1 again to close the shape
        poly.append(rect.topLeft() + QPointF(rect.width()/2, 0.0))
        
        path = QPainterPath()
        path.addPolygon(poly)
        return path
    
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