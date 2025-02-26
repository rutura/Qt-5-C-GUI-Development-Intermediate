import sys
from application import Application
from widget import Widget

def main():
    """Main application entry point.
    
    Returns:
        int: Application exit code
    """
    app = Application(sys.argv)
    window = Widget()
    window.show()
    
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())