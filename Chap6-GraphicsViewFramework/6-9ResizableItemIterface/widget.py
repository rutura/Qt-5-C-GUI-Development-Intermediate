from PySide6.QtWidgets import QWidget, QGraphicsScene, QGraphicsView, QGraphicsItem
from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QPixmap

from ui_widget import Ui_Widget
from resizablerectitem import ResizableRectItem
from resizableellipseitem import ResizableEllipseItem
from resizablepixmapitem import ResizablePixmapItem
from resizablestaritem import ResizableStarItem

class Widget(QWidget):
    """
    Main widget for the Resizable Graphics Items application.
    """
    def __init__(self, parent=None):
        """
        Initialize the widget.
        
        Args:
            parent: Parent widget
        """
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # Create the graphics scene
        self.scene = QGraphicsScene(self)
        
        # Create a resizable rectangle item
        rect_item = ResizableRectItem()
        rect_item.setRect(-50, -50, 100, 100)
        rect_item.setBrush(QBrush(Qt.green))
        rect_item.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)
        self.scene.addItem(rect_item)
        
        # Create a resizable ellipse item
        ellipse = ResizableEllipseItem()
        ellipse.setRect(-400, -400, 200, 200)
        ellipse.setBrush(QBrush(Qt.red))
        ellipse.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)
        self.scene.addItem(ellipse)
        
        # Create a resizable pixmap item
        pix_item = ResizablePixmapItem(QPixmap(":/images/Quick.png"))
        pix_item.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)
        self.scene.addItem(pix_item)
        
        # Create a resizable star item
        star_item = ResizableStarItem()
        star_item.setBrush(QBrush(Qt.blue))
        star_item.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)
        self.scene.addItem(star_item)
        
        # Create the view and set its scene
        self.view = QGraphicsView(self)
        self.view.setScene(self.scene)
        
        # Add the view to the layout
        self.ui.verticalLayout.addWidget(self.view)
        
        # Set window title
        self.setWindowTitle("Resizable Graphics Items with Handles")