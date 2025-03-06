from PySide6.QtCore import QAbstractListModel, Qt, QModelIndex
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