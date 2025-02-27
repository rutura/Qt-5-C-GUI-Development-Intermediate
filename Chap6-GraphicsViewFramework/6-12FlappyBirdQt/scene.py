from PySide6.QtCore import QObject, QTimer, Qt
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtWidgets import (QGraphicsScene, QGraphicsPixmapItem, 
                              QGraphicsTextItem)

class Scene(QGraphicsScene):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Initialize variables
        self.game_on = False
        self.score = 0
        self.best_score = 0
        self.game_over_pix = None
        self.score_text_item = None
        self.bird = None
        
        # Set up pillar timer
        self.setup_pillar_timer()
    
    def add_bird(self):
        from birditem import BirdItem
        self.bird = BirdItem(QPixmap(":/images/bird_blue_up.png"))
        self.addItem(self.bird)
    
    def start_game(self):
        # Start bird flying
        self.bird.start_flying()
        
        # Handle pillars
        if not self.pillar_timer.isActive():
            self.clean_pillars()
            self.set_game_on(True)
            self.set_score(0)
            self.hide_game_over_graphics()
            # Add a 1.5 second delay before first pillar and more time between pillars
            self.game_start_delay = QTimer(self)
            self.game_start_delay.setSingleShot(True)
            self.game_start_delay.timeout.connect(lambda: self.pillar_timer.start(1800))
            self.game_start_delay.start(1500)
    
    def setup_pillar_timer(self):
        self.pillar_timer = QTimer(self)
        
        def create_pillar():
            from pillaritem import PillarItem
            pillar_item = PillarItem()
            pillar_item.collide_fail.connect(self.on_collision)
            self.addItem(pillar_item)
        
        self.pillar_timer.timeout.connect(create_pillar)
    
    def on_collision(self):
        self.pillar_timer.stop()
        self.freeze_bird_and_pillars_in_place()
        self.set_game_on(False)
        self.show_game_over_graphics()
    
    def freeze_bird_and_pillars_in_place(self):
        # Freeze bird
        self.bird.freeze_in_place()
        
        # Freeze pillars
        from pillaritem import PillarItem
        for item in self.items():
            if isinstance(item, PillarItem):
                item.freeze_in_place()
    
    def set_score(self, value):
        self.score = value
    
    def get_game_on(self):
        return self.game_on
    
    def set_game_on(self, value):
        self.game_on = value
    
    def increment_score(self):
        self.score += 1
        if self.score > self.best_score:
            self.best_score = self.score
        print(f"Score: {self.score} Best Score: {self.best_score}")
    
    def keyPressEvent(self, event):
        from PySide6.QtCore import Qt
        if event.key() == Qt.Key.Key_Space:
            if self.game_on:
                self.bird.shoot_up()
        super().keyPressEvent(event)
    
    def mousePressEvent(self, event):
        from PySide6.QtCore import Qt
        if event.button() == Qt.MouseButton.LeftButton:
            if self.game_on:
                self.bird.shoot_up()
        super().mousePressEvent(event)
    
    def show_game_over_graphics(self):
        # Add game over pixmap
        self.game_over_pix = QGraphicsPixmapItem(QPixmap(":/images/game_over_red.png"))
        self.addItem(self.game_over_pix)
        self.game_over_pix.setPos(
            0 - self.game_over_pix.boundingRect().width()/2, 
            0 - self.game_over_pix.boundingRect().height()/2
        )
        
        # Add score text
        self.score_text_item = QGraphicsTextItem()
        
        html_string = f"<p>Score: {self.score}</p><p>Best Score: {self.best_score}</p>"
        font = QFont("Consolas", 30, QFont.Bold)
        
        self.score_text_item.setHtml(html_string)
        self.score_text_item.setFont(font)
        from PySide6.QtCore import Qt
        self.score_text_item.setDefaultTextColor(Qt.yellow)
        self.addItem(self.score_text_item)
        
        self.score_text_item.setPos(
            0 - self.score_text_item.boundingRect().width()/2, 
            0 - self.game_over_pix.boundingRect().height()/2
        )
    
    def hide_game_over_graphics(self):
        if self.game_over_pix:
            self.removeItem(self.game_over_pix)
            self.game_over_pix = None
        
        if self.score_text_item:
            self.removeItem(self.score_text_item)
            self.score_text_item = None
    
    def clean_pillars(self):
        from pillaritem import PillarItem
        for item in list(self.items()):  # Make a copy to avoid modification during iteration
            if isinstance(item, PillarItem):
                self.removeItem(item)