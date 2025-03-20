from PySide6.QtWidgets import QWidget
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
        
        # Connect signals if controller is provided
        if self._controller:
            self.ui.listView.clicked.connect(self._on_view_clicked)
            self.ui.tableView.clicked.connect(self._on_view_clicked)
            self.ui.treeView.clicked.connect(self._on_view_clicked)
            
            # Connect to controller's personSelected signal if needed
            # self._controller.personSelected.connect(self._on_person_selected)
        
        # Set window title
        self.setWindowTitle("Custom Model Demo (Qt Widgets)")
    
    @Slot(QModelIndex)
    def _on_view_clicked(self, index):
        """Handle view item clicked using controller"""
        if self._controller:
            self._controller.selectPersonByIndex(index)
    
    @Slot(int, str, str, int)
    def _on_person_selected(self, index, name, favorite_color, age):
        """Handle when a person is selected via the controller"""
        print(f"Person selected: {name}, {age}, {favorite_color}")