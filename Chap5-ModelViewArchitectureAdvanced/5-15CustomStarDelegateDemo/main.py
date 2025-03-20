import sys
import os
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QUrl, QDir
from PySide6.QtQml import QQmlApplicationEngine

from widget import Widget
from course_controller import CourseController

def run_widget():
    """Run the Qt Widgets version"""
    app = QApplication(sys.argv)
    window = Widget()
    window.show()
    return app.exec()

def run_qml():
    """Run the Qt Quick version"""
    app = QApplication(sys.argv)
    
    # Create controller with model
    controller = CourseController()
    
    # Create QML engine
    engine = QQmlApplicationEngine()
    
    # Expose controller and model to QML
    engine.rootContext().setContextProperty("courseController", controller)
    engine.rootContext().setContextProperty("courseModel", controller.model)
    
    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Add the current directory to the import path so QML can find StarRating.qml
    engine.addImportPath(current_dir)
    
    # Make sure StarRating.qml is in the current directory
    star_rating_path = os.path.join(current_dir, "StarRating.qml")
    if not os.path.exists(star_rating_path):
        print(f"Error: StarRating.qml not found at {star_rating_path}")
        return -1
    
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