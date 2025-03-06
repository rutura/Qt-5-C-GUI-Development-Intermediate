from PySide6.QtCore import QAbstractListModel, Qt
from person import Person

class PersonModel(QAbstractListModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # List to store Person objects
        self.persons = []
        
        # Populate with initial data
        self.persons.append(Person("Jamie Lannister", "red", 33))
        self.persons.append(Person("Marry Lane", "cyan", 26))
        self.persons.append(Person("Steve Moors", "yellow", 44))
        self.persons.append(Person("Victor Trunk", "dodgerblue", 30))
        self.persons.append(Person("Ariel Geeny", "blue", 33))
        self.persons.append(Person("Knut Vikran", "lightblue", 26))
    
    def __del__(self):
        # Clean up Person objects
        for person in self.persons:
            person.deleteLater()
    
    def rowCount(self, parent=None):
        """Return the number of rows in the model"""
        return len(self.persons)
    
    def data(self, index, role=Qt.DisplayRole):
        """Return data for the specified index and role"""
        if not index.isValid() or index.row() < 0 or index.row() >= len(self.persons):
            return None
        
        person = self.persons[index.row()]
        
        if role == Qt.DisplayRole:
            return f"{person.names()} {person.age()} {person.favoriteColor()}"
        
        if role == Qt.ToolTipRole:
            return f"{person.names()} {index.row()}"
            
        return None