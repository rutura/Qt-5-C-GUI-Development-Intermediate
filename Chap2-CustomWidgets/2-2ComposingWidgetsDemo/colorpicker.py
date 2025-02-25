from PySide6.QtWidgets import (QWidget, QVBoxLayout, QPushButton, 
                             QGridLayout, QLabel, QSizePolicy)
from PySide6.QtGui import QColor
from PySide6.QtCore import Signal
from PySide6.QtCore import Qt

class ColorPicker(QWidget):
    # Define the signal (equivalent to C++ signal)
    colorChanged = Signal(QColor)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Initialize color attributes
        self.color = QColor()
        self.colorList = []
        
        # Populate colors and set up UI
        self.populateColors()
        self.setupUi()
    
    def getColor(self):
        return self.color
    
    def setColor(self, value):
        self.color = value
    
    def button1Clicked(self):
        css = f"background-color: {self.colorList[0].name()}"
        self.label.setStyleSheet(css)
        self.colorChanged.emit(self.colorList[0])
    
    def button2Clicked(self):
        css = f"background-color: {self.colorList[1].name()}"
        self.label.setStyleSheet(css)
        self.colorChanged.emit(self.colorList[1])
    
    def button3Clicked(self):
        css = f"background-color: {self.colorList[2].name()}"
        self.label.setStyleSheet(css)
        self.colorChanged.emit(self.colorList[2])
    
    def button4Clicked(self):
        css = f"background-color: {self.colorList[3].name()}"
        self.label.setStyleSheet(css)
        self.colorChanged.emit(self.colorList[3])
    
    def button5Clicked(self):
        css = f"background-color: {self.colorList[4].name()}"
        self.label.setStyleSheet(css)
        self.colorChanged.emit(self.colorList[4])
    
    def button6Clicked(self):
        css = f"background-color: {self.colorList[5].name()}"
        self.label.setStyleSheet(css)
        self.colorChanged.emit(self.colorList[5])
    
    def button7Clicked(self):
        css = f"background-color: {self.colorList[6].name()}"
        self.label.setStyleSheet(css)
        self.colorChanged.emit(self.colorList[6])
    
    def button8Clicked(self):
        css = f"background-color: {self.colorList[7].name()}"
        self.label.setStyleSheet(css)
        self.colorChanged.emit(self.colorList[7])
    
    def button9Clicked(self):
        css = f"background-color: {self.colorList[8].name()}"
        self.label.setStyleSheet(css)
        self.colorChanged.emit(self.colorList[8])
    
    def populateColors(self):
        # Add colors to the list (equivalent to C++ QList appending)
        self.colorList = [
            QColor(Qt.red),
            QColor(Qt.green),
            QColor(Qt.blue),
            QColor(Qt.cyan),
            QColor(Qt.darkRed),
            QColor(Qt.darkGray),
            QColor(Qt.gray),
            QColor(Qt.yellow),
            QColor(Qt.darkYellow)
        ]
    
    def setupUi(self):
        # Create layout structure
        vLayout = QVBoxLayout(self)
        self.gLayout = QGridLayout()
        policy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        
        # Create and configure buttons
        # Button 1
        button1 = QPushButton("one", self)
        button1.setSizePolicy(policy)
        css = f"background-color: {self.colorList[0].name()}"
        button1.setStyleSheet(css)
        button1.clicked.connect(self.button1Clicked)
        
        # Button 2
        button2 = QPushButton("two", self)
        button2.setSizePolicy(policy)
        css = f"background-color: {self.colorList[1].name()}"
        button2.setStyleSheet(css)
        button2.clicked.connect(self.button2Clicked)
        
        # Button 3
        button3 = QPushButton("three", self)
        button3.setSizePolicy(policy)
        css = f"background-color: {self.colorList[2].name()}"
        button3.setStyleSheet(css)
        button3.clicked.connect(self.button3Clicked)
        
        # Button 4
        button4 = QPushButton("four", self)
        button4.setSizePolicy(policy)
        css = f"background-color: {self.colorList[3].name()}"
        button4.setStyleSheet(css)
        button4.clicked.connect(self.button4Clicked)
        
        # Button 5
        button5 = QPushButton("five", self)
        button5.setSizePolicy(policy)
        css = f"background-color: {self.colorList[4].name()}"
        button5.setStyleSheet(css)
        button5.clicked.connect(self.button5Clicked)
        
        # Button 6
        button6 = QPushButton("six", self)
        button6.setSizePolicy(policy)
        css = f"background-color: {self.colorList[5].name()}"
        button6.setStyleSheet(css)
        button6.clicked.connect(self.button6Clicked)
        
        # Button 7
        button7 = QPushButton("seven", self)
        button7.setSizePolicy(policy)
        css = f"background-color: {self.colorList[6].name()}"
        button7.setStyleSheet(css)
        button7.clicked.connect(self.button7Clicked)
        
        # Button 8
        button8 = QPushButton("eight", self)
        button8.setSizePolicy(policy)
        css = f"background-color: {self.colorList[7].name()}"
        button8.setStyleSheet(css)
        button8.clicked.connect(self.button8Clicked)
        
        # Button 9
        button9 = QPushButton("nine", self)
        button9.setSizePolicy(policy)
        css = f"background-color: {self.colorList[8].name()}"
        button9.setStyleSheet(css)
        button9.clicked.connect(self.button9Clicked)
        
        # Add buttons to grid layout
        self.gLayout.addWidget(button1, 0, 0)
        self.gLayout.addWidget(button2, 0, 1)
        self.gLayout.addWidget(button3, 0, 2)
        
        self.gLayout.addWidget(button4, 1, 0)
        self.gLayout.addWidget(button5, 1, 1)
        self.gLayout.addWidget(button6, 1, 2)
        
        self.gLayout.addWidget(button7, 2, 0)
        self.gLayout.addWidget(button8, 2, 1)
        self.gLayout.addWidget(button9, 2, 2)
        
        # Create and configure label
        self.label = QLabel("Color")
        css = "background-color: #eeeab6"
        self.label.setFixedHeight(50)
        self.label.setStyleSheet(css)
        
        # Add widgets to the vertical layout
        vLayout.addWidget(self.label)
        vLayout.addLayout(self.gLayout)