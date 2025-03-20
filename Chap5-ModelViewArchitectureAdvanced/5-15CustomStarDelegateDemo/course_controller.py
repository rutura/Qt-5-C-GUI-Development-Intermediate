from PySide6.QtCore import QObject, Slot, Signal, QAbstractTableModel, Qt, QModelIndex

class CourseModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Initialize data
        self.courses = [
            {"title": "Beginning Qt C++ GUI Development", "category": "Qt C++ GUI", "rating": 2},
            {"title": "Qt Quick and QML For Beginners", "category": "QML", "rating": 5},
            {"title": "Qt Quick and QML Intermediate", "category": "QML", "rating": 4},
            {"title": "Qt Quick and QML Advanced", "category": "QML", "rating": 4},
            {"title": "Qt 5 C++ GUI Intermediate", "category": "Qt C++ GUI", "rating": 1},
            {"title": "Qt 5 C++ GUI Advanced", "category": "Qt C++ GUI", "rating": 5}
        ]
        
        # Define column roles for QML
        self.TitleRole = Qt.UserRole + 1
        self.CategoryRole = Qt.UserRole + 2
        self.RatingRole = Qt.UserRole + 3
    
    def rowCount(self, parent=QModelIndex()):
        if parent.isValid():
            return 0
        return len(self.courses)
    
    def columnCount(self, parent=QModelIndex()):
        if parent.isValid():
            return 0
        return 3
    
    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        
        row = index.row()
        col = index.column()
        
        if row < 0 or row >= len(self.courses):
            return None
        
        course = self.courses[row]
        
        if role == Qt.DisplayRole or role == Qt.EditRole:
            if col == 0:
                return course["title"]
            elif col == 1:
                return course["category"]
            elif col == 2:
                return course["rating"]
        
        elif role == self.TitleRole:
            return course["title"]
        elif role == self.CategoryRole:
            return course["category"]
        elif role == self.RatingRole:
            return course["rating"]
        
        return None
    
    def setData(self, index, value, role=Qt.EditRole):
        if not index.isValid():
            return False
        
        row = index.row()
        col = index.column()
        
        if row < 0 or row >= len(self.courses):
            return False
        
        if role == Qt.EditRole:
            if col == 0:
                self.courses[row]["title"] = value
            elif col == 1:
                self.courses[row]["category"] = value
            elif col == 2:
                # Ensure rating is an integer
                try:
                    self.courses[row]["rating"] = int(value)
                except (ValueError, TypeError):
                    return False
            else:
                return False
            
            self.dataChanged.emit(index, index)
            return True
        
        return False
    
    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return None
        
        if orientation == Qt.Horizontal:
            if section == 0:
                return "Course Title"
            elif section == 1:
                return "Category"
            elif section == 2:
                return "Rating"
        
        return None
    
    def flags(self, index):
        if not index.isValid():
            return Qt.NoItemFlags
        
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable
    
    def roleNames(self):
        roles = {
            self.TitleRole: b"title",
            self.CategoryRole: b"category",
            self.RatingRole: b"rating"
        }
        return roles

class CourseController(QObject):
    ratingChanged = Signal(int, int)  # row, new rating
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.model = CourseModel(self)
    
    @Slot(int, int)
    def updateRating(self, row, rating):
        """Update the rating for a course"""
        if 0 <= row < self.model.rowCount() and 0 <= rating <= 5:
            index = self.model.index(row, 2)
            self.model.setData(index, rating)
            self.ratingChanged.emit(row, rating)
            return True
        return False