from typing import Optional
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtUiTools import QUiLoader

class Widget(QWidget):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        
        self.setup_ui()
    
    def setup_ui(self) -> None:
        """Load the UI file and set it up"""
        loader = QUiLoader()
        ui_file = QFile("widget.ui")
        
        if not ui_file.open(QIODevice.ReadOnly):
            raise RuntimeError(f"Cannot open widget.ui: {ui_file.errorString()}")
        
        ui_widget = loader.load(ui_file, self)
        ui_file.close()
        
        if not ui_widget:
            raise RuntimeError("Failed to load widget.ui")
            
        self.setWindowTitle(ui_widget.windowTitle())
        self.setGeometry(ui_widget.geometry())