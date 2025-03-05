from PySide6.QtGui import QUndoCommand

class AddCommand(QUndoCommand):
    """Command for adding items to the scene"""
    
    def __init__(self, item, scene):
        super().__init__()
        self.item = item
        self.scene = scene
    
    def undo(self):
        """Remove the item from the scene"""
        if self.item:
            self.scene.removeItem(self.item)
    
    def redo(self):
        """Add the item to the scene"""
        if self.item:
            self.scene.addItem(self.item)

class RemoveCommand(QUndoCommand):
    """Command for removing items from the scene"""
    
    def __init__(self, item, scene):
        super().__init__()
        self.item = item
        self.scene = scene
    
    def undo(self):
        """Add the item back to the scene"""
        if self.item:
            self.scene.addItem(self.item)
    
    def redo(self):
        """Remove the item from the scene"""
        if self.item:
            self.scene.removeItem(self.item)

class MoveCommand(QUndoCommand):
    """Command for moving items in the scene"""
    
    def __init__(self, item, scene, old_pos, new_pos):
        super().__init__()
        self.item = item
        self.scene = scene
        self.old_position = old_pos
        self.new_position = new_pos
    
    def undo(self):
        """Move the item back to its old position"""
        if self.item:
            self.item.setPos(self.old_position)
    
    def redo(self):
        """Move the item to its new position"""
        if self.item:
            self.item.setPos(self.new_position)