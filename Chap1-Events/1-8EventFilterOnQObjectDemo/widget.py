from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Slot
from ui_widget import Ui_Widget
from keyboardfilter import KeyboardFilter

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # Create the keyboard filter
        self.filter = KeyboardFilter(self)
        
        # Install the filter on the line edit
        self.ui.lineEdit.installEventFilter(self.filter)
        
        # Connect the remove filter button
        self.ui.removeFilterButton.clicked.connect(self.on_removeFilterButton_clicked)
    
    @Slot()
    def on_removeFilterButton_clicked(self):
        """Remove the event filter from the line edit"""
        self.ui.lineEdit.removeEventFilter(self.filter)