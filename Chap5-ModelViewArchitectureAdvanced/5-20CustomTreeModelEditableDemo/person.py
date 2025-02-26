from typing import List, Optional

class Person:
    def __init__(self, data: List[str] = None, parent: Optional['Person'] = None):
        """
        Initialize a Person object with optional data and parent
        
        :param data: List of column data for the person
        :param parent: Parent Person object
        """
        self._column_fields = data or []
        self._parent = parent
        self._children: List[Person] = []

    def append_child(self, child: 'Person'):
        """
        Add a child to this person's list of children
        
        :param child: Child Person object
        """
        self._children.append(child)

    def child(self, row: int) -> Optional['Person']:
        """
        Get a child at a specific row
        
        :param row: Index of the child
        :return: Child Person object or None
        """
        if 0 <= row < len(self._children):
            return self._children[row]
        return None

    def child_count(self) -> int:
        """
        Get the number of children
        
        :return: Number of children
        """
        return len(self._children)

    def column_count(self) -> int:
        """
        Get the number of columns
        
        :return: Number of columns
        """
        return len(self._column_fields)

    def data(self, column: int) -> str:
        """
        Get data for a specific column
        
        :param column: Column index
        :return: Data for the specified column
        """
        if 0 <= column < len(self._column_fields):
            return self._column_fields[column]
        return ""

    def parent_person(self) -> Optional['Person']:
        """
        Get the parent of this person
        
        :return: Parent Person object
        """
        return self._parent

    def row(self) -> int:
        """
        Get the row of this person in its parent's children list
        
        :return: Row index or 0 if no parent
        """
        if self._parent:
            return self._parent._children.index(self)
        return 0

    def set_data(self, column: int, value: str) -> bool:
        """
        Set data for a specific column
        
        :param column: Column index
        :param value: New value for the column
        :return: True if successful, False otherwise
        """
        if 0 <= column < len(self._column_fields):
            self._column_fields[column] = value
            return True
        return False

    def insert_children(self, position: int, count: int, columns: int) -> bool:
        """
        Insert new children at a specific position
        
        :param position: Position to insert children
        :param count: Number of children to insert
        :param columns: Number of columns for each child
        :return: True if successful, False otherwise
        """
        if position < 0 or position > len(self._children):
            return False

        for _ in range(count):
            child = Person([""]*columns, self)
            self._children.insert(position, child)

        return True

    def insert_columns(self, position: int, columns: int) -> bool:
        """
        Insert new columns
        
        :param position: Position to insert columns
        :param columns: Number of columns to insert
        :return: True if successful, False otherwise
        """
        if position < 0 or position > len(self._column_fields):
            return False

        for _ in range(columns):
            self._column_fields.insert(position, "")

        for child in self._children:
            child.insert_columns(position, columns)

        return True

    def remove_children(self, position: int, count: int) -> bool:
        """
        Remove children at a specific position
        
        :param position: Position to start removing children
        :param count: Number of children to remove
        :return: True if successful, False otherwise
        """
        if position < 0 or position + count > len(self._children):
            return False

        del self._children[position:position+count]
        return True

    def remove_columns(self, position: int, columns: int) -> bool:
        """
        Remove columns
        
        :param position: Position to start removing columns
        :param columns: Number of columns to remove
        :return: True if successful, False otherwise
        """
        if position < 0 or position + columns > len(self._column_fields):
            return False

        del self._column_fields[position:position+columns]

        for child in self._children:
            child.remove_columns(position, columns)

        return True

    def show_info(self, indent: int = 0):
        """
        Recursively print information about this person and their descendants
        
        :param indent: Indentation level for printing
        """
        print('  ' * indent + f"{' | '.join(self._column_fields)} - {self.child_count()} children")
        for child in self._children:
            child.show_info(indent + 1)