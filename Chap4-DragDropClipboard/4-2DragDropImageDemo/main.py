import sys
from pathlib import Path
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject, Slot, Signal, QUrl

class ImageController(QObject):
    """Controller for handling image operations in QML"""
    
    @Slot(str, result=bool)
    def isImage(self, file_path):
        """Check if the file is a supported image format"""
        ext = Path(file_path).suffix.lower()
        return ext in [".png", ".jpg", ".jpeg", ".bmp", ".gif"]

def main():
    # Create the application
    app = QGuiApplication(sys.argv)
    
    # Create controller and QML engine
    controller = ImageController()
    engine = QQmlApplicationEngine()
    
    # Expose controller to QML
    engine.rootContext().setContextProperty("controller", controller)
    
    # Load QML file
    qml_file = Path(__file__).resolve().parent / "main.qml"
    engine.load(qml_file)
    
    # Check if loading was successful
    if not engine.rootObjects():
        sys.exit(-1)
    
    # Run the event loop
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())