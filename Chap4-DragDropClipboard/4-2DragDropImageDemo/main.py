import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from widget import Widget

def main():
    # Create the application
    app = QApplication(sys.argv)
    
    # Create and show the widget
    window = Widget()
    window.setWindowTitle("Image Viewer")
    window.resize(600, 400)
    window.show()
    
    # Run the event loop
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())