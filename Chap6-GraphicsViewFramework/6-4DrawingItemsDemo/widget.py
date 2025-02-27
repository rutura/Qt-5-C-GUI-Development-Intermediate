from PySide6.QtWidgets import (QWidget, QGraphicsScene, QGraphicsView,
                             QGraphicsLineItem, QGraphicsRectItem,
                             QGraphicsEllipseItem, QGraphicsPathItem,
                             QGraphicsPixmapItem)
from PySide6.QtCore import QRectF, QPointF, QPoint, Qt
from PySide6.QtGui import QPen, QBrush, QPainterPath, QPolygon, QPixmap
from ui_widget import Ui_Widget
import resource_rc  # Import the compiled resource file

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # Create the graphics scene
        self.scene = QGraphicsScene(self)
        self.scene.setSceneRect(QRectF(-400, -400, 800, 800))
        
        # Add coordinate axes
        self.scene.addLine(-400, 0, 400, 0)  # Horizontal line
        self.scene.addLine(0, -400, 0, 400)  # Vertical line
        
        # Create the graphics view and set its scene
        self.view = QGraphicsView(self)
        self.view.setScene(self.scene)
        
        # Add the view to the layout
        self.ui.verticalLayout.addWidget(self.view)
        
        # Connect buttons to their slots
        self.ui.lineButton.clicked.connect(self.on_lineButton_clicked)
        self.ui.ellipseButton.clicked.connect(self.on_ellipseButton_clicked)
        self.ui.pathButton.clicked.connect(self.on_pathButton_clicked)
        self.ui.pieButton.clicked.connect(self.on_pieButton_clicked)
        self.ui.imageButton.clicked.connect(self.on_imageButton_clicked)
        self.ui.starButton.clicked.connect(self.on_starButton_clicked)
        
        # Set window title
        self.setWindowTitle("Graphics View Shapes Demo")
    
    def on_lineButton_clicked(self):
        """Add a line item to the scene"""
        # Create a line using QLineF
        line = QGraphicsLineItem(10, 10, 90, 90)  # x1, y1, x2, y2
        line.setPen(QPen(Qt.red, 3))
        
        # Create a movable bounding rectangle
        bound_rect = QGraphicsRectItem()
        bound_rect.setRect(line.boundingRect().adjusted(-10, -10, 10, 10))
        bound_rect.setFlag(QGraphicsRectItem.GraphicsItemFlag.ItemIsMovable)
        line.setParentItem(bound_rect)
        
        self.scene.addItem(bound_rect)
    
    def on_ellipseButton_clicked(self):
        """Add an ellipse item to the scene"""
        rect = QRectF(10, 10, 80, 60)
        ellipse = QGraphicsEllipseItem(rect)
        ellipse.setBrush(QBrush(Qt.green))
        
        # Create a movable bounding rectangle
        bound_rect = QGraphicsRectItem()
        bound_rect.setRect(ellipse.boundingRect().adjusted(-10, -10, 10, 10))
        bound_rect.setFlag(QGraphicsRectItem.GraphicsItemFlag.ItemIsMovable)
        ellipse.setParentItem(bound_rect)
        
        self.scene.addItem(bound_rect)
    
    def on_pathButton_clicked(self):
        """Add a path item to the scene"""
        path = QPainterPath()
        path.addEllipse(QRectF(10, 10, 90, 60))
        path.addRect(QRectF(20, 20, 50, 50))
        
        path_item = QGraphicsPathItem(path)
        path_item.setPen(QPen(Qt.black, 5))
        path_item.setBrush(Qt.green)
        
        # Create a movable bounding rectangle
        bound_rect = QGraphicsRectItem()
        bound_rect.setRect(path_item.boundingRect().adjusted(-10, -10, 10, 10))
        bound_rect.setFlag(QGraphicsRectItem.GraphicsItemFlag.ItemIsMovable)
        path_item.setParentItem(bound_rect)
        
        self.scene.addItem(bound_rect)
    
    def on_pieButton_clicked(self):
        """Add a pie-shaped path item to the scene"""
        path = QPainterPath(QPointF(60, 60))
        path.arcTo(QRectF(10, 10, 80, 80), 30, 170)
        path.lineTo(QPointF(60, 60))
        
        pie_path = QGraphicsPathItem(path)
        pie_path.setPen(QPen(Qt.black, 5))
        pie_path.setBrush(Qt.green)
        
        # Create a movable bounding rectangle
        bound_rect = QGraphicsRectItem()
        bound_rect.setRect(pie_path.boundingRect().adjusted(-10, -10, 10, 10))
        bound_rect.setFlag(QGraphicsRectItem.GraphicsItemFlag.ItemIsMovable)
        pie_path.setParentItem(bound_rect)
        
        self.scene.addItem(bound_rect)
    
    def on_imageButton_clicked(self):
        """Add an image item to the scene"""
        pixmap = QPixmap(":/images/LearnQt.png")
        pixmap_item = QGraphicsPixmapItem(pixmap.scaled(110, 110))
        
        # Create a movable bounding rectangle
        bound_rect = QGraphicsRectItem()
        bound_rect.setRect(pixmap_item.boundingRect().adjusted(-10, -10, 10, 10))
        bound_rect.setFlag(QGraphicsRectItem.GraphicsItemFlag.ItemIsMovable)
        pixmap_item.setParentItem(bound_rect)
        
        self.scene.addItem(bound_rect)
    
    def on_starButton_clicked(self):
        """Add a star-shaped path item to the scene"""
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
        
        # Create a movable bounding rectangle
        bound_rect = QGraphicsRectItem()
        bound_rect.setRect(star_path.boundingRect().adjusted(-10, -10, 10, 10))
        bound_rect.setFlag(QGraphicsRectItem.GraphicsItemFlag.ItemIsMovable)
        star_path.setParentItem(bound_rect)
        
        self.scene.addItem(bound_rect)