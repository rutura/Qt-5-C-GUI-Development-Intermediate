from PySide6.QtWidgets import (QGraphicsScene, QGraphicsItemGroup, 
                              QGraphicsEllipseItem, QGraphicsLineItem, QGraphicsItem)
from PySide6.QtCore import Qt, QPointF, QRectF, QLineF, QMimeData
from PySide6.QtGui import QPen, QBrush, QColor

class Scene(QGraphicsScene):
    """Custom scene for the drawing application"""
    
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
            self.line_group = QGraphicsItemGroup()
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