from PySide6.QtWidgets import QWidget, QGraphicsScene, QGraphicsItem
from PySide6.QtGui import QBrush, QColor, QPen
from PySide6.QtCore import Qt
from ui_widget import Ui_Widget
from rect import Rect
from view import View

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # Create the graphics scene
        self.scene = QGraphicsScene(self)
        self.scene.setBackgroundBrush(QBrush(QColor(Qt.yellow)))
        self.scene.setSceneRect(-300, -300, 600, 600)
        
        # Create a pen for the rectangle
        pen = QPen()
        pen.setWidth(5)
        pen.setColor(Qt.red)
        
        # Create an interactive rectangle
        rect_item = Rect()
        rect_item.setRect(10, 10, 200, 200)
        rect_item.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsFocusable)
        rect_item.setFocus()
        
        rect_item.setPen(pen)
        rect_item.setBrush(QBrush(Qt.green))
        
        self.scene.addItem(rect_item)
        
        # Add coordinate axes
        # Horizontal line
        self.scene.addLine(-300, 0, 300, 0)
        # Vertical line
        self.scene.addLine(0, -300, 0, 300)
        
        # Create the custom view
        self.view = View(self)
        self.view.setScene(self.scene)
        
        # Add the view to the layout
        self.ui.verticalLayout.addWidget(self.view)
        
        # Set window title
        self.setWindowTitle("Graphics View Demo")