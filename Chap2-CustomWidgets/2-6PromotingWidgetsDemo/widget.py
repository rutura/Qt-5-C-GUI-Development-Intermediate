from PySide6.QtWidgets import QWidget
from ui_widget import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # Connect signals from water tank to indicator
        self.ui.waterTank.normal.connect(self.ui.indicator.activateNormal)
        self.ui.waterTank.warning.connect(self.ui.indicator.activateWarning)
        self.ui.waterTank.danger.connect(self.ui.indicator.activateDanger)