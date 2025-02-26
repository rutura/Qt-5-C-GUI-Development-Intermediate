from PySide6.QtWidgets import QWidget, QLabel, QApplication
from PySide6.QtCore import Qt, QPoint, QByteArray, QIODevice, QDataStream, QBuffer, QMimeData
from PySide6.QtGui import (QPainter, QMouseEvent, QDragEnterEvent, QDragMoveEvent, 
                          QDragLeaveEvent, QDropEvent, QPixmap, QDrag, QColor, QImage)
import resource_rc  # Import the resource file

class Container(QWidget):
    """Container widget that supports internal drag and drop operations"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(150, 150)
        self.setAcceptDrops(True)
        self.startPos = QPoint()
        
        # Create initial icons
        try:
            # Qt icon
            qtIcon = QLabel(self)
            qtIcon.setPixmap(QPixmap(":/images/qt.png"))
            qtIcon.move(20, 20)
            qtIcon.show()
            qtIcon.setAttribute(Qt.WA_DeleteOnClose)
            
            # C++ icon
            cppIcon = QLabel(self)
            cppIcon.setPixmap(QPixmap(":/images/cpp.png"))
            cppIcon.move(150, 20)
            cppIcon.show()
            cppIcon.setAttribute(Qt.WA_DeleteOnClose)
            
            # Terminal icon
            terminalIcon = QLabel(self)
            terminalIcon.setPixmap(QPixmap(":/images/terminal.png"))
            terminalIcon.move(20, 150)
            terminalIcon.show()
            terminalIcon.setAttribute(Qt.WA_DeleteOnClose)
            
            print("Icons loaded successfully")
        except Exception as e:
            print(f"Error loading icons: {e}")
            # Fallback if images aren't available
            self.createSampleLabels()
    
    def createSampleLabels(self):
        """Create sample colored labels if images aren't available"""
        # Red label
        redLabel = QLabel(self)
        redPixmap = QPixmap(64, 64)
        redPixmap.fill(Qt.red)
        redLabel.setPixmap(redPixmap)
        redLabel.move(20, 20)
        redLabel.show()
        redLabel.setAttribute(Qt.WA_DeleteOnClose)
        
        # Green label
        greenLabel = QLabel(self)
        greenPixmap = QPixmap(64, 64)
        greenPixmap.fill(Qt.green)
        greenLabel.setPixmap(greenPixmap)
        greenLabel.move(150, 20)
        greenLabel.show()
        greenLabel.setAttribute(Qt.WA_DeleteOnClose)
        
        # Blue label
        blueLabel = QLabel(self)
        bluePixmap = QPixmap(64, 64)
        bluePixmap.fill(Qt.blue)
        blueLabel.setPixmap(bluePixmap)
        blueLabel.move(20, 150)
        blueLabel.show()
        blueLabel.setAttribute(Qt.WA_DeleteOnClose)
        
        print("Created colored label fallbacks")
    
    def mousePressEvent(self, event: QMouseEvent):
        """Remember the start position when mouse is pressed"""
        if event.button() == Qt.LeftButton:
            self.startPos = event.position().toPoint()
        super().mousePressEvent(event)
    
    def mouseMoveEvent(self, event: QMouseEvent):
        """Start drag operation if mouse moved beyond threshold"""
        if event.buttons() & Qt.LeftButton:
            # Calculate distance moved
            distance = (event.position().toPoint() - self.startPos).manhattanLength()
            
            # Check if distance exceeds drag start distance
            if distance >= QApplication.startDragDistance():
                # Get the child widget at the current position
                child = self.childAt(event.position().toPoint())
                
                if not child or not isinstance(child, QLabel):
                    return
                
                # Get pixmap from child
                pixmap = child.pixmap()
                if not pixmap:
                    return
                
                # Save pixmap to a byte array
                pixmap_ba = QByteArray()
                buffer = QBuffer(pixmap_ba)
                buffer.open(QIODevice.WriteOnly)
                pixmap.save(buffer, "PNG")
                buffer.close()
                
                # Calculate hotspot offset
                hotspot = event.position().toPoint() - child.pos()
                
                # Prepare data to be serialized (as bytes)
                # We'll use simple format: pixmap data followed by x,y coordinates
                mime_data = QMimeData()
                
                # Store the image data and hotspot directly in separate mime formats
                mime_data.setData("application/x-qtcustompixmap", pixmap_ba)
                
                # Store hotspot as a separate mime type
                hotspot_data = QByteArray()
                hotspot_buffer = QDataStream(hotspot_data, QIODevice.WriteOnly)
                hotspot_buffer << hotspot.x() << hotspot.y()
                mime_data.setData("application/x-qtcustomhotspot", hotspot_data)
                
                # Create drag object
                drag = QDrag(self)
                drag.setMimeData(mime_data)
                drag.setPixmap(pixmap)
                drag.setHotSpot(hotspot)
                
                # Execute drag operation
                if drag.exec(Qt.MoveAction | Qt.CopyAction, Qt.CopyAction) == Qt.MoveAction:
                    # Move operation - close the original child widget
                    print("Moving data")
                    child.close()
                else:
                    # Copy operation
                    print("Copying data")
    
    def dragEnterEvent(self, event: QDragEnterEvent):
        """Handle drag enter events"""
        if event.mimeData().hasFormat("application/x-qtcustompixmap"):
            if event.source() == self:
                event.setDropAction(Qt.MoveAction)
                event.accept()
            else:
                event.acceptProposedAction()
        else:
            event.ignore()
    
    def dragMoveEvent(self, event: QDragMoveEvent):
        """Handle drag move events"""
        if event.mimeData().hasFormat("application/x-qtcustompixmap"):
            if event.source() == self:
                event.setDropAction(Qt.MoveAction)
                event.accept()
            else:
                event.acceptProposedAction()
        else:
            event.ignore()
    
    def dragLeaveEvent(self, event: QDragLeaveEvent):
        """Handle drag leave events"""
        super().dragLeaveEvent(event)
    
    def dropEvent(self, event: QDropEvent):
        """Handle drop events, creating new label widgets"""
        if event.mimeData().hasFormat("application/x-qtcustompixmap"):
            # Get the pixmap data
            pixmap_ba = event.mimeData().data("application/x-qtcustompixmap")
            
            # Get the hotspot data
            hotspot_data = event.mimeData().data("application/x-qtcustomhotspot")
            hotspot_stream = QDataStream(hotspot_data, QIODevice.ReadOnly)
            
            # Read the x,y coordinates
            x, y = 0, 0
            hotspot_stream >> x >> y
            hotspot = QPoint(x, y)
            
            # Recreate the pixmap from the data
            pixmap = QPixmap()
            pixmap.loadFromData(pixmap_ba)
            
            # Create new label with the deserialized pixmap
            new_label = QLabel(self)
            new_label.setPixmap(pixmap)
            new_label.move(event.position().toPoint() - hotspot)
            new_label.show()
            new_label.setAttribute(Qt.WA_DeleteOnClose)
            
            # Set the drop action
            if event.source() == self:
                event.setDropAction(Qt.MoveAction)
                event.accept()
            else:
                event.acceptProposedAction()
        else:
            event.ignore()
    
    def paintEvent(self, event):
        """Paint a rounded rectangle border around the container"""
        painter = QPainter(self)
        painter.drawRoundedRect(0, 5, self.width() - 10, self.height() - 10, 3, 3)
        super().paintEvent(event)