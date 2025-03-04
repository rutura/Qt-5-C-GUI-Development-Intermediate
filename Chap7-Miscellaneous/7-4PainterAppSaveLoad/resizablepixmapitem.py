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
    
    def write_pixmap_item_to_stream(self, data_stream, item):
        """Write rectangle item data to stream"""
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
    
    def read_pixmap_item_from_stream(self, data_stream, item):
        """Read pixmap item data from stream"""
        # Frame rect
        rect_x = data_stream.readFloat()
        rect_y = data_stream.readFloat()
        rect_width = data_stream.readFloat()
        rect_height = data_stream.readFloat()
        
        # Position
        pos_x = data_stream.readFloat()
        pos_y = data_stream.readFloat()
        
        # Pixmap data
        pixmap = QPixmap()
        data_stream >> pixmap
        
        # Set properties to item
        item.set_pixmap(pixmap)
        
        # Note: To keep the size of the original item that you copied,
        # setSelectorFrameBounds has to come after we set the pixmap, because
        # the pixmap is at full size and we need the copy to have whatever size
        # was in the original object.
        item.set_selector_frame_bounds(QRectF(rect_x, rect_y, rect_width, rect_height))
        
        # Set position without offset
        item.setPos(QPointF(pos_x, pos_y))