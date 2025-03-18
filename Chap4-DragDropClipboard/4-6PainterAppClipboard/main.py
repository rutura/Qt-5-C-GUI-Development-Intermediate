import sys
from pathlib import Path
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, qmlRegisterType
from PySide6.QtCore import QUrl

from paint_canvas import PaintCanvas
from paint_controller import PaintController

import resource_rc

def main():
    # Create application
    app = QGuiApplication(sys.argv)
    
    # Register custom types
    qmlRegisterType(PaintCanvas, "PaintApp", 1, 0, "PaintCanvas")
    
    # Create QML engine
    engine = QQmlApplicationEngine()
    
    # Create and expose controller to QML
    controller = PaintController()
    engine.rootContext().setContextProperty("paintController", controller)
    
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