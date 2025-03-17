import sys
from pathlib import Path
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject, Slot, Signal

class CoordinateLogger(QObject):
    """Helper class to log coordinates to console, similar to original code"""
    
    @Slot(str, str)
    def logCoordinates(self, logical, physical):
        """Log the coordinates to console"""
        print(f"Logical coordinates: {logical}")
        print(f"Physical coordinates: {physical}")

def main():
    app = QGuiApplication(sys.argv)
    
    # Create QML engine
    engine = QQmlApplicationEngine()
    
    # Create and expose logger to QML
    logger = CoordinateLogger()
    engine.rootContext().setContextProperty("logger", logger)
    
    # Load QML file
    qml_file = Path(__file__).resolve().parent / "main.qml"
    engine.load(qml_file)
    
    # Check if loading was successful
    if not engine.rootObjects():
        sys.exit(-1)
        
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())