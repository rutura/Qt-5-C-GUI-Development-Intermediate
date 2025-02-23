from typing import Optional
from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import Slot
from PySide6.QtUiTools import QUiLoader
from custom_widgets import ChildButton, ChildLineEdit

class Widget(QWidget):
    """Main widget class containing the custom buttons and line edits."""
    
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.setup_ui()
        self.setup_widgets()
        
    def setup_ui(self) -> None:
        """Initialize the UI from the .ui file or create it programmatically."""
        # Create main layout
        self.setWindowTitle("Event Propagation Demo")
        self.resize(400, 300)
        
        # Create the main layout
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        
        # Store the layout for adding widgets
        self.vertical_layout = QVBoxLayout()
        main_layout.addLayout(self.vertical_layout)
        
    def setup_widgets(self) -> None:
        """Create and setup the custom widgets."""
        # Create child button
        button = ChildButton(self)
        button.setText("Child Button")
        button.clicked.connect(self.on_button_clicked)
        
        # Create child line edit
        line_edit = ChildLineEdit(self)
        
        # Add widgets to layout
        self.vertical_layout.addWidget(button)
        self.vertical_layout.addWidget(line_edit)
    
    @Slot()
    def on_button_clicked(self) -> None:
        """Slot handling button clicks."""
        print("Button clicked")