from PySide6.QtWidgets import (QWidget, QGraphicsScene, QGraphicsView, 
                             QGraphicsRectItem, QDial, QGraphicsProxyWidget)
from PySide6.QtCore import Qt, QObject
from PySide6.QtGui import QPen, QBrush
from ui_widget import Ui_Widget

class Widget(QWidget):
    """
    Main widget for the Graphics View with embedded dial widget.
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
        
        # Add coordinate grid lines
        self.scene.addLine(-400, 0, 400, 0, QPen(Qt.blue))
        self.scene.addLine(0, -400, 0, 400, QPen(Qt.blue))
        self.scene.setSceneRect(-800, -400, 1600, 800)
        
        # Add rectangle item
        self.rect = self.scene.addRect(-200, -100, 200, 70)
        self.rect.setBrush(QBrush(Qt.red))
        
        # Create a dial widget
        self.dial = QDial()
        self.dial.setMinimum(0)
        self.dial.setMaximum(360)
        
        # Connect dial's value changes to rectangle rotation
        self.dial.valueChanged.connect(self.on_dial_value_changed)
        
        # Create a proxy widget to embed the dial in the scene
        proxy_widget = QGraphicsProxyWidget()
        proxy_widget.setWidget(self.dial)
        proxy_widget.setPos(100, -300)
        
        # Add the proxy widget to the scene
        self.scene.addItem(proxy_widget)
        
        # Create the view and set its scene
        self.view = QGraphicsView(self)
        self.view.setScene(self.scene)
        
        # Add the view to the layout
        self.ui.verticalLayout.addWidget(self.view)
        
        # Set window title
        self.setWindowTitle("Graphics View with Embedded Widget")
    
    def on_dial_value_changed(self, value):
        """
        Handle dial value changes by rotating the rectangle.
        
        Args:
            value: The new value of the dial
        """
        print(f"Dial value changed to: {value}")
        self.rect.setRotation(value)