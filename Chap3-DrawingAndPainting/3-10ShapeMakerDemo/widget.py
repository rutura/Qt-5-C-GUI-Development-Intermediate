from PySide6.QtWidgets import QWidget
from PySide6.QtGui import (QPen, QBrush, QPixmap, QLinearGradient, 
                          QRadialGradient, QConicalGradient)
from PySide6.QtCore import Qt, Slot
from ui_widget import Ui_Widget
from shapecanvas import ShapeCanvas

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # Initialize and populate shape combo box
        self.ui.shapeCombo.addItem("Polygon", ShapeCanvas.Polygon)
        self.ui.shapeCombo.addItem("Rectangle", ShapeCanvas.Rect)
        self.ui.shapeCombo.addItem("Rounded Rectangle", ShapeCanvas.RoundedRect)
        self.ui.shapeCombo.addItem("Ellipse", ShapeCanvas.Ellipse)
        self.ui.shapeCombo.addItem("Pie", ShapeCanvas.Pie)
        self.ui.shapeCombo.addItem("Chord", ShapeCanvas.Chord)
        self.ui.shapeCombo.addItem("Text", ShapeCanvas.Text)
        self.ui.shapeCombo.addItem("Pixmap", ShapeCanvas.Pixmap)
        
        # Initialize and populate pen style combo box
        self.ui.penStyleCombobox.addItem("Solid", Qt.SolidLine)
        self.ui.penStyleCombobox.addItem("Dash", Qt.DashLine)
        self.ui.penStyleCombobox.addItem("Dot", Qt.DotLine)
        self.ui.penStyleCombobox.addItem("Dash Dot", Qt.DashDotLine)
        self.ui.penStyleCombobox.addItem("Dash Dot Dot", Qt.DashDotDotLine)
        self.ui.penStyleCombobox.addItem("None", Qt.NoPen)
        
        # Initialize and populate pen cap combo box
        self.ui.penCapCombobox.addItem("Flat", Qt.FlatCap)
        self.ui.penCapCombobox.addItem("Square", Qt.SquareCap)
        self.ui.penCapCombobox.addItem("Round", Qt.RoundCap)
        
        # Initialize and populate pen join combo box
        self.ui.penJoinComboBox.addItem("Miter", Qt.MiterJoin)
        self.ui.penJoinComboBox.addItem("Bevel", Qt.BevelJoin)
        self.ui.penJoinComboBox.addItem("Round", Qt.RoundJoin)
        
        # Initialize and populate brush style combo box
        self.ui.brushStyleCombobox.addItem("Linear Gradient", Qt.LinearGradientPattern)
        self.ui.brushStyleCombobox.addItem("Radial Gradient", Qt.RadialGradientPattern)
        self.ui.brushStyleCombobox.addItem("Conical Gradient", Qt.ConicalGradientPattern)
        self.ui.brushStyleCombobox.addItem("Texture", Qt.TexturePattern)
        self.ui.brushStyleCombobox.addItem("Solid", Qt.SolidPattern)
        self.ui.brushStyleCombobox.addItem("Horizontal", Qt.HorPattern)
        self.ui.brushStyleCombobox.addItem("Vertical", Qt.VerPattern)
        self.ui.brushStyleCombobox.addItem("Cross", Qt.CrossPattern)
        self.ui.brushStyleCombobox.addItem("Backward Diagonal", Qt.BDiagPattern)
        self.ui.brushStyleCombobox.addItem("Forward Diagonal", Qt.FDiagPattern)
        self.ui.brushStyleCombobox.addItem("Diagonal Cross", Qt.DiagCrossPattern)
        self.ui.brushStyleCombobox.addItem("Dense 1", Qt.Dense1Pattern)
        self.ui.brushStyleCombobox.addItem("Dense 2", Qt.Dense2Pattern)
        self.ui.brushStyleCombobox.addItem("Dense 3", Qt.Dense3Pattern)
        self.ui.brushStyleCombobox.addItem("Dense 4", Qt.Dense4Pattern)
        self.ui.brushStyleCombobox.addItem("Dense 5", Qt.Dense5Pattern)
        self.ui.brushStyleCombobox.addItem("Dense 6", Qt.Dense6Pattern)
        self.ui.brushStyleCombobox.addItem("Dense 7", Qt.Dense7Pattern)
        self.ui.brushStyleCombobox.addItem("None", Qt.NoBrush)
        
        # Create the canvas widget and add it to the layout
        self.canvas = ShapeCanvas(self)
        self.ui.canvasLayout.addWidget(self.canvas)
        
        # Connect signals to slots
        self.ui.shapeCombo.activated.connect(self.on_shapeCombo_activated)
        self.ui.penWidthSpinbox.valueChanged.connect(self.on_penWidthSpinbox_valueChanged)
        self.ui.penStyleCombobox.activated.connect(self.on_penStyleCombobox_activated)
        self.ui.penCapCombobox.activated.connect(self.on_penCapCombobox_activated)
        self.ui.penJoinComboBox.activated.connect(self.on_penJoinComboBox_activated)
        self.ui.brushStyleCombobox.activated.connect(self.on_brushStyleCombobox_activated)
        self.ui.antiAlisingCheckbox.toggled.connect(self.on_antiAlisingCheckbox_toggled)
        self.ui.transformsCheckbox.toggled.connect(self.on_transformsCheckbox_toggled)
        
        # Initialize pen and brush
        self.penChanged()
        self.brushChanged()
    
    @Slot(int)
    def on_shapeCombo_activated(self, index):
        """Handle shape combo box selection"""
        shape = self.ui.shapeCombo.itemData(index)
        self.canvas.setShape(shape)
    
    @Slot(int)
    def on_penWidthSpinbox_valueChanged(self, value):
        """Handle pen width change"""
        self.penChanged()
    
    @Slot(int)
    def on_penStyleCombobox_activated(self, index):
        """Handle pen style selection"""
        self.penChanged()
    
    @Slot(int)
    def on_penCapCombobox_activated(self, index):
        """Handle pen cap selection"""
        self.penChanged()
    
    @Slot(int)
    def on_penJoinComboBox_activated(self, index):
        """Handle pen join selection"""
        self.penChanged()
    
    @Slot(int)
    def on_brushStyleCombobox_activated(self, index):
        """Handle brush style selection"""
        self.brushChanged()
    
    @Slot(bool)
    def on_antiAlisingCheckbox_toggled(self, checked):
        """Handle antialiasing checkbox toggle"""
        self.canvas.setAntialiased(checked)
    
    @Slot(bool)
    def on_transformsCheckbox_toggled(self, checked):
        """Handle transforms checkbox toggle"""
        self.canvas.setTransformed(checked)
    
    def penChanged(self):
        """Update the pen based on UI controls"""
        pen_width = self.ui.penWidthSpinbox.value()
        
        # Get the selected pen style
        style_index = self.ui.penStyleCombobox.currentIndex()
        style = self.ui.penStyleCombobox.itemData(style_index)
        
        # Get the selected pen cap
        cap_index = self.ui.penCapCombobox.currentIndex()
        cap = self.ui.penCapCombobox.itemData(cap_index)
        
        # Get the selected pen join
        join_index = self.ui.penJoinComboBox.currentIndex()
        join = self.ui.penJoinComboBox.itemData(join_index)
        
        # Create and configure the pen
        pen = QPen()
        pen.setWidth(pen_width)
        pen.setStyle(Qt.PenStyle(style))
        pen.setCapStyle(Qt.PenCapStyle(cap))
        pen.setJoinStyle(Qt.PenJoinStyle(join))
        
        # Update the canvas
        self.canvas.setPen(pen)
    
    def brushChanged(self):
        """Update the brush based on UI controls"""
        # Get the selected brush style
        style_index = self.ui.brushStyleCombobox.currentIndex()
        style = Qt.BrushStyle(self.ui.brushStyleCombobox.itemData(style_index))
        
        # Create and configure the brush based on the selected style
        if style == Qt.LinearGradientPattern:
            # Linear gradient brush
            linear_gradient = QLinearGradient(0, 0, 100, 100)
            linear_gradient.setColorAt(0.0, Qt.red)
            linear_gradient.setColorAt(0.2, Qt.green)
            linear_gradient.setColorAt(1.0, Qt.blue)
            self.canvas.setBrush(QBrush(linear_gradient))
            
        elif style == Qt.RadialGradientPattern:
            # Radial gradient brush
            radial_gradient = QRadialGradient(50, 50, 50, 70, 70)
            radial_gradient.setColorAt(0.0, Qt.red)
            radial_gradient.setColorAt(0.2, Qt.green)
            radial_gradient.setColorAt(1.0, Qt.blue)
            self.canvas.setBrush(QBrush(radial_gradient))
            
        elif style == Qt.ConicalGradientPattern:
            # Conical gradient brush
            conical_gradient = QConicalGradient(50, 50, 150)
            conical_gradient.setColorAt(0.0, Qt.red)
            conical_gradient.setColorAt(0.2, Qt.green)
            conical_gradient.setColorAt(1.0, Qt.blue)
            self.canvas.setBrush(QBrush(conical_gradient))
            
        elif style == Qt.TexturePattern:
            # Texture brush
            try:
                pixmap = QPixmap("images/learnqt.png")
                if pixmap.isNull():
                    # Create a placeholder if image not found
                    pixmap = QPixmap(50, 50)
                    pixmap.fill(Qt.darkCyan)
                self.canvas.setBrush(QBrush(pixmap))
            except:
                # Fallback to a solid brush
                self.canvas.setBrush(QBrush(Qt.blue, Qt.SolidPattern))
                
        else:
            # Standard brush patterns
            self.canvas.setBrush(QBrush(Qt.blue, style))