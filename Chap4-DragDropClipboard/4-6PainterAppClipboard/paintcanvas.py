from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtGui import (QPainter, QMouseEvent, QPen, QColor, QBrush, 
                          QImage, QPaintEvent, QResizeEvent, QKeyEvent, 
                          QKeySequence, QPixmap)
from PySide6.QtCore import Qt, QPoint, QRect, QSize, QRectF

import os

class PaintCanvas(QWidget):
    """Canvas widget for drawing with various tools"""
    
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
        self.image = QImage(self.size(), QImage.Format.Format_RGB32)
        self.image.fill(Qt.white)
        
        # Set focus policy to enable key events
        self.setFocusPolicy(Qt.StrongFocus)
    
    def getTool(self):
        """Get the current tool"""
        return self.tool
    
    def setTool(self, value):
        """Set the current tool"""
        self.tool = value
    
    def getFill(self):
        """Get the fill property"""
        return self.fill
    
    def setFill(self, value):
        """Set the fill property"""
        self.fill = value
    
    def getPenWidth(self):
        """Get the pen width"""
        return self.penWidth
    
    def setPenWidth(self, value):
        """Set the pen width"""
        self.penWidth = value
    
    def getFillColor(self):
        """Get the fill color"""
        return self.fillColor
    
    def setFillColor(self, value):
        """Set the fill color"""
        self.fillColor = value
    
    def getPenColor(self):
        """Get the pen color"""
        return self.penColor
    
    def setPenColor(self, value):
        """Set the pen color"""
        self.penColor = value
    
    def copy(self):
        """Copy the canvas image to clipboard"""
        clipboard = QApplication.clipboard()
        mime_data = clipboard.mimeData()
        mime_data.setImageData(self.image)
        clipboard.setMimeData(mime_data)
        print("Image copied to clipboard")
    
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
                painter = QPainter(self.image)
                painter.setPen(QPen(self.penColor, self.penWidth, Qt.SolidLine, 
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
            pixmap = QPixmap(mime_data.imageData())
            
            painter = QPainter(self.image)
            painter.setPen(QPen(self.penColor, self.penWidth, Qt.SolidLine, 
                              Qt.RoundCap, Qt.RoundJoin))
            painter.setRenderHint(QPainter.Antialiasing, True)
            
            painter.drawPixmap(
                QRect(10, 10, 300, 300),
                pixmap.scaled(300, 300, Qt.KeepAspectRatio),
                QRect(0, 0, 300, 300)
            )
            
            self.update()
    
    def isImage(self, file_path):
        """Check if a file is a supported image format"""
        _, ext = os.path.splitext(file_path)
        ext = ext.lower()
        return ext in [".png", ".jpg", ".jpeg"]
    
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
        current_rect = QRect(topLeft, QSize(100, 100))
        painter.setBrush(Qt.white)
        painter.setPen(Qt.white)
        painter.drawRect(current_rect)
        
        # Draw current eraser rect
        painter.setBrush(Qt.black)
        painter.setPen(Qt.black)
        painter.drawRect(current_rect)
        
        self.lastEraserRect = current_rect
        
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
            return image
        
        newImage = QImage(newSize, QImage.Format.Format_RGB32)
        newImage.fill(Qt.white)
        painter = QPainter(newImage)
        painter.drawImage(QPoint(0, 0), image)
        
        return newImage
    
    def mousePressEvent(self, event):
        """Handle mouse press events"""
        self.setFocus()  # Ensure the widget has focus
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
    
    def keyPressEvent(self, event):
        """Handle key press events for clipboard operations"""
        if event.matches(QKeySequence.Copy):
            print("Copy sequence detected")
            self.copy()
            event.accept()
        elif event.matches(QKeySequence.Paste):
            print("Paste sequence detected")
            self.paste()
            event.accept()
        else:
            super().keyPressEvent(event)