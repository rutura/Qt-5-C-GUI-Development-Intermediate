from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QPen, QBrush, QPolygonF
from PySide6.QtCore import Qt, QPoint, QPointF
from ui_widget import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
    
    def paintEvent(self, event):
        """Override paint event to demonstrate pen styles"""
        painter = QPainter(self)
        mPen = QPen()  # No pen style set, default is Qt::SolidLine
        mPen.setColor(Qt.black)
        mPen.setWidth(5)
        
        # ----------------
        # Pen Style
        # ----------------
        
        # Default: Qt::SolidLine
        mPen.setStyle(Qt.SolidLine)
        painter.setPen(mPen)
        painter.setBrush(Qt.red)
        painter.drawRect(10, 10, 100, 100)  # Drawn with default SolidLine
        
        # Qt::NoPen
        mPen.setStyle(Qt.NoPen)
        painter.setPen(mPen)
        painter.drawRect(120, 10, 100, 100)  # Drawn with Qt::NoPen
        
        # Qt::DashLine
        mPen.setStyle(Qt.DashLine)
        painter.setPen(mPen)
        painter.drawRect(230, 10, 100, 100)  # Drawn with Qt::DashLine
        
        # Qt::DotLine
        mPen.setStyle(Qt.DotLine)
        painter.setPen(mPen)
        painter.drawRect(340, 10, 100, 100)  # Drawn with Qt::DotLine
        
        # Qt::DashDotLine
        mPen.setStyle(Qt.DashDotLine)
        painter.setPen(mPen)
        painter.drawRect(450, 10, 100, 100)  # Drawn with Qt::DashDotLine
        
        # Qt::DashDotDotLine
        mPen.setStyle(Qt.DashDotDotLine)
        painter.setPen(mPen)
        painter.drawRect(560, 10, 100, 100)  # Drawn with Qt::DashDotDotLine
        
        # CustomDash Line
        dashes = [1, 4, 3, 4, 9, 4, 27, 4, 9, 4]  # pattern of dash, space, dash, space...
        mPen.setDashPattern(dashes)
        painter.setPen(mPen)
        painter.drawRect(670, 10, 100, 100)  # Drawn with custom dash pattern
        
        # ----------------
        # Cap Style
        # ----------------
        
        start = QPoint(100, 150)
        end = QPoint(500, 150)
        mPen.setWidth(20)
        mPen.setStyle(Qt.SolidLine)
        
        # Qt::FlatCap
        mPen.setCapStyle(Qt.FlatCap)
        painter.setPen(mPen)
        painter.drawLine(start, end)
        
        # Qt::SquareCap
        start.setY(200)
        end.setY(200)
        mPen.setCapStyle(Qt.SquareCap)
        painter.setPen(mPen)
        painter.drawLine(start, end)
        
        # Qt::RoundCap
        start.setY(250)
        end.setY(250)
        mPen.setCapStyle(Qt.RoundCap)
        painter.setPen(mPen)
        painter.drawLine(start, end)
        
        # ----------------
        # Join Style
        # ----------------
        
        points = [
            QPointF(10.0, 380.0),
            QPointF(50.0, 310.0),
            QPointF(320.0, 330.0),
            QPointF(250.0, 370.0)
        ]
        
        mPen.setWidth(10)
        mPen.setStyle(Qt.SolidLine)
        
        # Qt::MiterJoin
        mPen.setJoinStyle(Qt.MiterJoin)
        painter.setPen(mPen)
        painter.setBrush(Qt.transparent)  # No fill
        polygon = QPolygonF(points)
        painter.drawPolygon(polygon)
        
        # Qt::BevelJoin
        # Move the points down and draw blue polygon
        for i in range(len(points)):
            points[i] = QPointF(points[i].x(), points[i].y() + 100.0)
        
        mPen.setJoinStyle(Qt.BevelJoin)
        painter.setPen(mPen)
        painter.setBrush(Qt.blue)
        polygon = QPolygonF(points)
        painter.drawPolygon(polygon)
        
        # Qt::RoundJoin
        # Move the points right and draw yellow polygon
        for i in range(len(points)):
            points[i] = QPointF(points[i].x() + 300.0, points[i].y())
        
        mPen.setJoinStyle(Qt.RoundJoin)
        painter.setPen(mPen)
        painter.setBrush(Qt.yellow)
        polygon = QPolygonF(points)
        painter.drawPolygon(polygon)