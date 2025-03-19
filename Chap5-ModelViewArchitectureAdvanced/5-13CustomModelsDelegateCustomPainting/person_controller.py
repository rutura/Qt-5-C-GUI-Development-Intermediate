from PySide6.QtCore import QObject, Slot, Signal, QModelIndex
from PySide6.QtGui import QColor
from person import Person

class PersonController(QObject):
    """Controller for person data with CRUD operations"""
    
    personSelected = Signal(int, str, str, int)  # index, name, favorite color, age
    personAdded = Signal(str)  # name
    personRemoved = Signal(int)  # index
    
    def __init__(self, model=None, parent=None):
        super().__init__(parent)
        self._model = model
        self._colorList = QColor.colorNames()
    
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
            return True
        return False
    
    @Slot(str, int)
    def addPerson(self, name, age):
        """Add a new person with default color"""
        if self._model:
            color = "blue"
            person = Person(name, color, age, self)
            self._model.addPerson(person)
            self.personAdded.emit(name)
            return True
        return False
    
    @Slot(str, str, int)
    def addPersonWithColor(self, name, color, age):
        """Add a new person with specified color"""
        if self._model:
            person = Person(name, color, age, self)
            self._model.addPerson(person)
            self.personAdded.emit(name)
            return True
        return False
    
    @Slot(int)
    def removePerson(self, index):
        """Remove a person at the given index"""
        if self._model and index >= 0 and index < self._model.rowCount():
            model_index = self._model.index(index, 0)
            self._model.removePerson(model_index)
            self.personRemoved.emit(index)
            return True
        return False
    
    @Slot(int, str, str, int)
    def updatePerson(self, index, name, color, age):
        """Update person data"""
        if self._model and index >= 0 and index < self._model.rowCount():
            self._model.setData(self._model.index(index, 0), name)
            self._model.setData(self._model.index(index, 1), age)
            self._model.setData(self._model.index(index, 2), color)
            return True
        return False
    
    @Slot(result=list)
    def getColorList(self):
        """Get available color names"""
        return self._colorList