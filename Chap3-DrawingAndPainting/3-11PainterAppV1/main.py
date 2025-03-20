import sys
from pathlib import Path
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject, Slot, Signal, Property, QUrl

class PaintController(QObject):
    """Bridge class to expose functions and manage state for QML"""
    
    toolChanged = Signal(int)
    statusMessageChanged = Signal(str)
    penIconChanged = Signal(QUrl)
    rectangleIconChanged = Signal(QUrl)
    circleIconChanged = Signal(QUrl)
    eraserIconChanged = Signal(QUrl)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._tool = 0  # Pen by default
        self._statusMessage = "Current tool: Pen"
        
        # Find icons
        self._iconPaths = {
            "rectangle": self._findIcon("rectangle.png"),
            "pen": self._findIcon("pen.png"),
            "circle": self._findIcon("circle.png"),
            "eraser": self._findIcon("eraser.png")
        }
    
    def _findIcon(self, filename):
        """Find an icon file or return empty string if not found"""
        try:
            path = Path(__file__).resolve().parent / "images" / filename
            if path.exists():
                return QUrl.fromLocalFile(str(path))
        except:
            pass
        return QUrl("")
    
    @Property(str, notify=statusMessageChanged)
    def statusMessage(self):
        return self._statusMessage
    
    @statusMessage.setter
    def statusMessage(self, message):
        if self._statusMessage != message:
            self._statusMessage = message
            self.statusMessageChanged.emit(message)
    
    @Property(int, notify=toolChanged)
    def tool(self):
        return self._tool
    
    @tool.setter
    def tool(self, value):
        if self._tool != value:
            self._tool = value
            tool_names = ["Pen", "Rect", "Ellipse", "Eraser"]
            self.statusMessage = f"Current tool: {tool_names[value]}"
            self.toolChanged.emit(value)
    
    @Property(QUrl, notify=penIconChanged)
    def penIcon(self):
        return self._iconPaths["pen"]
    
    @Property(QUrl, notify=rectangleIconChanged)
    def rectangleIcon(self):
        return self._iconPaths["rectangle"]
    
    @Property(QUrl, notify=circleIconChanged)
    def circleIcon(self):
        return self._iconPaths["circle"]
    
    @Property(QUrl, notify=eraserIconChanged)
    def eraserIcon(self):
        return self._iconPaths["eraser"]

def main():
    app = QGuiApplication(sys.argv)
    
    # Create controller and expose to QML
    controller = PaintController()
    
    # Create QML engine
    engine = QQmlApplicationEngine()
    
    # Expose controller to QML
    engine.rootContext().setContextProperty("controller", controller)
    
    # Load QML file
    qml_file = Path(__file__).resolve().parent / "main.qml"
    engine.load(qml_file)
    
    # Check if loading was successful
    if not engine.rootObjects():
        sys.exit(-1)
        
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())