from PySide6.QtWidgets import QWidget
from PySide6.QtGui import (QPainter, QBrush, QLinearGradient, QRadialGradient, 
                          QConicalGradient, QGradient)
from PySide6.QtCore import (QPointF, QLineF)
from ui_widget import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
    
    def paintEvent(self, event):
        """Override paint event to demonstrate gradient brushes"""
        painter = QPainter(self)
        
        # Linear Gradient
        linearGradient = QLinearGradient(QPointF(70, 20), QPointF(70, 170))
        linearGradient.setColorAt(0, "red")
        linearGradient.setColorAt(0.5, "gray")
        linearGradient.setColorAt(1, "yellow")
        
        # Set spread method - how the gradient fills areas outside its bounds
        linearGradient.setSpread(QGradient.ReflectSpread)
        
        # Create brush with the gradient and use it
        mBrush = QBrush(linearGradient)
        painter.setBrush(mBrush)
        painter.drawRect(20, 20, 100, 300)
        
        # Draw a line to show the gradient vector (from start to end point)
        painter.drawLine(QLineF(QPointF(70, 20), QPointF(70, 170)))
        
        # Radial Gradient
        radialGradient = QRadialGradient(QPointF(280, 170), 75)
        radialGradient.setColorAt(0, "blue")
        radialGradient.setColorAt(1, "yellow")
        
        # Set spread method
        radialGradient.setSpread(QGradient.RepeatSpread)
        
        # Create brush with the radial gradient
        mBrushRad = QBrush(radialGradient)
        painter.setBrush(mBrushRad)
        painter.drawRect(130, 20, 300, 300)
        
        # Conical Gradient
        # Parameters: center point and start angle in degrees
        conicalGradient = QConicalGradient(QPointF(600, 170), 90)
        conicalGradient.setColorAt(0, "blue")
        conicalGradient.setColorAt(1, "yellow")
        
        # Create brush with the conical gradient
        painter.setBrush(QBrush(conicalGradient))
        painter.drawEllipse(450, 20, 300, 300)