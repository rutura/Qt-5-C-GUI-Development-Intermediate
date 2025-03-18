import sys
from pathlib import Path
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QUrl

from fruit_controller import FruitController, FruitModel
import resource_rc  # Import the compiled resources

def main():
    # Create application
    app = QGuiApplication(sys.argv)
    
    # Create controller, model and QML engine
    engine = QQmlApplicationEngine()
    
    # Create model and controller
    fruit_model = FruitModel()
    controller = FruitController(fruit_model)
    
    # Expose controller and model to QML
    engine.rootContext().setContextProperty("fruitController", controller)
    engine.rootContext().setContextProperty("fruitModel", fruit_model)
    
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