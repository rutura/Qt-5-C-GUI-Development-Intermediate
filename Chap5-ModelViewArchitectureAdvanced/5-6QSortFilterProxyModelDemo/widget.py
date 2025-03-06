from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QColor, QPixmap
from PySide6.QtCore import Slot, QModelIndex,QStringListModel, QSortFilterProxyModel
from ui_widget import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # Get all available color names
        self.color_list = QColor.colorNames()
        
        # Create a string list model with the color names
        self.model = QStringListModel(self.color_list, self)
        
        # Create a proxy model for filtering
        self.proxy_model = QSortFilterProxyModel(self)
        self.proxy_model.setSourceModel(self.model)
        
        # Set the proxy model to the list view
        self.ui.listView.setModel(self.proxy_model)
        
        # Connect signals to slots
        self.ui.listView.clicked.connect(self.on_listView_clicked)
        self.ui.matchStringLineEdit.textChanged.connect(self.on_matchStringLineEdit_textChanged)
        
        # Set window title
        self.setWindowTitle("Color Filter Demo")
    
    @Slot(QModelIndex)
    def on_listView_clicked(self, index):
        """Handle list view item click to show the selected color"""
        # Get the color name from the proxy model
        color_name = self.proxy_model.data(index, role=0)  # DisplayRole is 0
        
        # Create a pixmap filled with the selected color
        pixmap = QPixmap(self.ui.label.size())
        pixmap.fill(QColor(color_name))
        
        # Set the pixmap to the label
        self.ui.label.setPixmap(pixmap)
        
        # Debug output
        print("Showing all the colors")
        print("--------------------->>> Model Internal String list", self.model.stringList())
        print("--------------------->>> Original External String list", self.color_list)
    
    @Slot(str)
    def on_matchStringLineEdit_textChanged(self, text):
        """Filter the list view based on the entered text"""
        # Set the filter pattern on the proxy model
        self.proxy_model.setFilterRegularExpression(text)