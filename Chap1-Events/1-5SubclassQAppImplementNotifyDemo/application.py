from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QObject, QEvent
from widget import Widget

class Application(QApplication):
    def __init__(self, argv):
        super().__init__(argv)

    def notify(self, dest, event):
        if event.type() == QEvent.MouseButtonPress or event.type() == QEvent.MouseButtonDblClick:
            print(" Application: mouse press or double click detected")
            
            print(f"Class Name: {dest.metaObject().className()}")
            
            # Try to cast the object to Widget
            if isinstance(dest, Widget):
                print("Cast successful")
            else:
                print("Cast failed")
                
            return False
        
        return super().notify(dest, event)