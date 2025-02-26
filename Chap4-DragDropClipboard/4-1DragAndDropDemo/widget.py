from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Slot
from ui_widget import Ui_Widget
from dragdroplabel import DragDropLabel


class Widget(QWidget):
    """Main application widget that hosts the drag and drop label"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # Create and add the drag drop label
        self.dragDropLabel = DragDropLabel(self)
        self.dragDropLabel.mimeChanged.connect(self.mimeChanged)
        self.ui.labelLayout.addWidget(self.dragDropLabel)
        
        # Connect the clear button
        self.ui.clearButton.clicked.connect(self.on_clearButton_clicked)
    
    @Slot(object)
    def mimeChanged(self, mimedata):
        """Process and display MIME data information"""
        self.ui.textEdit.clear()
        if not mimedata:
            return
        
        formats = mimedata.formats()
        for i, format_name in enumerate(formats):
            text = ""
            if format_name == "text/plain":
                text = mimedata.text().strip()
            elif format_name == "text/html":
                text = mimedata.html().strip()
            elif format_name == "text/uri-list":
                urlList = mimedata.urls()
                for url in urlList:
                    text += url.toString() + " -/- "
            else:
                data = mimedata.data(format_name)
                # Convert QByteArray to bytes and process each byte
                byte_data = bytes(data)
                for byte in byte_data:
                    text += f"{byte} "
            
            data_string = f"{i} | Format: {format_name}\n    | Data: {text}\n------------"
            self.ui.textEdit.append(data_string)
    
    @Slot()
    def on_clearButton_clicked(self):
        """Clear the text edit widget"""
        self.ui.textEdit.clear()