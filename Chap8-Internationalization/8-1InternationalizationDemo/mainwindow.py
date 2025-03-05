from PySide6.QtWidgets import QMainWindow, QFileDialog, QListWidgetItem, QColorDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QPixmap, QColor, QCursor, QKeySequence
from ui_mainwindow import Ui_MainWindow
from view import View
from scene import Scene
from shapelist import ShapeList
from colorlistwidget import ColorListWidget
from colorpicker import ColorPicker
from settingsdialog import SettingsDialog


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
        self.ui.colorPickerLayout.addWidget(self.color_picker)
        
        # Connect color picker signals
        self.color_picker.colorChanged.connect(self.on_color_picker_color_changed)
        
        # Create view
        self.view = View(self)
        self.view.setScene(self.scene)
        
        # Add widgets to layouts
        self.ui.listLayout.addWidget(self.shape_list)
        self.ui.viewLayout.addWidget(self.view)
        
        # Set up initial UI state
        color_qss = f"background-color: {self.scene.getPenColor().name()}"
        self.ui.penColorButton.setStyleSheet(color_qss)
        
        color_qss = f"background-color: {self.scene.getFillColor().name()}"
        self.ui.brushColorButton.setStyleSheet(color_qss)
        
        # Populate pen style combobox
        self.ui.penStyleCombobox.addItem(QIcon(":/images/pen_style_solid.png"), "Solid")
        self.ui.penStyleCombobox.addItem(QIcon(":/images/pen_style_dashed.png"), "Dashed")
        self.ui.penStyleCombobox.addItem(QIcon(":/images/pen_style_dotted.png"), "Dotted")
        self.ui.penStyleCombobox.addItem(QIcon(":/images/pen_style_dot_dashed.png"), "Dot Dashed")
        
        # Set initial pen width
        self.ui.penWidthSpinbox.setValue(self.scene.getPenWidth())
        
        # Populate brush style combobox
        self.ui.brushStyleComboBox.addItem("Solid")
        self.ui.brushStyleComboBox.addItem("Dense")
        self.ui.brushStyleComboBox.addItem("Horizontal Lines")
        self.ui.brushStyleComboBox.addItem("Vertical Lines")
        self.ui.brushStyleComboBox.addItem("Cross Pattern")
        
        # Set checkbox and button state
        self.ui.showgridCheckbox.setChecked(self.view.get_draw_grid_lines())
        
        # Use QColor constructor for proper color handling
        self.ui.sceneBackgroundButton.setStyleSheet(
            f"background-color: {QColor(Qt.GlobalColor.yellow).name()}"
        )
        
        # Set active tool
        self.set_active_tool(Scene.Cursor)
        
        # Connect signals/slots
        self.connect_signals()

        self.ui.actionUndo.setShortcut(QKeySequence("Ctrl+Z"))
        self.ui.actionRedo.setShortcut(QKeySequence("Ctrl+Y"))
    
    def connect_signals(self):
        """Connect UI signals to slots"""
        # Action triggers
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
        self.ui.actionLanguage_Settings.triggered.connect(self.on_actionLanguage_Settings_triggered)

        
        # UI element signals
        self.ui.penColorButton.clicked.connect(self.on_penColorButton_clicked)
        self.ui.penWidthSpinbox.valueChanged.connect(self.on_penWidthSpinbox_valueChanged)
        self.ui.penStyleCombobox.activated.connect(self.on_penStyleCombobox_activated)
        self.ui.brushColorButton.clicked.connect(self.on_brushColorButton_clicked)
        self.ui.brushStyleComboBox.activated.connect(self.on_brushStyleComboBox_activated)
        self.ui.showgridCheckbox.toggled.connect(self.on_showgridCheckbox_toggled)
        self.ui.centerSceneButton.clicked.connect(self.on_centerSceneButton_clicked)
        self.ui.sceneBackgroundButton.clicked.connect(self.on_sceneBackgroundButton_clicked)
    
    def on_color_picker_color_changed(self, color):
        """Handle color change from color picker"""
        self.scene.setPenColor(color)
        self.ui.penColorButton.setStyleSheet(
            f"background-color: {self.scene.getPenColor().name()}"
        )
    
    def on_actionCursor_triggered(self):
        """Set cursor tool"""
        self.view.setCursor(Qt.CursorShape.ArrowCursor)
        self.set_active_tool(Scene.Cursor)
        self.statusBar().showMessage("Current tool is Cursor")
        self.scene.set_tool(Scene.Cursor)
    
    def on_actionAbout_triggered(self):
        """Show about dialog"""
        pass
    
    def on_actionStar_triggered(self):
        """Set star tool"""
        cursor = QCursor(QPixmap(":/images/star_cursor.png"), 0, 32)
        self.view.setCursor(cursor)
        self.set_active_tool(Scene.Star)
        self.statusBar().showMessage("Current tool is Star")
        self.scene.set_tool(Scene.Star)
    
    def on_actionRectangle_triggered(self):
        """Set rectangle tool"""
        cursor = QCursor(QPixmap(":/images/rectangle_cursor.png"), 0, 32)
        self.view.setCursor(cursor)
        self.set_active_tool(Scene.Rect)
        self.statusBar().showMessage("Current tool is Rect")
        self.scene.set_tool(Scene.Rect)
    
    def on_actionEllipse_triggered(self):
        """Set ellipse tool"""
        cursor = QCursor(QPixmap(":/images/circle_cursor.png"), 0, 32)
        self.view.setCursor(cursor)
        self.set_active_tool(Scene.Ellipse)
        self.statusBar().showMessage("Current tool is Ellipse")
        self.scene.set_tool(Scene.Ellipse)
    
    def on_actionEraser_triggered(self):
        """Set eraser tool"""
        cursor = QCursor(QPixmap(":/images/eraser_cursor.png"), 32, 32)
        self.view.setCursor(cursor)
        self.set_active_tool(Scene.Eraser)
        self.statusBar().showMessage("Current tool is Eraser")
        self.scene.set_tool(Scene.Eraser)
    
    def on_actionPen_triggered(self):
        """Set pen tool"""
        cursor = QCursor(QPixmap(":/images/pen_cursor.png"), 0, 32)
        self.view.setCursor(cursor)
        self.set_active_tool(Scene.Pen)
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
        """Handle save button click"""
        filename, _ = QFileDialog.getSaveFileName(
            self, "Save File", "", "PainterApp (*.pa);;All Files (*)")
        if filename:
            if not filename.endswith('.pa'):
                filename += '.pa'
            self.scene.save_scene(filename)

    def on_actionLoad_triggered(self):
        """Handle load button click"""
        filename, _ = QFileDialog.getOpenFileName(
            self, "Open File", "", "PainterApp (*.pa);;All Files (*)")
        if filename:
            self.scene.load_scene(filename)
            
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
        """Handle undo button click"""
        self.scene.undo()

    def on_actionRedo_triggered(self):
        """Handle redo button click"""
        self.scene.redo()
    
    def on_penColorButton_clicked(self):
        """Handle pen color button click"""
        color = QColorDialog.getColor(QColor(Qt.GlobalColor.black), self)
        if color.isValid():
            self.scene.setPenColor(color)
            color_qss = f"background-color: {color.name()}"
            self.ui.penColorButton.setStyleSheet(color_qss)
    
    def on_penWidthSpinbox_valueChanged(self, value):
        """Handle pen width spinbox change"""
        self.scene.setPenWidth(value)
    
    def on_penStyleCombobox_activated(self, index):
        """Handle pen style combobox selection"""
        styles = [
            Qt.PenStyle.SolidLine,
            Qt.PenStyle.DashLine,
            Qt.PenStyle.DotLine,
            Qt.PenStyle.DashDotLine
        ]
        if 0 <= index < len(styles):
            self.scene.setPenStyle(styles[index])
    
    def on_brushColorButton_clicked(self):
        """Handle brush color button click"""
        color = QColorDialog.getColor(QColor(Qt.GlobalColor.black), self)
        if color.isValid():
            self.scene.setFillColor(color)
            color_qss = f"background-color: {color.name()}"
            self.ui.brushColorButton.setStyleSheet(color_qss)
            
            # Set the button color for the DragButton
            if hasattr(self.ui.brushColorButton, "set_button_color"):
                self.ui.brushColorButton.set_button_color(color)
    
    def on_brushStyleComboBox_activated(self, index):
        """Handle brush style combobox selection"""
        styles = [
            Qt.BrushStyle.SolidPattern,
            Qt.BrushStyle.Dense5Pattern,
            Qt.BrushStyle.HorPattern,
            Qt.BrushStyle.VerPattern,
            Qt.BrushStyle.CrossPattern
        ]
        if 0 <= index < len(styles):
            self.scene.setBrushStyle(styles[index])
    
    def on_showgridCheckbox_toggled(self, checked):
        """Handle show grid checkbox toggle"""
        self.view.set_draw_grid_lines(checked)
    
    def on_centerSceneButton_clicked(self):
        """Handle center scene button click"""
        self.view.centerOn(0, 0)
    
    def on_sceneBackgroundButton_clicked(self):
        """Handle scene background button click"""
        color = QColorDialog.getColor(QColor(Qt.GlobalColor.black), self)
        if color.isValid():
            self.view.setBackgroundColor(color)
            self.ui.sceneBackgroundButton.setStyleSheet(
                f"background-color: {color.name()}"
            )
    
    def set_active_tool(self, tool):
        """Update the toolbar icons based on the active tool"""
        # Reset all icons to inactive state
        self.ui.actionCursor.setIcon(QIcon(":/images/cursor.png"))
        self.ui.actionPen.setIcon(QIcon(":/images/pen.png"))
        self.ui.actionRectangle.setIcon(QIcon(":/images/rectangle1.png"))
        self.ui.actionEllipse.setIcon(QIcon(":/images/circle.png"))
        self.ui.actionStar.setIcon(QIcon(":/images/star.png"))
        self.ui.actionEraser.setIcon(QIcon(":/images/eraser.png"))
        
        # Set the active icon
        if tool == Scene.Cursor:
            self.ui.actionCursor.setIcon(QIcon(":/images/cursor_active.png"))
        elif tool == Scene.Pen:
            self.ui.actionPen.setIcon(QIcon(":/images/pen_active.png"))
        elif tool == Scene.Eraser:
            self.ui.actionEraser.setIcon(QIcon(":/images/eraser_active.png"))
        elif tool == Scene.Ellipse:
            self.ui.actionEllipse.setIcon(QIcon(":/images/circle_active.png"))
        elif tool == Scene.Star:
            self.ui.actionStar.setIcon(QIcon(":/images/star_active.png"))
        elif tool == Scene.Rect:
            self.ui.actionRectangle.setIcon(QIcon(":/images/rectangle1_active.png"))
    
    def on_actionCopy_triggered(self):
        """Copy selected items"""
        self.scene.copy()

    def on_actionCut_triggered(self):
        """Cut selected items"""
        self.scene.cut()

    def on_actionPaste_triggered(self):
        """Paste items from clipboard"""
        self.scene.paste()

    def on_actionLanguage_Settings_triggered(self):
        """Open language settings dialog"""
        dialog = SettingsDialog(self)
        dialog.exec()