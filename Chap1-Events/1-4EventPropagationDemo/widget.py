from PySide6.QtWidgets import QWidget
from ui_widget import Ui_Widget
from childbutton import ChildButton
from childlineedit import ChildLineEdit
from PySide6.QtCore import Slot

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # Create child button
        button = ChildButton(self)
        button.setText("Child Button")
        button.clicked.connect(self.on_button_clicked)
        
        # Create child line edit
        line_edit = ChildLineEdit(self)
        
        # Add widgets to layout
        self.ui.verticalLayout.addWidget(button)
        self.ui.verticalLayout.addWidget(line_edit)
    
    @Slot()
    def on_button_clicked(self):
        print("Button clicked")