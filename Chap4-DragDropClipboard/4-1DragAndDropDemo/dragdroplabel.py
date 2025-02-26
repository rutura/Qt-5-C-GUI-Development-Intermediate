from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QPalette, QDragEnterEvent, QDragMoveEvent, QDragLeaveEvent, QDropEvent


class DragDropLabel(QLabel):
    """A QLabel that accepts drag and drop events"""
    
    # Define the signal with the same signature as in C++
    mimeChanged = Signal(object)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(100, 100)
        self.setAlignment(Qt.AlignCenter)
        self.setAcceptDrops(True)
        self.setText("DROP SPACE")
        self.setAutoFillBackground(True)
    
    def dragEnterEvent(self, event: QDragEnterEvent):
        """Handle drag enter events"""
        self.setText("DROP YOUR DATA HERE")
        self.setBackgroundRole(QPalette.Highlight)
        event.acceptProposedAction()
        self.mimeChanged.emit(event.mimeData())
    
    def dragMoveEvent(self, event: QDragMoveEvent):
        """Handle drag move events"""
        event.acceptProposedAction()
    
    def dragLeaveEvent(self, event: QDragLeaveEvent):
        """Handle drag leave events"""
        self.clear()
    
    def dropEvent(self, event: QDropEvent):
        """Handle drop events"""
        mimeData = event.mimeData()
        
        if mimeData.hasText():
            self.setText(mimeData.text())
            self.setTextFormat(Qt.PlainText)
        elif mimeData.hasImage():
            self.setPixmap(mimeData.imageData())
        elif mimeData.hasHtml():
            self.setText(mimeData.html())
            self.setTextFormat(Qt.RichText)
        elif mimeData.hasUrls():
            urlList = mimeData.urls()
            text = ""
            for url in urlList:
                text += url.path() + "-----"
            self.setText(text)
        else:
            self.setText("Data cannot be displayed")
    
    def clear(self):
        """Reset the label to its default state"""
        self.setText("DROP SPACE")
        self.setBackgroundRole(QPalette.Dark)
        self.mimeChanged.emit(None)