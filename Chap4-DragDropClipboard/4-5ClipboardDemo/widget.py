from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtCore import Qt, QUrl, QFileInfo
from PySide6.QtGui import QKeyEvent, QKeySequence, QPixmap
from ui_widget import Ui_Widget
import os

class Widget(QWidget):
    """Main widget that demonstrates clipboard operations"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # Set focus policy to enable key events
        self.setFocusPolicy(Qt.StrongFocus)
        
        # Set a default text for the label
        self.ui.label.setText("Press Ctrl+V to paste an image from clipboard")
        self.ui.label.setAlignment(Qt.AlignCenter)
    
    def keyPressEvent(self, event: QKeyEvent):
        """Handle key press events for clipboard operations"""
        if event.matches(QKeySequence.Copy):
            self.copy()
            event.accept()
            print("Copy sequence detected")
        elif event.matches(QKeySequence.Paste):
            self.paste()
            event.accept()
            print("Paste sequence detected")
        else:
            super().keyPressEvent(event)
    
    def isImage(self, file_path):
        """Check if a file is a supported image format"""
        _, ext = os.path.splitext(file_path)
        ext = ext.lower()
        return ext in [".png", ".jpg", ".jpeg"]
    
    def copy(self):
        """Handle copy operation - currently not implemented"""
        # No operation in this example
        pass
    
    def paste(self):
        """Handle paste operation - paste image from clipboard"""
        # Get the clipboard and its MIME data
        clipboard = QApplication.clipboard()
        mime_data = clipboard.mimeData()
        
        # Check if the clipboard contains URLs (e.g., files)
        if mime_data.hasUrls():
            urls = mime_data.urls()
            if len(urls) != 1:
                return
                
            # Get the file path from the URL
            file_path = urls[0].toLocalFile()
            
            # Check if it's an image and display it
            if self.isImage(file_path):
                pixmap = QPixmap(file_path)
                if not pixmap.isNull():
                    # Scale the pixmap to fit the label while maintaining aspect ratio
                    self.ui.label.setPixmap(pixmap.scaled(
                        self.ui.label.size(),
                        Qt.KeepAspectRatio,
                        Qt.SmoothTransformation
                    ))
        # Also check for image data directly
        elif mime_data.hasImage():
            pixmap = QPixmap(mime_data.imageData())
            if not pixmap.isNull():
                self.ui.label.setPixmap(pixmap.scaled(
                    self.ui.label.size(),
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                ))
    
    def resizeEvent(self, event):
        """Handle resize events to scale the image"""
        if self.ui.label.pixmap() and not self.ui.label.pixmap().isNull():
            # Store the original pixmap if we haven't already
            if not hasattr(self, 'original_pixmap'):
                self.original_pixmap = self.ui.label.pixmap()
            
            # Scale the pixmap to fit the new size
            self.ui.label.setPixmap(self.original_pixmap.scaled(
                self.ui.label.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            ))
        
        super().resizeEvent(event)