import sys
from pathlib import Path
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject, Slot, Signal, Property, QUrl

class DragDropController(QObject):
    """Bridge class for handling MIME data in QML"""
    
    mimeDataChanged = Signal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._mimeEntries = []
    
    @Slot(str, list, str, bool)
    def processMimeData(self, text, urls, html, hasImage):
        """Process mime data from QML"""
        self._mimeEntries = []
        
        # Process text/plain
        if text:
            self._mimeEntries.append({
                "format": "text/plain",
                "data": text
            })
        
        # Process text/html
        if html:
            self._mimeEntries.append({
                "format": "text/html",
                "data": html
            })
        
        # Process URLs
        if urls and len(urls) > 0:
            urlData = ""
            for url in urls:
                urlData += url + " -/- "
            
            self._mimeEntries.append({
                "format": "text/uri-list",
                "data": urlData
            })
        
        # Mark the presence of image data
        if hasImage:
            self._mimeEntries.append({
                "format": "image/*",
                "data": "[Image data not shown]"
            })
        
        self.mimeDataChanged.emit()
    
    @Slot()
    def clearData(self):
        """Clear mime data"""
        self._mimeEntries = []
        self.mimeDataChanged.emit()
    
    @Property(list, notify=mimeDataChanged)
    def mimeEntries(self):
        return self._mimeEntries

def main():
    app = QGuiApplication(sys.argv)
    
    # Create controller and expose to QML
    controller = DragDropController()
    
    # Create QML engine
    engine = QQmlApplicationEngine()
    
    # Expose controller to QML
    engine.rootContext().setContextProperty("controller", controller)
    
    # Load QML file
    qml_file = Path(__file__).resolve().parent / "main.qml"
    engine.load(qml_file)
    
    # Check if loading was successful
    if not engine.rootObjects():
        sys.exit(-1)
        
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())