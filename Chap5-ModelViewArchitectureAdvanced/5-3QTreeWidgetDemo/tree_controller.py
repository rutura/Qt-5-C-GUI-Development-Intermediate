from PySide6.QtCore import QObject, Slot, Signal, Property, QModelIndex

class OrganizationController(QObject):
    """Controller for organization tree hierarchy
    
    Acts as an intermediary between models and views
    """
    
    # Signals for view notifications
    organizationClicked = Signal(str, str)
    organizationAdded = Signal(str)
    organizationRemoved = Signal(str)
    
    def __init__(self, model=None, parent=None):
        super().__init__(parent)
        self._model = model
    
    def set_model(self, model):
        """Set the model for this controller"""
        self._model = model
    
    @Slot(str, str)
    def addOrganization(self, name, description):
        """Add a root organization"""
        if self._model:
            org = self._model.add_organization(name, description)
            self.organizationAdded.emit(name)
            return True
        return False
    
    @Slot(QModelIndex, str, str)
    def addChildOrganization(self, parent_index, name, description):
        """Add a child organization to a parent"""
        if self._model and parent_index.isValid():
            parent_node = parent_index.internalPointer()
            child = self._model.add_child_organization(parent_node, name, description)
            self.organizationAdded.emit(name)
            return True
        return False
    
    @Slot(str, str)
    def onOrganizationSelected(self, name, description):
        """Called when an organization is selected"""
        self.organizationClicked.emit(name, description)
        print(f"Selected organization: {name}, {description}")
    
    @Slot(QModelIndex)
    def toggleExpanded(self, index):
        """Toggle expanded state of an organization"""
        if self._model and index.isValid():
            return self._model.toggle_expanded(index)
        return False