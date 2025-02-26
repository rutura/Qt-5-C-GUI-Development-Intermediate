from PySide6.QtCore import QObject, Signal

class Person(QObject):
    namesChanged = Signal(str)
    favoriteColorChanged = Signal(str)
    ageChanged = Signal(int)
    
    def __init__(self, names="", favorite_color="", age=0, parent=None):
        super().__init__(parent)
        self._names = names
        self._favorite_color = favorite_color
        self._age = age
    
    def names(self):
        """Get the person's name"""
        return self._names
    
    def favoriteColor(self):
        """Get the person's favorite color"""
        return self._favorite_color
    
    def age(self):
        """Get the person's age"""
        return self._age
    
    def setNames(self, names):
        """Set the person's name"""
        if self._names == names:
            return
        
        self._names = names
        self.namesChanged.emit(self._names)
    
    def setFavoriteColor(self, favorite_color):
        """Set the person's favorite color"""
        print("Favorite color called")
        if self._favorite_color == favorite_color:
            return
        
        self._favorite_color = favorite_color
        self.favoriteColorChanged.emit(self._favorite_color)
    
    def setAge(self, age):
        """Set the person's age"""
        if self._age == age:
            return
        
        self._age = age
        self.ageChanged.emit(self._age)