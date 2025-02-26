from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtCore import QPointF, Qt, QEvent, Slot
from PySide6.QtGui import QMouseEvent
from ui_widget import Ui_Widget
from button import Button

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # Create custom button
        self.button1 = Button(self)
        self.button1.setText("I am the phoenix king")
        self.button1.setGeometry(130, 70, 150, 28)  # Position the button
        
        # Connect button2 clicked signal
        self.ui.button2.clicked.connect(self.on_button2_clicked)
    
    @Slot()
    def on_button2_clicked(self):
        """Create and post a synthetic mouse event to button1"""
        
        # Create a mouse press event
        mouse_event = QMouseEvent(
            QEvent.MouseButtonPress,  # Type
            QPointF(10, 10),          # Local position
            QPointF(10, 10),          # Screen position 
            Qt.LeftButton,            # Button
            Qt.LeftButton,            # Buttons
            Qt.NoModifier             # Modifiers
        )
        
        # Using postEvent (asynchronous)
        QApplication.postEvent(self.button1, mouse_event)
        
        # Alternatively, using sendEvent (synchronous)
        # if QApplication.sendEvent(self.button1, mouse_event):
        #     print("Event accepted")
        # else:
        #     print("Event not accepted")