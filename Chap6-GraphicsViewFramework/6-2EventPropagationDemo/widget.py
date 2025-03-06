from PySide6.QtWidgets import QWidget, QGraphicsItem
from ui_widget import Ui_Widget
from view import View
from scene import Scene
from rect import Rect

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # Create the custom graphics scene
        self.scene = Scene(self)
        
        # Create a rectangle item and add it to the scene
        self.rect_item = Rect()
        self.rect_item.setRect(10, 10, 200, 200)
        
        self.scene.addItem(self.rect_item)
        
        # Set the rectangle to be focusable and movable
        self.rect_item.setFlag(QGraphicsItem.ItemIsFocusable)
        self.rect_item.setFlag(QGraphicsItem.ItemIsMovable)
        self.rect_item.setFocus()
        
        # Create the custom view and set its scene
        self.view = View(self)
        self.view.setScene(self.scene)
        
        # Add the view to the layout
        self.ui.verticalLayout.addWidget(self.view)
        
        # Set window title
        self.setWindowTitle("Event Propagation Demo")