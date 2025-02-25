from PySide6.QtWidgets import QWidget, QSizePolicy
from PySide6.QtCore import Qt, QTimer, QSize, Signal
from PySide6.QtGui import QPainter, QPen, QBrush, QPaintEvent, QWheelEvent

class WaterTank(QWidget):
    # Define signals
    normal = Signal()   # Green - normal water level
    warning = Signal()  # Yellow - warning water level
    danger = Signal()   # Red - danger water level
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Initialize water height
        self.waterHeight = 50
        
        # Set size policy
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        
        # Set up timer for water level changes
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.updateWaterLevel)
        self.timer.start()
    
    def updateWaterLevel(self):
        """Increase water level and emit appropriate signals"""
        self.waterHeight += 15
        self.update()
        
        # Emit signals based on water level
        if self.waterHeight <= 210:
            self.normal.emit()
        elif 211 <= self.waterHeight <= 239:
            self.warning.emit()
        else:
            self.danger.emit()
    
    def paintEvent(self, event: QPaintEvent):
        """Custom paint event to draw the water tank"""
        # Set up painter and pen
        mPen = QPen()
        mPen.setColor(Qt.black)
        mPen.setWidth(3)
        
        painter = QPainter(self)
        painter.setPen(mPen)
        
        # Draw the tank walls
        painter.drawLine(10, 10, 10, 300)      # Left
        painter.drawLine(10, 300, 300, 300)    # Bottom
        painter.drawLine(300, 300, 300, 10)    # Right
        
        # Draw the water
        painter.setBrush(Qt.blue)
        painter.drawRect(10, 300 - self.waterHeight, 290, self.waterHeight)
    
    def sizeHint(self) -> QSize:
        """Suggested size for the widget"""
        return QSize(400, 400)
    
    def wheelEvent(self, event: QWheelEvent):
        """Handle mouse wheel events to decrease water level"""
        # Check for backward wheel movement and if water height is greater than minimum
        if event.angleDelta().y() < 0 and self.waterHeight > 10:
            self.waterHeight -= 10
            self.update()
            
            # Emit signals based on updated water level
            if self.waterHeight <= 210:
                self.normal.emit()
            elif 211 <= self.waterHeight <= 239:
                self.warning.emit()
            else:
                self.danger.emit()