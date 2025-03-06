from PySide6.QtWidgets import QMainWindow, QGraphicsView, QFileDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QPixmap, QColor
from ui_mainwindow import Ui_MainWindow
from scene import Scene
from shapelist import ShapeList
from colorlistwidget import ColorListWidget
import resource_rc

class MainWindow(QMainWindow):
    """Main window for the drawing application"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Create scene
        self.scene = Scene(self)
        
        # Create shape list
        self.shape_map = {}
        self.shape_map[10] = "Ellipse"
        self.shape_map[20] = "Quick"
        self.shape_map[30] = "Rectangle"
        self.shape_map[40] = "Star"
        
        shape_list = ShapeList(self)
        
        for key in self.shape_map.keys():
            item = shape_list.addItem(self.shape_map[key])
            item = shape_list.item(shape_list.count() - 1)
            filename = f":/images/{self.shape_map[key].lower()}.png"
            item.setIcon(QIcon(filename))
            item.setData(Qt.ItemDataRole.UserRole, key)
        
        # Create color list
        color_list = ColorListWidget(self)
        color_list.addItems(QColor.colorNames())
        
        colors = QColor.colorNames()
        
        for i in range(len(colors)):
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
        
        # Connect actions
        self.ui.actionCursor.triggered.connect(self.on_action_cursor_triggered)
        self.ui.actionStar.triggered.connect(self.on_action_star_triggered)
        self.ui.actionRectangle.triggered.connect(self.on_action_rectangle_triggered)
        self.ui.actionEllipse.triggered.connect(self.on_action_ellipse_triggered)
        self.ui.actionEraser.triggered.connect(self.on_action_eraser_triggered)
        self.ui.actionPen.triggered.connect(self.on_action_pen_triggered)
        self.ui.actionAdd_Image.triggered.connect(self.on_action_add_image_triggered)
        
    def on_action_cursor_triggered(self):
        """Set cursor tool"""
        self.statusBar().showMessage("Current tool is Cursor")
        self.scene.set_tool(Scene.Cursor)
    
    def on_action_star_triggered(self):
        """Set star tool"""
        self.statusBar().showMessage("Current tool is Star")
        self.scene.set_tool(Scene.Star)
    
    def on_action_rectangle_triggered(self):
        """Set rectangle tool"""
        self.statusBar().showMessage("Current tool is Rect")
        self.scene.set_tool(Scene.Rect)
    
    def on_action_ellipse_triggered(self):
        """Set ellipse tool"""
        self.statusBar().showMessage("Current tool is Ellipse")
        self.scene.set_tool(Scene.Ellipse)
    
    def on_action_eraser_triggered(self):
        """Set eraser tool"""
        self.statusBar().showMessage("Current tool is Eraser")
        self.scene.set_tool(Scene.Eraser)
    
    def on_action_pen_triggered(self):
        """Set pen tool"""
        self.statusBar().showMessage("Current tool is Pen")
        self.scene.set_tool(Scene.Pen)
    
    def on_action_add_image_triggered(self):
        """Add an image to the scene"""
        file_name = QFileDialog.getOpenFileName(
            self, "Open File", "/home", "Images (*.png *.xpm *.jpg)"
        )
        if not file_name[0]:
            return
        
        self.scene.add_image_item(file_name[0])