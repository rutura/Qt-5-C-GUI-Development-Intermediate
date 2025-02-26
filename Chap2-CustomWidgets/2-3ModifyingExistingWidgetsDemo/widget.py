from PySide6.QtWidgets import QWidget
from ui_widget import Ui_Widget
from datetimewidget import DateTimeWidget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # Create the datetime widget
        self.datetimeWidget = DateTimeWidget(self)
        
        # Add it to the layout from the UI file
        self.ui.verticalLayout.addWidget(self.datetimeWidget)