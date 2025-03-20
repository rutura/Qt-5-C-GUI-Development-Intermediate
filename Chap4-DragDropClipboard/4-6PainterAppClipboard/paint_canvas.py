from PySide6.QtQuick import QQuickPaintedItem
from PySide6.QtGui import (QPainter, QPen, QColor, QBrush, QImage, QPixmap)
from PySide6.QtCore import (Qt, QPoint, QRect, QRectF, QSize, Property, Signal, 
                          Slot, QPointF)
from PySide6.QtWidgets import QApplication

import os

class PaintCanvas(QQuickPaintedItem):
    """Canvas item for drawing with various tools"""
    
    # Signals
    penColorChanged = Signal()
    fillColorChanged = Signal()
    penWidthChanged = Signal()
    fillChanged = Signal()
    toolChanged = Signal()
    
    # Tool type enum (match the values with QML)
    PEN, RECT, ELLIPSE, ERASER = range(4)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Initialize properties
        self._tool = self.PEN
        self._fill = False
        self._drawing = False
        self._penWidth = 3
        self._fillColor = QColor(Qt.red)
        self._penColor = QColor(Qt.green)
        self._lastPoint = QPointF()
        self._lastRect = QRectF(0, 0, 0, 0)
        self._lastEraserRect = QRectF(0, 0, 0, 0)
        
        # Create a white image to paint on
        self._image = QImage(1200, 800, QImage.Format.Format_RGB32)
        self._image.fill(Qt.white)
        
        # Enable mouse tracking
        self.setAcceptedMouseButtons(Qt.LeftButton)
        self.setAcceptHoverEvents(True)
    
    def paint(self, painter):
        """Paint the image on the item"""
        painter.drawImage(0, 0, self._image)
    
    @Property(int, notify=toolChanged)
    def tool(self):
        """Get the current tool"""
        return self._tool
    
    @tool.setter
    def tool(self, value):
        """Set the current tool"""
        if self._tool != value:
            self._tool = value
            self.toolChanged.emit()
    
    @Property(bool, notify=fillChanged)
    def fill(self):
        """Get the fill property"""
        return self._fill
    
    @fill.setter
    def fill(self, value):
        """Set the fill property"""
        if self._fill != value:
            self._fill = value
            self.fillChanged.emit()
    
    @Property(int, notify=penWidthChanged)
    def penWidth(self):
        """Get the pen width"""
        return self._penWidth
    
    @penWidth.setter
    def penWidth(self, value):
        """Set the pen width"""
        if self._penWidth != value:
            self._penWidth = value
            self.penWidthChanged.emit()
    
    @Property(QColor, notify=fillColorChanged)
    def fillColor(self):
        """Get the fill color"""
        return self._fillColor
    
    @fillColor.setter
    def fillColor(self, value):
        """Set the fill color"""
        if self._fillColor != value:
            self._fillColor = QColor(value)
            self.fillColorChanged.emit()
    
    @Property(QColor, notify=penColorChanged)
    def penColor(self):
        """Get the pen color"""
        return self._penColor
    
    @penColor.setter
    def penColor(self, value):
        """Set the pen color"""
        if self._penColor != value:
            self._penColor = QColor(value)
            self.penColorChanged.emit()
    
    @Slot()
    def copy(self):
        """Copy the canvas image to clipboard"""
        clipboard = QApplication.clipboard()
        clipboard.setImage(self._image)
        print("Image copied to clipboard")
    
    @Slot()
    def paste(self):
        """Paste image from clipboard to canvas"""
        # Get data from the clipboard
        mime_data = QApplication.clipboard().mimeData()
        
        if mime_data.hasUrls():
            urls = mime_data.urls()
            if len(urls) != 1:
                return
            
            file_path = urls[0].toLocalFile()
            
            if self.isImage(file_path):
                # Build the image object
                pixmap = QPixmap(file_path)
                
                # Paint it on the canvas
                painter = QPainter(self._image)
                painter.setPen(QPen(self._penColor, self._penWidth, Qt.SolidLine, 
                                  Qt.RoundCap, Qt.RoundJoin))
                painter.setRenderHint(QPainter.Antialiasing, True)
                
                painter.drawPixmap(
                    QRect(10, 10, 300, 300),
                    pixmap.scaled(300, 300, Qt.KeepAspectRatio),
                    QRect(0, 0, 300, 300)
                )
                
                self.update()
        elif mime_data.hasImage():
            # If clipboard contains an image, paste it directly
            image = mime_data.imageData()
            if not image.isNull():
                # Paint it on the canvas
                painter = QPainter(self._image)
                painter.setPen(QPen(self._penColor, self._penWidth, Qt.SolidLine, 
                                  Qt.RoundCap, Qt.RoundJoin))
                painter.setRenderHint(QPainter.Antialiasing, True)
                
                painter.drawImage(
                    QRect(10, 10, 300, 300),
                    image,
                    image.rect()
                )
                
                self.update()
    
    def isImage(self, file_path):
        """Check if a file is a supported image format"""
        _, ext = os.path.splitext(file_path)
        ext = ext.lower()
        return ext in [".png", ".jpg", ".jpeg"]
    
    @Slot(QPointF, QPointF)
    def drawLineTo(self, startPoint, endPoint):
        """Draw a line from start point to end point"""
        painter = QPainter(self._image)
        painter.setPen(QPen(self._penColor, self._penWidth, Qt.SolidLine, 
                           Qt.RoundCap, Qt.RoundJoin))
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.drawLine(startPoint, endPoint)
        
        self.update()
    
    @Slot(QPointF, QPointF, bool)
    def drawRectTo(self, startPoint, endPoint, ellipse=False):
        """Draw a rectangle/ellipse from start point to end point"""
        painter = QPainter(self._image)
        painter.setPen(QPen(self._penColor, self._penWidth, Qt.SolidLine, 
                           Qt.RoundCap, Qt.RoundJoin))
        
        # Set brush based on fill property
        if self._fill:
            painter.setBrush(self._fillColor)
        else:
            painter.setBrush(Qt.NoBrush)
        
        # Draw rect or ellipse
        rect = QRectF(startPoint, endPoint)
        if not ellipse:
            painter.drawRect(rect)
        else:
            painter.drawEllipse(rect)
        
        self.update()
    
    @Slot(QPointF)
    def eraseAt(self, point):
        """Erase content at a specific point"""
        painter = QPainter(self._image)
        
        # Erase the content at the point
        eraserSize = 50  # Size of the eraser
        rect = QRectF(point.x() - eraserSize/2, point.y() - eraserSize/2, 
                     eraserSize, eraserSize)
        
        painter.setBrush(Qt.white)
        painter.setPen(Qt.white)
        painter.drawRect(rect)
        
        self.update()
    
    @Slot(QPointF)
    def handleMousePress(self, position):
        """Handle mouse press from QML"""
        self._lastPoint = position
        self._drawing = True
    
    @Slot(QPointF)
    def handleMouseMove(self, position):
        """Handle mouse move from QML"""
        if self._drawing:
            if self._tool == self.PEN:
                self.drawLineTo(self._lastPoint, position)
                self._lastPoint = position
            elif self._tool == self.ERASER:
                self.eraseAt(position)
        
    @Slot(QPointF)
    def handleMouseRelease(self, position):
        """Handle mouse release from QML"""
        if self._drawing:
            if self._tool == self.PEN:
                self.drawLineTo(self._lastPoint, position)
            elif self._tool == self.RECT:
                self.drawRectTo(self._lastPoint, position, False)
            elif self._tool == self.ELLIPSE:
                self.drawRectTo(self._lastPoint, position, True)
            elif self._tool == self.ERASER:
                self.eraseAt(position)
            
            self._drawing = False
            self._lastRect = QRectF(0, 0, 0, 0)
    
    @Slot(int, int)
    def resizeImage(self, width, height):
        """Resize the image to a new size"""
        if (self._image.width() == width and self._image.height() == height):
            return
        
        newImage = QImage(width, height, QImage.Format.Format_RGB32)
        newImage.fill(Qt.white)
        
        painter = QPainter(newImage)
        painter.drawImage(QPoint(0, 0), self._image)
        
        self._image = newImage
        self.update()