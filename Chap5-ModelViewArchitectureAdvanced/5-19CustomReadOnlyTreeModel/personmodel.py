import os
from PySide6.QtCore import QAbstractItemModel, QModelIndex, Qt, QByteArray
from person import Person
import resources_rc

class PersonModel(QAbstractItemModel):
    def __init__(self, parent=None):
        """
        Initialize the PersonModel with a root person
        
        :param parent: Parent QObject
        """
        super().__init__(parent)
        self.root_person = Person("Names", "Profession")
        self.filename = ":/data/familytree1.txt"
        self.read_file()
        
        # For Qt Quick TreeView, expose role names
        self._role_names = {
            Qt.DisplayRole: QByteArray(b'display'),
            Qt.UserRole: QByteArray(b'profession')
        }

    def roleNames(self):
        """
        Override roleNames to provide mapping for QML
        
        :return: Dictionary of role names
        """
        return self._role_names

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
        return 2

    def data(self, index, role=Qt.DisplayRole):
        """
        Get data for a given index and role
        
        :param index: Model index
        :param role: Display role
        :return: Data for the specified index and role
        """
        if not index.isValid():
            return None

        person = index.internalPointer()
        
        if role == Qt.DisplayRole and index.column() == 0:
            return person.data(0)
        elif role == Qt.UserRole or (role == Qt.DisplayRole and index.column() == 1):
            return person.data(1)
            
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
            return "Name" if section == 0 else "Profession"
        return None

    def flags(self, index):
        """
        Get item flags for a given index
        
        :param index: Model index
        :return: Item flags
        """
        if not index.isValid():
            return Qt.NoItemFlags
        return super().flags(index)

    def read_file(self):
        """
        Read and parse the family tree file
        Parse the indentation-based hierarchical text file
        """
        last_indentation = 0
        last_parent = self.root_person
        last_person = None

        # Use QFile for resource file
        from PySide6.QtCore import QFile, QIODevice, QTextStream
        file = QFile(self.filename)
        
        if file.open(QIODevice.ReadOnly | QIODevice.Text):
            text_stream = QTextStream(file)
            
            while not text_stream.atEnd():
                line = text_stream.readLine()
                
                current_indentation = line.count('\t')
                names, profession = self.parse_line(line.strip())

                diff_indent = current_indentation - last_indentation

                if diff_indent == 0:
                    # Sibling level
                    person = Person(names, profession, last_parent)
                    last_parent.append_child(person)
                    last_person = person
                elif diff_indent > 0:
                    # Child level
                    last_parent = last_person
                    person = Person(names, profession, last_parent)
                    last_parent.append_child(person)
                    last_person = person
                else:
                    # Move up the parent chain
                    iterations = -diff_indent
                    for _ in range(iterations):
                        last_parent = last_parent.parent_person()
                    
                    person = Person(names, profession, last_parent)
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