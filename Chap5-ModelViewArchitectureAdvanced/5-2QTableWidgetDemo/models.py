from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex, Slot, Signal, Property, QObject

class Person:
    """Model class representing a person's data"""
    def __init__(self, first_name, last_name, age, profession, marital_status, country, city, social_score):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.profession = profession
        self.marital_status = marital_status
        self.country = country
        self.city = city
        self.social_score = social_score

class PersonModel(QAbstractTableModel):
    """Table model for displaying person data in Qt widgets"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._people = []
        self._headers = ["First Name", "Last Name", "Age", "Profession", "Marital Status", 
                        "Country", "City", "Social Score"]
        self.load_sample_data()
    
    def load_sample_data(self):
        """Load sample data for demonstration"""
        sample_data = [
            ["John", "Doe", "32", "Farmer", "Single", "Gounduana", "Mestkv", "89"],
            ["Mary", "Jane", "27", "Teacher", "Married", "Verkso", "Tukk", "55"],
            ["John", "Doe", "32", "Farmer", "Single", "Gounduana", "Mestkv", "67"],
            ["Mary", "Jane", "27", "Teacher", "Married", "Verkso", "Tukk", "78"],
            ["John", "Doe", "32", "Farmer", "Single", "Gounduana", "Mestkv", "51"],
            ["Mary", "Jane", "27", "Teacher", "Married", "Verkso", "Tukk", "83"],
            ["John", "Doe", "32", "Farmer", "Single", "Gounduana", "Mestkv", "59"],
            ["Mary", "Jane", "27", "Teacher", "Married", "Verkso", "Tukk", "62"],
            ["John", "Doe", "32", "Farmer", "Single", "Gounduana", "Mestkv", "69"],
            ["Mary", "Jane", "27", "Teacher", "Married", "Verkso", "Tukk", "58"],
            ["John", "Doe", "32", "Farmer", "Single", "Gounduana", "Mestkv", "73"],
            ["Mary", "Jane", "27", "Teacher", "Married", "Verkso", "Tukk", "83"],
            ["John", "Doe", "32", "Farmer", "Single", "Gounduana", "Mestkv", "71"],
            ["Mary", "Jane", "27", "Teacher", "Married", "Verkso", "Tukk", "65"],
            ["John", "Doe", "32", "Farmer", "Single", "Gounduana", "Mestkv", "77"],
            ["Mary", "Jane", "27", "Teacher", "Married", "Verkso", "Tukk", "64"],
            ["John", "Doe", "32", "Farmer", "Single", "Gounduana", "Mestkv", "88"],
            ["Mary", "Jane", "27", "Teacher", "Married", "Verkso", "Tukk", "86"],
            ["John", "Doe", "32", "Farmer", "Single", "Gounduana", "Mestkv", "58"],
            ["Mary", "Jane", "27", "Teacher", "Married", "Verkso", "Tukk", "72"]
        ]
        
        for row in sample_data:
            person = Person(*row)
            self._people.append(person)
    
    def rowCount(self, parent=QModelIndex()):
        """Return number of rows in model"""
        return len(self._people)
    
    def columnCount(self, parent=QModelIndex()):
        """Return number of columns in model"""
        return len(self._headers)
    
    def data(self, index, role=Qt.DisplayRole):
        """Return data for given index and role"""
        if not index.isValid():
            return None
        
        if role == Qt.DisplayRole or role == Qt.EditRole:
            person = self._people[index.row()]
            if index.column() == 0:
                return person.first_name
            elif index.column() == 1:
                return person.last_name
            elif index.column() == 2:
                return person.age
            elif index.column() == 3:
                return person.profession
            elif index.column() == 4:
                return person.marital_status
            elif index.column() == 5:
                return person.country
            elif index.column() == 6:
                return person.city
            elif index.column() == 7:
                return person.social_score
        
        elif role == Qt.TextAlignmentRole:
            return Qt.AlignRight | Qt.AlignVCenter
        
        return None
    
    def headerData(self, section, orientation, role=Qt.DisplayRole):
        """Return header data for the given section, orientation and role"""
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            if 0 <= section < len(self._headers):
                return self._headers[section]
        
        return None


class PersonListModel(QObject):
    """List model for displaying person data in Qt Quick"""
    
    dataChanged = Signal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._people = []
        self.load_sample_data()
    
    def load_sample_data(self):
        """Load sample data for demonstration"""
        sample_data = [
            ["John", "Doe", "32", "Farmer", "Single", "Gounduana", "Mestkv", "89"],
            ["Mary", "Jane", "27", "Teacher", "Married", "Verkso", "Tukk", "55"],
            ["John", "Doe", "32", "Farmer", "Single", "Gounduana", "Mestkv", "67"],
            ["Mary", "Jane", "27", "Teacher", "Married", "Verkso", "Tukk", "78"],
            ["John", "Doe", "32", "Farmer", "Single", "Gounduana", "Mestkv", "51"],
            ["Mary", "Jane", "27", "Teacher", "Married", "Verkso", "Tukk", "83"],
            ["John", "Doe", "32", "Farmer", "Single", "Gounduana", "Mestkv", "59"],
            ["Mary", "Jane", "27", "Teacher", "Married", "Verkso", "Tukk", "62"],
            ["John", "Doe", "32", "Farmer", "Single", "Gounduana", "Mestkv", "69"],
            ["Mary", "Jane", "27", "Teacher", "Married", "Verkso", "Tukk", "58"],
            ["John", "Doe", "32", "Farmer", "Single", "Gounduana", "Mestkv", "73"],
            ["Mary", "Jane", "27", "Teacher", "Married", "Verkso", "Tukk", "83"],
            ["John", "Doe", "32", "Farmer", "Single", "Gounduana", "Mestkv", "71"],
            ["Mary", "Jane", "27", "Teacher", "Married", "Verkso", "Tukk", "65"],
            ["John", "Doe", "32", "Farmer", "Single", "Gounduana", "Mestkv", "77"],
            ["Mary", "Jane", "27", "Teacher", "Married", "Verkso", "Tukk", "64"],
            ["John", "Doe", "32", "Farmer", "Single", "Gounduana", "Mestkv", "88"],
            ["Mary", "Jane", "27", "Teacher", "Married", "Verkso", "Tukk", "86"],
            ["John", "Doe", "32", "Farmer", "Single", "Gounduana", "Mestkv", "58"],
            ["Mary", "Jane", "27", "Teacher", "Married", "Verkso", "Tukk", "72"]
        ]
        
        for row in sample_data:
            person = {
                "firstName": row[0],
                "lastName": row[1],
                "age": row[2],
                "profession": row[3],
                "maritalStatus": row[4],
                "country": row[5],
                "city": row[6],
                "socialScore": row[7]
            }
            self._people.append(person)
    
    @Property(list)
    def people(self):
        """Return list of people for QML"""
        return self._people
    
    @Slot(int, result=dict)
    def getPerson(self, index):
        """Return person at specified index"""
        if 0 <= index < len(self._people):
            return self._people[index]
        return {}
    
    @Property(int)
    def count(self):
        """Return number of people in model"""
        return len(self._people)