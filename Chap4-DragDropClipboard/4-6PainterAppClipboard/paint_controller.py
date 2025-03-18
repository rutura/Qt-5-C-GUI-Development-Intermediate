from PySide6.QtCore import QObject, Signal, Slot, Property
from PySide6.QtGui import QColor

class PaintController(QObject):
    """Controller class to provide tool and resource paths to QML"""
    
    # Signals
    toolChanged = Signal()
    resourcesChanged = Signal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._currentTool = 0  # PEN
        # Initialize constant resource paths
        self._penIconPath = "qrc:/images/pen.png"
        self._rectIconPath = "qrc:/images/rectangle.png"
        self._ellipseIconPath = "qrc:/images/circle.png"
        self._eraserIconPath = "qrc:/images/eraser.png"
    
    @Property(int, notify=toolChanged)
    def currentTool(self):
        """Get the current tool"""
        return self._currentTool
    
    @currentTool.setter
    def currentTool(self, value):
        """Set the current tool"""
        if self._currentTool != value:
            self._currentTool = value
            self.toolChanged.emit()
    
    @Slot(int)
    def setTool(self, tool):
        """Set the tool and notify QML"""
        self.currentTool = tool
    
    # Resource paths with NOTIFY signals
    @Property(str, constant=True)
    def penIconPath(self):
        return self._penIconPath
    
    @Property(str, constant=True)
    def rectIconPath(self):
        return self._rectIconPath
    
    @Property(str, constant=True)
    def ellipseIconPath(self):
        return self._ellipseIconPath
    
    @Property(str, constant=True)
    def eraserIconPath(self):
        return self._eraserIconPath
    
    # Tool name mapping
    @Slot(int, result=str)
    def getToolName(self, tool):
        """Get the name of a tool by its index"""
        tool_names = {
            0: "Pen",
            1: "Rectangle",
            2: "Ellipse",
            3: "Eraser"
        }
        return tool_names.get(tool, "Unknown")