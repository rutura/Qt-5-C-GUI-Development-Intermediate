from typing import Optional
from PySide6.QtWidgets import QWidget, QMenu
from PySide6.QtCore import QPoint, Qt
from PySide6.QtGui import (
    QMouseEvent, 
    QCloseEvent, 
    QContextMenuEvent,
    QEnterEvent,
    QKeyEvent,
    QWheelEvent,
    QResizeEvent,
    QPaintEvent
)
from ui_widget import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        print(f"Widget, Mouse Pressed at {event.pos()}")

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        print(f"Widget, Mouse Released at {event.pos()}")

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        print(f"Widget, Mouse Move at {event.pos()}")

    def closeEvent(self, event: QCloseEvent) -> None:
        print("Widget about to close")
        # event.ignore()  # Uncomment to prevent closing

    def contextMenuEvent(self, event: QContextMenuEvent) -> None:
        print("ContextMenu event")
        menu = QMenu(self)
        menu.addAction("Action1")
        menu.addAction("Action2")
        
        # Convert position to global coordinates
        menu.popup(self.mapToGlobal(event.pos()))
        
        print(f"Event x: {event.x()} event y: {event.y()}")
        print(f"Event reason: {event.reason()}")

    def enterEvent(self, event: QEnterEvent) -> None:
        print("Enter event")

    def leaveEvent(self, event) -> None:
        print("Leave event")

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.modifiers() & Qt.ControlModifier:
            print(f"Control + {event.text()}")
        if event.modifiers() & Qt.AltModifier:
            print(f"Alt + {event.text()}")

        # Detect Shift+A
        if event.modifiers() & Qt.ShiftModifier:
            if event.key() == Qt.Key.Key_A:
                print("Shift + A detected")

    def wheelEvent(self, event: QWheelEvent) -> None:
        delta = event.pixelDelta() if event.hasPixelDelta() else QPoint(0, 0)
        print(f"Wheel Event Delta: {delta}")
        print(f"x: {event.position().x()}, y: {event.position().y()}")
        print(f"Orientation: {event.angleDelta()}")

    def resizeEvent(self, event: QResizeEvent) -> None:
        print(f"Widget resized, old size: {event.oldSize()}")
        print(f"new size: {event.size()}")

    def paintEvent(self, event: QPaintEvent) -> None:
        print("Paint event triggered")