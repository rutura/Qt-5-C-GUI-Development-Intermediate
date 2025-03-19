from PySide6.QtCore import (
    QAbstractListModel, QModelIndex, Qt, QMimeData
)

class PersonModel(QAbstractListModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._persons = [
            "Donald Bush", 
            "Xi Jing Tao", 
            "Vladmir Golbathev", 
            "Emmanuel Mitterand", 
            "Jacob Mandela"
        ]

    def rowCount(self, parent=QModelIndex()):
        """Return the number of rows in the model."""
        return len(self._persons)

    def data(self, index, role=Qt.DisplayRole):
        """Provide data for the given index and role."""
        if not index.isValid():
            return None

        if index.row() < 0 or index.row() >= len(self._persons):
            return None

        if role in (Qt.DisplayRole, Qt.EditRole):
            return self._persons[index.row()]

        return None

    def setData(self, index, value, role=Qt.EditRole):
        """Update data for a given index."""
        if role == Qt.EditRole and index.isValid():
            self._persons[index.row()] = str(value)
            self.dataChanged.emit(index, index)
            return True
        return False

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        """Provide header data."""
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return "Names" if section == 0 else None
        return None

    def insertRows(self, row, count=1, parent=QModelIndex()):
        """Insert rows into the model."""
        self.beginInsertRows(parent, row, row + count - 1)
        for _ in range(count):
            self._persons.insert(row, "")
        self.endInsertRows()
        return True

    def removeRows(self, row, count=1, parent=QModelIndex()):
        """Remove rows from the model."""
        self.beginRemoveRows(parent, row, row + count - 1)
        del self._persons[row:row+count]
        self.endRemoveRows()
        return True

    def mimeTypes(self):
        """Define supported MIME types."""
        return super().mimeTypes() + ["plain/text"]

    def mimeData(self, indexes):
        """Create MIME data for drag operations."""
        mime_data = super().mimeData(indexes)
        text_data = ",".join(str(index.data()) for index in indexes)
        mime_data.setText(text_data)
        return mime_data

    def dropMimeData(self, data, action, row, column, parent):
        """Handle drop operations."""
        if isinstance(data, dict) and "text" in data:
            # For QML integration
            text = data["text"]
        elif hasattr(data, "hasText") and data.hasText():
            # For Qt Widgets
            text = data.text()
        else:
            return False

        if parent.isValid():
            # Overwrite existing item
            self.setData(parent, text)
        else:
            # Add new item at the end
            self.insertRows(self.rowCount())
            self.setData(self.index(self.rowCount() - 1), text)

        return True

    def flags(self, index):
        """Define item flags for drag and drop."""
        if not index.isValid():
            return Qt.ItemIsEnabled | Qt.ItemIsDropEnabled

        return (super().flags(index) | 
                Qt.ItemIsEditable | 
                Qt.ItemIsDragEnabled | 
                Qt.ItemIsDropEnabled)
                
    def roleNames(self):
        """Define role names for QML."""
        return {Qt.DisplayRole: b"display"}