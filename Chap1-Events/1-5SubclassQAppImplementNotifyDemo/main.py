import sys
from application import Application
from widget import Widget

def main():
    app = Application(sys.argv)
    window = Widget()
    window.show()
    
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())