from PySide6.QtCore import QObject, Slot, Signal, QModelIndex
from PySide6.QtGui import QColor
from person import Person

class PersonController(QObject):
    personUpdated = Signal(int, str, str, int, int)  # index, name, color, age, score
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._model = None
        self.colorList = QColor.colorNames()
    
    def set_model(self, model):
        """Set the model for this controller"""
        self._model = model
    
    @Slot(result=list)
    def getColorList(self):
        return self.colorList
    
    @Slot(int, str)
    def updateColor(self, row, color):
        if self._model and 0 <= row < self._model.rowCount():
            index = self._model.index(row, 2)
            self._model.setData(index, color, self._model.FavoriteColorRole)
            return True
        return False
    
    @Slot(int, int)
    def updateScore(self, row, score):
        if self._model and 0 <= row < self._model.rowCount() and 0 <= score <= 5:
            index = self._model.index(row, 3)
            self._model.setData(index, score, self._model.SocialScoreRole)
            return True
        return False
    
    @Slot(str, int, str, int)
    def addPerson(self, name, age, color, score):
        if self._model:
            person = Person(name, color, age, score, self)
            self._model.addPerson(person)
            return True
        return False
    
    @Slot(int)
    def removePerson(self, row):
        if self._model and 0 <= row < self._model.rowCount():
            index = self._model.index(row, 0)
            self._model.removePerson(index)
            return True
        return False