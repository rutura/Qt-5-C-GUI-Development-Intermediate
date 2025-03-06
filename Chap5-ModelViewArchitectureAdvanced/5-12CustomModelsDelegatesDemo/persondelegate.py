from PySide6.QtWidgets import QStyledItemDelegate, QComboBox
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QColor, QPixmap, QIcon
from personmodel import PersonModel

class PersonDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)
    
    def createEditor(self, parent, option, index):
        """Create editor widget for editing data"""
        if index.column() == 2:  # Favorite color column
            editor = QComboBox(parent)
            
            # Add all color names with color swatches as icons
            for color in QColor.colorNames():
                pixmap = QPixmap(50, 50)
                pixmap.fill(QColor(color))
                editor.addItem(QIcon(pixmap), color)
            
            return editor
        else:
            # For other columns, use default editor
            return super().createEditor(parent, option, index)
    
    def setEditorData(self, editor, index):
        """Set editor data based on model data"""
        if index.column() == 2:  # Favorite color column
            combo = editor
            color_name = index.data(Qt.DisplayRole)
            color_index = QColor.colorNames().index(color_name)
            combo.setCurrentIndex(color_index)
        else:
            # For other columns, use default behavior
            super().setEditorData(editor, index)
    
    def setModelData(self, editor, model, index):
        """Update model with data from editor"""
        if index.column() == 2:  # Favorite color column
            combo = editor
            # Use FavoriteColorRole to update the model
            model.setData(index, combo.currentText(), PersonModel.FavoriteColorRole)
        else:
            # For other columns, use default behavior
            super().setModelData(editor, model, index)
    
    def updateEditorGeometry(self, editor, option, index):
        """Position editor within the cell"""
        editor.setGeometry(option.rect)
    
    def sizeHint(self, option, index):
        """Provide size hint for items"""
        # Make sure items have at least 64px width and enough height
        default_size = super().sizeHint(option, index)
        return default_size.expandedTo(QSize(64, option.fontMetrics.height() + 10))