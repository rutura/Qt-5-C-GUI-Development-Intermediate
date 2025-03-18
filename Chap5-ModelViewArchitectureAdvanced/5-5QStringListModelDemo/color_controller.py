from PySide6.QtCore import QObject, Slot, Signal, QModelIndex

class ColorController(QObject):
    """Controller for color selection
    
    Acts as an intermediary between the color model and views
    """
    
    # Signal when a color is selected
    colorSelected = Signal(str)
    
    def __init__(self, model=None, parent=None):
        super().__init__(parent)
        self._model = model
    
    def set_model(self, model):
        """Set the model for this controller"""
        self._model = model
    
    @Slot(int)
    def selectColor(self, index):
        """Select a color by index"""
        if self._model and index >= 0 and index < self._model.rowCount():
            color_name = self._model.data(self._model.index(index, 0), 0)  # DisplayRole is 0
            self.colorSelected.emit(color_name)
            print(f"Selected color: {color_name}")
            return color_name
        return ""
    
    @Slot(QModelIndex)
    def selectColorByIndex(self, index):
        """Select a color by QModelIndex (for Qt Widgets)"""
        if self._model and index.isValid():
            color_name = self._model.data(index, 0)  # DisplayRole is 0
            self.colorSelected.emit(color_name)
            print(f"Selected color: {color_name}")
            return color_name
        return ""