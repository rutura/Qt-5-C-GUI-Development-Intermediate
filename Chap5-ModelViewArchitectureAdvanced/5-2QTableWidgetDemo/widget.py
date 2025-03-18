from PySide6.QtWidgets import QWidget, QTableView
from PySide6.QtCore import Qt
from ui_widget import Ui_Widget
from models import PersonModel

class Widget(QWidget):
    """Main application widget using MVC pattern"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # Create model
        self.model = PersonModel()
        
        # Set up view
        self.ui.tableWidget.hide()  # Hide the original QTableWidget
        
        # Create QTableView and add it to the layout
        self.tableView = QTableView(self)
        self.ui.verticalLayout.addWidget(self.tableView)
        
        # Set model to view
        self.tableView.setModel(self.model)
        
        # Set visual properties
        self.tableView.setAlternatingRowColors(True)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.verticalHeader().setVisible(False)
        
        # Set window title
        self.setWindowTitle("QTableView MVC Demo")