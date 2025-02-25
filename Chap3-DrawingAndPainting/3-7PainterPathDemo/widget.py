from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QPainterPath, QBrush
from PySide6.QtCore import Qt
from ui_widget import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
    
    def paintEvent(self, event):
        """Override paint event to demonstrate painter paths"""
        painter = QPainter(self)
        
        # First path: rectangle with line and arc
        path = QPainterPath()
        
        # Add a rectangle to the path
        path.addRect(100, 100, 100, 100)
        
        # Move to the center of the rectangle
        path.moveTo(150, 150)
        
        # Draw a line upward
        path.lineTo(150, 50)
        
        # Draw an arc (center x, y, width, height, startAngle, sweepLength)
        # Note: angles are specified in degrees * 16
        path.arcTo(50, 50, 200, 200, 90, 90)
        
        # Complete the shape by going back to center
        path.lineTo(150, 150)
        
        # Fill the path with green color
        painter.setBrush(Qt.green)
        painter.drawPath(path)
        
        # Second path: two circles connected by lines
        path2 = QPainterPath()
        
        # Add two circles to the path
        path2.addEllipse(100, 220, 100, 100)
        path2.addEllipse(400, 220, 100, 100)
        
        # Draw the upper connecting line
        path2.moveTo(150, 220)
        path2.lineTo(450, 220)
        
        # Draw the lower connecting line
        path2.moveTo(150, 320)
        path2.lineTo(450, 320)
        
        # Draw the path (no fill)
        painter.setBrush(Qt.transparent)  # No fill color
        painter.drawPath(path2)
        
        # Draw a translated copy of the second path
        # Create a translated copy using path2's translate method
        path2.translate(150, 150)
        painter.drawPath(path2)