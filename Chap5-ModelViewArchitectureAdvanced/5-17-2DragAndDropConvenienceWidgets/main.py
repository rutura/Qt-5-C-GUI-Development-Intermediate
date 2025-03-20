import sys
import os
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QUrl, QObject, Slot, Signal, Qt, QAbstractListModel, QAbstractTableModel, QModelIndex
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtGui import QColor

from widget import Widget

class ColorController(QObject):
    """Controller for color list drag and drop operations"""
    
    def __init__(self, model=None, parent=None):
        super().__init__(parent)
        self._model = model
    
    def set_model(self, model):
        """Set the model for this controller"""
        self._model = model
    
    @Slot(int, int)
    def moveItem(self, sourceIndex, targetIndex):
        """Move an item from source to target index"""
        if not self._model:
            return False
            
        return self._model.moveRow(sourceIndex, targetIndex)

class TableController(QObject):
    """Controller for table drag and drop operations"""
    
    def __init__(self, model=None, parent=None):
        super().__init__(parent)
        self._model = model
    
    def set_model(self, model):
        """Set the model for this controller"""
        self._model = model
    
    @Slot(int, int)
    def moveRow(self, sourceRow, targetRow):
        """Move a row from source to target"""
        if not self._model:
            return False
            
        return self._model.moveRow(sourceRow, targetRow)

class ColorListModel(QAbstractListModel):
    """Model for color names"""
    
    DisplayRole = Qt.DisplayRole
    ColorRole = Qt.UserRole
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._colors = QColor.colorNames()
    
    def rowCount(self, parent=QModelIndex()):
        if parent.isValid():
            return 0
        return len(self._colors)
    
    def data(self, index, role):
        if not index.isValid() or index.row() >= len(self._colors):
            return None
            
        if role == self.DisplayRole:
            return self._colors[index.row()]
        elif role == self.ColorRole:
            return QColor(self._colors[index.row()])
            
        return None
    
    def roleNames(self):
        """Define role names for QML access"""
        roles = super().roleNames()
        roles[self.ColorRole] = b"color"
        roles[self.DisplayRole] = b"display"
        return roles
        
    def moveRow(self, sourceRow, destinationRow):
        """Move a row from source to destination"""
        if sourceRow < 0 or sourceRow >= len(self._colors) or destinationRow < 0 or destinationRow > len(self._colors):
            return False
            
        # Skip if source and destination are the same
        if sourceRow == destinationRow:
            return True
            
        # Begin move operation
        self.beginMoveRows(QModelIndex(), sourceRow, sourceRow, QModelIndex(), 
                           destinationRow if destinationRow > sourceRow else destinationRow)
        
        # Move the color
        color = self._colors.pop(sourceRow)
        self._colors.insert(destinationRow if destinationRow < sourceRow else destinationRow - 1, color)
        
        # End move operation
        self.endMoveRows()
        return True

