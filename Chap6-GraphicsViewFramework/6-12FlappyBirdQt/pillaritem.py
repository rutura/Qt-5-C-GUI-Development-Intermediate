from PySide6.QtCore import QObject, Property, QPropertyAnimation, QEasingCurve, Signal
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QGraphicsItemGroup, QGraphicsPixmapItem
import random

class PillarItem(QObject, QGraphicsItemGroup):
    # Define Signal
    collide_fail = Signal()
    
    def __init__(self):
        QObject.__init__(self)
        QGraphicsItemGroup.__init__(self)
        
        # Create top and bottom pillars
        self.top_pillar = QGraphicsPixmapItem(QPixmap(":/images/pillar.png"))
        self.bottom_pillar = QGraphicsPixmapItem(QPixmap(":/images/pillar.png"))
        
        # Position top pillar with a larger gap (120 pixels instead of 60)
        self.top_pillar.setPos(
            0 - self.top_pillar.boundingRect().width()/2, 
            0 - self.top_pillar.boundingRect().height() - 120
        )
        
        # Position bottom pillar with a larger gap
        self.bottom_pillar.setPos(
            0 - self.bottom_pillar.boundingRect().width()/2, 
            120
        )
        
        # Add pillars to the group
        self.addToGroup(self.top_pillar)
        self.addToGroup(self.bottom_pillar)
        
        # Initialize variables
        self.past_bird = False
        self.m_x = 0
        
        # Generate random y position
        self.y_pos = random.randint(0, 150)
        x_randomizer = random.randint(0, 200)
        
        # Set initial position
        self.setPos(260 + x_randomizer, self.y_pos)
        
        # Set up animation for x position with slower movement (2500ms instead of 1500ms)
        self.x_animation = QPropertyAnimation(self, b"x", self)
        self.x_animation.setStartValue(260 + x_randomizer)
        self.x_animation.setEndValue(-260)
        self.x_animation.setEasingCurve(QEasingCurve.Linear)
        self.x_animation.setDuration(2500)
        
        # Connect finished signal to cleanup
        self.x_animation.finished.connect(self._on_animation_finished)
        
        # Start animation
        self.x_animation.start()
    
    def _on_animation_finished(self):
        print("Animation finished")
        self.scene().removeItem(self)
        self.deleteLater()
    
    def x(self):
        return self.m_x
    
    def freeze_in_place(self):
        self.x_animation.stop()
    
    def set_x(self, x):
        self.m_x = x
        
        # Check if passed the bird
        if x < 0 and not self.past_bird:
            self.past_bird = True
            scene = self.scene()
            # Use isinstance instead of dynamic_cast
            from scene import Scene
            if isinstance(scene, Scene):
                scene.increment_score()
        
        # Check collision with bird
        if self.collides_with_bird():
            self.collide_fail.emit()
        
        # Update position
        self.setPos(x, self.y_pos)
    
    def collides_with_bird(self):
        from birditem import BirdItem
        
        # Get colliding items
        colliding_items = self.top_pillar.collidingItems()
        colliding_items.extend(self.bottom_pillar.collidingItems())
        
        # Check for collision with bird
        for item in colliding_items:
            if isinstance(item, BirdItem):
                # Create a more forgiving collision by checking the actual distance
                # This adds a small buffer zone around the collision boundaries
                
                # Get bird center position
                bird_pos = item.scenePos()
                
                # Get pillar positions
                top_pillar_rect = self.top_pillar.sceneBoundingRect()
                bottom_pillar_rect = self.bottom_pillar.sceneBoundingRect()
                
                # Add a 5-pixel forgiveness margin to all sides
                top_pillar_rect.adjust(5, 5, -5, -5)
                bottom_pillar_rect.adjust(5, 5, -5, -5)
                
                # Check if bird is actually inside the adjusted rectangles
                if (top_pillar_rect.contains(bird_pos) or 
                    bottom_pillar_rect.contains(bird_pos)):
                    return True
                
                # If we reach here, it was a border collision that we're forgiving
                return False
        
        return False
    
    # Define property for animation
    x = Property(float, x, set_x)