from PySide6.QtWidgets import QWidget, QTableWidgetItem
from PySide6.QtCore import Qt
from ui_widget import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # Initialize table data
        self.table = [
            ["John", "Doe", "32", "Farmer", "Single", "Gounduana", "Mestkv", "89"],
            ["Mary", "Jane", "27", "Teacher", "Married", "Verkso", "Tukk", "55"],
            ["John", "Doe", "32", "Farmer", "Single", "Gounduana", "Mestkv", "67"],
            ["Mary", "Jane", "27", "Teacher", "Married", "Verkso", "Tukk", "78"],
            ["John", "Doe", "32", "Farmer", "Single", "Gounduana", "Mestkv", "51"],
            ["Mary", "Jane", "27", "Teacher", "Married", "Verkso", "Tukk", "83"],
            ["John", "Doe", "32", "Farmer", "Single", "Gounduana", "Mestkv", "59"],
            ["Mary", "Jane", "27", "Teacher", "Married", "Verkso", "Tukk", "62"],
            ["John", "Doe", "32", "Farmer", "Single", "Gounduana", "Mestkv", "69"],
            ["Mary", "Jane", "27", "Teacher", "Married", "Verkso", "Tukk", "58"],
            ["John", "Doe", "32", "Farmer", "Single", "Gounduana", "Mestkv", "73"],
            ["Mary", "Jane", "27", "Teacher", "Married", "Verkso", "Tukk", "83"],
            ["John", "Doe", "32", "Farmer", "Single", "Gounduana", "Mestkv", "71"],
            ["Mary", "Jane", "27", "Teacher", "Married", "Verkso", "Tukk", "65"],
            ["John", "Doe", "32", "Farmer", "Single", "Gounduana", "Mestkv", "77"],
            ["Mary", "Jane", "27", "Teacher", "Married", "Verkso", "Tukk", "64"],
            ["John", "Doe", "32", "Farmer", "Single", "Gounduana", "Mestkv", "88"],
            ["Mary", "Jane", "27", "Teacher", "Married", "Verkso", "Tukk", "86"],
            ["John", "Doe", "32", "Farmer", "Single", "Gounduana", "Mestkv", "58"],
            ["Mary", "Jane", "27", "Teacher", "Married", "Verkso", "Tukk", "72"]
        ]
        
        # Set table headers
        labels = ["First Name", "Last Name", "Age", "Profession", "Marital Status", 
                  "Country", "City", "Social Score"]
        self.ui.tableWidget.setHorizontalHeaderLabels(labels)
        
        # Populate table with data
        rows = len(self.table)
        columns = len(self.table[0])
        
        for row in range(rows):
            self.new_row()
            for col in range(columns):
                # Set text for each cell
                self.ui.tableWidget.item(row, col).setText(self.table[row][col])
        
        # Set alternating row colors for better readability
        self.ui.tableWidget.setAlternatingRowColors(True)
        
        # Set window title
        self.setWindowTitle("QTableWidget Demo")
    
    def new_row(self):
        """Add a new row to the table widget"""
        row = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row)
        
        first_item = None
        
        # Create items for each column in the new row
        for i in range(8):
            item = QTableWidgetItem()
            if i == 0:
                first_item = item
            
            # Right align text in table cells
            item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.ui.tableWidget.setItem(row, i, item)
        
        # Set focus on the first item of the new row
        if first_item:
            self.ui.tableWidget.setCurrentItem(first_item)