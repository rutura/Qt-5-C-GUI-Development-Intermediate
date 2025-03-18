from PySide6.QtCore import QObject, Slot, Signal, Property, QAbstractListModel, Qt, QModelIndex, QByteArray

class FruitModel(QAbstractListModel):
    NameRole = Qt.UserRole + 1
    IconSourceRole = Qt.UserRole + 2
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Define fruit list
        self._fruit_list = [
            {"name": "Apple", "iconSource": "qrc:/images/apple.png"},
            {"name": "Avocado", "iconSource": "qrc:/images/avocado.png"},
            {"name": "Banana", "iconSource": "qrc:/images/banana.png"},
            {"name": "Blueberries", "iconSource": "qrc:/images/blueberries.png"},
            {"name": "Cucumber", "iconSource": "qrc:/images/cucumber.png"},
            {"name": "EggFruit", "iconSource": "qrc:/images/eggfruit.png"},
            {"name": "Fig", "iconSource": "qrc:/images/fig.png"},
            {"name": "Grape", "iconSource": "qrc:/images/grape.png"},
            {"name": "Mango", "iconSource": "qrc:/images/mango.png"},
            {"name": "Pear", "iconSource": "qrc:/images/pear.png"},
            {"name": "Pineapple", "iconSource": "qrc:/images/pineapple.png"},
            {"name": "Watermellon", "iconSource": "qrc:/images/watermellon.png"}
        ]
    
    def rowCount(self, parent=QModelIndex()):
        return len(self._fruit_list)
    
    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or index.row() >= len(self._fruit_list):
            return None
        
        fruit = self._fruit_list[index.row()]
        
        if role == self.NameRole:
            # Return the normal name for internal use
            return fruit["name"]
        elif role == Qt.DisplayRole:
            # Return a "funny" name for display
            return f"{fruit['name']}Funny"
        elif role == self.IconSourceRole:
            return fruit["iconSource"]
        
        return None
    
    def roleNames(self):
        roles = super().roleNames()
        roles[self.NameRole] = QByteArray(b"name")
        roles[self.IconSourceRole] = QByteArray(b"iconSource")
        return roles


class FruitController(QObject):
    selectedFruitChanged = Signal()
    
    def __init__(self, model, parent=None):
        super().__init__(parent)
        self._fruit_model = model
        self._selected_index = -1
        self._selected_fruit = ""
    
    @Property(int, notify=selectedFruitChanged)
    def selectedIndex(self):
        return self._selected_index
    
    @selectedIndex.setter
    def selectedIndex(self, index):
        if self._selected_index != index:
            self._selected_index = index
            if 0 <= index < self._fruit_model.rowCount():
                self._selected_fruit = self._fruit_model.data(
                    self._fruit_model.index(index, 0), 
                    Qt.DisplayRole
                )
            else:
                self._selected_fruit = ""
            self.selectedFruitChanged.emit()
    
    @Property(str, notify=selectedFruitChanged)
    def selectedFruit(self):
        return self._selected_fruit
    
    @Slot(result=str)
    def readData(self):
        """Read the currently selected fruit data"""
        if self._selected_index >= 0:
            fruit = self._selected_fruit
            print(f"Current fruit: {fruit}")
            print(f"Current index: {self._selected_index}")
            return f"Selected: {fruit} (index: {self._selected_index})"
        else:
            print("No fruit selected")
            return "No fruit selected"