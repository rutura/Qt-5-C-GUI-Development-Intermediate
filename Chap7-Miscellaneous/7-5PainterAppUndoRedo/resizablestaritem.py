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
        
        painter.setPen(self.pen())
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

    def type(self):
        """Return the custom item type for this item"""
        from painterapptypes import ResizableStarType
        return ResizableStarType
    
    def write_star_item_to_stream(self, data_stream, item):
        """Write star item data to stream"""
        # Frame rect
        data_stream.writeFloat(item.rect().x())
        data_stream.writeFloat(item.rect().y())
        data_stream.writeFloat(item.rect().width())
        data_stream.writeFloat(item.rect().height())
        
        # Position
        data_stream.writeFloat(item.scenePos().x())
        data_stream.writeFloat(item.scenePos().y())
        
        # Brush color
        data_stream.writeInt16(item.brush().color().red())
        data_stream.writeInt16(item.brush().color().green())
        data_stream.writeInt16(item.brush().color().blue())
        
        # Pen color and properties
        data_stream.writeInt16(item.pen().color().red())
        data_stream.writeInt16(item.pen().color().green())
        data_stream.writeInt16(item.pen().color().blue())
        
        # Convert PenStyle enum to integer
        data_stream.writeInt16(int(item.pen().style()))
        data_stream.writeInt16(item.pen().width())
    
    def read_star_item_from_stream(self, data_stream, item):
        """Read star item data from stream"""
        # Frame rect
        rect_x = data_stream.readFloat()
        rect_y = data_stream.readFloat()
        rect_width = data_stream.readFloat()
        rect_height = data_stream.readFloat()
        
        # Position
        pos_x = data_stream.readFloat()
        pos_y = data_stream.readFloat()
        
        # Brush color
        brush_red = data_stream.readInt16()
        brush_green = data_stream.readInt16()
        brush_blue = data_stream.readInt16()
        
        # Pen color and properties
        pen_red = data_stream.readInt16()
        pen_green = data_stream.readInt16()
        pen_blue = data_stream.readInt16()
        pen_style = data_stream.readInt16()
        pen_width = data_stream.readInt16()
        
        # Set properties to item
        item.setRect(QRectF(rect_x, rect_y, rect_width, rect_height))
        item.setBrush(QBrush(QColor(brush_red, brush_green, brush_blue)))
        
        pen = QPen()
        pen.setColor(QColor(pen_red, pen_green, pen_blue))
        pen.setStyle(pen_style)
        pen.setWidth(pen_width)
        item.setPen(pen)
        
        # Set position without offset
        item.setPos(QPointF(pos_x, pos_y))