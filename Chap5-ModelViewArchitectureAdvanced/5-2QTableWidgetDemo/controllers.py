from PySide6.QtCore import QObject, Slot, Signal, Property

class Controller(QObject):
    """Controller class implementing MVC pattern
    
    This acts as the bridge between model and view in both widget and QML interfaces.
    """
    
    # Signals for view notifications
    dataChanged = Signal()
    
    def __init__(self, model=None, parent=None):
        super().__init__(parent)
        self._model = model
    
    def set_model(self, model):
        """Set the model for this controller"""
        self._model = model
    
    @Slot(int, str, str)
    def update_person(self, row, field, value):
        """Update a person's data in the model"""
        if not self._model or row < 0 or row >= self._model.count:
            return False
        
        # In a real app, you would update the model here
        # This is just a placeholder implementation
        print(f"Updating person at row {row}, field: {field}, value: {value}")
        
        # Signal that data has changed
        self.dataChanged.emit()
        return True
    
    @Slot(str, str, str, str, str, str, str, str)
    def add_person(self, first_name, last_name, age, profession, marital_status, country, city, social_score):
        """Add a new person to the model"""
        if not self._model:
            return False
            
        # In a real app, you would add to the model here
        # This is just a placeholder implementation
        print(f"Adding new person: {first_name} {last_name}")
        
        # Signal that data has changed
        self.dataChanged.emit()
        return True
    
    @Slot(int)
    def remove_person(self, row):
        """Remove a person from the model"""
        if not self._model or row < 0 or row >= self._model.count:
            return False
            
        # In a real app, you would remove from the model here
        # This is just a placeholder implementation
        print(f"Removing person at row {row}")
        
        # Signal that data has changed
        self.dataChanged.emit()
        return True