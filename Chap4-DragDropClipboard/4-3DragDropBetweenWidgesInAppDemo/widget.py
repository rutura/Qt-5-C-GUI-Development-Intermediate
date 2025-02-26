from PySide6.QtWidgets import QWidget, QSplitter
from ui_widget import Ui_Widget
from container import Container

class Widget(QWidget):
    """Main widget that contains multiple container widgets"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # Create a splitter with two container widgets
        splitter = QSplitter(self)
        
        # Add two container widgets to the splitter
        splitter.addWidget(Container(self))
        splitter.addWidget(Container(self))
        
        # Add the splitter to the layout
        self.ui.verticalLayout.addWidget(splitter)
        
        # Set window title
        self.setWindowTitle("Drag and Drop Demo")