from PySide6.QtWidgets import (QGraphicsView, QGraphicsLineItem, QGraphicsRectItem,
                             QGraphicsEllipseItem, QGraphicsPathItem,
                             QGraphicsPixmapItem, QGraphicsItem)
from PySide6.QtCore import QPointF, QPoint, QRectF, Qt
from PySide6.QtGui import QPen, QBrush, QPainterPath, QPolygon, QPixmap

class View(QGraphicsView):
    """
    Custom QGraphicsView that handles different drawing tools
    """
    # Enum for different drawing tools
    Cursor = 0
    Line = 1
    Ellipse = 2
    Path = 3
    Pie = 4
    Image = 5
    Star = 6
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.current_tool = self.Cursor
    
    def mousePressEvent(self, event):
        """Handle mouse press events based on the current tool"""
        if self.current_tool == self.Cursor:
            super().mousePressEvent(event)
        elif self.current_tool == self.Line:
            self.addLine(self.mapToScene(event.pos()))
        elif self.current_tool == self.Ellipse:
            self.addEllipse(self.mapToScene(event.pos()))
        elif self.current_tool == self.Path:
            self.addPath(self.mapToScene(event.pos()))
        elif self.current_tool == self.Pie:
            self.addPie(self.mapToScene(event.pos()))
        elif self.current_tool == self.Image:
            self.addImage(self.mapToScene(event.pos()))
        elif self.current_tool == self.Star:
            self.addStar(self.mapToScene(event.pos()))
    
    def addLine(self, pos):
        """Add a line item at the specified position"""
        line = QGraphicsLineItem(10, 10, 90, 90)
        line.setPen(QPen(Qt.red, 3))
        
        bound_rect = QGraphicsRectItem()
        bound_rect.setRect(line.boundingRect().adjusted(-10, -10, 10, 10))
        bound_rect.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsMovable | 
                           QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        line.setParentItem(bound_rect)
        
        bound_rect.setPos(pos)
        self.scene().addItem(bound_rect)
    
    def addEllipse(self, pos):
        """Add an ellipse item at the specified position"""
        rect = QRectF(10, 10, 80, 60)
        ellipse = QGraphicsEllipseItem(rect)
        ellipse.setBrush(QBrush(Qt.green))
        
        bound_rect = QGraphicsRectItem()
        bound_rect.setRect(ellipse.boundingRect().adjusted(-10, -10, 10, 10))
        bound_rect.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsMovable | 
                           QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        ellipse.setParentItem(bound_rect)
        
        bound_rect.setPos(pos)
        self.scene().addItem(bound_rect)
    
    def addPath(self, pos):
        """Add a path item at the specified position"""
        path = QPainterPath()
        path.addEllipse(QRectF(10, 10, 90, 60))
        path.addRect(QRectF(20, 20, 50, 50))
        
        path_item = QGraphicsPathItem(path)
        path_item.setPen(QPen(Qt.black, 5))
        path_item.setBrush(Qt.green)
        
        bound_rect = QGraphicsRectItem()
        bound_rect.setRect(path_item.boundingRect().adjusted(-10, -10, 10, 10))
        bound_rect.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsMovable | 
                           QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        path_item.setParentItem(bound_rect)
        
        bound_rect.setPos(pos)
        self.scene().addItem(bound_rect)
    
    def addPie(self, pos):
        """Add a pie-shaped path item at the specified position"""
        path = QPainterPath(QPointF(60, 60))
        path.arcTo(QRectF(10, 10, 80, 80), 30, 170)
        path.lineTo(QPointF(60, 60))
        
        pie_path = QGraphicsPathItem(path)
        pie_path.setPen(QPen(Qt.black, 5))
        pie_path.setBrush(Qt.green)
        
        bound_rect = QGraphicsRectItem()
        bound_rect.setRect(pie_path.boundingRect().adjusted(-10, -10, 10, 10))
        bound_rect.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsMovable | 
                           QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        pie_path.setParentItem(bound_rect)
        
        bound_rect.setPos(pos)
        self.scene().addItem(bound_rect)
    
    def addImage(self, pos):
        """Add an image item at the specified position"""
        pixmap = QPixmap(":/images/LearnQt.png")
        pixmap_item = QGraphicsPixmapItem(pixmap.scaled(110, 110))
        
        bound_rect = QGraphicsRectItem()
        bound_rect.setRect(pixmap_item.boundingRect().adjusted(-10, -10, 10, 10))
        bound_rect.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsMovable | 
                           QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        pixmap_item.setParentItem(bound_rect)
        
        bound_rect.setPos(pos)
        self.scene().addItem(bound_rect)
    
    def addStar(self, pos):
        """Add a star-shaped path item at the specified position"""
        poly = QPolygon()
        poly.append(QPoint(0, 85))
        poly.append(QPoint(75, 75))
        poly.append(QPoint(100, 10))
        poly.append(QPoint(125, 75))
        poly.append(QPoint(200, 85))
        poly.append(QPoint(150, 125))
        poly.append(QPoint(160, 190))
        poly.append(QPoint(100, 150))
        poly.append(QPoint(40, 190))
        poly.append(QPoint(50, 125))
        poly.append(QPoint(0, 85))
        
        path = QPainterPath()
        path.addPolygon(poly)
        
        star_path = QGraphicsPathItem(path)
        star_path.setPen(QPen(Qt.black, 5))
        star_path.setBrush(Qt.green)
        
        bound_rect = QGraphicsRectItem()
        bound_rect.setRect(star_path.boundingRect().adjusted(-10, -10, 10, 10))
        bound_rect.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsMovable | 
                           QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        star_path.setParentItem(bound_rect)
        
        bound_rect.setPos(pos)
        self.scene().addItem(bound_rect)
    
    def getCurrentTool(self):
        """Get the current tool"""
        return self.current_tool
    
    def setCurrentTool(self, tool):
        """Set the current tool"""
        self.current_tool = tool