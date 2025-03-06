from PySide6.QtWidgets import (QGraphicsScene, QGraphicsItemGroup, 
                              QGraphicsEllipseItem, QGraphicsLineItem, QGraphicsItem,
                              QApplication)
from PySide6.QtCore import Qt, QPointF, QRectF, QLineF, QMimeData, QByteArray, QDataStream, QIODevice
from PySide6.QtGui import QPen, QBrush, QColor, QClipboard, QPixmap

# Import the stroke item class
from strokeitem import StrokeItem

# Define the mime type for our custom clipboard content
MIME_TYPE = "application/com.blikoontech.painterapp"

# Define item types (from painterapptypes.h)
ResizableRectType = QGraphicsItem.UserType + 1
ResizableEllipseType = QGraphicsItem.UserType + 2
ResizablePixmapType = QGraphicsItem.UserType + 3
ResizableStarType = QGraphicsItem.UserType + 4
StrokeType = QGraphicsItem.UserType + 5

class Scene(QGraphicsScene):
    """Custom scene for the drawing application with copy/paste functionality"""
    
    # Tool type enumeration
    Cursor = 0
    Pen = 1
    Rect = 2
    Ellipse = 3
    Star = 4
    QtQuick = 5
    Eraser = 6
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Initialize properties
        self.tool = self.Cursor
        self.drawing = False
        self.line_group = None
        self.last_eraser_circle = None
        self.last_item = None
        self.starting_point = QPointF()
        self.last_pen_point = QPointF()
        
        # Set pen and brush properties
        self.pen_color = QColor(Qt.GlobalColor.black)
        self.pen_width = 2
        self.pen_style = Qt.PenStyle.SolidLine
        self.fill_color = QColor(Qt.GlobalColor.gray)
        self.brush_style = Qt.BrushStyle.SolidPattern
        
        # Set up guide lines
        self.hor_guide_line = self.addLine(-400, 0, 400, 0, QPen(QColor(Qt.GlobalColor.blue)))
        self.ver_guide_line = self.addLine(0, -400, 0, 400, QPen(QColor(Qt.GlobalColor.blue)))
        self.setSceneRect(-800, -600, 1600, 1200)
    
    def dragMoveEvent(self, event):
        """Handle drag move events for shape dragging"""
        # In PySide6, use hasFormat or property() method instead of hasProperty
        if hasattr(event.mimeData(), "property") and event.mimeData().property("Key") is not None:
            event.acceptProposedAction()
        elif event.mimeData().hasText():
            event.acceptProposedAction()
        else:
            super().dragMoveEvent(event)
    
    def dropEvent(self, event):
        """Handle drop events for creating shapes"""
        key = None
        # Try to get key from property or text
        if hasattr(event.mimeData(), "property") and event.mimeData().property("Key") is not None:
            key = event.mimeData().property("Key")
        elif event.mimeData().hasText():
            try:
                key = int(event.mimeData().text())
            except:
                pass
        
        if key is not None:
            # Create pen and brush for the new shape
            m_pen = QPen()
            m_pen.setColor(self.pen_color)
            m_pen.setWidth(self.pen_width)
            m_pen.setStyle(self.pen_style)
            
            m_brush = QBrush()
            m_brush.setColor(self.fill_color)
            m_brush.setStyle(self.brush_style)
            
            if key == 10:  # Ellipse
                from resizableellipseitem import ResizableEllipseItem
                ellipse = ResizableEllipseItem()
                ellipse.setRect(0, 0, 80, 50)
                ellipse.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsMovable | 
                                QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
                ellipse.setBrush(m_brush)
                ellipse.setPen(m_pen)
                self.addItem(ellipse)
                ellipse.setPos(event.scenePos() - QPointF(ellipse.boundingRect().width()/2,
                                                       ellipse.boundingRect().height()/2))
            
            elif key == 20:  # Qt Quick Image
                from resizablepixmapitem import ResizablePixmapItem
                from PySide6.QtGui import QPixmap
                pix_item = ResizablePixmapItem(QPixmap(":/images/quick.png"))
                pix_item.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsMovable | 
                                QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
                pix_item.setPen(m_pen)
                self.addItem(pix_item)
                pix_item.setPos(event.scenePos() - QPointF(pix_item.boundingRect().width()/2,
                                                        pix_item.boundingRect().height()/2))
            
            elif key == 30:  # Rectangle
                from resizablerectitem import ResizableRectItem
                rect_item = ResizableRectItem()
                rect_item.setRect(0, 0, 80, 50)
                rect_item.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsMovable | 
                                QGraphicsItem.GraphicsItemFlag.ItemIsSelectable | 
                                QGraphicsItem.GraphicsItemFlag.ItemIsFocusable)
                rect_item.setBrush(m_brush)
                rect_item.setPen(m_pen)
                self.addItem(rect_item)
                rect_item.setPos(event.scenePos() - QPointF(rect_item.boundingRect().width()/2,
                                                        rect_item.boundingRect().height()/2))
            
            elif key == 40:  # Star
                from resizablestaritem import ResizableStarItem
                star_item = ResizableStarItem()
                star_item.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsMovable | 
                                QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
                star_item.setBrush(m_brush)
                star_item.setPen(m_pen)
                self.addItem(star_item)
                star_item.setPos(event.scenePos() - QPointF(star_item.boundingRect().width()/2,
                                                        star_item.boundingRect().height()/2))
            
            event.acceptProposedAction()
        else:
            super().dropEvent(event)
    
    def mousePressEvent(self, event):
        """Handle mouse press events for drawing"""
        if event.button() == Qt.MouseButton.LeftButton:
            if self.tool in [self.Pen, self.Eraser, self.Rect, self.Star, self.Ellipse]:
                self.starting_point = event.scenePos()
                self.drawing = True
            else:
                super().mousePressEvent(event)
        else:
            super().mousePressEvent(event)
    
    def mouseMoveEvent(self, event):
        """Handle mouse move events for drawing"""
        if (event.buttons() & Qt.MouseButton.LeftButton) and self.drawing:
            if self.tool == self.Pen:
                self.draw_line_to(event.scenePos())
            elif self.tool == self.Eraser:
                self.draw_eraser_at(event.scenePos())
            else:
                self.draw_shape_to(event.scenePos())
        else:
            super().mouseMoveEvent(event)
    
    def mouseReleaseEvent(self, event):
        """Handle mouse release events for finalizing drawings"""
        if (event.button() == Qt.MouseButton.LeftButton) and self.drawing:
            # Create pen and brush for the new shape
            m_pen = QPen()
            m_pen.setColor(self.pen_color)
            m_pen.setWidth(self.pen_width)
            m_pen.setStyle(self.pen_style)
            
            m_brush = QBrush()
            m_brush.setColor(self.fill_color)
            m_brush.setStyle(self.brush_style)
            
            if self.last_item and (self.tool in [self.Rect, self.Ellipse, self.Star]):
                self.removeItem(self.last_item)
                del self.last_item
                self.last_item = None
            
            if self.tool == self.Pen:
                self.line_group = None
                self.drawing = False
            
            elif self.tool == self.Eraser:
                if self.last_eraser_circle:
                    self.removeItem(self.last_eraser_circle)
                    del self.last_eraser_circle
                    self.last_eraser_circle = None
                self.drawing = False
            
            elif self.tool == self.Rect:
                from resizablerectitem import ResizableRectItem
                m_rect = ResizableRectItem()
                m_rect.setRect(QRectF(self.starting_point, event.scenePos()).normalized())
                m_rect.setBrush(m_brush)
                m_rect.setPen(m_pen)
                m_rect.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsMovable | 
                               QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
                self.addItem(m_rect)
                self.drawing = False
            
            elif self.tool == self.Ellipse:
                from resizableellipseitem import ResizableEllipseItem
                ellipse_item = ResizableEllipseItem()
                ellipse_item.setRect(QRectF(self.starting_point, event.scenePos()).normalized())
                ellipse_item.setBrush(m_brush)
                ellipse_item.setPen(m_pen)
                ellipse_item.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsMovable | 
                                     QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
                self.addItem(ellipse_item)
                self.drawing = False
            
            elif self.tool == self.Star:
                from resizablestaritem import ResizableStarItem
                star_item = ResizableStarItem()
                star_item.setRect(QRectF(self.starting_point, event.scenePos()).normalized())
                star_item.setBrush(m_brush)
                star_item.setPen(m_pen)
                star_item.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsMovable | 
                                  QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
                self.addItem(star_item)
                self.drawing = False
        
        else:
            super().mouseReleaseEvent(event)
    
    def keyPressEvent(self, event):
        """Handle key press events for item deletion"""
        if event.key() == Qt.Key.Key_Delete:
            if len(self.selectedItems()) > 0:
                item_to_remove = self.selectedItems()[0]
                self.removeItem(item_to_remove)
                del item_to_remove
        
        super().keyPressEvent(event)
    
    def draw_line_to(self, end_point):
        """Draw a line from the last point to the end point"""
        if not self.line_group:
            self.line_group = StrokeItem()
            self.line_group.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsMovable | 
                                    QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
            self.addItem(self.line_group)
            self.last_pen_point = self.starting_point
        
        local_line = QGraphicsLineItem(QLineF(self.last_pen_point, end_point))
        m_pen = QPen()
        m_pen.setWidth(self.pen_width)
        m_pen.setColor(self.pen_color)
        m_pen.setStyle(self.pen_style)
        local_line.setPen(m_pen)
        self.line_group.addToGroup(local_line)
        
        self.last_pen_point = end_point
    
    def draw_eraser_at(self, end_point):
        """Draw an eraser circle at the end point"""
        if not self.last_eraser_circle:
            self.last_eraser_circle = self.addEllipse(0, 0, 50, 50)
        
        self.last_eraser_circle.setPos(end_point - QPointF(self.last_eraser_circle.boundingRect().width()/2,
                                                          self.last_eraser_circle.boundingRect().height()/2))
        self.erase_strokes_under(self.last_eraser_circle)
    
    def erase_strokes_under(self, item):
        """Erase strokes under the eraser circle"""
        items_to_remove = item.collidingItems()
        group_items = []
        
        for my_item in items_to_remove:
            if isinstance(my_item, QGraphicsItemGroup):
                group_items.append(my_item)
            
            if (isinstance(my_item, QGraphicsLineItem) and 
                my_item != self.hor_guide_line and 
                my_item != self.ver_guide_line):
                self.removeItem(my_item)
                del my_item
        
        # Remove group items that don't have any children
        for group in group_items:
            if len(group.childItems()) == 0:
                print("Group item has no child. Removing it")
                self.removeItem(group)
                del group
    
    def draw_shape_to(self, end_point):
        """Draw a shape from the starting point to the end point"""
        if self.last_item:
            self.removeItem(self.last_item)
            del self.last_item
        
        # Create pen and brush for the new shape
        m_pen = QPen()
        m_pen.setColor(self.pen_color)
        m_pen.setWidth(self.pen_width)
        m_pen.setStyle(self.pen_style)
        
        m_brush = QBrush()
        m_brush.setColor(self.fill_color)
        m_brush.setStyle(self.brush_style)
        
        item_rect = QRectF(self.starting_point, end_point).normalized()
        
        if self.tool == self.Rect:
            from resizablerectitem import ResizableRectItem
            m_rect = ResizableRectItem()
            m_rect.setRect(item_rect)
            m_rect.setBrush(m_brush)
            m_rect.setPen(m_pen)
            self.addItem(m_rect)
            m_rect.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsMovable | 
                           QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
            self.last_item = m_rect
        
        elif self.tool == self.Ellipse:
            from resizableellipseitem import ResizableEllipseItem
            ellipse_item = ResizableEllipseItem()
            ellipse_item.setRect(item_rect)
            ellipse_item.setBrush(m_brush)
            ellipse_item.setPen(m_pen)
            self.addItem(ellipse_item)
            ellipse_item.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsMovable | 
                                 QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
            self.last_item = ellipse_item
        
        elif self.tool == self.Star:
            from resizablestaritem import ResizableStarItem
            star_item = ResizableStarItem()
            star_item.setRect(item_rect)
            star_item.setBrush(m_brush)
            star_item.setPen(m_pen)
            self.addItem(star_item)
            star_item.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsMovable | 
                              QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
            self.last_item = star_item
    
    def copy(self):
        """Copy selected items to clipboard"""
        if not self.selectedItems():
            return
            
        byte_array = QByteArray()
        data_stream = QDataStream(byte_array, QIODevice.WriteOnly)
        
        # Write selected items to data stream
        self.write_items_to_data_stream(data_stream, self.selectedItems())
        
        # Create mime data and set it to clipboard
        mime_data = QMimeData()
        mime_data.setData(MIME_TYPE, byte_array)
        
        # Get system clipboard and set mime data
        clipboard = QApplication.clipboard()
        clipboard.setMimeData(mime_data)
    
    def cut(self):
        """Cut selected items to clipboard and remove them from scene"""
        if not self.selectedItems():
            return
            
        # First copy items to clipboard
        self.copy()
        
        # Then remove the items from scene
        for item in self.selectedItems():
            self.removeItem(item)
            del item
    
    def paste(self):
        """Paste items from clipboard to scene"""
        clipboard = QApplication.clipboard()
        mime_data = clipboard.mimeData()
        
        if not mime_data or not mime_data.hasFormat(MIME_TYPE):
            return
            
        # Get byte array from mime data
        byte_array = mime_data.data(MIME_TYPE)
        data_stream = QDataStream(byte_array, QIODevice.ReadOnly)
        
        # Read items from data stream and add to scene
        self.read_items_from_data_stream(data_stream)
    
    def write_items_to_data_stream(self, data_stream, items):
        """Write items to data stream for copying"""
        for item in items:
            # Write item type
            item_type = item.type()
            data_stream.writeInt32(item_type)
            
            # Write item-specific data based on type
            if item_type == ResizableRectType:
                from resizablerectitem import ResizableRectItem
                self.write_rect_item_to_stream(data_stream, item)
            elif item_type == ResizableEllipseType:
                from resizableellipseitem import ResizableEllipseItem
                self.write_ellipse_item_to_stream(data_stream, item)
            elif item_type == ResizablePixmapType:
                from resizablepixmapitem import ResizablePixmapItem
                self.write_pixmap_item_to_stream(data_stream, item)
            elif item_type == ResizableStarType:
                from resizablestaritem import ResizableStarItem
                self.write_star_item_to_stream(data_stream, item)
            elif item_type == StrokeType:
                self.write_stroke_item_to_stream(data_stream, item)
    
    def write_rect_item_to_stream(self, data_stream, item):
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
        data_stream.writeInt16(item.pen().style())
        data_stream.writeInt16(item.pen().width())
    
    def write_ellipse_item_to_stream(self, data_stream, item):
        """Write ellipse item data to stream"""
        # Similar to rectangle item
        self.write_rect_item_to_stream(data_stream, item)
    
    def write_star_item_to_stream(self, data_stream, item):
        """Write star item data to stream"""
        # Similar to rectangle item
        self.write_rect_item_to_stream(data_stream, item)
    
    def write_pixmap_item_to_stream(self, data_stream, item):
        """Write pixmap item data to stream"""
        # Frame rect
        data_stream.writeFloat(item.rect().x())
        data_stream.writeFloat(item.rect().y())
        data_stream.writeFloat(item.rect().width())
        data_stream.writeFloat(item.rect().height())
        
        # Position
        data_stream.writeFloat(item.scenePos().x())
        data_stream.writeFloat(item.scenePos().y())
        
        # Pixmap data
        data_stream << item.get_pixmap()
    
    def write_stroke_item_to_stream(self, data_stream, item):
        """Write stroke item data to stream"""
        # Use the StrokeItem's to_data_stream method
        item.to_data_stream(data_stream)
    
    def read_items_from_data_stream(self, data_stream):
        """Read items from data stream for pasting"""
        # Clear selection for new pasted items
        self.clearSelection()
        
        while not data_stream.atEnd():
            # Read item type
            item_type = data_stream.readInt32()
            
            # Create and configure item based on its type
            if item_type == ResizableRectType:
                from resizablerectitem import ResizableRectItem
                rect_item = ResizableRectItem()
                self.read_rect_item_from_stream(data_stream, rect_item)
                rect_item.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsMovable | 
                                  QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
                self.addItem(rect_item)
                rect_item.setSelected(True)
            
            elif item_type == ResizableEllipseType:
                from resizableellipseitem import ResizableEllipseItem
                ellipse_item = ResizableEllipseItem()
                self.read_ellipse_item_from_stream(data_stream, ellipse_item)
                ellipse_item.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsMovable | 
                                     QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
                self.addItem(ellipse_item)
                ellipse_item.setSelected(True)
            
            elif item_type == ResizablePixmapType:
                from resizablepixmapitem import ResizablePixmapItem
                from PySide6.QtGui import QPixmap
                pixmap_item = ResizablePixmapItem(QPixmap())
                self.read_pixmap_item_from_stream(data_stream, pixmap_item)
                pixmap_item.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsMovable | 
                                    QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
                self.addItem(pixmap_item)
                pixmap_item.setSelected(True)
            
            elif item_type == ResizableStarType:
                from resizablestaritem import ResizableStarItem
                star_item = ResizableStarItem()
                self.read_star_item_from_stream(data_stream, star_item)
                star_item.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsMovable | 
                                  QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
                self.addItem(star_item)
                star_item.setSelected(True)
            
            elif item_type == StrokeType:
                stroke_item = StrokeItem()
                self.read_stroke_item_from_stream(data_stream, stroke_item)
                stroke_item.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsMovable | 
                                    QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
                self.addItem(stroke_item)
                stroke_item.setSelected(True)
    
    def read_rect_item_from_stream(self, data_stream, item):
        """Read rectangle item data from stream"""
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
        
        # Set position with a small offset to make it visible it's a copy
        item.setPos(QPointF(pos_x, pos_y) + QPointF(10, 10))
    
    def read_ellipse_item_from_stream(self, data_stream, item):
        """Read ellipse item data from stream"""
        # Similar to rectangle item
        self.read_rect_item_from_stream(data_stream, item)
    
    def read_star_item_from_stream(self, data_stream, item):
        """Read star item data from stream"""
        # Similar to rectangle item
        self.read_rect_item_from_stream(data_stream, item)
    
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
        item.setRect(QRectF(rect_x, rect_y, rect_width, rect_height))
        item.set_pixmap(pixmap)
        
        # Set position with a small offset to make it visible it's a copy
        item.setPos(QPointF(pos_x, pos_y) + QPointF(10, 10))
    
    def read_stroke_item_from_stream(self, data_stream, item):
        """Read stroke item data from stream"""
        # Use the StrokeItem's from_data_stream method
        item.from_data_stream(data_stream)
    
    def getPenColor(self):
        """Get the current pen color"""
        return self.pen_color
    
    def setPenColor(self, value):
        """Set the current pen color"""
        self.pen_color = value
    
    def getFillColor(self):
        """Get the current fill color"""
        return self.fill_color
    
    def setFillColor(self, value):
        """Set the current fill color"""
        self.fill_color = value
    
    def getPenWidth(self):
        """Get the current pen width"""
        return self.pen_width
    
    def setPenWidth(self, value):
        """Set the current pen width"""
        self.pen_width = value
    
    def getPenStyle(self):
        """Get the current pen style"""
        return self.pen_style
    
    def setPenStyle(self, value):
        """Set the current pen style"""
        self.pen_style = value
    
    def getBrushStyle(self):
        """Get the current brush style"""
        return self.brush_style
    
    def setBrushStyle(self, value):
        """Set the current brush style"""
        self.brush_style = value
    
    def get_tool(self):
        """Get the current tool"""
        return self.tool
    
    def set_tool(self, value):
        """Set the current tool"""
        self.tool = value
    
    def add_image_item(self, path):
        """Add an image item to the scene"""
        from resizablepixmapitem import ResizablePixmapItem
        from PySide6.QtGui import QPixmap
        
        pix_item = ResizablePixmapItem(QPixmap(path))
        pix_item.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsMovable | 
                         QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        self.addItem(pix_item)
        
        pix_item.setPos(QPointF(0, 0) - QPointF(pix_item.boundingRect().width()/2,
                                               pix_item.boundingRect().height()/2))