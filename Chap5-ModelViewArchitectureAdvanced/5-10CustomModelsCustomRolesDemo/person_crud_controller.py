from PySide6.QtCore import QObject, Slot, Signal, QModelIndex

class PersonCrudController(QObject):
    """Controller for person data with CRUD operations
    
    Acts as an intermediary between the person model and QML views
    """
    
    # Signal when a person is selected
    personSelected = Signal(int, str, str, int)  # index, name, favorite color, age
    
    # Signal when a person is added
    personAdded = Signal(str)  # name
    
    # Signal when a person is removed
    personRemoved = Signal(int)  # index
    
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
    
    @Slot(str, int)
    def addPerson(self, name, age):
        """Add a new person with the specified name and age"""
        if self._model:
            from person import Person
            color = "blue"  # Default color
            person = Person(name, color, age)
            self._model.addPerson(person)
            self.personAdded.emit(name)
            print(f"Added person: {name}, age: {age}")
            return True
        return False
    
    @Slot(str, str, int)
    def addPersonWithColor(self, name, color, age):
        """Add a new person with the specified name, color, and age"""
        if self._model:
            from person import Person
            person = Person(name, color, age)
            self._model.addPerson(person)
            self.personAdded.emit(name)
            print(f"Added person: {name}, color: {color}, age: {age}")
            return True
        return False
    
    @Slot()
    def addDefaultPerson(self):
        """Add a person with default values"""
        if self._model:
            self._model.addPersonDefault()
            self.personAdded.emit("Added Person")
            print("Added default person")
            return True
        return False
    
    @Slot(int)
    def removePerson(self, index):
        """Remove a person at the given index"""
        if self._model and index >= 0 and index < self._model.rowCount():
            model_index = self._model.index(index, 0)
            self._model.removePerson(model_index)
            self.personRemoved.emit(index)
            print(f"Removed person at index: {index}")
            return True
        return False