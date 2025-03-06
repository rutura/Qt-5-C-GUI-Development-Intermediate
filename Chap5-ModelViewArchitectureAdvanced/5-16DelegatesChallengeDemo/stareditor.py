from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt, Signal, QSize, QPoint
from PySide6.QtGui import QPainter, QMouseEvent, QPaintEvent, QPolygon, QBrush

class StarEditor(QWidget):
    # Define a signal for when editing is finished
    editingFinished = Signal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Enable mouse tracking for this widget
        self.setMouseTracking(True)
        
        # Create star polygon shape
        self.poly = QPolygon()
        self.poly << QPoint(0, 85) << QPoint(75, 75) \
                 << QPoint(100, 10) << QPoint(125, 75) \
                 << QPoint(200, 85) << QPoint(150, 125) \
                 << QPoint(160, 190) << QPoint(100, 150) \
                 << QPoint(40, 190) << QPoint(50, 125) \
                 << QPoint(0, 85)
        
        # Initialize star rating
        self.starRating = 0
    
    def sizeHint(self):
        """Return the recommended size for the widget"""
        return QSize(100, 50)
    
    def getStarRating(self):
        """Get the current star rating"""
        return self.starRating
    
    def setStarRating(self, value):
        """Set the star rating"""
        self.starRating = value
        self.update()  # Trigger a repaint
    
    def mouseReleaseEvent(self, event):
        """Handle mouse release events to finalize editing"""
        self.editingFinished.emit()
    
    def mouseMoveEvent(self, event):
        """Handle mouse move events to update the star rating"""
        rating = int(event.position().x() // 20)
        
        # Only update if the rating has changed and is valid
        if rating != self.starRating and rating < 6:
            self.starRating = rating
            self.update()  # Trigger a repaint
    
    def paintEvent(self, event):
        """Paint the star editor widget"""
        painter = QPainter(self)
        painter.save()
        
        # Enable antialiasing for smoother drawing
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        painter.setPen(Qt.PenStyle.NoPen)
        
        # Draw background
        painter.setBrush(QBrush(Qt.GlobalColor.green))
        painter.drawRect(self.rect())
        
        # Draw stars
        painter.setBrush(QBrush(Qt.GlobalColor.yellow))
        
        # Move painter for star drawing
        painter.translate(self.rect().x(), self.rect().y() + 10)
        painter.scale(0.1, 0.1)
        
        # Draw the stars based on current rating
        for i in range(self.starRating):
            painter.drawPolygon(self.poly)
            painter.translate(220, 0)
        
        painter.restore()