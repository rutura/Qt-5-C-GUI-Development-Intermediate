from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QPen, QPaintEvent
from PySide6.QtCore import Qt
from ui_widget import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
    
    def paintEvent(self, event: QPaintEvent):
        """Override paint event to demonstrate coordinate systems"""
        # Create a pen and painter
        mPen = QPen(Qt.red)
        mPen.setWidth(3)
        
        painter = QPainter(self)
        painter.setPen(mPen)
        
        # Display the logical and physical coordinates
        print(f"Logical coordinates: {painter.window()}")
        print(f"Physical coordinates: {painter.viewport()}")
        
        # Draw a red rectangle using default coordinates
        painter.drawRect(50, 50, 100, 100)
        
        # Change the logical coordinates, keep physical coords the same
        painter.save()
        
        painter.setWindow(0, 0, 300, 200)
        # painter.setViewport(0, 0, 300, 200)  # Commented out as in original
        mPen.setColor(Qt.green)
        painter.setPen(mPen)
        
        # Draw a green rectangle with modified logical coordinates
        painter.drawRect(50, 50, 100, 100)
        
        painter.restore()
        
        # Change physical coordinates, keep logical the same
        painter.save()
        
        mPen.setColor(Qt.blue)
        painter.setPen(mPen)
        painter.setViewport(0, 0, 300, 200)
        
        # Draw a blue rectangle with modified physical coordinates
        painter.drawRect(50, 50, 100, 100)
        
        painter.restore()