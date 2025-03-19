from PySide6.QtCore import QObject, Slot, Signal, QModelIndex, Qt
from PySide6.QtGui import QStandardItem

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
        if not self._model:
            print(f"Error: No model set")
            return False
            
        if sourceIndex < 0 or targetIndex < 0:
            print(f"Invalid move: source={sourceIndex}, target={targetIndex}")
            return False
            
        # Handle the case where targetIndex is equal to rowCount
        # (dropping after the last item)
        row_count = self._model.rowCount()
        if targetIndex > row_count:
            targetIndex = row_count
            
        if sourceIndex >= row_count:
            print(f"Source index out of range: source={sourceIndex}, count={row_count}")
            return False
            
        # Skip if source and target are the same
        if sourceIndex == targetIndex:
            print(f"Source and target are the same: {sourceIndex}")
            return True
        
        try:
            # Get source item data for recreation
            sourceText = self._model.data(self._model.index(sourceIndex, 0), Qt.DisplayRole)
            canDrag = self._model.data(self._model.index(sourceIndex, 0), self._model.CanDragRole)
            canDrop = self._model.data(self._model.index(sourceIndex, 0), self._model.CanDropRole)
            
            print(f"Moving item: text={sourceText}, canDrag={canDrag}, canDrop={canDrop}")
            
            # Create a new item with the source properties
            newItem = QStandardItem(sourceText)
            newItem.setData(canDrag, self._model.CanDragRole)
            newItem.setData(canDrop, self._model.CanDropRole)
            
            # Remove the original item
            self._model.removeRow(sourceIndex)
            
            # Adjust target index if needed (when moving down)
            actualTargetIndex = targetIndex
            if sourceIndex < targetIndex:
                actualTargetIndex -= 1
                
            # Insert at the new position
            self._model.insertRow(actualTargetIndex, newItem)
            
            # Emit signal
            self.itemMoved.emit(sourceIndex, targetIndex)
            
            print(f"Moved item from index {sourceIndex} to {targetIndex}")
            return True
            
        except Exception as e:
            print(f"Error moving item: {e}")
            return False