from PySide6.QtCore import QObject, Slot, Signal, QModelIndex, QSortFilterProxyModel

class ColorFilterController(QObject):
    """Controller for color selection and filtering
    
    Acts as an intermediary between the color model, proxy model and views
    """
    
    # Signal when a color is selected
    colorSelected = Signal(str)
    
    def __init__(self, model=None, proxy_model=None, parent=None):
        super().__init__(parent)
        self._model = model
        self._proxy_model = proxy_model
        
    def set_model(self, model):
        """Set the model for this controller"""
        self._model = model
        
        # If we have a proxy model, update its source model
        if self._proxy_model:
            self._proxy_model.setSourceModel(self._model)
    
    def set_proxy_model(self, proxy_model):
        """Set the proxy model for this controller"""
        self._proxy_model = proxy_model
        
        # If we have a model, set it as the source for the proxy
        if self._model:
            self._proxy_model.setSourceModel(self._model)
    
    @Slot(int)
    def selectColor(self, index):
        """Select a color by index (using the proxy model)"""
        if self._proxy_model and index >= 0 and index < self._proxy_model.rowCount():
            color_name = self._proxy_model.data(self._proxy_model.index(index, 0), 0)
            self.colorSelected.emit(color_name)
            print(f"Selected color: {color_name}")
            return color_name
        return ""
    
    @Slot(QModelIndex)
    def selectColorByIndex(self, index):
        """Select a color by QModelIndex (for Qt Widgets, using the proxy model)"""
        if self._proxy_model and index.isValid():
            color_name = self._proxy_model.data(index, 0)
            self.colorSelected.emit(color_name)
            print(f"Selected color: {color_name}")
            return color_name
        return ""
    
    @Slot(str)
    def filterColors(self, filter_text):
        """Filter the colors by the given text"""
        if self._proxy_model:
            self._proxy_model.setFilterRegularExpression(filter_text)