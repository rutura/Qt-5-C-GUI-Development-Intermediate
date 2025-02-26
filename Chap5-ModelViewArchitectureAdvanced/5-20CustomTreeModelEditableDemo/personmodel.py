from PySide6.QtCore import (
    QAbstractItemModel, QModelIndex, Qt, QFile, QIODevice, QTextStream
)
from PySide6.QtGui import QColor
from person import Person

class PersonModel(QAbstractItemModel):
    def __init__(self, parent=None):
        """
        Initialize the PersonModel with a root person
        
        :param parent: Parent QObject
        """
        super().__init__(parent)
        # Create root person with column headers
        self.root_person = Person(["Names", "Profession"])
        self.read_file()

    def get_person_from_index(self, index):
        """
        Get Person object from a model index
        
        :param index: Model index
        :return: Person object
        """
        return index.internalPointer() if index.isValid() else self.root_person

    def index(self, row, column, parent=QModelIndex()):
        """
        Create a model index for a given row and column
        
        :param row: Row of the item
        :param column: Column of the item
        :param parent: Parent model index
        :return: Model index for the specified item
        """
        if not self.hasIndex(row, column, parent):
            return QModelIndex()

        parent_person = parent.internalPointer() if parent.isValid() else self.root_person
        child_person = parent_person.child(row)

        return self.createIndex(row, column, child_person) if child_person else QModelIndex()

    def parent(self, child):
        """
        Get the parent model index for a given child index
        
        :param child: Child model index
        :return: Parent model index
        """
        if not child.isValid():
            return QModelIndex()

        child_person = child.internalPointer()
        parent_person = child_person.parent_person()

        if parent_person == self.root_person:
            return QModelIndex()

        return self.createIndex(parent_person.row(), 0, parent_person)

    def rowCount(self, parent=QModelIndex()):
        """
        Get the number of rows for a given parent
        
        :param parent: Parent model index
        :return: Number of rows
        """
        if parent.column() > 0:
            return 0

        parent_person = parent.internalPointer() if parent.isValid() else self.root_person
        return parent_person.child_count()

    def columnCount(self, parent=QModelIndex()):
        """
        Get the number of columns
        
        :param parent: Parent model index
        :return: Number of columns
        """
        return self.root_person.column_count()

    def data(self, index, role=Qt.DisplayRole):
        """
        Get data for a given index and role
        
        :param index: Model index
        :param role: Display role
        :return: Data for the specified index and role
        """
        if not index.isValid():
            return None

        if role in (Qt.DisplayRole, Qt.EditRole):
            person = index.internalPointer()
            return person.data(index.column())

        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        """
        Get header data
        
        :param section: Section number
        :param orientation: Horizontal or vertical orientation
        :param role: Display role
        :return: Header data
        """
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.root_person.data(section)
        return None

    def flags(self, index):
        """
        Get item flags for a given index
        
        :param index: Model index
        :return: Item flags
        """
        if not index.isValid():
            return Qt.NoItemFlags
        return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def setData(self, index, value, role=Qt.EditRole):
        """
        Set data for a given index
        
        :param index: Model index
        :param value: New value
        :param role: Edit role
        :return: True if successful
        """
        if role != Qt.EditRole:
            return False

        person = index.internalPointer()
        result = person.set_data(index.column(), value)

        if result:
            self.dataChanged.emit(index, index, [role])

        return result

    def insertColumns(self, position, columns, parent=QModelIndex()):
        """
        Insert columns at a specific position
        
        :param position: Position to insert columns
        :param columns: Number of columns to insert
        :param parent: Parent model index
        :return: True if successful
        """
        parent_person = parent.internalPointer() if parent.isValid() else self.root_person

        self.beginInsertColumns(parent, position, position + columns - 1)
        success = parent_person.insert_columns(position, columns)
        self.endInsertColumns()

        return success

    def removeColumns(self, position, columns, parent=QModelIndex()):
        """
        Remove columns at a specific position
        
        :param position: Position to start removing columns
        :param columns: Number of columns to remove
        :param parent: Parent model index
        :return: True if successful
        """
        parent_person = parent.internalPointer() if parent.isValid() else self.root_person

        self.beginRemoveColumns(parent, position, position + columns - 1)
        success = parent_person.remove_columns(position, columns)
        self.endRemoveColumns()

        return success

    def insertRows(self, position, rows, parent=QModelIndex()):
        """
        Insert rows at a specific position
        
        :param position: Position to insert rows
        :param rows: Number of rows to insert
        :param parent: Parent model index
        :return: True if successful
        """
        parent_person = self.get_person_from_index(parent)

        self.beginInsertRows(parent, position, position + rows - 1)
        success = parent_person.insert_children(position, rows, self.columnCount())
        self.endInsertRows()

        return success

    def removeRows(self, position, rows, parent=QModelIndex()):
        """
        Remove rows at a specific position
        
        :param position: Position to start removing rows
        :param rows: Number of rows to remove
        :param parent: Parent model index
        :return: True if successful
        """
        parent_person = self.get_person_from_index(parent)

        self.beginRemoveRows(parent, position, position + rows - 1)
        success = parent_person.remove_children(position, rows)
        self.endRemoveRows()

        return success

    def read_file(self):
        """
        Read and parse the family tree file
        Parse the indentation-based hierarchical text file
        """
        filename = ":/data/familytree1.txt"
        file = QFile(filename)
        
        if file.open(QIODevice.ReadOnly | QIODevice.Text):
            last_indentation = 0
            last_parent = self.root_person
            last_person = None

            text_stream = QTextStream(file)
            
            while not text_stream.atEnd():
                line = text_stream.readLine()
                
                current_indentation = line.count('\t')
                names, profession = self.parse_line(line.strip())

                diff_indent = current_indentation - last_indentation

                # Create a new person with [names, profession]
                person_data = [names, profession]

                if diff_indent == 0:
                    # Sibling level
                    person = Person(person_data, last_parent)
                    last_parent.append_child(person)
                    last_person = person
                elif diff_indent > 0:
                    # Child level
                    last_parent = last_person
                    person = Person(person_data, last_parent)
                    last_parent.append_child(person)
                    last_person = person
                else:
                    # Move up the parent chain
                    iterations = -diff_indent
                    for _ in range(iterations):
                        last_parent = last_parent.parent_person()
                    
                    person = Person(person_data, last_parent)
                    last_parent.append_child(person)
                    last_person = person

                last_indentation = current_indentation

            file.close()

    def parse_line(self, line):
        """
        Parse a line into names and profession
        
        :param line: Line from the input file
        :return: Tuple of (names, profession)
        """
        parts = line.split('(')
        names = parts[0].strip()
        profession = parts[1].rstrip(')').strip()
        return names, profession