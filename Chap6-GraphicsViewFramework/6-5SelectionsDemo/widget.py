from PySide6.QtWidgets import QWidget, QGraphicsScene, QGraphicsItem, QColorDialog
from PySide6.QtCore import QRectF, Qt
from PySide6.QtGui import QBrush, QColor
from ui_widget import Ui_Widget
from view import View
import resource_rc  # Import the compiled resource file

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # Initialize current color
        self.current_color = QColor(Qt.white)
        
        # Create the graphics scene
        self.scene = QGraphicsScene(self)
        self.scene.setSceneRect(QRectF(-400, -400, 800, 800))
        
        # Add coordinate axes
        self.scene.addLine(-400, 0, 400, 0)
        self.scene.addLine(0, -400, 0, 400)
        
        # Create custom view and set its scene
        self.view = View(self)
        self.view.setScene(self.scene)
        self.view.setCurrentTool(View.Cursor)
        self.view.setDragMode(View.RubberBandDrag)
        
        # Add the view to the layout
        self.ui.verticalLayout.addWidget(self.view)
        
        # Connect buttons to their slots
        self.ui.cursorButton.clicked.connect(self.on_cursorButton_clicked)
        self.ui.lineButton.clicked.connect(self.on_lineButton_clicked)
        self.ui.ellipseButton.clicked.connect(self.on_ellipseButton_clicked)
        self.ui.pathButton.clicked.connect(self.on_pathButton_clicked)
        self.ui.pieButton.clicked.connect(self.on_pieButton_clicked)
        self.ui.imageButton.clicked.connect(self.on_imageButton_clicked)
        self.ui.starButton.clicked.connect(self.on_starButton_clicked)
        self.ui.colorButton.clicked.connect(self.on_colorButton_clicked)
        self.ui.chooseColorButton.clicked.connect(self.on_chooseColorButton_clicked)
        self.ui.infoButton.clicked.connect(self.on_infoButton_clicked)
        
        # Set window title
        self.setWindowTitle("Graphics View Drawing Tool")
    
    def on_cursorButton_clicked(self):
        """Set the current tool to cursor (selection mode)"""
        self.view.setCurrentTool(View.Cursor)
    
    def on_lineButton_clicked(self):
        """Set the current tool to line drawing"""
        self.view.setCurrentTool(View.Line)
    
    def on_ellipseButton_clicked(self):
        """Set the current tool to ellipse drawing"""
        self.view.setCurrentTool(View.Ellipse)
    
    def on_pathButton_clicked(self):
        """Set the current tool to path drawing"""
        self.view.setCurrentTool(View.Path)
    
    def on_pieButton_clicked(self):
        """Set the current tool to pie drawing"""
        self.view.setCurrentTool(View.Pie)
    
    def on_imageButton_clicked(self):
        """Set the current tool to image placement"""
        self.view.setCurrentTool(View.Image)
    
    def on_starButton_clicked(self):
        """Set the current tool to star drawing"""
        self.view.setCurrentTool(View.Star)
    
    def on_chooseColorButton_clicked(self):
        """Open a color dialog to choose a color"""
        color = QColorDialog.getColor(self.current_color)
        if color.isValid():
            self.current_color = color
            qss = f"background-color: {self.current_color.name()}"
            self.ui.colorButton.setStyleSheet(qss)
            self.setSelectItemColor(color)
    
    def on_colorButton_clicked(self):
        """Apply the current color to selected items"""
        self.setSelectItemColor(self.current_color)
    
    def on_infoButton_clicked(self):
        """Print information about items in the scene"""
        print(f"Item count: {len(self.scene.items())}")
        print(f"Selected items: {len(self.scene.selectedItems())}")
    
    def setSelectItemColor(self, color):
        """Set the color of selected items"""
        if not self.scene.selectedItems():
            return
        
        # Loop through the selected items
        for item in self.scene.selectedItems():
            # Loop to find children
            for child_item in item.childItems():
                # Is it a rect?
                rect_item = self.qgraphicsitem_cast_rect(child_item)
                if rect_item:
                    rect_item.setBrush(QBrush(color))
                
                # Is it a path?
                path_item = self.qgraphicsitem_cast_path(child_item)
                if path_item:
                    path_item.setBrush(QBrush(color))
                
                # Is it an ellipse?
                ellipse_item = self.qgraphicsitem_cast_ellipse(child_item)
                if ellipse_item:
                    ellipse_item.setBrush(QBrush(color))
    
    # Helper methods for type casting (equivalent to qgraphicsitem_cast in C++)
    def qgraphicsitem_cast_rect(self, item):
        """Cast item to QGraphicsRectItem if possible"""
        if isinstance(item, QGraphicsRectItem):
            return item
        return None
    
    def qgraphicsitem_cast_path(self, item):
        """Cast item to QGraphicsPathItem if possible"""
        if isinstance(item, QGraphicsPathItem):
            return item
        return None
    
    def qgraphicsitem_cast_ellipse(self, item):
        """Cast item to QGraphicsEllipseItem if possible"""
        if isinstance(item, QGraphicsEllipseItem):
            return item
        return None