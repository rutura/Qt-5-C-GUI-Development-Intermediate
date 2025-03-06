from PySide6.QtWidgets import QWidget, QListWidgetItem, QGraphicsView
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QPixmap, QColor, QPen

from ui_widget import Ui_Widget
from scene import Scene
from shapelist import ShapeList
from colorlistwidget import ColorListWidget

class Widget(QWidget):
    """
    Main widget for the graphics editor application.
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
        self.scene = Scene(self)
        
        # Add coordinate grid lines
        # In PySide6, we need to create a QPen with the color
        blue_pen = QPen(QColor("blue"))
        self.scene.addLine(-400, 0, 400, 0, blue_pen)
        self.scene.addLine(0, -400, 0, 400, blue_pen)
        self.scene.setSceneRect(-800, -400, 1600, 800)
        
        # Create shape list with draggable shapes
        self.shape_list = ShapeList(self)
        self.shape_map = {
            10: "Ellipse",
            20: "Quick",
            30: "Rectangle",
            40: "Star"
        }
        
        # Populate the shape list
        for key in self.shape_map.keys():
            item = QListWidgetItem(self.shape_map[key], self.shape_list)
            filename = f":/images/{self.shape_map[key].lower()}.png"
            item.setIcon(QIcon(filename))
            item.setData(Qt.UserRole, key)
        
        # Create color list with draggable colors
        self.color_list = ColorListWidget(self)
        
        # Add all named colors to the list
        color_names = QColor.colorNames()
        self.color_list.addItems(color_names)
        
        # Add color icons to the color list
        for i in range(len(color_names)):
            pixmap = QPixmap(40, 40)
            pixmap.fill(QColor(color_names[i]))
            icon = QIcon()
            icon.addPixmap(pixmap)
            self.color_list.item(i).setIcon(icon)
        
        # Create the view and set its scene
        self.view = QGraphicsView(self)
        self.view.setScene(self.scene)
        
        # Add widgets to the layouts
        self.ui.listLayout.addWidget(self.shape_list)
        self.ui.listLayout.addWidget(self.color_list)
        self.ui.viewLayout.addWidget(self.view)
        
        # Set window title
        self.setWindowTitle("Graphics Editor with Drag and Drop")