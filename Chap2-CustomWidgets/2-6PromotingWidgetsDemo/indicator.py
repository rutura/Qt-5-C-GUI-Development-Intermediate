from PySide6.QtWidgets import QWidget, QSizePolicy
from PySide6.QtCore import Qt, QTimer, QSize, QRectF, Slot
from PySide6.QtGui import QPainter, QPen, QBrush, QPaintEvent

class Indicator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Initialize state variables
        self.greenActive = False
        self.redActive = False
        self.yellowActive = False
        self.lightsOn = True
        
        # Set size policy
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        
        # Set initial state
        self.activateNormal()
        
        # Set up blinking timer
        self.timer = QTimer(self)
        self.timer.setInterval(300)
        self.timer.timeout.connect(self.toggleLights)
        self.timer.start()
    
    @Slot()
    def activateNormal(self):
        """Activate the green light (normal state)"""
        self.greenActive = True
        self.yellowActive = self.redActive = False
        self.update()
    
    @Slot()
    def activateWarning(self):
        """Activate the yellow light (warning state)"""
        self.yellowActive = True
        self.redActive = self.greenActive = False
        self.update()
    
    @Slot()
    def activateDanger(self):
        """Activate the red light (danger state)"""
        self.redActive = True
        self.yellowActive = self.greenActive = False
        self.update()
    
    def paintEvent(self, event: QPaintEvent):
        """Custom paint event to draw the traffic light indicator"""
        # Set up painter and pen
        mPen = QPen()
        mPen.setWidth(3)
        mPen.setColor(Qt.black)
        
        painter = QPainter(self)
        painter.setPen(mPen)
        painter.setBrush(Qt.gray)  # Fill color
        
        # Draw the traffic light box
        painter.drawRect(QRectF(0, 0, 120, 330))
        
        # Draw the appropriate active light
        if self.redActive:
            # Red light
            painter.setBrush(Qt.red if self.lightsOn else Qt.black)
            painter.drawEllipse(10, 10, 100, 100)
            
            painter.setBrush(Qt.black)
            painter.drawEllipse(10, 115, 100, 100)
            
            painter.setBrush(Qt.black)
            painter.drawEllipse(10, 220, 100, 100)
            
        elif self.greenActive:
            # Green light
            painter.setBrush(Qt.black)
            painter.drawEllipse(10, 10, 100, 100)
            
            painter.setBrush(Qt.green if self.lightsOn else Qt.black)
            painter.drawEllipse(10, 115, 100, 100)
            
            painter.setBrush(Qt.black)
            painter.drawEllipse(10, 220, 100, 100)
            
        elif self.yellowActive:
            # Yellow light
            painter.setBrush(Qt.black)
            painter.drawEllipse(10, 10, 100, 100)
            
            painter.setBrush(Qt.black)
            painter.drawEllipse(10, 115, 100, 100)
            
            painter.setBrush(Qt.yellow if self.lightsOn else Qt.black)
            painter.drawEllipse(10, 220, 100, 100)
    
    def sizeHint(self) -> QSize:
        """Suggested size for the widget"""
        return QSize(120, 350)
    
    def toggleLights(self):
        """Toggle the lights on/off for blinking effect"""
        self.lightsOn = not self.lightsOn
        self.update()