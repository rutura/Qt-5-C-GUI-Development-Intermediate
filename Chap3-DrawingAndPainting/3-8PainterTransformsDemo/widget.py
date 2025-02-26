from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QPen
from PySide6.QtCore import Qt
from ui_widget import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
    
    def paintEvent(self, event):
        """Override paint event to demonstrate painter transformations"""
        painter = QPainter(self)
        mPen = QPen()
        mPen.setWidth(5)
        
        # Draw original rectangle (black)
        painter.setPen(mPen)
        painter.drawRect(100, 100, 200, 200)
        
        # Rotate the coordinate system and draw rectangle (green)
        # 1. Translate to the center of the rectangle
        painter.translate(200, 200)
        # 2. Apply rotation
        painter.rotate(45)
        # 3. Translate back
        painter.translate(-200, -200)
        
        mPen.setColor(Qt.green)
        painter.setPen(mPen)
        painter.drawRect(100, 100, 200, 200)
        
        # Scale the coordinate system and draw rectangle (blue)
        # 1. Translate to the center of the rectangle
        painter.translate(200, 200)
        # 2. Undo the previous rotation
        painter.rotate(-45)
        # 3. Translate back
        painter.translate(-200, -200)
        
        # Apply scaling
        painter.scale(0.6, 0.6)
        
        mPen.setColor(Qt.blue)
        painter.setPen(mPen)
        painter.drawRect(100, 100, 200, 200)
        
        # Reset all transformations and draw the original rectangle again (red)
        painter.resetTransform()
        
        mPen.setColor(Qt.red)
        painter.setPen(mPen)
        painter.drawRect(100, 100, 200, 200)
        
        # Apply shearing transformation and draw rectangle (yellow)
        # 1. Translate to the center of the rectangle
        painter.translate(200, 200)
        # 2. Apply shearing
        painter.shear(0.6, 0.6)
        # 3. Translate back
        painter.translate(-200, -200)
        
        mPen.setColor(Qt.yellow)
        painter.setPen(mPen)
        painter.drawRect(100, 100, 200, 200)