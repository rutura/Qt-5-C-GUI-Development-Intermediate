class Person:
    def __init__(self, names, profession, parent=None):
        """
        Initialize a Person object with a name, profession, and optional parent
        
        :param names: Full name of the person
        :param profession: Person's profession
        :param parent: Parent Person object
        """
        self._names = names
        self._profession = profession
        self._parent = parent
        self._children = []

    def append_child(self, child):
        """
        Add a child to this person's list of children
        
        :param child: Child Person object
        """
        self._children.append(child)

    def child(self, row):
        """
        Get a child at a specific row
        
        :param row: Index of the child
        :return: Child Person object or None
        """
        return self._children[row] if 0 <= row < len(self._children) else None

    def child_count(self):
        """
        Get the number of children
        
        :return: Number of children
        """
        return len(self._children)

    def data(self, column):
        """
        Get data for a specific column
        
        :param column: Column index (0 for name, 1 for profession)
        :return: Data for the specified column
        """
        if column == 0:
            return self._names
        elif column == 1:
            return self._profession
        return None

    def set_name(self, name):
        """
        Set the name of this person
        
        :param name: New name
        """
        self._names = name

    def set_profession(self, profession):
        """
        Set the profession of this person
        
        :param profession: New profession
        """
        self._profession = profession

    def row(self):
        """
        Get the row of this person in its parent's children list
        
        :return: Row index or 0 if no parent
        """
        return self._parent._children.index(self) if self._parent else 0

    def parent_person(self):
        """
        Get the parent of this person
        
        :return: Parent Person object
        """
        return self._parent

    def show_info(self, indent=0):
        """
        Recursively print information about this person and their descendants
        
        :param indent: Indentation level for printing
        """
        print('  ' * indent + f"{self._names} ({self._profession}) - {self.child_count()} children")
        for child in self._children:
            child.show_info(indent + 1)