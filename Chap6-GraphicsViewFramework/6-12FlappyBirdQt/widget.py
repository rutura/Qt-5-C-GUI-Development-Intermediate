from PySide6.QtWidgets import QWidget, QGraphicsPixmapItem
from PySide6.QtCore import QPointF
from PySide6.QtGui import QPixmap
from ui_widget import Ui_Widget
from scene import Scene
import resource_rc  # Import resources

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Set up UI
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # Create and set up scene
        self.scene = Scene(self)
        self.scene.setSceneRect(-250, -300, 500, 600)
        
        # Add background
        pix_item = QGraphicsPixmapItem(QPixmap(":/images/sky.png"))
        self.scene.addItem(pix_item)
        pix_item.setPos(
            0 - pix_item.boundingRect().width()/2, 
            0 - pix_item.boundingRect().height()/2
        )
        
        # Connect scene to view
        self.ui.graphicsView.setScene(self.scene)
        
        # Add bird to scene
        self.scene.add_bird()
        
        # Connect start button
        self.ui.startGameButton.clicked.connect(self.on_start_game_button_clicked)
        
        # Set window title
        self.setWindowTitle("Flappy Bird Clone")
    
    def on_start_game_button_clicked(self):
        self.scene.start_game()