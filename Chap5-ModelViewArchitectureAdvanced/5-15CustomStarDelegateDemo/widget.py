from PySide6.QtWidgets import QWidget, QTableWidgetItem
from ui_widget import Ui_Widget
from stardelegate import StarDelegate

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # Create the star delegate
        self.delegate = StarDelegate(self)
        
        # Initialize data
        self.data = [
            ["Beginning Qt C++ GUI Development", "Qt C++ GUI", 2],
            ["Qt Quick and QML For Beginners", "QML", 5],
            ["Qt Quick and QML Intermediate", "QML", 4],
            ["Qt Quick and QML Advanced", "QML", 4],
            ["Qt 5 C++ GUI Intermediate", "Qt C++ GUI", 1],
            ["Qt 5 C++ GUI Advanced", "Qt C++ GUI", 5]
        ]
        
        # Set up table widget
        self.ui.tableWidget.setRowCount(len(self.data))
        self.ui.tableWidget.setColumnCount(len(self.data[0]))
        
        # Set column headers
        self.ui.tableWidget.setHorizontalHeaderLabels(["Course Title", "Category", "Rating"])
        
        # Apply delegate to the rating column
        self.ui.tableWidget.setItemDelegateForColumn(2, self.delegate)
        
        # Populate table with data
        for row in range(len(self.data)):
            item0 = QTableWidgetItem(self.data[row][0])
            item1 = QTableWidgetItem(self.data[row][1])
            item2 = QTableWidgetItem(str(self.data[row][2]))
            
            self.ui.tableWidget.setItem(row, 0, item0)
            self.ui.tableWidget.setItem(row, 1, item1)
            self.ui.tableWidget.setItem(row, 2, item2)
        
        # Resize columns to fit content
        self.ui.tableWidget.resizeColumnsToContents()
        
        # Set window title
        self.setWindowTitle("Star Rating Delegate Demo")