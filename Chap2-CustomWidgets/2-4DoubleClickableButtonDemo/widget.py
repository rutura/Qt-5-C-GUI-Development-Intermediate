from PySide6.QtWidgets import QWidget
from ui_widget import Ui_Widget
from doubleclickablebutton import DoubleClickableButton

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # Create the double-clickable button
        self.button = DoubleClickableButton(self)
        self.button.setText("Double Clickable Button")
        self.button.setGeometry(100, 100, 200, 50)  # Position the button
        
        # Connect the doubleClicked signal to our slot
        self.button.doubleClicked.connect(self.onButtonDoubleClicked)
    
    def onButtonDoubleClicked(self):
        """Handle double click on the button"""
        print("Button double clicked")