from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QUrl, Qt
from PySide6.QtGui import (QDragEnterEvent, QDragMoveEvent, 
                          QDragLeaveEvent, QDropEvent, QPixmap)
from ui_widget import Ui_Widget
import os

class Widget(QWidget):
    """Main application widget that accepts image drops"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.setAcceptDrops(True)
        
        # Set an initial label text
        self.ui.label.setText("Drag and drop an image here")
        self.ui.label.setAlignment(Qt.AlignCenter)
    
    def dragEnterEvent(self, event: QDragEnterEvent):
        """Handle drag enter events"""
        event.accept()
    
    def dragMoveEvent(self, event: QDragMoveEvent):
        """Handle drag move events"""
        event.accept()
    
    def dragLeaveEvent(self, event: QDragLeaveEvent):
        """Handle drag leave events"""
        event.accept()
    
    def dropEvent(self, event: QDropEvent):
        """Handle drop events, loading image files"""
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            if len(urls) > 1:
                return
            
            file_path = urls[0].toLocalFile()
            if self.isImage(file_path):
                pixmap = QPixmap()
                if pixmap.load(file_path):
                    # Scale the pixmap to fit the label while preserving aspect ratio
                    self.ui.label.setPixmap(pixmap.scaled(
                        self.ui.label.size(), 
                        Qt.AspectRatioMode.KeepAspectRatio, 
                        Qt.TransformationMode.SmoothTransformation
                    ))
    
    def isImage(self, file_path):
        """Check if the file is a supported image format"""
        _, ext = os.path.splitext(file_path)
        ext = ext.lower()
        return ext in [".png", ".jpg", ".jpeg"]
    
    def resizeEvent(self, event):
        """Handle resize events to scale the image"""
        if self.ui.label.pixmap():
            # Get the original pixmap stored as a property
            original_pixmap = getattr(self, '_original_pixmap', None)
            if original_pixmap:
                # Scale the original pixmap to the new size
                self.ui.label.setPixmap(original_pixmap.scaled(
                    self.ui.label.size(),
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
                ))
        super().resizeEvent(event)