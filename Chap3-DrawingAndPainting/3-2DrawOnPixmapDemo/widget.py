from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPixmap, QPainter, QPen, QFont, QBrush
from PySide6.QtCore import Qt
from ui_widget import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # Create a pixmap with the widget's dimensions (minus some margin)
        mPix = QPixmap(self.width() - 10, self.height() - 10)
        mPix.fill(Qt.gray)
        
        # Configure pen, brush, and font
        pen = QPen()
        pen.setWidth(5)
        pen.setColor(Qt.white)
        
        mFont = QFont("Consolas", 20, QFont.Bold)
        
        # Create painter for the pixmap
        painter = QPainter(mPix)
        painter.setPen(pen)
        painter.setBrush(Qt.green)
        painter.setFont(mFont)
        
        # Draw a rectangle around the pixmap's border
        painter.drawRect(mPix.rect())
        
        # Change brush color and draw another rectangle
        painter.setBrush(Qt.blue)
        painter.drawRect(50, 50, 100, 100)
        
        # Draw some text
        painter.drawText(30, 120, "I'm loving Qt")
        
        # Print debug information about the painter's coordinate systems
        print(f"Painter window (logical): {painter.window()}")
        print(f"Painter viewPort (physical): {painter.viewport()}")
        
        # End painting
        painter.end()
        
        # Set the pixmap to the label
        self.ui.label.setPixmap(mPix)
        
    def resizeEvent(self, event):
        """Handle resize events to update the pixmap size"""
        # This ensures the pixmap is recreated when the widget is resized
        # Re-implementation of the constructor's painting logic
        mPix = QPixmap(self.width() - 10, self.height() - 10)
        mPix.fill(Qt.gray)
        
        pen = QPen()
        pen.setWidth(5)
        pen.setColor(Qt.white)
        
        mFont = QFont("Consolas", 20, QFont.Bold)
        
        painter = QPainter(mPix)
        painter.setPen(pen)
        painter.setBrush(Qt.green)
        painter.setFont(mFont)
        
        painter.drawRect(mPix.rect())
        
        painter.setBrush(Qt.blue)
        painter.drawRect(50, 50, 100, 100)
        
        painter.drawText(30, 120, "I'm loving Qt")
        
        painter.end()
        
        self.ui.label.setPixmap(mPix)
        
        # Call the parent class's resizeEvent
        super().resizeEvent(event)