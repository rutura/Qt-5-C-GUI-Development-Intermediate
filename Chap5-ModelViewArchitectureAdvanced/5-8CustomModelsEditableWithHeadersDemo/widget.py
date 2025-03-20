from PySide6.QtWidgets import QWidget, QAbstractItemView
from PySide6.QtCore import Slot, QModelIndex
from ui_widget import Ui_Widget
from personmodel import PersonModel

class Widget(QWidget):
    def __init__(self, model=None, controller=None, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # Store model and controller
        self._model = model
        self._controller = controller
        
        # If no model provided, create one for backward compatibility
        if not self._model:
            self._model = PersonModel(self)
        
        # Set the model for all three views
        self.ui.listView.setModel(self._model)
        self.ui.tableView.setModel(self._model)
        self.ui.treeView.setModel(self._model)
        
        # Enable editing in views - use QAbstractItemView's edit triggers
        self.ui.listView.setEditTriggers(QAbstractItemView.DoubleClicked | QAbstractItemView.EditKeyPressed)
        self.ui.tableView.setEditTriggers(QAbstractItemView.DoubleClicked | QAbstractItemView.EditKeyPressed)
        self.ui.treeView.setEditTriggers(QAbstractItemView.DoubleClicked | QAbstractItemView.EditKeyPressed)
        
        # Connect signals if controller is provided
        if self._controller:
            self.ui.listView.clicked.connect(self._on_view_clicked)
            self.ui.tableView.clicked.connect(self._on_view_clicked)
            self.ui.treeView.clicked.connect(self._on_view_clicked)
            
            # Connect to dataChanged signal to handle edits directly
            # Note: This is an alternative to connecting to the controller's signal
            # The model's own signals are sufficient for simple editing
            #self._model.dataChanged.connect(self._on_data_changed)
        
        # Set window title
        self.setWindowTitle("Editable Custom Model Demo (Qt Widgets)")
    
    @Slot(QModelIndex)
    def _on_view_clicked(self, index):
        """Handle view item clicked using controller"""
        if self._controller:
            self._controller.selectPersonByIndex(index)
    
    @Slot(QModelIndex, QModelIndex)
    def _on_data_changed(self, topLeft, bottomRight):
        """Handle data changed in the model"""
        print(f"Data changed in model: rows {topLeft.row()} to {bottomRight.row()}")