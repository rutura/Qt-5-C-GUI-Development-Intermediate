from PySide6.QtGui import QGuiApplication
from PySide6.QtCore import QObject, QEvent

class Application(QGuiApplication):
    def __init__(self, argv):
        super().__init__(argv)
        # Store a reference to our main window/root object
        self.mainWindow = None
        # Flag to indicate if the application is ready to intercept events
        self.ready = False

    def setMainWindow(self, window):
        """Store a reference to the main QML window for identification"""
        self.mainWindow = window
        # Now that we have the main window, we're ready to intercept events
        self.ready = True
        print("Application is ready to intercept events")

    def notify(self, dest: QObject, event: QEvent) -> bool:
        """Override the notify method to intercept mouse events.
        
        Args:
            dest: Destination object receiving the event
            event: Event being processed
            
        Returns:
            bool: True if the event should be processed, False otherwise
        """
        # Only intercept events after the application is ready
        if self.ready and (event.type() == QEvent.Type.MouseButtonPress or 
                           event.type() == QEvent.Type.MouseButtonDblClick):
            print("Application: mouse press or double click detected")
            
            # Get class name from meta object
            print(f"Class Name: {dest.metaObject().className()}")
            
            # Check if this is our main window
            if self.mainWindow and dest == self.mainWindow:
                print("Cast successful")
            else:
                print("Cast failed")
                
            # Instead of blocking ALL events, let's allow them through
            # but log that we've seen them - this prevents freezing
            return True
        
        # Let the default handler process other events
        return super().notify(dest, event)