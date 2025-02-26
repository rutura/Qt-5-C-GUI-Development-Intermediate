from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QSizePolicy
from PySide6.QtCore import QTimer, QDate, QTime, Qt, Slot
from PySide6.QtGui import QFont

class DateTimeWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Create layout
        layout = QVBoxLayout(self)
        
        # Set font and size policy
        mFont = QFont("Consolas", 20, QFont.Bold)
        policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        
        # Initialize date label
        self.dateString = QDate.currentDate().toString(Qt.TextDate)
        self.labelTop = QLabel(self)
        self.labelTop.setText(self.dateString)
        self.labelTop.setFont(mFont)
        self.labelTop.setAlignment(Qt.AlignCenter)
        
        # Initialize time label
        self.timeString = QTime.currentTime().toString()
        self.labelBottom = QLabel(self)
        self.labelBottom.setText(self.timeString)
        self.labelBottom.setFont(mFont)
        self.labelBottom.setAlignment(Qt.AlignCenter)
        self.labelBottom.setSizePolicy(policy)
        
        # Set style for time label
        css = "background-color: #00eff9; color: #fffff1"
        self.labelBottom.setStyleSheet(css)
        
        # Add widgets to layout
        layout.addWidget(self.labelTop)
        layout.addWidget(self.labelBottom)
        self.setLayout(layout)
        self.setSizePolicy(policy)
        
        # Set up timer
        self.timer = QTimer(self)
        self.timer.setInterval(1000)  # Update every second
        self.timer.timeout.connect(self.updateTime)
        self.timer.start()
    
    @Slot()
    def updateTime(self):
        """Update the time display, and date if it has changed"""
        # Update time
        self.timeString = QTime.currentTime().toString()
        self.labelBottom.setText(self.timeString)
        
        # Check if date has changed
        current_date = QDate.currentDate().toString(Qt.TextDate)
        if self.dateString != current_date:
            self.dateString = current_date
            self.labelTop.setText(self.dateString)