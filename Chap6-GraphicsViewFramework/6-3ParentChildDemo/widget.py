from PySide6.QtWidgets import (QWidget, QGraphicsScene, QGraphicsView, 
                             QGraphicsRectItem, QGraphicsEllipseItem)
from PySide6.QtGui import QBrush, QPixmap
from PySide6.QtCore import Qt
from ui_widget import Ui_Widget
from imageitem import ImageItem
import resource_rc  # Import the compiled resource file

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # Create graphics scene
        self.scene = QGraphicsScene(self)
        
        # Create main rectangle that will be the parent item
        self.rect1 = QGraphicsRectItem(-50, -50, 100, 100)
        self.rect1.setFlag(QGraphicsRectItem.GraphicsItemFlag.ItemIsMovable)
        self.rect1.setBrush(QBrush(Qt.yellow))
        
        # Create first ellipse as a child of rect1
        ellipse1 = QGraphicsEllipseItem(-20, -20, 40, 40)
        ellipse1.setBrush(QBrush(Qt.red))
        ellipse1.setParentItem(self.rect1)
        
        # Create second ellipse as a child of rect1
        ellipse2 = QGraphicsEllipseItem(20, 20, 20, 40)
        ellipse2.setBrush(QBrush(Qt.green))
        ellipse2.setParentItem(self.rect1)
        
        # Create image item as a child of rect1
        image_item = ImageItem()
        image_item.setPixmap(QPixmap(":/images/Quick.png"))
        image_item.setParentItem(self.rect1)
        
        # Add the parent item (and thus all its children) to the scene
        self.scene.addItem(self.rect1)
        
        # Create the view and set its scene
        self.view = QGraphicsView(self)
        self.view.setScene(self.scene)
        
        # Add the view to the layout
        self.ui.verticalLayout.addWidget(self.view)
        
        # Connect buttons to their slots
        self.ui.showHideButton.clicked.connect(self.on_showHideButton_clicked)
        self.ui.removeItem.clicked.connect(self.on_removeItem_clicked)
        
        # Set window title
        self.setWindowTitle("Graphics Item Hierarchy Demo")
        
    def on_showHideButton_clicked(self):
        """Toggle visibility of the rectangle and all its children"""
        is_visible = self.rect1.isVisible()
        self.rect1.setVisible(not is_visible)
        
    def on_removeItem_clicked(self):
        """Remove the rectangle (and its children) from the scene"""
        self.scene.removeItem(self.rect1)
        # Note: Not deleting the item here, as in the C++ version