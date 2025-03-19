from PySide6.QtCore import QObject, Slot, Signal, QModelIndex

class DragDropController(QObject):
    """Controller for drag and drop operations
    
    Acts as an intermediary between the item model and views
    """
    
    # Signal when an item is moved
    itemMoved = Signal(int, int)
    
    def __init__(self, model=None, parent=None):
        super().__init__(parent)
        self._model = model
    
    def set_model(self, model):
        """Set the model for this controller"""
        self._model = model
    
    @Slot(int, int)
    def moveItem(self, sourceIndex, targetIndex):
        """Move an item from source to target index"""
        if not self._model or sourceIndex < 0 or targetIndex < 0:
            return False
            
        if sourceIndex >= self._model.rowCount() or targetIndex >= self._model.rowCount():
            return False
            
        # Skip if source and target are the same
        if sourceIndex == targetIndex:
            return True
            
        # Get the item to move
        sourceItem = self._model.takeItem(sourceIndex)
        if not sourceItem:
            return False
            
        # Insert at new position
        self._model.insertRow(targetIndex, sourceItem)
        
        # Emit signal
        self.itemMoved.emit(sourceIndex, targetIndex)
        
        print(f"Moved item from index {sourceIndex} to {targetIndex}")
        return True