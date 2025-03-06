from PySide6.QtWidgets import QMainWindow, QColorDialog, QFileDialog, QListWidgetItem
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QIcon
from ui_mainwindow import Ui_MainWindow
from view import View
from scene import Scene
from shapelist import ShapeList
from colorpicker import ColorPicker


class MainWindow(QMainWindow):
    """Main application window for the drawing application"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Create scene for the graphics view
        self.scene = Scene(self)
        
        # Create shape list with draggable shapes
        self.shape_list = ShapeList(self)
        self.shape_map = {}
        self.shape_map[10] = "Ellipse"
        self.shape_map[20] = "Quick"
        self.shape_map[30] = "Rectangle"
        self.shape_map[40] = "Star"
        
        # Populate shape list with items
        for key in self.shape_map.keys():
            item = QListWidgetItem(self.shape_map[key], self.shape_list)
            filename = f":/images/{self.shape_map[key].lower()}.png"
            item.setIcon(QIcon(filename))
            item.setData(Qt.ItemDataRole.UserRole, key)
        
        # Create color picker
        self.color_picker = ColorPicker(self)
        
        # Connect color picker to scene
        self.color_picker.colorChanged.connect(self.on_color_picker_color_changed)
        
        # Create and set up view
        self.view = View(self)
        self.view.setScene(self.scene)
        
        # Add widgets to layouts
        self.ui.colorPickerLayout.addWidget(self.color_picker)
        self.ui.listLayout.addWidget(self.shape_list)
        self.ui.viewLayout.addWidget(self.view)
        
        # Set initial button colors
        pen_color_qss = f"background-color: {self.scene.get_pen_color().name()}"
        self.ui.penColorButton.setStyleSheet(pen_color_qss)
        
        # Populate pen style combo
        self.ui.penStyleCombobox.addItem(QIcon(":/images/pen_style_solid.png"), "Solid")
        self.ui.penStyleCombobox.addItem(QIcon(":/images/pen_style_dashed.png"), "Dashed")
        self.ui.penStyleCombobox.addItem(QIcon(":/images/pen_style_dotted.png"), "Dotted")
        self.ui.penStyleCombobox.addItem(QIcon(":/images/pen_style_dot_dashed.png"), "Dot Dashed")
        
        # Set initial pen width
        self.ui.penWidthSpinbox.setValue(self.scene.get_pen_width())
        
        # Connect action signals to slots
        self.ui.actionCursor.triggered.connect(self.on_actionCursor_triggered)
        self.ui.actionAbout.triggered.connect(self.on_actionAbout_triggered)
        self.ui.actionStar.triggered.connect(self.on_actionStar_triggered)
        self.ui.actionRectangle.triggered.connect(self.on_actionRectangle_triggered)
        self.ui.actionEllipse.triggered.connect(self.on_actionEllipse_triggered)
        self.ui.actionEraser.triggered.connect(self.on_actionEraser_triggered)
        self.ui.actionPen.triggered.connect(self.on_actionPen_triggered)
        self.ui.actionQuit.triggered.connect(self.on_actionQuit_triggered)
        self.ui.actionAdd_Image.triggered.connect(self.on_actionAdd_Image_triggered)
        self.ui.actionSave.triggered.connect(self.on_actionSave_triggered)
        self.ui.actionLoad.triggered.connect(self.on_actionLoad_triggered)
        self.ui.actionCopy.triggered.connect(self.on_actionCopy_triggered)
        self.ui.actionCut.triggered.connect(self.on_actionCut_triggered)
        self.ui.actionPaste.triggered.connect(self.on_actionPaste_triggered)
        self.ui.actionUndo.triggered.connect(self.on_actionUndo_triggered)
        self.ui.actionRedo.triggered.connect(self.on_actionRedo_triggered)
        
        # Connect widget signals to slots
        self.ui.penColorButton.clicked.connect(self.on_penColorButton_clicked)
        self.ui.penWidthSpinbox.valueChanged.connect(self.on_penWidthSpinbox_valueChanged)
        self.ui.penStyleCombobox.activated.connect(self.on_penStyleCombobox_activated)
    
    def on_color_picker_color_changed(self, color):
        """Handle color change from color picker"""
        self.scene.set_pen_color(color)
        self.ui.penColorButton.setStyleSheet(f"background-color: {self.scene.get_pen_color().name()}")
    
    def on_actionCursor_triggered(self):
        """Set cursor tool"""
        self.statusBar().showMessage("Current tool is Cursor")
        self.scene.set_tool(Scene.Cursor)
    
    def on_actionAbout_triggered(self):
        """Show about dialog"""
        pass
    
    def on_actionStar_triggered(self):
        """Set star tool"""
        self.statusBar().showMessage("Current tool is Star")
        self.scene.set_tool(Scene.Star)
    
    def on_actionRectangle_triggered(self):
        """Set rectangle tool"""
        self.statusBar().showMessage("Current tool is Rect")
        self.scene.set_tool(Scene.Rect)
    
    def on_actionEllipse_triggered(self):
        """Set ellipse tool"""
        self.statusBar().showMessage("Current tool is Ellipse")
        self.scene.set_tool(Scene.Ellipse)
    
    def on_actionEraser_triggered(self):
        """Set eraser tool"""
        self.statusBar().showMessage("Current tool is Eraser")
        self.scene.set_tool(Scene.Eraser)
    
    def on_actionPen_triggered(self):
        """Set pen tool"""
        self.statusBar().showMessage("Current tool is Pen")
        self.scene.set_tool(Scene.Pen)
    
    def on_actionQuit_triggered(self):
        """Close the application"""
        self.close()
    
    def on_actionAdd_Image_triggered(self):
        """Add an image to the scene"""
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Open File", "/home", "Images (*.png *.xpm *.jpg)"
        )
        if not file_name:
            return
        
        self.scene.add_image_item(file_name)
    
    def on_actionSave_triggered(self):
        """Save the drawing"""
        pass
    
    def on_actionLoad_triggered(self):
        """Load a drawing"""
        pass
    
    def on_actionCopy_triggered(self):
        """Copy selected items"""
        pass
    
    def on_actionCut_triggered(self):
        """Cut selected items"""
        pass
    
    def on_actionPaste_triggered(self):
        """Paste items"""
        pass
    
    def on_actionUndo_triggered(self):
        """Undo last action"""
        pass
    
    def on_actionRedo_triggered(self):
        """Redo last undone action"""
        pass
    
    def on_penColorButton_clicked(self):
        """Open color dialog for pen color"""
        color = QColorDialog.getColor(Qt.black, self)
        
        if color.isValid():
            self.scene.set_pen_color(color)
            color_qss = f"background-color: {color.name()}"
            self.ui.penColorButton.setStyleSheet(color_qss)
    
    def on_penWidthSpinbox_valueChanged(self, value):
        """Set pen width"""
        self.scene.set_pen_width(value)
    
    def on_penStyleCombobox_activated(self, index):
        """Set pen style"""
        if index == 0:  # Solid
            self.scene.set_pen_style(Qt.PenStyle.SolidLine)
        elif index == 1:  # Dashed
            self.scene.set_pen_style(Qt.PenStyle.DashLine)
        elif index == 2:  # Dotted
            self.scene.set_pen_style(Qt.PenStyle.DotLine)
        elif index == 3:  # Dot Dashed
            self.scene.set_pen_style(Qt.PenStyle.DashDotLine)