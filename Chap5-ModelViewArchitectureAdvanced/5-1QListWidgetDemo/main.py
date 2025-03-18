import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication, QMessageBox, QPushButton, QVBoxLayout, QDialog

from widget import Widget

from fruit_controller import FruitController, FruitModel
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QUrl

import resource_rc  # Import the compiled resources

def run_widget():
    """Run the Qt Widgets implementation"""
    app = QApplication(sys.argv)
    window = Widget()
    window.show()
    return app.exec()


def run_quick():
    """Run the Qt Quick implementation"""
    app = QGuiApplication(sys.argv)
    
    # Create QML engine
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
    
    return app.exec()

def main():
    """Main entry point with option to choose which version to run"""
    
    mode = input("Select mode (1 for Widgets, 2 for Quick): ")
    
    if mode == "2":
        print("Running Qt Quick version")
        return run_quick()
    else:
        print("Running Qt Widgets version")
        return run_widget()

if __name__ == "__main__":
    sys.exit(main())