from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QColor
from PySide6.QtCore import Slot
from ui_widget import Ui_Widget
from colorpicker import ColorPicker

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # Create color picker and add it to the layout
        self.colorPicker = ColorPicker(self)
        self.colorPicker.colorChanged.connect(self.colorChanged)
        
        # Add the color picker to the vertical layout from the UI
        self.ui.verticalLayout.addWidget(self.colorPicker)
    
    @Slot(QColor)
    def colorChanged(self, color):
        """Handle color change from the color picker"""
        print(f"Color changed to: {color.name()}")