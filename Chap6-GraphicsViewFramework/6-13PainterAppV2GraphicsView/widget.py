from PySide6.QtWidgets import QWidget, QGraphicsView
from PySide6.QtGui import QPen, QIcon, QPixmap
from PySide6.QtCore import Qt
from ui_widget import Ui_Widget
from scene import Scene
from shapelist import ShapeList
from colorlistwidget import ColorListWidget
import resource_rc

class Widget(QWidget):
    """Main widget for the drawing application"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # Create scene
        self.scene = Scene(self)
        self.scene.addLine(-400, 0, 400, 0, QPen(Qt.blue))
        self.scene.addLine(0, -400, 0, 400, QPen(Qt.blue))
        self.scene.setSceneRect(-800, -400, 1600, 800)
        
        # Create shape list
        self.shape_map = {}
        self.shape_map[10] = "Ellipse"
        self.shape_map[20] = "Quick"
        self.shape_map[30] = "Rectangle"
        self.shape_map[40] = "Star"
        
        shape_list = ShapeList(self)
        
        for key in self.shape_map.keys():
            shape_list.addItem(self.shape_map[key])
            item = shape_list.item(shape_list.count() - 1)
            filename = f":/images/{self.shape_map[key].lower()}.png"
            item.setIcon(QIcon(filename))
            item.setData(Qt.ItemDataRole.UserRole, key)
        
        # Create color list
        color_list = ColorListWidget(self)
        color_list.addItems(QColor.colorNames())
        
        colors = QColor.colorNames()
        
        for i in range(len(colors)):
            from PySide6.QtGui import QColor
            m_pix = QPixmap(40, 40)
            m_pix.fill(QColor(colors[i]))
            icon = QIcon()
            icon.addPixmap(m_pix)
            color_list.item(i).setIcon(icon)
        
        # Create view
        view = QGraphicsView(self)
        view.setScene(self.scene)
        
        # Add widgets to layout
        self.ui.listLayout.addWidget(shape_list)
        self.ui.listLayout.addWidget(color_list)
        self.ui.viewLayout.addWidget(view)
        
        # Set window title
        self.setWindowTitle("Drawing Application")