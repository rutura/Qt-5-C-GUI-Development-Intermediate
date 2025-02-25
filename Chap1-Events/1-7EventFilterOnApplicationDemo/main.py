import sys
from PySide6.QtWidgets import QApplication
from widget import Widget
from filter import Filter

def main():
    """Main application entry point"""
    app = QApplication(sys.argv)
    window = Widget()
    
    # Create and install the event filter
    event_filter = Filter(window)
    app.installEventFilter(event_filter)
    
    window.show()
    
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())