from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QPen, QBrush, QFont, QPixmap
from PySide6.QtCore import Qt, QSize, QPoint, QRect

class ShapeCanvas(QWidget):
    # Shape enum
    Polygon, Rect, RoundedRect, Ellipse, Pie, Chord, Text, Pixmap = range(8)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Initialize properties
        self.shape = self.Polygon
        self.antialiased = False
        self.transformed = False
        
        # Load pixmap - will use a fallback if image isn't found
        self.pixmap = QPixmap()
        try:
            self.pixmap.load("images/learnqt.png")
            if self.pixmap.isNull():
                # Create a simple placeholder
                self.pixmap = QPixmap(50, 50)
                self.pixmap.fill(Qt.darkCyan)
        except:
            # Create a simple placeholder
            self.pixmap = QPixmap(50, 50)
            self.pixmap.fill(Qt.darkCyan)
        
        # Initialize pen and brush (will be set by the main widget)
        self.pen = QPen()
        self.brush = QBrush()
    
    def minimumSizeHint(self) -> QSize:
        """Return the minimum size for the widget"""
        return QSize(400, 200)
    
    def sizeHint(self) -> QSize:
        """Return the preferred size for the widget"""
        return QSize(500, 300)
    
    def paintEvent(self, event):
        """Custom paint event to draw shapes"""
        painter = QPainter(self)
        
        # Define polygon points
        points = [
            QPoint(10, 80),
            QPoint(20, 10),
            QPoint(80, 30),
            QPoint(90, 70)
        ]
        
        # Define rectangle and arc parameters
        rect = QRect(10, 20, 80, 60)
        startAngle = 20 * 16
        arcLength = 120 * 16
        
        # Set up painter
        painter.setPen(self.pen)
        painter.setBrush(self.brush)
        painter.setFont(QFont("Consolas", 8, QFont.Bold))
        
        # Apply antialiasing if enabled
        if self.antialiased:
            painter.setRenderHint(QPainter.Antialiasing, True)
        
        # Loop to draw shapes in a grid pattern
        for x in range(0, self.width(), 100):
            for y in range(0, self.height(), 100):
                # Save the painter state
                painter.save()
                
                # Translate to the grid position
                painter.translate(x, y)
                
                # Apply transformation if enabled
                if self.transformed:
                    painter.translate(50, 50)
                    painter.rotate(60.0)
                    painter.scale(0.6, 0.9)
                    painter.translate(-50, -50)
                
                # Draw the selected shape
                if self.shape == self.Polygon:
                    painter.drawPolygon(points)
                
                elif self.shape == self.Rect:
                    painter.drawRect(rect)
                
                elif self.shape == self.RoundedRect:
                    painter.drawRoundedRect(rect, 25, 25, Qt.RelativeSize)
                
                elif self.shape == self.Ellipse:
                    painter.drawEllipse(rect)
                
                elif self.shape == self.Chord:
                    painter.drawChord(rect, startAngle, arcLength)
                
                elif self.shape == self.Pie:
                    painter.drawPie(rect, startAngle, arcLength)
                
                elif self.shape == self.Text:
                    painter.drawText(rect, Qt.AlignCenter, "Qt GUI")
                
                elif self.shape == self.Pixmap:
                    painter.drawPixmap(10, 10, self.pixmap)
                
                # Restore the painter state
                painter.restore()
        
        # Draw a red border around the canvas
        painter.setRenderHint(QPainter.Antialiasing, False)
        painter.setBrush(Qt.NoBrush)
        painter.setPen(Qt.red)
        painter.drawRect(0, 0, self.width() - 1, self.height() - 1)
    
    # Getter/setter methods
    def getShape(self):
        return self.shape
    
    def setShape(self, value):
        self.shape = value
        self.update()
    
    def getPen(self):
        return self.pen
    
    def setPen(self, value):
        self.pen = value
        self.update()
    
    def getBrush(self):
        return self.brush
    
    def setBrush(self, value):
        self.brush = value
        self.update()
    
    def getAntialiased(self):
        return self.antialiased
    
    def setAntialiased(self, value):
        self.antialiased = value
        self.update()
    
    def getTransformed(self):
        return self.transformed
    
    def setTransformed(self, value):
        self.transformed = value
        self.update()