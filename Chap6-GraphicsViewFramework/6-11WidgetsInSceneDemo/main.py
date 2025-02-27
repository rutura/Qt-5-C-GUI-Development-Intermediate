import sys
from PySide6.QtWidgets import QApplication
from widget import Widget

def main():
    """
    Application entry point.
    """
    app = QApplication(sys.argv)
    window = Widget()
    window.show()
    
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())