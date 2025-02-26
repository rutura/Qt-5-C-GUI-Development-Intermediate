from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Slot
from ui_widget import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # Connect signals to slots
        self.ui.pushButton.clicked.connect(self.on_pushButton_clicked)
        
    @Slot()
    def on_pushButton_clicked(self):
        """Slot for the push button's clicked signal"""
        print("Button clicked")