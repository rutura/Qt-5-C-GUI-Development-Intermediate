from typing import Optional
from PySide6.QtWidgets import QWidget
from ui_widget import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        """Initialize the Widget with UI from the .ui file.
        
        Args:
            parent: Optional parent widget
        """
        super().__init__(parent)
        
        # Set up the UI
        self.ui = Ui_Widget()
        self.ui.setupUi(self)