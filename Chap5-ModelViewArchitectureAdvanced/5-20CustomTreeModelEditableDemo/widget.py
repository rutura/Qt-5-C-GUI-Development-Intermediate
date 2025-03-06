from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QModelIndex, QItemSelectionModel, Qt
from ui_widget import Ui_Widget
from personmodel import PersonModel

class Widget(QWidget):
    def __init__(self, parent=None):
        """
        Initialize the widget with a tree view model and buttons
        
        :param parent: Parent widget
        """
        super().__init__(parent)
        
        # Setup UI
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # Create and set model
        self.person_model = PersonModel(self)
        
        # Configure tree view
        self.ui.treeView.setModel(self.person_model)
        self.ui.treeView.setAlternatingRowColors(True)
        
        # Connect buttons to their respective methods
        self.ui.addRowButton.clicked.connect(self.on_add_row_button_clicked)
        self.ui.removeRowButton.clicked.connect(self.on_remove_row_button_clicked)
        self.ui.addColumnButton.clicked.connect(self.on_add_column_button_clicked)
        self.ui.removeColumnButton.clicked.connect(self.on_remove_column_button_clicked)
        self.ui.addChildButton.clicked.connect(self.on_add_child_button_clicked)
        
        # Set window title
        self.setWindowTitle("Editable Family Tree Model")

    def on_add_row_button_clicked(self):
        """
        Add a new row at the current index
        """
        index = self.ui.treeView.selectionModel().currentIndex()
        model = self.ui.treeView.model()

        if model.insertRow(index.row() + 1, index.parent()):
            for column in range(model.columnCount(index.parent())):
                child_index = model.index(index.row() + 1, column, index.parent())
                model.setData(child_index, "[Empty Cell]", role=0)

    def on_remove_row_button_clicked(self):
        """
        Remove the currently selected row
        """
        index = self.ui.treeView.selectionModel().currentIndex()
        model = self.ui.treeView.model()
        model.removeRow(index.row(), index.parent())

    def on_add_column_button_clicked(self):
        """
        Add a new column
        """
        model = self.ui.treeView.model()
        column = self.ui.treeView.selectionModel().currentIndex().column()

        # Insert a column and set a header
        if model.insertColumn(column + 1):
            model.setHeaderData(column + 1, Qt.Horizontal, "[No Header]")

    def on_remove_column_button_clicked(self):
        """
        Remove the currently selected column
        """
        model = self.ui.treeView.model()
        column = self.ui.treeView.selectionModel().currentIndex().column()
        model.removeColumn(column)

    def on_add_child_button_clicked(self):
        """
        Add a new child to the currently selected item
        """
        index = self.ui.treeView.selectionModel().currentIndex()
        model = self.ui.treeView.model()

        # Ensure there are columns
        if model.columnCount(index) == 0:
            if not model.insertColumn(0, index):
                return

        # Insert a new row as a child
        if model.insertRow(0, index):
            for column in range(model.columnCount(index)):
                child_index = model.index(0, column, index)
                model.setData(child_index, "[Empty Cell]", role=0)

            # Set the new child as the current index
            selection_model = self.ui.treeView.selectionModel()
            selection_model.setCurrentIndex(
                model.index(0, 0, index), 
                QItemSelectionModel.ClearAndSelect
            )