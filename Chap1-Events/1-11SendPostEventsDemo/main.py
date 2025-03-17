import sys
from pathlib import Path

from PySide6.QtGui import QGuiApplication, QMouseEvent
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject, Slot, Signal, QPointF, Qt, QEvent, QMetaObject

class EventBridge(QObject):
    """Bridge class to handle events between QML and Python"""
    
    @Slot(str)
    def log(self, message):
        """Log messages from QML to console"""
        print(message)
    
    @Slot(QObject)
    def sendSyntheticMousePress(self, target):
        """Send a synthetic mouse press event to the target object
        
        Args:
            target: QML object to receive the synthetic event
        """
        print("Sending synthetic mouse press event")
        
        # Create a mouse press event
        mouse_event = QMouseEvent(
            QEvent.Type.MouseButtonPress,  # Type
            QPointF(10, 10),               # Local position
            QPointF(10, 10),               # Screen position 
            Qt.MouseButton.LeftButton,     # Button
            Qt.MouseButton.LeftButton,     # Buttons
            Qt.KeyboardModifier.NoModifier # Modifiers
        )
        
        # Use QCoreApplication.postEvent to send the event asynchronously
        QGuiApplication.postEvent(target, mouse_event)


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    
    # Create QML engine
    engine = QQmlApplicationEngine()
    
    # Create and expose the EventBridge to QML
    bridge = EventBridge()
    engine.rootContext().setContextProperty("eventBridge", bridge)
    
    # Load QML file
    qml_file = Path(__file__).resolve().parent / "main.qml"
    engine.load(qml_file)
    
    # Check if loading was successful
    if not engine.rootObjects():
        sys.exit(-1)
        
    sys.exit(app.exec())