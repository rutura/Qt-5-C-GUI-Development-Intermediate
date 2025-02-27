from PySide6.QtWidgets import QMainWindow, QFileDialog, QColorDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QPixmap, QColor
from ui_mainwindow import Ui_MainWindow
from scene import Scene
from view import View
from shapelist import ShapeList
from colorpicker import ColorPicker
import resource_rc

class MainWindow(QMainWindow):
    """Main window for the drawing application"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Create scene
        self.scene = Scene(self)
        
        # Create shape list
        self.shape_map = {}
        self.shape_map[10] = "Ellipse"
        self.shape_map[20] = "Quick"
        self.shape_map[30] = "Rectangle"
        self.shape_map[40] = "Star"
        
        shape_list = ShapeList(self)
        
        for key in self.shape_map.keys():
            shape_list.addItem(self.shape_map[key])
            item = shape_list.item(shape_list.count() - 1)
            filename = f":/images/{self.shape_map[key].lower()}.png"
            item.setIcon(QIcon(filename))
            item.setData(Qt.ItemDataRole.UserRole, key)
        
        # Create color picker
        color_picker = ColorPicker(self)
        color_picker.colorChanged.connect(self.on_colorpicker_color_changed)
        
        # Create view
        view = View(self)
        view.setScene(self.scene)
        
        # Add widgets to layout
        self.ui.colorPickerLayout.addWidget(color_picker)
        self.ui.listLayout.addWidget(shape_list)
        self.ui.viewLayout.addWidget(view)
        
        # Set initial color buttons
        pen_color_qss = f"background-color: {self.scene.get_pen_color().name()}"
        self.ui.penColorButton.setStyleSheet(pen_color_qss)
        
        brush_color_qss = f"background-color: {self.scene.get_fill_color().name()}"
        self.ui.brushColorButton.setStyleSheet(brush_color_qss)
        if hasattr(self.ui.brushColorButton, 'set_button_color'):
            self.ui.brushColorButton.set_button_color(self.scene.get_fill_color())
        
        # Populate pen style combo
        self.ui.penStyleCombobox.addItem(QIcon(":/images/pen_style_solid.png"), "Solid")
        self.ui.penStyleCombobox.addItem(QIcon(":/images/pen_style_dashed.png"), "Dashed")
        self.ui.penStyleCombobox.addItem(QIcon(":/images/pen_style_dotted.png"), "Dotted")
        self.ui.penStyleCombobox.addItem(QIcon(":/images/pen_style_dot_dashed.png"), "Dot Dashed")
        
        # Set initial pen width
        self.ui.penWidthSpinbox.setValue(self.scene.get_pen_width())
        
        # Populate brush style combo
        self.ui.brushStyleComboBox.addItem("Solid")
        self.ui.brushStyleComboBox.addItem("Dense")
        self.ui.brushStyleComboBox.addItem("Horizontal Lines")
        self.ui.brushStyleComboBox.addItem("Vertical Lines")
        self.ui.brushStyleComboBox.addItem("Cross Pattern")
        
        # Connect actions
        self.ui.actionCursor.triggered.connect(self.on_action_cursor_triggered)
        self.ui.actionStar.triggered.connect(self.on_action_star_triggered)
        self.ui.actionRectangle.triggered.connect(self.on_action_rectangle_triggered)
        self.ui.actionEllipse.triggered.connect(self.on_action_ellipse_triggered)
        self.ui.actionEraser.triggered.connect(self.on_action_eraser_triggered)
        self.ui.actionPen.triggered.connect(self.on_action_pen_triggered)
        self.ui.actionAdd_Image.triggered.connect(self.on_action_add_image_triggered)
        self.ui.actionQuit.triggered.connect(self.on_action_quit_triggered)
        
        # Connect other UI elements
        self.ui.penColorButton.clicked.connect(self.on_pen_color_button_clicked)
        self.ui.penWidthSpinbox.valueChanged.connect(self.on_pen_width_spinbox_value_changed)
        self.ui.penStyleCombobox.activated.connect(self.on_pen_style_combobox_activated)
        self.ui.brushColorButton.clicked.connect(self.on_brush_color_button_clicked)
        self.ui.brushStyleComboBox.activated.connect(self.on_brush_style_combo_box_activated)
        
    def on_action_cursor_triggered(self):
        """Set cursor tool"""
        self.statusBar().showMessage("Current tool is Cursor")
        self.scene.set_tool(Scene.Cursor)
    
    def on_action_star_triggered(self):
        """Set star tool"""
        self.statusBar().showMessage("Current tool is Star")
        self.scene.set_tool(Scene.Star)
    
    def on_action_rectangle_triggered(self):
        """Set rectangle tool"""
        self.statusBar().showMessage("Current tool is Rect")
        self.scene.set_tool(Scene.Rect)
    
    def on_action_ellipse_triggered(self):
        """Set ellipse tool"""
        self.statusBar().showMessage("Current tool is Ellipse")
        self.scene.set_tool(Scene.Ellipse)
    
    def on_action_eraser_triggered(self):
        """Set eraser tool"""
        self.statusBar().showMessage("Current tool is Eraser")
        self.scene.set_tool(Scene.Eraser)
    
    def on_action_pen_triggered(self):
        """Set pen tool"""
        self.statusBar().showMessage("Current tool is Pen")
        self.scene.set_tool(Scene.Pen)
    
    def on_action_quit_triggered(self):
        """Quit the application"""
        self.close()
    
    def on_action_add_image_triggered(self):
        """Add an image to the scene"""
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Open File", "/home", "Images (*.png *.xpm *.jpg)"
        )
        if not file_name:
            return
        
        self.scene.add_image_item(file_name)
    
    def on_pen_color_button_clicked(self):
        """Handle pen color button click"""
        color = QColorDialog.getColor(Qt.black, self)
        
        if color.isValid():
            self.scene.set_pen_color(color)
            color_qss = f"background-color: {color.name()}"
            self.ui.penColorButton.setStyleSheet(color_qss)
    
    def on_pen_width_spinbox_value_changed(self, value):
        """Handle pen width spinbox value change"""
        self.scene.set_pen_width(value)
    
    def on_pen_style_combobox_activated(self, index):
        """Handle pen style combobox selection"""
        if index == 0:  # Solid
            self.scene.set_pen_style(Qt.PenStyle.SolidLine)
        elif index == 1:  # Dashed
            self.scene.set_pen_style(Qt.PenStyle.DashLine)
        elif index == 2:  # Dotted
            self.scene.set_pen_style(Qt.PenStyle.DotLine)
        elif index == 3:  # Dot Dashed
            self.scene.set_pen_style(Qt.PenStyle.DashDotLine)
    
    def on_brush_color_button_clicked(self):
        """Handle brush color button click"""
        color = QColorDialog.getColor(Qt.black, self)
        
        if color.isValid():
            self.scene.set_fill_color(color)
            if hasattr(self.ui.brushColorButton, 'set_button_color'):
                self.ui.brushColorButton.set_button_color(color)
            color_qss = f"background-color: {color.name()}"
            self.ui.brushColorButton.setStyleSheet(color_qss)
    
    def on_brush_style_combo_box_activated(self, index):
        """Handle brush style combobox selection"""
        if index == 0:  # Solid
            self.scene.set_brush_style(Qt.BrushStyle.SolidPattern)
        elif index == 1:  # Dense
            self.scene.set_brush_style(Qt.BrushStyle.Dense5Pattern)
        elif index == 2:  # Horizontal Lines
            self.scene.set_brush_style(Qt.BrushStyle.HorPattern)
        elif index == 3:  # Vertical Lines
            self.scene.set_brush_style(Qt.BrushStyle.VerPattern)
        elif index == 4:  # Cross Pattern
            self.scene.set_brush_style(Qt.BrushStyle.CrossPattern)
    
    def on_colorpicker_color_changed(self, color):
        """Handle color changed from color picker"""
        self.scene.set_pen_color(color)
        color_qss = f"background-color: {self.scene.get_pen_color().name()}"
        self.ui.penColorButton.setStyleSheet(color_qss)