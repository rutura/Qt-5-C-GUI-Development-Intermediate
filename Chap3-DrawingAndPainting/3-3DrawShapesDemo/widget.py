from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QPen, QBrush, QFont, QPixmap, QPolygonF
from PySide6.QtCore import Qt, QPointF, QRectF
from ui_widget import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
    
    def paintEvent(self, event):
        """Override paint event to draw various shapes"""
        painter = QPainter(self)
        mPen = QPen()
        mPen.setColor(Qt.black)
        mPen.setWidth(5)
        
        painter.setPen(mPen)
        
        # Draw rectangle
        painter.setBrush(Qt.red)
        painter.drawRect(10, 10, 100, 100)
        
        # Draw ellipse
        painter.setBrush(Qt.green)
        painter.drawEllipse(120, 10, 200, 100)
        
        # Draw rounded rectangle
        painter.setBrush(Qt.gray)
        painter.drawRoundedRect(330, 10, 200, 100, 20, 20)
        
        # Draw individual lines
        painter.drawLine(550, 30, 650, 30)
        painter.drawLine(550, 50, 650, 50)
        painter.drawLine(550, 70, 650, 70)
        painter.drawLine(550, 90, 650, 90)
        
        # Draw lines using a vector of points
        mPen.setColor(Qt.red)
        painter.setPen(mPen)
        pointVec = [
            QPointF(660, 30), QPointF(760, 30),
            QPointF(660, 50), QPointF(760, 50),
            QPointF(660, 70), QPointF(760, 70),
            QPointF(660, 90), QPointF(760, 90)
        ]
        painter.drawLines(pointVec)
        
        # Draw polygon
        polygon = QPolygonF([
            QPointF(240.0, 150.0),
            QPointF(10.0, 150.0),
            QPointF(60.0, 200.0),
            QPointF(30.0, 250.0),
            QPointF(120.0, 250.0)
        ])
        painter.drawPolygon(polygon)
        
        # Draw arc
        rectangle = QRectF(250.0, 150.0, 150.0, 150.0)
        startAngle = 30 * 16  # Qt uses 16th of a degree for angles
        spanAngle = 240 * 16
        painter.drawArc(rectangle, startAngle, spanAngle)
        
        # Draw chord
        chordRect = QRectF(450.0, 150.0, 150.0, 150.0)
        startAngle = 30 * 16
        spanAngle = 240 * 16
        painter.drawChord(chordRect, startAngle, spanAngle)
        
        # Draw pie
        pieRect = QRectF(650.0, 150.0, 150.0, 150.0)
        startAngle = 30 * 16
        spanAngle = 240 * 16
        painter.drawPie(pieRect, startAngle, spanAngle)
        
        # Draw text
        mPen.setColor(Qt.blue)
        painter.setPen(mPen)
        painter.setFont(QFont("Times", 40, QFont.Bold))
        painter.drawText(50.0, 400.0, "I'm loving Qt")
        
        # Draw pixmap
        try:
            target = QRectF(520.0, 350.0, 200.0, 200.0)
            mPix = QPixmap("images/LearnQt.png")  # Update path as needed
            
            # If we can't find the original image, use a placeholder
            if mPix.isNull():
                mPix = QPixmap(200, 200)
                mPix.fill(Qt.darkCyan)
                
                # Draw a placeholder text on the pixmap
                tempPainter = QPainter(mPix)
                tempPainter.setPen(Qt.white)
                tempPainter.setFont(QFont("Arial", 20))
                tempPainter.drawText(mPix.rect(), Qt.AlignCenter, "Qt Logo")
                tempPainter.end()
                
            mSourceRect = mPix.rect()
            painter.drawPixmap(target, mPix, mSourceRect)
        except Exception as e:
            print(f"Error drawing pixmap: {e}")