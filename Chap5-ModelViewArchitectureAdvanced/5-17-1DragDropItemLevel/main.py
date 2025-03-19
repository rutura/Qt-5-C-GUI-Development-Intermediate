import sys
import os
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QUrl
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtGui import QStandardItemModel, QStandardItem

from item_model import ItemModel
from drag_drop_controller import DragDropController
from widget import Widget

def run_widget():
    """Run the application in Qt Widgets mode"""
    app = QApplication(sys.argv)
    window = Widget()
    window.show()
    
    return app.exec()

def run_quick():
    """Run the application in Qt Quick mode"""
    app = QApplication(sys.argv)
    
    # Create QML engine
    engine = QQmlApplicationEngine()
    
    # Create model
    model = ItemModel()
    
    # Create controller
    controller = DragDropController(model)
    
    # Expose model and controller to QML
    engine.rootContext().setContextProperty("itemModel", model)
    engine.rootContext().setContextProperty("dragDropController", controller)
    
    # Load QML file
    qml_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dragdrop.qml")
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