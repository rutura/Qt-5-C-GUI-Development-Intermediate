import sys
from pathlib import Path
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject, Slot, Signal, Property, QUrl
from resource_controller import ResourceController

import resource_rc

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