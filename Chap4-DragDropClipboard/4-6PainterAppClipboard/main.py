import sys
from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(950, 684)
    window.show()
    
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())