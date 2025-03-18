from PySide6.QtCore import QObject, Slot, Signal, Property, QUrl, QTemporaryFile, QDir
from PySide6.QtGui import QGuiApplication
import os

class ClipboardController(QObject):
    """Controller class to handle clipboard operations"""
    
    # Signal to notify QML when a new image is available
    imageChanged = Signal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._imageUrl = ""
        self._hasImage = False
        self._tempFile = None
    
    @Property(bool, notify=imageChanged)
    def hasImage(self):
        """Property that indicates if an image is available"""
        return self._hasImage
    
    @Property(str, notify=imageChanged)
    def imageUrl(self):
        """Property that provides the image URL"""
        return self._imageUrl
    
    @Slot(result=bool)
    def paste(self):
        """Handle paste operation - paste image from clipboard"""
        # Get the clipboard and its MIME data
        clipboard = QGuiApplication.clipboard()
        mime_data = clipboard.mimeData()
        
        # Check if the clipboard contains URLs (e.g., files)
        if mime_data.hasUrls():
            urls = mime_data.urls()
            if len(urls) != 1:
                return False
                
            # Get the file path from the URL
            file_path = urls[0].toLocalFile()
            
            # Check if it's an image and display it
            if self.isImage(file_path):
                self._imageUrl = QUrl.fromLocalFile(file_path).toString()
                self._hasImage = True
                self.imageChanged.emit()
                return True
        
        # Also check for image data directly
        elif mime_data.hasImage():
            # Save the image to a temporary file
            image = mime_data.imageData()
            if not image.isNull():
                # Clean up previous temp file if it exists
                if self._tempFile:
                    self._tempFile.remove()
                
                # Create a new temporary file with the .png extension
                self._tempFile = QTemporaryFile(QDir.tempPath() + "/XXXXXX.png")
                if self._tempFile.open():
                    # Save the image to the temporary file
                    image.save(self._tempFile.fileName(), "PNG")
                    self._tempFile.close()
                    
                    # Set the image URL to the temporary file
                    self._imageUrl = QUrl.fromLocalFile(self._tempFile.fileName()).toString()
                    self._hasImage = True
                    self.imageChanged.emit()
                    return True
        
        return False
    
    def isImage(self, file_path):
        """Check if a file is a supported image format"""
        _, ext = os.path.splitext(file_path)
        ext = ext.lower()
        return ext in [".png", ".jpg", ".jpeg"]