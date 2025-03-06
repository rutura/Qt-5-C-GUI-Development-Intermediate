from PySide6.QtWidgets import QGraphicsPixmapItem

class ImageItem(QGraphicsPixmapItem):
    """
    A custom QGraphicsPixmapItem for displaying images in a graphics scene
    """
    def __init__(self):
        super().__init__()
    
    def __del__(self):
        print("Image item deleted")