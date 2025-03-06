from PySide6.QtCore import QAbstractListModel, Qt, QModelIndex, QByteArray
from person import Person

class PersonModel(QAbstractListModel):
    # Define custom roles
    NamesRole = Qt.UserRole + 1
    FavoriteColorRole = Qt.UserRole + 2
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
    
    def __del__(self):
        # Clean up Person objects
        for person in self.persons:
            person.deleteLater()
    
    def addPerson(self, person):
        """Add a given person to the model using insertRows and setData"""
        self.insertRows(len(self.persons), 1)
        index = self.index(len(self.persons) - 1)
        self.setData(index, person.names(), self.NamesRole)
        self.setData(index, person.favoriteColor(), self.FavoriteColorRole)
        self.setData(index, person.age(), self.AgeRole)
    
    def addPersonDefault(self):
        """Add a person with default values"""
        person = Person("Added Person", "yellowgreen", 45, self)
        self.addPerson(person)
    
    def addPersonWithDetails(self, names, age):
        """Add a person with specified name and age"""
        person = Person(names, "yellowgreen", age)
        self.addPerson(person)
    
    def removePerson(self, index):
        """Remove a person at the given index using removeRows"""
        if not index.isValid():
            return
        
        self.removeRows(index.row(), 1)
    
    def rowCount(self, parent=None):
        """Return the number of rows in the model"""
        if parent and parent.isValid():
            return 0
        return len(self.persons)
    
    def data(self, index, role=Qt.DisplayRole):
        """Return data for the specified index and role"""
        if not index.isValid() or index.row() < 0 or index.row() >= len(self.persons):
            return None
        
        person = self.persons[index.row()]
        
        if role == Qt.DisplayRole:
            return person.names()
        
        if role == Qt.EditRole:
            print("Data method called with edit role")
            return person.names()
        
        if role == self.NamesRole:
            return person.names()
        
        if role == self.FavoriteColorRole:
            return person.favoriteColor()
        
        if role == self.AgeRole:
            return person.age()
        
        if role == Qt.ToolTipRole:
            return person.names()
        
        return None
    
    def setData(self, index, value, role=Qt.EditRole):
        """Set data for the specified index and role"""
        if not index.isValid():
            return False
        
        person = self.persons[index.row()]
        something_changed = False
        
        if role == Qt.EditRole:
            if person.names() != value:
                person.setNames(value)
                something_changed = True
        
        elif role == self.NamesRole:
            print(f"Names role changing names, index {index.row()}")
            if person.names() != value:
                person.setNames(value)
                something_changed = True
        
        elif role == self.AgeRole:
            if person.age() != value:
                person.setAge(value)
                something_changed = True
        
        elif role == self.FavoriteColorRole:
            if person.favoriteColor() != value:
                person.setFavoriteColor(value)
                something_changed = True
        
        if something_changed:
            self.dataChanged.emit(index, index)
            return True
        
        return False
    
    def headerData(self, section, orientation, role=Qt.DisplayRole):
        """Return header data for the model"""
        if role != Qt.DisplayRole:
            return None
        
        if orientation == Qt.Horizontal:
            return "Person names"
        
        # Vertical rows
        return f"Person {section}"
    
    def flags(self, index):
        """Return item flags"""
        if not index.isValid():
            return super().flags(index)
        
        return super().flags(index) | Qt.ItemIsEditable
    
    def insertRows(self, row, count, parent=QModelIndex()):
        """Insert rows into the model"""
        self.beginInsertRows(QModelIndex(), row, row + count - 1)
        
        for i in range(count):
            self.persons.insert(row, Person())
        
        self.endInsertRows()
        return True
    
    def removeRows(self, row, count, parent=QModelIndex()):
        """Remove rows from the model"""
        self.beginRemoveRows(QModelIndex(), row, row + count - 1)
        
        for i in range(count):
            self.persons.pop(row)
        
        self.endRemoveRows()
        return True
    
    def roleNames(self):
        """Return role names for QML integration"""
        roles = {}
        roles[self.NamesRole] = QByteArray(b"names")
        roles[self.FavoriteColorRole] = QByteArray(b"favoritecolor")
        roles[self.AgeRole] = QByteArray(b"age")
        return roles