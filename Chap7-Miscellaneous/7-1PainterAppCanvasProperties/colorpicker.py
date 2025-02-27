from PySide6.QtWidgets import QWidget, QGridLayout, QColorDialog
from PySide6.QtGui import QColor
from PySide6.QtCore import Signal
from doubleclickbutton import DoubleclickButton

class ColorPicker(QWidget):
    """Color picker widget with a grid of color buttons"""
    
    # Signal emitted when a color is selected
    colorChanged = Signal(QColor)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.colors = []
        self.populate_colors()
        
        # Create the grid layout
        layout = QGridLayout(self)
        
        # Row 1
        button1 = DoubleclickButton(self)
        button1.setFixedSize(30, 30)
        self.set_button_color(button1, self.colors[0])
        self.make_connections(button1, 0)
        
        button2 = DoubleclickButton(self)
        button2.setFixedSize(30, 30)
        self.set_button_color(button2, self.colors[1])
        self.make_connections(button2, 1)
        
        button3 = DoubleclickButton(self)
        button3.setFixedSize(30, 30)
        self.set_button_color(button3, self.colors[2])
        self.make_connections(button3, 2)
        
        button4 = DoubleclickButton(self)
        button4.setFixedSize(30, 30)
        self.set_button_color(button4, self.colors[3])
        self.make_connections(button4, 3)
        
        button5 = DoubleclickButton(self)
        button5.setFixedSize(30, 30)
        self.set_button_color(button5, self.colors[4])
        self.make_connections(button5, 4)
        
        button6 = DoubleclickButton(self)
        button6.setFixedSize(30, 30)
        self.set_button_color(button6, self.colors[5])
        self.make_connections(button6, 5)
        
        button7 = DoubleclickButton(self)
        button7.setFixedSize(30, 30)
        self.set_button_color(button7, self.colors[6])
        self.make_connections(button7, 6)
        
        # Row 2
        button8 = DoubleclickButton(self)
        button8.setFixedSize(30, 30)
        self.set_button_color(button8, self.colors[7])
        self.make_connections(button8, 7)
        
        button9 = DoubleclickButton(self)
        button9.setFixedSize(30, 30)
        self.set_button_color(button9, self.colors[8])
        self.make_connections(button9, 8)
        
        button10 = DoubleclickButton(self)
        button10.setFixedSize(30, 30)
        self.set_button_color(button10, self.colors[9])
        self.make_connections(button10, 9)
        
        button11 = DoubleclickButton(self)
        button11.setFixedSize(30, 30)
        self.set_button_color(button11, self.colors[10])
        self.make_connections(button11, 10)
        
        button12 = DoubleclickButton(self)
        button12.setFixedSize(30, 30)
        self.set_button_color(button12, self.colors[11])
        self.make_connections(button12, 11)
        
        button13 = DoubleclickButton(self)
        button13.setFixedSize(30, 30)
        self.set_button_color(button13, self.colors[12])
        self.make_connections(button13, 12)
        
        button14 = DoubleclickButton(self)
        button14.setFixedSize(30, 30)
        self.set_button_color(button14, self.colors[13])
        self.make_connections(button14, 13)
        
        # Add buttons to layout
        layout.addWidget(button1, 0, 0)
        layout.addWidget(button2, 0, 1)
        layout.addWidget(button3, 0, 2)
        layout.addWidget(button4, 0, 3)
        layout.addWidget(button5, 0, 4)
        layout.addWidget(button6, 0, 5)
        layout.addWidget(button7, 0, 6)
        
        layout.addWidget(button8, 1, 0)
        layout.addWidget(button9, 1, 1)
        layout.addWidget(button10, 1, 2)
        layout.addWidget(button11, 1, 3)
        layout.addWidget(button12, 1, 4)
        layout.addWidget(button13, 1, 5)
        layout.addWidget(button14, 1, 6)
        
        self.setLayout(layout)
    
    def populate_colors(self):
        """Populate the colors list with default colors"""
        self.colors = [
            QColor(34, 56, 78),
            QColor(67, 156, 200),
            QColor(134, 6, 98),
            QColor(14, 56, 178),
            QColor(114, 16, 208),
            QColor(34, 56, 78),
            QColor(67, 156, 200),
            QColor(51, 102, 255),
            QColor(255, 0, 102),
            QColor(204, 51, 153),
            QColor(204, 204, 0),
            QColor(255, 102, 255),
            QColor(51, 153, 255),
            QColor(153, 255, 153)
        ]
    
    def set_button_color(self, button, color):
        """Set the background color of a button"""
        button.setStyleSheet(f"background-color: {color.name()}")
    
    def make_connections(self, button, index):
        """Connect button signals to slots"""
        # Simple click - emit the color
        button.clicked.connect(lambda checked=False, idx=index: self.colorChanged.emit(self.colors[idx]))
        
        # Double click - open color dialog
        button.doubleClicked.connect(lambda idx=index: self.open_color_dialog(button, idx))
    
    def open_color_dialog(self, button, index):
        """Open a color dialog to select a new color"""
        color = QColorDialog.getColor(self.colors[index], self, "Pick Color")
        if color.isValid():
            self.colors[index] = color
            self.set_button_color(button, color)