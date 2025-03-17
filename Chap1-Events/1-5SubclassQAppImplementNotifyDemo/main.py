import sys
from pathlib import Path
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject, Slot, Signal, QEvent

class EventFilter(QObject):
    """Event filter that can be installed on the application"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.interceptEvents = False  # Start with event interception off
    
    def eventFilter(self, watched, event):
        # Only filter mouse events when interception is enabled
        if self.interceptEvents and (event.type() == QEvent.Type.MouseButtonPress or 
                                    event.type() == QEvent.Type.MouseButtonDblClick):
            print("Application: mouse press or double click detected")
            print(f"Class Name: {watched.metaObject().className()}")
            
            # Signal whether this is our main window
            if hasattr(self, 'mainWindow') and watched == self.mainWindow:
                print("Cast successful")
            else:
                print("Cast failed")
            
            # Block the event
            return True  # Return true to indicate the event was handled
            
        # Let other events pass through
        return super().eventFilter(watched, event)
    
    def setMainWindow(self, window):
        """Store a reference to the main window"""
        self.mainWindow = window
        
    @Slot(bool)
    def setInterceptEvents(self, intercept):
        """Enable or disable event interception"""
        self.interceptEvents = intercept
        print(f"Event interception {'enabled' if intercept else 'disabled'}")


class EventLogger(QObject):
    """Python backend class to handle logging events from QML"""
    
    @Slot(str)
    def log(self, message):
        """Log messages from QML to console"""
        print(message)


def main():
    """Main application entry point."""
    # Create standard QGuiApplication
    app = QGuiApplication(sys.argv)
    
    # Create our event filter
    eventFilter = EventFilter()
    
    # Install the event filter on the application
    app.installEventFilter(eventFilter)
    
    # Create QML engine
    engine = QQmlApplicationEngine()
    
    # Create and expose objects to QML
    logger = EventLogger()
    engine.rootContext().setContextProperty("eventLogger", logger)
    engine.rootContext().setContextProperty("eventFilter", eventFilter)
    
    # Load QML file
    qml_file = Path(__file__).resolve().parent / "main.qml"
    engine.load(qml_file)
    
    # Check if loading was successful
    if not engine.rootObjects():
        sys.exit(-1)
    
    # Store reference to the main window in our event filter
    eventFilter.setMainWindow(engine.rootObjects()[0])
    
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())