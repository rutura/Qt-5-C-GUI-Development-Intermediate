from PySide6.QtCore import QObject, QEvent

class Filter(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
    
    def eventFilter(self, watched, event):
        """Filter events for all objects that install this filter
        
        Args:
            watched: The object that is being watched
            event: The event that was sent
            
        Returns:
            bool: True if the event is handled and should be filtered out, 
                  False to allow further processing
        """
        if (event.type() == QEvent.Type.MouseButtonPress or 
            event.type() == QEvent.Type.MouseButtonDblClick):
            
            print("Event hijacked in filter")
            # return True  # Event handled, no need to notify original destination
            return False   # Allow event to continue to destination
        
        return super().eventFilter(watched, event)