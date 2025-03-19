from PySide6.QtCore import Qt, QAbstractListModel, QModelIndex, Property, Slot
from PySide6.QtGui import QStandardItemModel, QStandardItem

class ItemModel(QStandardItemModel):
    """Extended standard item model with drag/drop property roles"""
    
    # Define custom roles
    CanDragRole = Qt.UserRole + 1
    CanDropRole = Qt.UserRole + 2
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Create the initial items
        self.setupItems()
    
    def setupItems(self):
        """Set up the initial items with drag/drop properties"""
        
        # Create item 0 - Can Drag, Can Drop
        item0 = QStandardItem("Item0 [CAN DRAG] [CAN DROP]")
        item0.setData(True, ItemModel.CanDragRole)
        item0.setData(True, ItemModel.CanDropRole)
        
        # Create item 1 - Can Drag, Can't Drop
        item1 = QStandardItem("Item1 [CAN DRAG] [CAN'T DROP]")
        item1.setData(True, ItemModel.CanDragRole)
        item1.setData(False, ItemModel.CanDropRole)
        
        # Create item 2 - Can't Drag, Can Drop
        item2 = QStandardItem("Item2 [CAN'T DRAG] [CAN DROP]")
        item2.setData(False, ItemModel.CanDragRole)
        item2.setData(True, ItemModel.CanDropRole)
        
        # Create item 3 - Can't Drag, Can't Drop
        item3 = QStandardItem("Item3 [CAN'T DRAG] [CAN'T DROP]")
        item3.setData(False, ItemModel.CanDragRole)
        item3.setData(False, ItemModel.CanDropRole)
        
        # Add items to the model
        self.appendRow(item0)
        self.appendRow(item1)
        self.appendRow(item2)
        self.appendRow(item3)
    
    def roleNames(self):
        """Define the role names for QML access"""
        roles = super().roleNames()
        roles[ItemModel.CanDragRole] = b"canDrag"
        roles[ItemModel.CanDropRole] = b"canDrop"
        return roles
    
    def data(self, index, role=Qt.DisplayRole):
        """Override to provide custom role data"""
        if not index.isValid():
            return None
            
        if role == ItemModel.CanDragRole:
            return super().data(index, ItemModel.CanDragRole)
        elif role == ItemModel.CanDropRole:
            return super().data(index, ItemModel.CanDropRole)
            
        return super().data(index, role)