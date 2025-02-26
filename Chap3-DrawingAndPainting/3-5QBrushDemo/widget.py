from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QBrush, QPixmap
from PySide6.QtCore import Qt
from ui_widget import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
    
    def paintEvent(self, event):
        """Override paint event to demonstrate brush styles"""
        painter = QPainter(self)
        
        # Create a brush
        mBrush = QBrush()
        
        # First Row of Brush Patterns
        
        # Solid Pattern
        mBrush.setColor(Qt.red)
        mBrush.setStyle(Qt.SolidPattern)
        painter.setBrush(mBrush)
        painter.drawRect(20, 20, 100, 100)
        
        # Dense1Pattern
        mBrush.setColor(Qt.blue)
        mBrush.setStyle(Qt.Dense1Pattern)
        painter.setBrush(mBrush)
        painter.drawRect(130, 20, 100, 100)
        
        # Dense2Pattern
        mBrush.setColor(Qt.red)
        mBrush.setStyle(Qt.Dense2Pattern)
        painter.setBrush(mBrush)
        painter.drawRect(240, 20, 100, 100)
        
        # Dense3Pattern
        mBrush.setColor(Qt.black)
        mBrush.setStyle(Qt.Dense3Pattern)
        painter.setBrush(mBrush)
        painter.drawRect(350, 20, 100, 100)
        
        # Dense4Pattern
        mBrush.setColor(Qt.blue)
        mBrush.setStyle(Qt.Dense4Pattern)
        painter.setBrush(mBrush)
        painter.drawRect(460, 20, 100, 100)
        
        # Dense5Pattern
        mBrush.setColor(Qt.blue)
        mBrush.setStyle(Qt.Dense5Pattern)
        painter.setBrush(mBrush)
        painter.drawRect(570, 20, 100, 100)
        
        # Dense6Pattern
        mBrush.setColor(Qt.blue)
        mBrush.setStyle(Qt.Dense6Pattern)
        painter.setBrush(mBrush)
        painter.drawRect(680, 20, 100, 100)
        
        # Dense7Pattern
        mBrush.setColor(Qt.blue)
        mBrush.setStyle(Qt.Dense7Pattern)
        painter.setBrush(mBrush)
        painter.drawRect(790, 20, 100, 100)
        
        # Second Row of Brush Patterns
        
        # HorPattern - Horizontal lines
        mBrush.setColor(Qt.blue)
        mBrush.setStyle(Qt.HorPattern)
        painter.setBrush(mBrush)
        painter.drawRect(20, 130, 100, 100)
        
        # VerPattern - Vertical lines
        mBrush.setColor(Qt.blue)
        mBrush.setStyle(Qt.VerPattern)
        painter.setBrush(mBrush)
        painter.drawRect(130, 130, 100, 100)
        
        # CrossPattern - Crossing horizontal and vertical lines
        mBrush.setColor(Qt.blue)
        mBrush.setStyle(Qt.CrossPattern)
        painter.setBrush(mBrush)
        painter.drawRect(240, 130, 100, 100)
        
        # BDiagPattern - Backward diagonal lines
        mBrush.setColor(Qt.blue)
        mBrush.setStyle(Qt.BDiagPattern)
        painter.setBrush(mBrush)
        painter.drawRect(350, 130, 100, 100)
        
        # FDiagPattern - Forward diagonal lines
        mBrush.setColor(Qt.blue)
        mBrush.setStyle(Qt.FDiagPattern)
        painter.setBrush(mBrush)
        painter.drawRect(460, 130, 100, 100)
        
        # DiagCrossPattern - Crossing diagonal lines
        mBrush.setColor(Qt.blue)
        mBrush.setStyle(Qt.DiagCrossPattern)
        painter.setBrush(mBrush)
        painter.drawRect(570, 130, 100, 100)
        
        # TexturePattern - Custom image pattern
        try:
            # Try to load image from a file
            mPix = QPixmap("images/LearnQt.png")
            
            # If we can't find the original image, use a placeholder
            if mPix.isNull():
                mPix = QPixmap(50, 50)
                mPix.fill(Qt.darkCyan)
                
                # Create a simple pattern in the pixmap
                tempPainter = QPainter(mPix)
                tempPainter.setPen(Qt.white)
                tempPainter.drawLine(0, 0, 50, 50)
                tempPainter.drawLine(0, 50, 50, 0)
                tempPainter.end()
                
            mBrush.setTexture(mPix.scaled(50, 50))
            painter.setBrush(mBrush)
            painter.drawRect(680, 130, 210, 100)
        except Exception as e:
            print(f"Error setting texture: {e}")