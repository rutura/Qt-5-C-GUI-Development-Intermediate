import sys
import os
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QUrl
from PySide6.QtQml import QQmlApplicationEngine

from widget import Widget
from personmodel import PersonModel
from person_controller import PersonController

def run_widget():
    """Run the Qt Widgets version"""
    app = QApplication(sys.argv)
    window = Widget()
    window.show()
    return app.exec()

def run_qml():
    """Run the Qt Quick version"""
    app = QApplication(sys.argv)
    
    # Create model first
    model = PersonModel()
    
    # Create controller and set the model
    controller = PersonController()
    controller.set_model(model)
    
    # Create QML engine
    engine = QQmlApplicationEngine()
    
    # Expose both model and controller to QML
    engine.rootContext().setContextProperty("personModel", model)
    engine.rootContext().setContextProperty("personController", controller)
    
    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Add the current directory to the import path
    engine.addImportPath(current_dir)
    
    # Load main QML file
    qml_file = os.path.join(current_dir, "main.qml")
    engine.load(QUrl.fromLocalFile(qml_file))
    
    # Check if QML loaded successfully
    if not engine.rootObjects():
        return -1
    
    return app.exec()

def main():
    """Main entry point with option to choose which version to run"""
    mode = input("Select mode (1 for Widgets, 2 for QML): ")
    
    if mode == "2":
        print("Running Qt Quick version")
        return run_qml()
    else:
        print("Running Qt Widgets version")
        return run_widget()

if __name__ == "__main__":
    sys.exit(main())