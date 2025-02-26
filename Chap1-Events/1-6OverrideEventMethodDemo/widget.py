from typing import Optional
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Slot
from ui_widget import Ui_Widget
from button import Button

class Widget(QWidget):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # Create custom button
        self.setup_buttons()
    
    def setup_buttons(self) -> None:
        """Create and configure buttons"""
        button = Button(self)
        button.setText("Button")
        button.clicked.connect(self.on_button_clicked)
        
        # Add button to the vertical layout
        self.ui.verticalLayout.addWidget(button)
    
    @Slot()
    def on_button_clicked(self) -> None:
        """Handle button click event"""
        print("Button clicked")