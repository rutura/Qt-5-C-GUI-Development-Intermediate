import sys
from pathlib import Path
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject, Slot
from keyboardfilter import KeyboardFilter

def main():
    """Main application entry point"""
    # Create application
    app = QGuiApplication(sys.argv)
    
    # Create QML engine
    engine = QQmlApplicationEngine()
    
    # Create the keyboard filter
    keyboard_filter = KeyboardFilter()
    
    # Expose the filter to QML
    engine.rootContext().setContextProperty("keyboardFilter", keyboard_filter)
    
    # Load QML file
    qml_file = Path(__file__).resolve().parent / "main.qml"
    engine.load(qml_file)
    
    # Check if loading was successful
    if not engine.rootObjects():
        sys.exit(-1)
    
    # Get the text input object and install filter
    root_objects = engine.rootObjects()
    if root_objects:
        # We'll get the TextField from QML and install our filter
        root = root_objects[0]
        text_field = root.findChild(QObject, "textInput")
        if text_field:
            text_field.installEventFilter(keyboard_filter)
    
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())