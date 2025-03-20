import sys
from pathlib import Path
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject, Slot, Signal, Property

class DrawingController(QObject):
    """Bridge class to expose functions to QML"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._pixmapPath = self._findPixmap()
    
    def _findPixmap(self):
        """Find the pixmap or return empty string if not found"""
        try:
            path = Path(__file__).resolve().parent / "images" / "learnqt.png"
            if path.exists():
                return str(path)
        except:
            pass
        return ""
    
    @Property(str)
    def pixmapPath(self):
        """Return the pixmap path for QML to use"""
        return self._pixmapPath

def main():
    app = QGuiApplication(sys.argv)
    
    # Create controller and expose to QML
    controller = DrawingController()
    
    # Create QML engine
    engine = QQmlApplicationEngine()
    
    # Expose controller to QML
    engine.rootContext().setContextProperty("controller", controller)
    
    # Load QML file
    qml_file = Path(__file__).resolve().parent / "main.qml"
    engine.load(qml_file)
    
    # Check if loading was successful
    if not engine.rootObjects():
        sys.exit(-1)
        
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())