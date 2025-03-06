from PySide6.QtWidgets import QWidget, QGraphicsScene, QGraphicsView, QGraphicsRectItem, QGraphicsItem
from PySide6.QtCore import Qt
from PySide6.QtGui import QPen, QBrush, QTransform
from ui_widget import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # Initialize rotation angle
        self.rotation_angle = 0
        
        # Create the graphics scene
        self.scene = QGraphicsScene(self)
        
        # Draw the center guide lines
        self.scene.addLine(-400, 0, 400, 0, QPen(Qt.blue))
        self.scene.addLine(0, -400, 0, 400, QPen(Qt.blue))
        self.scene.setSceneRect(-800, -400, 1600, 800)
        
        # Create a green rectangle
        green_rect = self.scene.addRect(0, 0, 200, 100)
        green_rect.setPen(Qt.NoPen)
        green_rect.setFlag(QGraphicsItem.ItemIsSelectable)
        green_rect.setBrush(QBrush(Qt.green))
        
        # Create a red rectangle
        red_rect = self.scene.addRect(0, 0, 200, 100)
        red_rect.setPen(Qt.NoPen)
        red_rect.setFlag(QGraphicsItem.ItemIsSelectable)
        red_rect.setBrush(QBrush(Qt.red))
        
        # Create a blue rectangle as a child of the green rectangle
        blue_rect = self.scene.addRect(10, 10, 40, 40)
        blue_rect.setPen(Qt.NoPen)
        blue_rect.setFlag(QGraphicsItem.ItemIsSelectable)
        blue_rect.setBrush(QBrush(Qt.blue))
        blue_rect.setParentItem(green_rect)
        
        # Transform the red rectangle
        transform = red_rect.transform()
        transform.rotate(45, Qt.ZAxis)
        transform.translate(50, 0)
        red_rect.setTransform(transform)
        
        # Create the graphics view and set its scene
        self.view = QGraphicsView(self)
        self.view.setScene(self.scene)
        
        # Add the view to the layout
        self.ui.viewLayout.addWidget(self.view)
        
        # Connect spin box signals to slots
        self.ui.xTranslateSpinbox.valueChanged.connect(self.on_xTranslateSpinbox_valueChanged)
        self.ui.yTranslateSpinbox.valueChanged.connect(self.on_yTranslateSpinbox_valueChanged)
        self.ui.xScaleSpinbox.valueChanged.connect(self.on_xScaleSpinbox_valueChanged)
        self.ui.yScaleSpinbox.valueChanged.connect(self.on_yScaleSpinbox_valueChanged)
        self.ui.xShearSpinbox.valueChanged.connect(self.on_xShearSpinbox_valueChanged)
        self.ui.yShearSpinbox.valueChanged.connect(self.on_yShearSpinbox_valueChanged)
        self.ui.rotationSpinbox.valueChanged.connect(self.on_rotationSpinbox_valueChanged)
        
        # Set window title
        self.setWindowTitle("Graphics View Transformations")
    
    def on_xTranslateSpinbox_valueChanged(self, value):
        """Handle changes in the X translation spin box"""
        item = self.getSelectedItem()
        if item:
            transform = item.transform()
            transform.translate(value - transform.dx(), 0)
            item.setTransform(transform)
    
    def on_yTranslateSpinbox_valueChanged(self, value):
        """Handle changes in the Y translation spin box"""
        item = self.getSelectedItem()
        if item:
            transform = item.transform()
            transform.translate(0, value - transform.dy())
            item.setTransform(transform)
    
    def on_xScaleSpinbox_valueChanged(self, value):
        """Handle changes in the X scale spin box"""
        item = self.getSelectedItem()
        if item:
            transform = item.transform()
            scale_factor = value / transform.m11()
            transform.scale(scale_factor, 1)
            item.setTransform(transform)
    
    def on_yScaleSpinbox_valueChanged(self, value):
        """Handle changes in the Y scale spin box"""
        item = self.getSelectedItem()
        if item:
            transform = item.transform()
            scale_factor = value / transform.m22()
            transform.scale(1, scale_factor)
            item.setTransform(transform)
    
    def on_xShearSpinbox_valueChanged(self, value):
        """Handle changes in the X shear spin box"""
        item = self.getSelectedItem()
        if item:
            transform = item.transform()
            transform.shear(value - transform.m21(), 0)
            item.setTransform(transform)
    
    def on_yShearSpinbox_valueChanged(self, value):
        """Handle changes in the Y shear spin box"""
        item = self.getSelectedItem()
        if item:
            transform = item.transform()
            transform.shear(0, value - transform.m12())
            item.setTransform(transform)
    
    def on_rotationSpinbox_valueChanged(self, value):
        """Handle changes in the rotation spin box"""
        item = self.getSelectedItem()
        if item:
            transform = item.transform()
            transform.rotate(value - self.rotation_angle)
            item.setTransform(transform)
            self.rotation_angle = value
    
    def getSelectedItem(self):
        """Get the first selected item from the scene, or None if nothing is selected"""
        if self.scene.selectedItems():
            return self.scene.selectedItems()[0]
        return None