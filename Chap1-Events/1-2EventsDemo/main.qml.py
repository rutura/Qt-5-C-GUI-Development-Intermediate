import sys
from pathlib import Path

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject, Slot


class EventLogger(QObject):
    """Python backend class to handle logging events from QML"""
    
    @Slot(str)
    def log(self, message):
        """Log messages from QML to console"""
        print(message)


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    
    # Create QML engine
    engine = QQmlApplicationEngine()
    
    # Create and expose the EventLogger to QML
    logger = EventLogger()
    engine.rootContext().setContextProperty("eventLogger", logger)
    
    # Load QML file
    qml_file = Path(__file__).resolve().parent / "main.qml"
    engine.load(qml_file)
    
    # Check if loading was successful
    if not engine.rootObjects():
        sys.exit(-1)
        
    sys.exit(app.exec())