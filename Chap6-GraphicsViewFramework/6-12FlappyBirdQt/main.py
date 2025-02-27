import sys
from PySide6.QtWidgets import QApplication
from widget import Widget
import resource_rc

def main():
    app = QApplication(sys.argv)
    window = Widget()
    window.show()
    
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())