class PersonTableModel(QAbstractTableModel):
    """Model for person data"""
    
    # Column roles
    FirstNameRole = Qt.UserRole + 1
    LastNameRole = Qt.UserRole + 2
    AgeRole = Qt.UserRole + 3
    ProfessionRole = Qt.UserRole + 4
    MaritalStatusRole = Qt.UserRole + 5
    CountryRole = Qt.UserRole + 6
    CityRole = Qt.UserRole + 7
    SocialScoreRole = Qt.UserRole + 8
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._headers = ["First Name", "Last Name", "Age", "Profession", "Marital Status", 
                         "Country", "City", "Social Score"]
        
        # Initialize with sample data
        self._data = [
            ["John", "Doe", "32", "Farmer", "Single", "Gounduana", "Mestkv", "89"],
            ["Mary", "Jane", "27", "Teacher", "Married", "Verkso", "Tukk", "55"],
            ["Donald", "Milton", "32", "Farmer", "Single", "Gounduana", "Mestkv", "67"],
            ["Samatha", "Chan", "27", "Teacher", "Married", "Verkso", "Tukk", "78"],
            ["Andrew", "Knut", "32", "Farmer", "Single", "Gounduana", "Mestkv", "51"]
        ]
    
    def rowCount(self, parent=QModelIndex()):
        if parent.isValid():
            return 0
        return len(self._data)
    
    def columnCount(self, parent=QModelIndex()):
        if parent.isValid():
            return 0
        return len(self._headers)
    
    def data(self, index, role):
        if not index.isValid() or index.row() >= len(self._data) or index.column() >= len(self._headers):
            return None
            
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]
        elif role == Qt.ToolTipRole:
            return f"item [{index.row()},{index.column()}]"
        elif role == self.FirstNameRole:
            return self._data[index.row()][0]
        elif role == self.LastNameRole:
            return self._data[index.row()][1]
        elif role == self.AgeRole:
            return self._data[index.row()][2]
        elif role == self.ProfessionRole:
            return self._data[index.row()][3]
        elif role == self.MaritalStatusRole:
            return self._data[index.row()][4]
        elif role == self.CountryRole:
            return self._data[index.row()][5]
        elif role == self.CityRole:
            return self._data[index.row()][6]
        elif role == self.SocialScoreRole:
            return self._data[index.row()][7]
                
        return None
    
    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal and section < len(self._headers):
            return self._headers[section]
        return None
    
    def roleNames(self):
        """Define role names for QML access"""
        roles = super().roleNames()
        roles[Qt.DisplayRole] = b"display"
        roles[self.FirstNameRole] = b"firstName"
        roles[self.LastNameRole] = b"lastName"
        roles[self.AgeRole] = b"age"
        roles[self.ProfessionRole] = b"profession"
        roles[self.MaritalStatusRole] = b"maritalStatus"
        roles[self.CountryRole] = b"country"
        roles[self.CityRole] = b"city"
        roles[self.SocialScoreRole] = b"socialScore"
        return roles
        
    def moveRow(self, sourceRow, targetRow):
        """Move a row from source to target"""
        if sourceRow < 0 or sourceRow >= len(self._data) or targetRow < 0 or targetRow > len(self._data):
            return False
            
        # Skip if source and target are the same
        if sourceRow == targetRow:
            return True
            
        # Begin move operation
        self.beginMoveRows(QModelIndex(), sourceRow, sourceRow, QModelIndex(), 
                          targetRow if targetRow > sourceRow else targetRow)
        
        # Move the row
        row = self._data.pop(sourceRow)
        self._data.insert(targetRow if targetRow < sourceRow else targetRow - 1, row)
        
        # End move operation
        self.endMoveRows()
        return True

def run_widgets():
    """Run the application in Qt Widgets mode"""
    app = QApplication(sys.argv)
    window = Widget()
    window.show()
    
    return app.exec()

def run_quick():
    """Run the application in Qt Quick mode"""
    app = QApplication(sys.argv)
    
    # Create QML engine
    engine = QQmlApplicationEngine()
    
    # Create models
    colorModel = ColorListModel()
    tableModel = PersonTableModel()
    
    # Create controllers
    colorController = ColorController(colorModel)
    tableController = TableController(tableModel)
    
    # Expose models and controllers to QML
    engine.rootContext().setContextProperty("colorModel", colorModel)
    engine.rootContext().setContextProperty("tableModel", tableModel)
    engine.rootContext().setContextProperty("colorController", colorController)
    engine.rootContext().setContextProperty("tableController", tableController)
    
    # Load QML file
    qml_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dragdrop.qml")
    engine.load(QUrl.fromLocalFile(qml_file))
    
    # Check if QML loaded successfully
    if not engine.rootObjects():
        return -1
    
    return app.exec()

def main():
    """Main entry point with option to choose which version to run"""
    
    mode = input("Select mode (1 for Widgets, 2 for Quick): ")
    
    if mode == "2":
        print("Running Qt Quick version")
        return run_quick()
    else:
        print("Running Qt Widgets version")
        return run_widgets()

if __name__ == "__main__":
    sys.exit(main())