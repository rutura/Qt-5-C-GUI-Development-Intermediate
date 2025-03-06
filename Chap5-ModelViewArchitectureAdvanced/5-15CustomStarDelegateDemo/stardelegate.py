from PySide6.QtWidgets import QStyledItemDelegate, QWidget
from PySide6.QtCore import Qt, QSize, QPoint, Slot
from PySide6.QtGui import QPainter, QPolygon, QBrush
from stareditor import StarEditor

class StarDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Create star polygon shape
        self.poly = QPolygon()
        self.poly << QPoint(0, 85) << QPoint(75, 75) \
                 << QPoint(100, 10) << QPoint(125, 75) \
                 << QPoint(200, 85) << QPoint(150, 125) \
                 << QPoint(160, 190) << QPoint(100, 150) \
                 << QPoint(40, 190) << QPoint(50, 125) \
                 << QPoint(0, 85)
    
    def paint(self, painter, option, index):
        """Custom paint method to draw stars"""
        if index.column() == 2:
            rect = option.rect.adjusted(10, 10, -10, -10)
            star_number = index.data()
            
            # Convert from QVariant if necessary
            if isinstance(star_number, str):
                star_number = int(star_number)
            
            painter.save()
            
            # Enable antialiasing for smoother drawing
            painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
            painter.setPen(Qt.PenStyle.NoPen)
            painter.setBrush(QBrush(Qt.GlobalColor.black))
            
            # Move painter for star drawing
            painter.translate(rect.x(), rect.y())
            painter.scale(0.1, 0.1)
            
            # Draw the stars based on rating
            for i in range(star_number):
                painter.drawPolygon(self.poly)
                painter.translate(220, 0)
            
            painter.restore()
        else:
            # For other columns, use default painting
            super().paint(painter, option, index)
    
    def sizeHint(self, option, index):
        """Return size hint for the item"""
        return super().sizeHint(option, index)
    
    def createEditor(self, parent, option, index):
        """Create a custom editor for star ratings"""
        if index.column() == 2:
            star_rating = index.data()
            
            # Convert from QVariant if necessary
            if isinstance(star_rating, str):
                star_rating = int(star_rating)
            
            # Create and configure the star editor
            editor = StarEditor(parent)
            editor.setStarRating(star_rating)
            
            # Connect to the editing finished signal
            editor.editingFinished.connect(self.commitAndCloseEditor)
            
            return editor
        else:
            # For other columns, use default editor
            return super().createEditor(parent, option, index)
    
    def setEditorData(self, editor, index):
        """Set the editor data from the model"""
        if index.column() == 2:
            star_rating = index.data()
            
            # Convert from QVariant if necessary
            if isinstance(star_rating, str):
                star_rating = int(star_rating)
            
            # Set the star rating in the editor
            star_editor = editor
            star_editor.setStarRating(star_rating)
        else:
            # For other columns, use default behavior
            super().setEditorData(editor, index)
    
    def setModelData(self, editor, model, index):
        """Update the model with data from the editor"""
        if index.column() == 2:
            star_editor = editor
            # Set the data in the model - directly use Python int
            model.setData(index, star_editor.getStarRating(), Qt.ItemDataRole.EditRole)
        else:
            # For other columns, use default behavior
            super().setModelData(editor, model, index)
    
    @Slot()
    def commitAndCloseEditor(self):
        """Commit data and close the editor"""
        editor = self.sender()
        self.commitData.emit(editor)
        self.closeEditor.emit(editor)