from PySide6.QtCore import QObject, Slot, Signal, QModelIndex

class FileSystemController(QObject):
    """Controller for file system operations
    
    Acts as an intermediary between the file system model and views
    """
    
    # Signals for view notifications
    directoryCreated = Signal(str)
    directoryRemoved = Signal(str)
    fileRemoved = Signal(str)
    fileSystemError = Signal(str, str)
    
    def __init__(self, model=None, parent=None):
        super().__init__(parent)
        self._model = model
    
    def set_model(self, model):
        """Set the model for this controller"""
        self._model = model
    
    @Slot(QModelIndex, str)
    def createDirectory(self, parent_index, dir_name):
        """Create a directory at the specified location"""
        if self._model and parent_index.isValid() and dir_name:
            # Try to create the directory
            if not self._model.mkdir(parent_index, dir_name).isValid():
                self.fileSystemError.emit("Create Directory", "Failed to create the directory")
                return False
            self.directoryCreated.emit(dir_name)
            return True
        return False
    
    @Slot(QModelIndex)
    def removeFileOrDirectory(self, index):
        """Remove a file or directory at the specified index"""
        if not self._model or not index.isValid():
            return False
            
        # Determine if it's a directory or file and remove it accordingly
        file_info = self._model.fileInfo(index)
        filename = self._model.fileName(index)
        ok = False
        
        if file_info.isDir():
            ok = self._model.rmdir(index)
            if ok:
                self.directoryRemoved.emit(filename)
        else:
            ok = self._model.remove(index)
            if ok:
                self.fileRemoved.emit(filename)
        
        if not ok:
            self.fileSystemError.emit("Delete", f"Failed to delete {filename}")
            
        return ok