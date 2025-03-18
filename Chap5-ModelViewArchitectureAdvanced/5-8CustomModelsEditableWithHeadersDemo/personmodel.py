from PySide6.QtCore import QAbstractListModel, Qt, QModelIndex, QByteArray
from person import Person
import weakref

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
    
    def __del__(self):
        # Clean up Person objects
        # Using a safer approach to avoid accessing already deleted objects
        if hasattr(self, 'persons'):
            for person in self.persons:
                try:
                    if person is not None and not person.isDestroyed():
                        person.deleteLater()
                except (RuntimeError, ReferenceError):
                    # Object already deleted or reference lost, skip it
                    pass
    
    def _on_person_data_changed(self, row):
        """Handle when a person's data changes"""
        index = self.index(row, 0)
        self.dataChanged.emit(index, index)
    
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
        
        if role == self.NameRole:
            return person.names()
            
        if role == self.ColorRole:
            return person.favoriteColor()
            
        if role == self.AgeRole:
            return person.age()
            
        return None
    
    def setData(self, index, value, role=Qt.EditRole):
        """Set data for the specified index and role"""
        if not index.isValid() or index.row() < 0 or index.row() >= len(self.persons):
            return False
        
        person = self.persons[index.row()]
        something_changed = False
        
        if role == Qt.EditRole or role == self.NameRole:
            if person.names() != value:
                person.setNames(value)
                something_changed = True
        
        if role == self.ColorRole:
            if person.favoriteColor() != value:
                person.setFavoriteColor(value)
                something_changed = True
        
        if role == self.AgeRole:
            if person.age() != value:
                person.setAge(value)
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
    
    def roleNames(self):
        """Return the role names for QML"""
        roles = {
            self.NameRole: QByteArray(b"name"),
            self.ColorRole: QByteArray(b"favoriteColor"),
            self.AgeRole: QByteArray(b"age"),
            Qt.EditRole: QByteArray(b"edit")
        }
        return roles