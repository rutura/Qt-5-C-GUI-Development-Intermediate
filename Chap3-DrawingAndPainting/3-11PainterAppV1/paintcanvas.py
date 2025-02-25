from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QPen, QColor, QImage, QMouseEvent, QPaintEvent, QResizeEvent
from PySide6.QtCore import Qt, QPoint, QRect, QRectF, QSize

class PaintCanvas(QWidget):
    # Tool type enum
    Pen, Rect, Ellipse, Eraser = range(4)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Initialize properties
        self.tool = self.Pen
        self.fill = False
        self.drawing = False
        self.penWidth = 3
        self.fillColor = QColor(Qt.red)
        self.penColor = QColor(Qt.green)
        self.lastPoint = QPoint()
        self.lastRect = QRectF(0, 0, 0, 0)
        self.lastEraserRect = QRectF(0, 0, 0, 0)
        
        # Create a white image to paint on
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)
    
    def getTool(self):
        return self.tool
    
    def setTool(self, value):
        self.tool = value
    
    def getFill(self):
        return self.fill
    
    def setFill(self, value):
        self.fill = value
    
    def getPenWidth(self):
        return self.penWidth
    
    def setPenWidth(self, value):
        self.penWidth = value
    
    def getFillColor(self):
        return self.fillColor
    
    def setFillColor(self, value):
        self.fillColor = value
    
    def getPenColor(self):
        return self.penColor
    
    def setPenColor(self, value):
        self.penColor = value
    
    def drawLineTo(self, endPoint):
        """Draw a line from last point to current point"""
        painter = QPainter(self.image)
        painter.setPen(QPen(self.penColor, self.penWidth, Qt.SolidLine, 
                           Qt.RoundCap, Qt.RoundJoin))
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.drawLine(self.lastPoint, endPoint)
        
        # Update only the drawn part for efficiency
        adjustment = self.penWidth + 2
        updateRect = QRect(self.lastPoint, endPoint).normalized().adjusted(
            -adjustment, -adjustment, adjustment, adjustment)
        self.update(updateRect)
        
        self.lastPoint = endPoint
    
    def drawRectTo(self, endPoint, ellipse=False):
        """Draw a rectangle/ellipse from last point to current point"""
        painter = QPainter(self.image)
        painter.setPen(QPen(self.penColor, self.penWidth, Qt.SolidLine, 
                           Qt.RoundCap, Qt.RoundJoin))
        
        # Set brush based on fill property
        if self.fill:
            painter.setBrush(self.fillColor)
        else:
            painter.setBrush(Qt.NoBrush)
        
        # Draw rect or ellipse
        if not ellipse:
            painter.drawRect(QRect(self.lastPoint, endPoint))
        else:
            painter.drawEllipse(QRect(self.lastPoint, endPoint))
        
        # When still drawing, erase the last temporary shape
        if self.drawing:
            painter.setPen(QPen(Qt.white, self.penWidth+2, Qt.SolidLine, 
                               Qt.RoundCap, Qt.RoundJoin))
            
            if self.fill:
                painter.setBrush(Qt.white)
            else:
                painter.setBrush(Qt.NoBrush)
            
            if not ellipse:
                painter.drawRect(self.lastRect)
            else:
                painter.drawEllipse(self.lastRect)
            
            # Reset the pen and brush
            painter.setPen(QPen(self.penColor, self.penWidth, Qt.SolidLine, 
                               Qt.RoundCap, Qt.RoundJoin))
            if self.fill:
                painter.setBrush(self.fillColor)
            else:
                painter.setBrush(Qt.NoBrush)
        
        self.lastRect = QRectF(self.lastPoint, endPoint)
        self.update()
    
    def eraseUnder(self, topLeft):
        """Erase content under a specific point"""
        painter = QPainter(self.image)
        
        # Erase last eraser rect
        painter.setBrush(Qt.white)
        painter.setPen(Qt.white)
        painter.drawRect(self.lastEraserRect)
        
        # Erase the content under current eraser rect
        currentRect = QRect(topLeft, QSize(100, 100))
        painter.setBrush(Qt.white)
        painter.setPen(Qt.white)
        painter.drawRect(currentRect)
        
        # Draw current eraser rect
        painter.setBrush(Qt.black)
        painter.setPen(Qt.black)
        painter.drawRect(currentRect)
        
        self.lastEraserRect = currentRect
        
        # If not drawing, erase the last eraser rect
        if not self.drawing:
            painter.setBrush(Qt.white)
            painter.setPen(Qt.white)
            painter.drawRect(self.lastEraserRect)
            self.lastEraserRect = QRect(0, 0, 0, 0)
        
        self.update()
    
    def resizeImage(self, image, newSize):
        """Resize the image to a new size"""
        if image.size() == newSize:
            return
        
        newImage = QImage(newSize, QImage.Format_RGB32)
        newImage.fill(Qt.white)
        painter = QPainter(newImage)
        painter.drawImage(QPoint(0, 0), image)
        
        return newImage
    
    def mousePressEvent(self, event):
        """Handle mouse press events"""
        if event.button() == Qt.LeftButton:
            self.lastPoint = event.position().toPoint()
            self.drawing = True
    
    def mouseMoveEvent(self, event):
        """Handle mouse move events"""
        if (event.buttons() & Qt.LeftButton) and self.drawing:
            pos = event.position().toPoint()
            
            if self.tool == self.Pen:
                self.drawLineTo(pos)
            elif self.tool == self.Rect:
                self.drawRectTo(pos)
            elif self.tool == self.Ellipse:
                self.drawRectTo(pos, True)
            elif self.tool == self.Eraser:
                self.eraseUnder(pos)
    
    def mouseReleaseEvent(self, event):
        """Handle mouse release events"""
        if event.button() == Qt.LeftButton and self.drawing:
            pos = event.position().toPoint()
            
            self.drawing = False
            if self.tool == self.Pen:
                self.drawLineTo(pos)
            elif self.tool == self.Rect:
                self.drawRectTo(pos)
            elif self.tool == self.Ellipse:
                self.drawRectTo(pos, True)
            elif self.tool == self.Eraser:
                self.eraseUnder(pos)
            
            # Reset the last rect
            self.lastRect = QRect(0, 0, 0, 0)
    
    def paintEvent(self, event):
        """Paint event to display the image"""
        painter = QPainter(self)
        rectToDraw = event.rect()
        painter.drawImage(rectToDraw, self.image, rectToDraw)
    
    def resizeEvent(self, event):
        """Handle resize events"""
        if self.width() > self.image.width() or self.height() > self.image.height():
            newWidth = max(self.width() + 128, self.image.width())
            newHeight = max(self.height() + 128, self.image.height())
            self.image = self.resizeImage(self.image, QSize(newWidth, newHeight))
            self.update()
        
        super().resizeEvent(event)