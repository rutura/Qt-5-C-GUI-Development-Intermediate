from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QColor, QPixmap
from PySide6.QtCore import Slot, QModelIndex, QStringListModel, QSortFilterProxyModel
from ui_widget import Ui_Widget

class Widget(QWidget):
    def __init__(self, model=None, proxy_model=None, controller=None, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # Store model, proxy model, and controller
        self._model = model
        self._proxy_model = proxy_model
        self._controller = controller
        
        # If no models provided, create them
        if not self._model:
            # Get all available color names
            self.color_list = QColor.colorNames()
            # Create a string list model with the color names
            self._model = QStringListModel(self.color_list, self)
        
        if not self._proxy_model:
            # Create a proxy model for filtering
            self._proxy_model = QSortFilterProxyModel(self)
            self._proxy_model.setSourceModel(self._model)
        
        # Set the proxy model to the list view
        self.ui.listView.setModel(self._proxy_model)
        
        # Connect signals to slots
        if self._controller:
            self.ui.listView.clicked.connect(self._on_listView_clicked_with_controller)
            self.ui.matchStringLineEdit.textChanged.connect(self._on_filter_text_changed_with_controller)
            self._controller.colorSelected.connect(self._on_color_selected)
        else:
            self.ui.listView.clicked.connect(self._on_listView_clicked_legacy)
            self.ui.matchStringLineEdit.textChanged.connect(self._on_filter_text_changed_legacy)
        
        # Set window title
        self.setWindowTitle("Color Filter Demo (Qt Widgets)")
    
    @Slot(QModelIndex)
    def _on_listView_clicked_with_controller(self, index):
        """Handle list view item click using controller"""
        if self._controller:
            self._controller.selectColorByIndex(index)
    
    @Slot(str)
    def _on_filter_text_changed_with_controller(self, text):
        """Handle filter text changes using controller"""
        if self._controller:
            self._controller.filterColors(text)
    
    @Slot(str)
    def _on_color_selected(self, color_name):
        """Handle color selection from controller"""
        self._update_color_display(color_name)
    
    @Slot(QModelIndex)
    def _on_listView_clicked_legacy(self, index):
        """Legacy method for backward compatibility"""
        # Get the color name from the proxy model
        color_name = self._proxy_model.data(index, 0)
        self._update_color_display(color_name)
        
        # Debug output
        print("Selected color:", color_name)
        print("--------------------->>> Model Internal String list", self._model.stringList())
    
    @Slot(str)
    def _on_filter_text_changed_legacy(self, text):
        """Legacy method for backward compatibility"""
        # Set the filter pattern on the proxy model
        self._proxy_model.setFilterRegularExpression(text)
    
    def _update_color_display(self, color_name):
        """Update the color display with the given color"""
        # Create a pixmap filled with the selected color
        pixmap = QPixmap(self.ui.label.size())
        pixmap.fill(QColor(color_name))
        
        # Set the pixmap to the label
        self.ui.label.setPixmap(pixmap)