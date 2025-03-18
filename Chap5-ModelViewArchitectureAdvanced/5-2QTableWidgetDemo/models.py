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

class PersonTableModel(QAbstractTableModel):
    """Table model for Qt Quick TableView"""
    
    # Define roles for QML
    FirstNameRole = Qt.UserRole + 1
    LastNameRole = Qt.UserRole + 2
    AgeRole = Qt.UserRole + 3
    ProfessionRole = Qt.UserRole + 4
    MaritalStatusRole = Qt.UserRole + 5
    CountryRole = Qt.UserRole + 6
    CityRole = Qt.UserRole + 7
    SocialScoreRole = Qt.UserRole + 8
    
    # Signal for notifying data changes
    dataChanged = Signal()
    
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
    
    def roleNames(self):
        """Return the role names for QML"""
        roles = {
            self.FirstNameRole: b"firstName",
            self.LastNameRole: b"lastName",
            self.AgeRole: b"age",
            self.ProfessionRole: b"profession",
            self.MaritalStatusRole: b"maritalStatus",
            self.CountryRole: b"country",
            self.CityRole: b"city",
            self.SocialScoreRole: b"socialScore"
        }
        return roles
    
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
            
        row = index.row()
        if row < 0 or row >= len(self._people):
            return None
            
        if role == Qt.DisplayRole or role == Qt.EditRole:
            column = index.column()
            person = self._people[row]
            
            if column == 0:
                return person["firstName"]
            elif column == 1:
                return person["lastName"]
            elif column == 2:
                return person["age"]
            elif column == 3:
                return person["profession"]
            elif column == 4:
                return person["maritalStatus"]
            elif column == 5:
                return person["country"]
            elif column == 6:
                return person["city"]
            elif column == 7:
                return person["socialScore"]
        
        elif role == self.FirstNameRole:
            return self._people[row]["firstName"]
        elif role == self.LastNameRole:
            return self._people[row]["lastName"]
        elif role == self.AgeRole:
            return self._people[row]["age"]
        elif role == self.ProfessionRole:
            return self._people[row]["profession"]
        elif role == self.MaritalStatusRole:
            return self._people[row]["maritalStatus"]
        elif role == self.CountryRole:
            return self._people[row]["country"]
        elif role == self.CityRole:
            return self._people[row]["city"]
        elif role == self.SocialScoreRole:
            return self._people[row]["socialScore"]
        
        elif role == Qt.TextAlignmentRole:
            return int(Qt.AlignRight | Qt.AlignVCenter)
        
        return None
    
    def headerData(self, section, orientation, role=Qt.DisplayRole):
        """Return header data for the given section, orientation and role"""
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            if 0 <= section < len(self._headers):
                return self._headers[section]
        
        return None
    
    @Slot(int, int, result=str)
    def getPersonDataAt(self, row, column):
        """Get data at specific row and column - utility method for QML"""
        if row < 0 or row >= len(self._people) or column < 0 or column >= len(self._headers):
            return ""
        
        index = self.index(row, column)
        result = self.data(index, Qt.DisplayRole)
        return str(result) if result is not None else ""
    
    @Slot(int, result=str)
    def getPersonName(self, row):
        """Get person's full name for the status bar"""
        if row < 0 or row >= len(self._people):
            return ""
        
        firstName = self.getPersonDataAt(row, 0)
        lastName = self.getPersonDataAt(row, 1)
        return f"{firstName} {lastName}"
    
    @Property(int)
    def count(self):
        """Return number of people in model"""
        return len(self._people)