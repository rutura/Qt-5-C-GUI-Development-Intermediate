from PySide6.QtWidgets import (QMainWindow, QLabel, QSpinBox, QColorDialog, 
                             QPushButton, QCheckBox)
from PySide6.QtGui import QIcon, QColor
from PySide6.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from paintcanvas import PaintCanvas
import resource_rc  # Import resources

class MainWindow(QMainWindow):
    """Main window for the Paint Application"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Create and set the canvas as central widget
        self.canvas = PaintCanvas(self)
        self.setCentralWidget(self.canvas)
        
        # Create toolbar controls
        
        # Pen width controls
        penWidthLabel = QLabel("Pen Width", self)
        penWidthSpinBox = QSpinBox(self)
        penWidthSpinBox.setValue(2)
        penWidthSpinBox.setRange(1, 15)
        
        # Pen color controls
        penColorLabel = QLabel("Pen Color", self)
        self.penColorButton = QPushButton(self)
        
        # Fill color controls
        fillColorLabel = QLabel("Fill Color", self)
        self.fillColorButton = QPushButton(self)
        
        # Fill checkbox
        self.fillCheckBox = QCheckBox("Fill Shape", self)
        
        # Tool buttons
        rectButton = QPushButton(self)
        rectButton.setIcon(QIcon(":/images/rectangle.png"))
        
        penButton = QPushButton(self)
        penButton.setIcon(QIcon(":/images/pen.png"))
        
        ellipseButton = QPushButton(self)
        ellipseButton.setIcon(QIcon(":/images/circle.png"))
        
        eraserButton = QPushButton(self)
        eraserButton.setIcon(QIcon(":/images/eraser.png"))
        
        # Connect tool button signals
        rectButton.clicked.connect(lambda: self.setTool(PaintCanvas.Rect))
        penButton.clicked.connect(lambda: self.setTool(PaintCanvas.Pen))
        ellipseButton.clicked.connect(lambda: self.setTool(PaintCanvas.Ellipse))
        eraserButton.clicked.connect(lambda: self.setTool(PaintCanvas.Eraser))
        
        # Connect other control signals
        penWidthSpinBox.valueChanged.connect(self.penWidthChanged)
        self.penColorButton.clicked.connect(self.changePenColor)
        self.fillColorButton.clicked.connect(self.changeFillColor)
        self.fillCheckBox.clicked.connect(self.changeFillProperty)
        
        # Add widgets to toolbar
        self.ui.mainToolBar.addWidget(penWidthLabel)
        self.ui.mainToolBar.addWidget(penWidthSpinBox)
        self.ui.mainToolBar.addWidget(penColorLabel)
        self.ui.mainToolBar.addWidget(self.penColorButton)
        self.ui.mainToolBar.addWidget(fillColorLabel)
        self.ui.mainToolBar.addWidget(self.fillColorButton)
        self.ui.mainToolBar.addWidget(self.fillCheckBox)
        self.ui.mainToolBar.addSeparator()
        self.ui.mainToolBar.addWidget(penButton)
        self.ui.mainToolBar.addWidget(rectButton)
        self.ui.mainToolBar.addWidget(ellipseButton)
        self.ui.mainToolBar.addWidget(eraserButton)
        
        # Set initial button colors
        css = f"background-color: {self.canvas.getPenColor().name()}"
        self.penColorButton.setStyleSheet(css)
        
        css = f"background-color: {self.canvas.getFillColor().name()}"
        self.fillColorButton.setStyleSheet(css)
        
        # Set window title
        self.setWindowTitle("Paint with Clipboard Support")
        
        # Show clipboard usage instructions in status bar
        self.ui.statusBar.showMessage("Press Ctrl+C to copy and Ctrl+V to paste images")
    
    def setTool(self, tool):
        """Set the current drawing tool"""
        self.canvas.setTool(tool)
        
        # Update status bar message
        tool_names = {
            PaintCanvas.Pen: "Pen",
            PaintCanvas.Rect: "Rectangle",
            PaintCanvas.Ellipse: "Ellipse",
            PaintCanvas.Eraser: "Eraser"
        }
        self.ui.statusBar.showMessage(f"Current tool: {tool_names[tool]} | Ctrl+C to copy, Ctrl+V to paste")
    
    @Slot(int)
    def penWidthChanged(self, width):
        """Handle pen width change"""
        self.canvas.setPenWidth(width)
    
    @Slot()
    def changePenColor(self):
        """Handle pen color change"""
        color = QColorDialog.getColor(self.canvas.getPenColor())
        if color.isValid():
            self.canvas.setPenColor(color)
            css = f"background-color: {color.name()}"
            self.penColorButton.setStyleSheet(css)
    
    @Slot()
    def changeFillColor(self):
        """Handle fill color change"""
        color = QColorDialog.getColor(self.canvas.getFillColor())
        if color.isValid():
            self.canvas.setFillColor(color)
            css = f"background-color: {color.name()}"
            self.fillColorButton.setStyleSheet(css)
    
    @Slot()
    def changeFillProperty(self):
        """Handle fill property change"""
        self.canvas.setFill(self.fillCheckBox.isChecked())