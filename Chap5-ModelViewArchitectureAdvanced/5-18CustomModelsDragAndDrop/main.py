import os
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QUrl
from widget import Widget
from personmodel import PersonModel

def run_widgets():
    """Run the Qt Widgets version of the application"""
    app = QApplication(sys.argv)
    window = Widget()
    window.show()
    return app.exec()

def run_quick():
    """Run the Qt Quick version of the application"""
    app = QApplication(sys.argv)
    
    # Create model
    model = PersonModel()
    
    # Create QML engine
    engine = QQmlApplicationEngine()
    
    # Expose model to QML
    engine.rootContext().setContextProperty("personModel", model)
    
    # Get path to QML file using os.path for portability
    current_dir = os.path.dirname(os.path.abspath(__file__))
    qml_file = os.path.join(current_dir, "main.qml")
    
    # Load QML file
    engine.load(QUrl.fromLocalFile(qml_file))
    
    # Check if loading was successful
    if not engine.rootObjects():
        print("Error: Failed to load QML file")
        return -1
        
    return app.exec()

def main():
    """Main entry point with option to choose which version to run"""
    
    mode = input("Select mode (1 for Widgets, 2 for Quick): ")
    
    if mode == "2":
        print("Running Qt Quick version")
        return run_quick()
    else:
        print("Running Qt Widgets version")
        return run_widgets()

if __name__ == "__main__":
    sys.exit(main())