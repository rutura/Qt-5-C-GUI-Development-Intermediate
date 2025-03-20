from PySide6.QtCore import QAbstractItemModel, QModelIndex, Qt, Signal, Slot, Property, QObject

class TreeNode:
    """Represents a node in the tree structure"""
    def __init__(self, name, description, parent=None):
        self.name = name
        self.description = description
        self.parent = parent
        self.children = []
        self.expanded = True if parent is None else False
        
    def child(self, row):
        """Return the child at the specified row"""
        if 0 <= row < len(self.children):
            return self.children[row]
        return None
    
    def child_count(self):
        """Return the number of children"""
        return len(self.children)
    
    def row(self):
        """Return the row of this node in its parent's children list"""
        if self.parent:
            return self.parent.children.index(self)
        return 0
        
    def add_child(self, name, description):
        """Add a child node with the given name and description"""
        child = TreeNode(name, description, self)
        self.children.append(child)
        return child
    
    def data(self, column):
        """Return data for the given column"""
        if column == 0:
            return self.name
        elif column == 1:
            return self.description
        return None


class OrganizationTreeModel(QAbstractItemModel):
    """TreeModel for organization hierarchy using QAbstractItemModel for both Qt Widgets and Qt Quick"""
    
    # Roles for QML access
    NameRole = Qt.UserRole + 1
    DescriptionRole = Qt.UserRole + 2
    ExpandedRole = Qt.UserRole + 3
    HasChildrenRole = Qt.UserRole + 4
    DepthRole = Qt.UserRole + 5
    
    # Signal to notify QML of data changes
    dataChanged = Signal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.root_node = TreeNode("", "")
        self.setup_model_data()
    
    def setup_model_data(self):
        """Initialize with sample data"""
        # Add Google root organization
        google_root = self.add_organization("Google Inc", "Head Quarters")
        
        # Add India branch
        google_india = self.add_child_organization(google_root, "Google India", "Google India Branch")
        self.add_child_organization(google_india, "Mumbai", "AI Research")
        self.add_child_organization(google_india, "Bangalore", "Sales")
        
        # Add Ghana branch
        google_ghana = self.add_child_organization(google_root, "Google Ghana", "Ghana Branch")
        self.add_child_organization(google_ghana, "Akra", "AI")
    
    def add_organization(self, name, description):
        """Add a root-level organization"""
        # Begin model operation
        self.beginInsertRows(QModelIndex(), self.root_node.child_count(), self.root_node.child_count())
        node = self.root_node.add_child(name, description)
        # End model operation
        self.endInsertRows()
        return node
    
    def add_child_organization(self, parent_node, name, description):
        """Add a child organization to a parent node"""
        if parent_node:
            # Create index for parent
            parent_index = self.createIndex(parent_node.row(), 0, parent_node)
            # Begin model operation
            self.beginInsertRows(parent_index, parent_node.child_count(), parent_node.child_count())
            node = parent_node.add_child(name, description)
            # End model operation
            self.endInsertRows()
            return node
        return None
    
    def toggle_expanded(self, index):
        """Toggle expanded state of a node"""
        if not index.isValid():
            return False
            
        node = index.internalPointer()
        node.expanded = not node.expanded
        self.dataChanged.emit(index, index, [self.ExpandedRole])
        return True
        
    def index(self, row, column, parent=QModelIndex()):
        """Returns the index of the item in the model specified by row, column and parent"""
        if not self.hasIndex(row, column, parent):
            return QModelIndex()
            
        if not parent.isValid():
            parent_node = self.root_node
        else:
            parent_node = parent.internalPointer()
            
        child_node = parent_node.child(row)
        if child_node:
            return self.createIndex(row, column, child_node)
        return QModelIndex()
    
    def parent(self, index):
        """Returns the parent of the model item with the given index"""
        if not index.isValid():
            return QModelIndex()
            
        child_node = index.internalPointer()
        if not child_node or child_node == self.root_node:
            return QModelIndex()
            
        parent_node = child_node.parent
        if parent_node == self.root_node:
            return QModelIndex()
            
        return self.createIndex(parent_node.row(), 0, parent_node)
    
    def rowCount(self, parent=QModelIndex()):
        """Returns the number of rows under the given parent"""
        if parent.column() > 0:
            return 0
            
        if not parent.isValid():
            parent_node = self.root_node
        else:
            parent_node = parent.internalPointer()
            
        return parent_node.child_count()
    
    def columnCount(self, parent=QModelIndex()):
        """Returns the number of columns for the children of the given parent"""
        return 2
    
    def data(self, index, role=Qt.DisplayRole):
        """Returns the data stored under the given role for the item referred to by the index"""
        if not index.isValid():
            return None
            
        node = index.internalPointer()
        
        if role == Qt.DisplayRole:
            return node.data(index.column())
        elif role == self.NameRole:
            return node.name
        elif role == self.DescriptionRole:
            return node.description
        elif role == self.ExpandedRole:
            return node.expanded
        elif role == self.HasChildrenRole:
            return node.child_count() > 0
        elif role == self.DepthRole:
            # Calculate depth by counting parents
            depth = 0
            parent = node.parent
            while parent and parent != self.root_node:
                depth += 1
                parent = parent.parent
            return depth
                
        return None
    
    def setData(self, index, value, role=Qt.EditRole):
        """Sets the role data for the item at index to value"""
        if not index.isValid():
            return False
            
        node = index.internalPointer()
        
        if role == self.ExpandedRole:
            node.expanded = value
            self.dataChanged.emit(index, index, [self.ExpandedRole])
            return True
            
        return False
    
    def headerData(self, section, orientation, role=Qt.DisplayRole):
        """Returns the data for the given role and section in the header with the specified orientation"""
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            if section == 0:
                return "Organization"
            elif section == 1:
                return "Description"
                
        return None
        
    def roleNames(self):
        """Returns the model's role names"""
        roles = {
            self.NameRole: b"name",
            self.DescriptionRole: b"description",
            self.ExpandedRole: b"expanded",
            self.HasChildrenRole: b"hasChildren",
            self.DepthRole: b"depth"
        }
        return roles