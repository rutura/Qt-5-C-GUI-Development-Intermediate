from PySide6.QtCore import QObject, Property, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QPixmap, QTransform
from PySide6.QtWidgets import QGraphicsPixmapItem

class BirdItem(QObject, QGraphicsPixmapItem):
    # Enum for wing positions
    class WingPosition:
        Up = 0
        Middle = 1
        Down = 2
    
    def __init__(self, pixmap):
        QObject.__init__(self)
        QGraphicsPixmapItem.__init__(self, pixmap)
        
        self.wing_position = self.WingPosition.Up
        self.wing_direction = 0  # 0: down, 1: up
        self.m_rotation = 0
        self.m_y = 0
        
        # Set up wing flapping animation timer
        from PySide6.QtCore import QTimer
        bird_wings_timer = QTimer(self)
        bird_wings_timer.timeout.connect(self.update_pixmap)
        bird_wings_timer.start(80)
        
        # Store ground position
        self.ground_position = self.scenePos().y() + 290
        
        # Y position animation
        self.y_animation = QPropertyAnimation(self, b"y", self)
        self.y_animation.setStartValue(self.scenePos().y())
        self.y_animation.setEndValue(self.ground_position)
        self.y_animation.setEasingCurve(QEasingCurve.InQuad)
        self.y_animation.setDuration(1000)
        
        # Rotation animation
        self.rotation_animation = QPropertyAnimation(self, b"rotation", self)
    
    def get_rotation(self):
        return self.m_rotation
    
    def get_y(self):
        return self.m_y
    
    def shoot_up(self):
        self.y_animation.stop()
        self.rotation_animation.stop()
        
        cur_pos_y = self.get_y()
        
        self.y_animation.setStartValue(cur_pos_y)
        # Make the bird jump higher (1/6 of screen height instead of 1/8)
        self.y_animation.setEndValue(cur_pos_y - self.scene().sceneRect().height()/6)
        self.y_animation.setEasingCurve(QEasingCurve.OutQuad)
        # Slightly longer jump duration for smoother movement
        self.y_animation.setDuration(300)
        
        self.y_animation.finished.connect(self.fall_to_ground_if_necessary)
        
        self.y_animation.start()
        
        self.rotate_to(-20, 200, QEasingCurve.OutCubic)
    
    def start_flying(self):
        self.y_animation.start()
        self.rotate_to(90, 1200, QEasingCurve.InQuad)
    
    def freeze_in_place(self):
        self.y_animation.stop()
        self.rotation_animation.stop()
    
    def set_rotation(self, rotation):
        self.m_rotation = rotation
        
        c = self.boundingRect().center()
        
        t = QTransform()
        t.translate(c.x(), c.y())
        t.rotate(rotation)
        t.translate(-c.x(), -c.y())
        self.setTransform(t)
    
    def set_y(self, y):
        self.moveBy(0, y - self.m_y)
        self.m_y = y
    
    def rotate_to(self, end, duration, curve):
        self.rotation_animation.setStartValue(self.get_rotation())
        self.rotation_animation.setEndValue(end)
        self.rotation_animation.setEasingCurve(curve)
        self.rotation_animation.setDuration(duration)
        
        self.rotation_animation.start()
    
    def fall_to_ground_if_necessary(self):
        if self.get_y() < self.ground_position:
            self.rotation_animation.stop()
            
            self.y_animation.setStartValue(self.get_y())
            self.y_animation.setEasingCurve(QEasingCurve.InQuad)
            self.y_animation.setEndValue(self.ground_position)
            # Slower falling for more reaction time
            self.y_animation.setDuration(1600)
            self.y_animation.start()
            
            self.rotate_to(90, 1100, QEasingCurve.InCubic)
    
    def update_pixmap(self):
        if self.wing_position == self.WingPosition.Middle:
            if self.wing_direction:
                # Up
                self.setPixmap(QPixmap(":/images/bird_blue_up.png"))
                self.wing_position = self.WingPosition.Up
                self.wing_direction = 0
            else:
                # Down
                self.setPixmap(QPixmap(":/images/bird_blue_down.png"))
                self.wing_position = self.WingPosition.Down
                self.wing_direction = 1
        else:
            self.setPixmap(QPixmap(":/images/bird_blue_middle.png"))
            self.wing_position = self.WingPosition.Middle
    
    # Define properties for animation
    rotation = Property(float, get_rotation, set_rotation)
    y = Property(float, get_y, set_y)