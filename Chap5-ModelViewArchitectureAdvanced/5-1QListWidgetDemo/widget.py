from PySide6.QtWidgets import QWidget, QListWidgetItem
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, Slot, QSize
from ui_widget import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # Set icon size for list widget
        self.ui.listWidget.setIconSize(QSize(70, 70))
        
        # Define fruit list
        self.fruitList = [
            "Apple", "Avocado", "Banana", "Blueberries", 
            "Cucumber", "EggFruit", "Fig", "Grape", 
            "Mango", "Pear", "Pineapple", "Watermellon"
        ]
        
        # Add items to list widget
        self.ui.listWidget.addItems(self.fruitList)
        
        # Set icons and additional data for each item
        for i in range(self.ui.listWidget.count()):
            item = self.ui.listWidget.item(i)
            filename = f":/images/{self.fruitList[i].lower()}.png"
            item.setIcon(QIcon(filename))
            item.setData(Qt.UserRole, self.fruitList[i])
            item.setData(Qt.DisplayRole, f"{self.fruitList[i]}Funny")
        
        # Connect button click signal to slot
        self.ui.readDataButton.clicked.connect(self.on_readDataButton_clicked)
        
        # Set window title
        self.setWindowTitle("Fruit List Demo")
    
    @Slot()
    def on_readDataButton_clicked(self):
        """Handle Read Data button click"""
        current_item = self.ui.listWidget.currentItem()
        if current_item:
            fruit = current_item.data(Qt.DisplayRole)
            print(f"Current fruit: {fruit}")
            print(f"Current index: {self.ui.listWidget.currentRow()}")