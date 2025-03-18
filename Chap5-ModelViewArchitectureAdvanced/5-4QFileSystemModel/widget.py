from PySide6.QtWidgets import QWidget, QInputDialog, QMessageBox, QFileSystemModel
from PySide6.QtCore import QDir, Slot
from ui_widget import Ui_Widget

class Widget(QWidget):
    def __init__(self, model=None, controller=None, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # Store model and controller
        self._model = model if model else QFileSystemModel(self)
        self._controller = controller
        
        # If no model was provided, configure the default one
        if not model:
            self._model.setReadOnly(False)
            self._model.setRootPath(QDir.currentPath())
        
        # Connect model to tree view
        self.ui.treeView.setModel(self._model)
        self.ui.treeView.setRootIndex(self._model.index(QDir.currentPath()))
        self.ui.treeView.setAlternatingRowColors(True)
        
        # Set the current directory as the initial location
        index = self._model.index(QDir.currentPath())
        self.ui.treeView.expand(index)
        self.ui.treeView.scrollTo(index)
        self.ui.treeView.resizeColumnToContents(0)
        
        # Connect button signals to slots
        self.ui.addDirButton.clicked.connect(self.on_addDirButton_clicked)
        self.ui.removeFileDir.clicked.connect(self.on_removeFileDir_clicked)
        
        # Connect controller signals to handler slots if controller is provided
        if self._controller:
            self._controller.fileSystemError.connect(self.on_fileSystemError)
        
        # Set window title
        self.setWindowTitle("File System Browser (Qt Widgets)")
    
    @Slot()
    def on_addDirButton_clicked(self):
        """Handle the Add Dir button click"""
        index = self.ui.treeView.currentIndex()
        if not index.isValid():
            return
        
        # Get directory name from user
        dir_name, ok = QInputDialog.getText(
            self, 
            "Create Directory",
            "Directory name"
        )
        
        if ok and dir_name:
            if self._controller:
                # Use controller to create directory
                self._controller.createDirectory(index, dir_name)
            else:
                # Fallback to direct model manipulation
                if not self._model.mkdir(index, dir_name).isValid():
                    QMessageBox.information(
                        self, 
                        "Create Directory",
                        "Failed to create the directory"
                    )
    
    @Slot()
    def on_removeFileDir_clicked(self):
        """Handle the Remove File or Dir button click"""
        index = self.ui.treeView.currentIndex()
        if not index.isValid():
            return
        
        if self._controller:
            # Use controller to remove file/directory
            self._controller.removeFileOrDirectory(index)
        else:
            # Fallback to direct model manipulation
            file_info = self._model.fileInfo(index)
            ok = False
            
            if file_info.isDir():
                ok = self._model.rmdir(index)
            else:
                ok = self._model.remove(index)
            
            if not ok:
                QMessageBox.information(
                    self, 
                    "Delete",
                    f"Failed to delete {self._model.fileName(index)}"
                )
    
    @Slot(str, str)
    def on_fileSystemError(self, operation, message):
        """Handle file system error messages from the controller"""
        QMessageBox.information(self, operation, message)