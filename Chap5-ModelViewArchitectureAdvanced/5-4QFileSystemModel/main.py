import sys
import os
from PySide6.QtWidgets import QApplication, QFileSystemModel
from PySide6.QtCore import QUrl, QDir
from PySide6.QtQml import QQmlApplicationEngine

from widget import Widget
from file_system_controller import FileSystemController

def run_widget():
    """Run the application in Qt Widgets mode"""
    app = QApplication(sys.argv)
    
    # Create model
    model = QFileSystemModel()
    model.setReadOnly(False)
    model.setRootPath(QDir.currentPath())
    
    # Create controller
    controller = FileSystemController(model)
    
    # Create and show window with model and controller
    window = Widget(model, controller)
    window.show()
    
    return app.exec()

def run_quick():
    """Run the application in Qt Quick mode"""
    app = QApplication(sys.argv)
    
    # Create QML engine
    engine = QQmlApplicationEngine()
    
    # Set the current directory path for the QML FolderListModel
    engine.rootContext().setContextProperty("currentDirPath", QDir.currentPath())
    
    # Load QML file
    qml_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "filesystem.qml")
    engine.load(QUrl.fromLocalFile(qml_file))
    
    # Check if QML loaded successfully
    if not engine.rootObjects():
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
        return run_widget()

if __name__ == "__main__":
    sys.exit(main())