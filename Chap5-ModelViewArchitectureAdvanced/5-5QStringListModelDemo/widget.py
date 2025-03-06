from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QColor, QPixmap
from PySide6.QtCore import Slot, QModelIndex, QStringListModel
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
        
        # Set the model to the list view
        self.ui.listView.setModel(self.model)
        
        # Connect the clicked signal to our slot
        self.ui.listView.clicked.connect(self.on_listView_clicked)
        
        # Set window title
        self.setWindowTitle("Color Picker Demo")
    
    @Slot(QModelIndex)
    def on_listView_clicked(self, index):
        """Handle list view item click to show the selected color"""
        # Get the color name from the model
        color_name = self.model.data(index, role=0)  # DisplayRole is 0
        
        # Create a pixmap filled with the selected color
        pixmap = QPixmap(self.ui.label.size())
        pixmap.fill(QColor(color_name))
        
        # Set the pixmap to the label
        self.ui.label.setPixmap(pixmap)
        
        # Debug output
        print("Showing all the colors")
        print("--------------------->>> Model Internal String list", self.model.stringList())
        print("--------------------->>> Original External String list", self.color_list)