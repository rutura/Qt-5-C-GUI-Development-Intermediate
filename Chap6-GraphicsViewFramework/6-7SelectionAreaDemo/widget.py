from PySide6.QtWidgets import QWidget, QGraphicsScene, QGraphicsRectItem, QGraphicsEllipseItem, QGraphicsItem
from PySide6.QtCore import Qt
from PySide6.QtGui import QPen, QBrush
from ui_widget import Ui_Widget
from view import View

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # Create the graphics scene
        self.scene = QGraphicsScene(self)
        
        # Draw the center guide lines
        self.scene.addLine(-400, 0, 400, 0, QPen(Qt.blue))
        self.scene.addLine(0, -400, 0, 400, QPen(Qt.blue))
        self.scene.setSceneRect(-800, -400, 1600, 800)
        
        # Set background color
        self.scene.setBackgroundBrush(Qt.gray)
        
        # Add a basic rectangle
        rect = self.scene.addRect(20, 20, 200, 100)
        rect.setFlag(QGraphicsItem.ItemIsSelectable)
        
        # Add green rectangle
        green_rect = self.scene.addRect(-50, -50, 100, 100)
        green_rect.setPen(Qt.NoPen)
        green_rect.setFlag(QGraphicsItem.ItemIsSelectable)
        green_rect.setFlag(QGraphicsItem.ItemIsMovable)
        green_rect.setBrush(QBrush(Qt.green))
        
        # Add blue rectangle
        blue_rect = self.scene.addRect(-100, -100, 100, 100)
        blue_rect.setPen(Qt.NoPen)
        blue_rect.setFlag(QGraphicsItem.ItemIsSelectable)
        blue_rect.setFlag(QGraphicsItem.ItemIsMovable)
        blue_rect.setBrush(QBrush(Qt.blue))
        
        # Add red ellipse
        self.red_ellipse = self.scene.addEllipse(-850, -50, 500, 500)
        self.red_ellipse.setPen(Qt.NoPen)
        self.red_ellipse.setFlag(QGraphicsItem.ItemIsSelectable)
        self.red_ellipse.setFlag(QGraphicsItem.ItemIsMovable)
        self.red_ellipse.setBrush(QBrush(Qt.red))
        
        # Create the custom view and set its scene
        self.view = View(self)
        self.view.setScene(self.scene)
        
        # Add the view to the layout
        self.ui.viewLayout.addWidget(self.view)
        
        # Initialize the grid checkbox state
        self.ui.showGridCheckbox.setChecked(self.view.getDrawGridLines())
        
        # Connect buttons to slots
        self.ui.centerInViewButton.clicked.connect(self.on_centerInViewButton_clicked)
        self.ui.showGridCheckbox.toggled.connect(self.on_showGridCheckbox_toggled)
        self.ui.ensureVisibleButton.clicked.connect(self.on_ensureVisibleButton_clicked)
        self.ui.fitInViewButton.clicked.connect(self.on_fitInViewButton_clicked)
        self.ui.zoomInButton.clicked.connect(self.on_zoomInButton_clicked)
        self.ui.zoomOutButton.clicked.connect(self.on_zoomOutButton_clicked)
        self.ui.resetButton.clicked.connect(self.on_resetButton_clicked)
        
        # Set window title
        self.setWindowTitle("Graphics View Navigation Demo")
    
    def on_centerInViewButton_clicked(self):
        """Center the view on the origin (0,0)"""
        self.view.centerOn(0, 0)
    
    def on_showGridCheckbox_toggled(self, checked):
        """Toggle grid lines visibility"""
        self.view.setDrawGridLines(checked)
    
    def on_ensureVisibleButton_clicked(self):
        """Ensure the red ellipse is visible in the view"""
        self.view.ensureVisible(self.red_ellipse)
    
    def on_fitInViewButton_clicked(self):
        """Scale the view to fit the red ellipse"""
        self.view.fitInView(self.red_ellipse)
    
    def on_zoomInButton_clicked(self):
        """Zoom in by scaling the view"""
        scale_factor = 1.1
        self.view.scale(scale_factor, scale_factor)
    
    def on_zoomOutButton_clicked(self):
        """Zoom out by scaling the view"""
        scale_factor = 1.1
        self.view.scale(1/scale_factor, 1/scale_factor)
    
    def on_resetButton_clicked(self):
        """Reset the view's transformation matrix"""
        self.view.resetTransform()