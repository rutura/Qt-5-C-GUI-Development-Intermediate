from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from ui_widget import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # Initialize the table data
        self.table = [
            ["John", "Doe", "32", "Farmer", "Single", "Gounduana", "Mestkv", "89"],
            ["Mary", "Jane", "27", "Teacher", "Married", "Verkso", "Tukk", "55"],
            ["Donald", "Milton", "32", "Farmer", "Single", "Gounduana", "Mestkv", "67"],
            ["Samatha", "Chan", "27", "Teacher", "Married", "Verkso", "Tukk", "78"],
            ["Andrew", "Knut", "32", "Farmer", "Single", "Gounduana", "Mestkv", "51"]
        ]
        
        # Configure list widget with color names
        self.ui.listWidget.addItems(QColor.colorNames())
        self.ui.listWidget.setDragEnabled(True)
        self.ui.listWidget.setAcceptDrops(True)
        self.ui.listWidget.setDropIndicatorShown(True)
        self.ui.listWidget.setDragDropMode(QAbstractItemView.DragDropMode.InternalMove)
        
        # Configure table widget
        labels = ["First Name", "Last Name", "Age", "Profession", "Marital Status", 
                  "Country", "City", "Social Score"]
        self.ui.tableWidget.setHorizontalHeaderLabels(labels)
        
        # Populate table with data
        rows = len(self.table)
        columns = len(self.table[0])
        
        for row in range(rows):
            self.new_row()
            for col in range(columns):
                self.ui.tableWidget.item(row, col).setText(self.table[row][col])
                self.ui.tableWidget.item(row, col).setData(
                    Qt.ItemDataRole.ToolTipRole, 
                    f"item [{row},{col}]"
                )
        
        # Configure table widget for drag and drop
        self.ui.tableWidget.setDragEnabled(True)
        self.ui.tableWidget.setAcceptDrops(True)
        self.ui.tableWidget.setDropIndicatorShown(True)
        
        # Set window title
        self.setWindowTitle("Drag and Drop Demo with ListWidget and TableWidget")
    
    def new_row(self):
        """Add a new row to the table widget"""
        row = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row)
        
        first_item = None
        
        for i in range(8):
            item = QTableWidgetItem()
            if i == 0:
                first_item = item
            
            # Right align text in table cells
            item.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
            self.ui.tableWidget.setItem(row, i, item)
        
        # Set focus on the first item of the new row
        if first_item:
            self.ui.tableWidget.setCurrentItem(first_item)