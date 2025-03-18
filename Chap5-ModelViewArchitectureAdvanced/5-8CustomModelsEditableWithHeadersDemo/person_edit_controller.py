from PySide6.QtCore import QObject, Slot, Signal, QModelIndex

class PersonEditController(QObject):
    """Controller for person data with editing capabilities
    
    Acts as an intermediary between the person model and views
    """
    
    # Signal when a person is selected
    personSelected = Signal(int, str, str, int)  # index, name, favorite color, age
    
    # Signal when a person is edited
    personEdited = Signal(int, str)  # index, new name
    
    def __init__(self, model=None, parent=None):
        super().__init__(parent)
        self._model = model
    
    def set_model(self, model):
        """Set the model for this controller"""
        self._model = model
    
    @Slot(int)
    def selectPerson(self, index):
        """Select a person by index"""
        if self._model and index >= 0 and index < self._model.rowCount():
            person = self._model.persons[index]
            self.personSelected.emit(
                index,
                person.names(),
                person.favoriteColor(),
                person.age()
            )
            print(f"Selected person: {person.names()}")
            return True
        return False
    
    @Slot(QModelIndex)
    def selectPersonByIndex(self, index):
        """Select a person by QModelIndex (for Qt Widgets)"""
        if self._model and index.isValid() and index.row() < self._model.rowCount():
            person = self._model.persons[index.row()]
            self.personSelected.emit(
                index.row(),
                person.names(),
                person.favoriteColor(),
                person.age()
            )
            print(f"Selected person: {person.names()}")
            return True
        return False
    
    @Slot(int, str)
    def editPersonName(self, index, name):
        """Edit a person's name by index"""
        if self._model and index >= 0 and index < self._model.rowCount():
            model_index = self._model.index(index, 0)
            success = self._model.setData(model_index, name, role=0)  # EditRole is 0
            if success:
                self.personEdited.emit(index, name)
                print(f"Edited person {index}: {name}")
            return success
        return False
    
    @Slot(QModelIndex, str)
    def editPersonByIndex(self, index, name):
        """Edit a person's name by QModelIndex (for Qt Widgets)"""
        if self._model and index.isValid() and index.row() < self._model.rowCount():
            success = self._model.setData(index, name, role=0)  # EditRole is 0
            if success:
                self.personEdited.emit(index.row(), name)
                print(f"Edited person {index.row()}: {name}")
            return success
        return False