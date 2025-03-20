from PySide6.QtCore import QObject, Slot, Signal, Property

class ResourceController(QObject):
    """Controller class to provide resource paths to QML"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
    
    @Property(str)
    def qtIconPath(self):
        return "qrc:/images/qt.png"
    
    @Property(str)
    def cppIconPath(self):
        return "qrc:/images/cpp.png"
    
    @Property(str)
    def terminalIconPath(self):
        return "qrc:/images/terminal.png"
    
    @Slot(str, result=str)
    def getIconDescription(self, source):
        """Get a description for an icon based on its source path"""
        if source.endswith("qt.png"):
            return "Qt Icon"
        elif source.endswith("cpp.png"):
            return "C++ Icon"
        elif source.endswith("terminal.png"):
            return "Terminal Icon"
        return "Unknown Icon"