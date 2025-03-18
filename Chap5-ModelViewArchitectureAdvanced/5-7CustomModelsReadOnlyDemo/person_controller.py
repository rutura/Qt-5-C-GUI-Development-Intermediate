from PySide6.QtCore import QObject, Slot, Signal, QModelIndex

class PersonController(QObject):
    """Controller for person data
    
    Acts as an intermediary between the person model and views
    """
    
    # Signal when a person is selected
    personSelected = Signal(int, str, str, int)  # index, name, favorite color, age
    
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
    def setPersonName(self, index, name):
        """Set the name of a person at the given index"""
        if self._model and index >= 0 and index < self._model.rowCount():
            person = self._model.persons[index]
            person.setNames(name)
            return True
        return False
    
    @Slot(int, str)
    def setPersonFavoriteColor(self, index, color):
        """Set the favorite color of a person at the given index"""
        if self._model and index >= 0 and index < self._model.rowCount():
            person = self._model.persons[index]
            person.setFavoriteColor(color)
            return True
        return False
    
    @Slot(int, int)
    def setPersonAge(self, index, age):
        """Set the age of a person at the given index"""
        if self._model and index >= 0 and index < self._model.rowCount():
            person = self._model.persons[index]
            person.setAge(age)
            return True
        return False