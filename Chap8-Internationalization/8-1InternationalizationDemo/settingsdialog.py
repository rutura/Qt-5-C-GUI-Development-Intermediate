from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QSettings
import ui_settingsdialog  # We'll need to generate this with pyside6-uic

class SettingsDialog(QDialog):
    """Dialog for changing language settings"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ui_settingsdialog.Ui_SettingsDialog()
        self.ui.setupUi(self)
    
    def accept(self):
        """Handle OK button click"""
        settings = QSettings("Blikoon Technologies", "Painter App")
        
        # Save the selected language
        index = self.ui.languageCombobox.currentIndex()
        if index == 0:
            # Default
            settings.setValue("language", "default")
        elif index == 1:
            # English
            settings.setValue("language", "english")
        elif index == 2:
            # French
            settings.setValue("language", "french")
        elif index == 3:
            # Chinese
            settings.setValue("language", "chinese")
        
        super().accept()