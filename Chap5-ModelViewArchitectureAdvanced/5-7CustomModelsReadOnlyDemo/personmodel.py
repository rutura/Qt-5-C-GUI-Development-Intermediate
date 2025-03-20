from PySide6.QtCore import QAbstractListModel, Qt, QModelIndex, QByteArray
from person import Person

class PersonModel(QAbstractListModel):
    # Define custom roles
    NameRole = Qt.UserRole + 1
    ColorRole = Qt.UserRole + 2
    AgeRole = Qt.UserRole + 3
    
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
        
        # Connect to each person's signals to emit dataChanged
        for i, person in enumerate(self.persons):
            person.namesChanged.connect(lambda name, row=i: self._on_person_data_changed(row))
            person.favoriteColorChanged.connect(lambda color, row=i: self._on_person_data_changed(row))
            person.ageChanged.connect(lambda age, row=i: self._on_person_data_changed(row))
    
    def _on_person_data_changed(self, row):
        """Handle when a person's data changes"""
        index = self.index(row, 0)
        self.dataChanged.emit(index, index)
    
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
        
        if role == self.NameRole:
            return person.names()
            
        if role == self.ColorRole:
            return person.favoriteColor()
            
        if role == self.AgeRole:
            return person.age()
            
        return None
    
    def roleNames(self):
        """Return the role names for QML"""
        roles = {
            self.NameRole: QByteArray(b"name"),
            self.ColorRole: QByteArray(b"favoriteColor"),
            self.AgeRole: QByteArray(b"age")
        }
        return roles