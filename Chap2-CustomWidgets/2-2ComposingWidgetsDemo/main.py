import sys
from pathlib import Path

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject, Slot


class ColorHandler(QObject):
    """Python backend class to handle color selections from QML"""
    
    @Slot(str)
    def colorChanged(self, colorName):
        """Handle color change signal from QML"""
        print(f"Color changed to: {colorName}")


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    
    # Create QML engine
    engine = QQmlApplicationEngine()
    
    # Create and expose the ColorHandler to QML
    colorHandler = ColorHandler()
    engine.rootContext().setContextProperty("colorHandler", colorHandler)
    
    # Load QML file
    qml_file = Path(__file__).resolve().parent / "main.qml"
    engine.load(qml_file)
    
    # Check if loading was successful
    if not engine.rootObjects():
        sys.exit(-1)
        
    sys.exit(app.exec())