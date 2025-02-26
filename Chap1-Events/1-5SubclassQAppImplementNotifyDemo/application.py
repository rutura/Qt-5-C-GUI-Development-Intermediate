from typing import Optional
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QObject, QEvent
from widget import Widget

class Application(QApplication):
    def __init__(self, argv):
        super().__init__(argv)

    def notify(self, dest: QObject, event: QEvent) -> bool:
        """Override the notify method to intercept mouse events.
        
        Args:
            dest: Destination object receiving the event
            event: Event being processed
            
        Returns:
            bool: True if the event should be processed, False otherwise
        """
        if event.type() == QEvent.MouseButtonPress or event.type() == QEvent.MouseButtonDblClick:
            print("Application: mouse press or double click detected")
            
            print(f"Class Name: {dest.metaObject().className()}")
            
            # Try to cast the object to Widget
            if isinstance(dest, Widget):
                print("Cast successful")
            else:
                print("Cast failed")
                
            return False
        
        # Let the default handler process other events
        return super().notify(dest, event)