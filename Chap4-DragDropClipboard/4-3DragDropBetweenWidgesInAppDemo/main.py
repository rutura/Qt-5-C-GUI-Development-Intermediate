import sys
from pathlib import Path
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject, Slot, Signal, Property, QUrl

import resource_rc

class ResourceController(QObject):
    """Controller class to provide resource paths to QML"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
    @Property(str)
    def qtIconPath(self):
        return "qrc:/images/qt.png"
    
    @Property(str)
    def cppIconPath(self):
        return "qrc:/images/cpp.png"
    
    @Property(str)
    def terminalIconPath(self):
        return "qrc:/images/terminal.png"

def main():
    # Create application
    app = QGuiApplication(sys.argv)
    
    # Create controller and QML engine
    controller = ResourceController()
    engine = QQmlApplicationEngine()
    
    # Expose controller to QML
    engine.rootContext().setContextProperty("resourceController", controller)
    
    # Load QML file
    qml_file = Path(__file__).resolve().parent / "main.qml"
    engine.load(qml_file)
    
    # Check if loading was successful
    if not engine.rootObjects():
        print("Error: Could not load QML file")
        sys.exit(-1)
    
    # Run the event loop
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())