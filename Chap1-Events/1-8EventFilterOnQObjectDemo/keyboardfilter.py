from PySide6.QtCore import QObject, QEvent, Slot
from PySide6.QtGui import QKeyEvent

class KeyboardFilter(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.active = True
    
    def eventFilter(self, watched, event):
        """Filter keyboard events, blocking number inputs
        
        Args:
            watched: The object being monitored
            event: The event that occurred
            
        Returns:
            bool: True if the event should be filtered out, False to pass it on
        """
        if self.active and event.type() == QEvent.Type.KeyPress:
            key_event = event  # In Python, we don't need to cast
            numbers = "1234567890"
            if key_event.text() in numbers:
                print("Number filtered out")
                return True  # Event handled, no need to notify the destination
                
        return super().eventFilter(watched, event)
    
    @Slot()
    def removeFilter(self):
        """Deactivate the filter without physically removing it"""
        self.active = False
        print("Filter deactivated")
    
    @Slot()
    def installFilter(self):
        """Activate the filter"""
        self.active = True
        print("Filter activated")