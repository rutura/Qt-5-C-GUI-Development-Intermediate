from PySide6.QtCore import QObject, QEvent
from PySide6.QtGui import QKeyEvent

class KeyboardFilter(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
    
    def eventFilter(self, watched, event):
        """Filter keyboard events, blocking number inputs
        
        Args:
            watched: The object being monitored
            event: The event that occurred
            
        Returns:
            bool: True if the event should be filtered out, False to pass it on
        """
        if event.type() == QEvent.KeyPress:
            key_event = event  # In Python, we don't need to cast
            numbers = "1234567890"
            if key_event.text() in numbers:
                print("Number filtered out")
                return True  # Event handled, no need to notify the destination
                
        return super().eventFilter(watched, event)