from PySide6.QtWidgets import QGraphicsItemGroup, QGraphicsLineItem
from PySide6.QtCore import QLineF
from PySide6.QtGui import QPen

class StrokeItem(QGraphicsItemGroup):
    """Item group for representing a stroke (collection of lines)"""
    
    # Define the type for the item
    StrokeType = 5  # From painterapptypes.h
    
    def __init__(self):
        super().__init__()
    
    def type(self):
        """Return the custom type for this item"""
        return self.StrokeType
    
    def to_data_stream(self, out):
        """Write the stroke item to a data stream"""
        # Write position
        pos_x = self.scenePos().x()
        pos_y = self.scenePos().y()
        out.writeFloat(pos_x)
        out.writeFloat(pos_y)
        
        # Write line count
        out.writeInt(len(self.childItems()))
        
        # Write Pen (from the first line)
        for item in self.childItems():
            if isinstance(item, QGraphicsLineItem):
                pen = item.pen()
                # Write pen properties
                out.writeInt(pen.color().red())
                out.writeInt(pen.color().green())
                out.writeInt(pen.color().blue())
                out.writeInt(pen.style())
                out.writeInt(pen.width())
                break
        
        # Write composing lines
        for item in self.childItems():
            if isinstance(item, QGraphicsLineItem):
                line = item.line()
                out.writeFloat(line.x1())
                out.writeFloat(line.y1())
                out.writeFloat(line.x2())
                out.writeFloat(line.y2())
    
    def from_data_stream(self, in_stream):
        """Read the stroke item from a data stream"""
        # Read position
        pos_x = in_stream.readFloat()
        pos_y = in_stream.readFloat()
        
        # Read line count
        line_count = in_stream.readInt()
        
        # Read pen properties
        red = in_stream.readInt()
        green = in_stream.readInt()
        blue = in_stream.readInt()
        pen_style = in_stream.readInt()
        pen_width = in_stream.readInt()
        
        # Create pen
        pen = QPen()
        pen.setColor(QColor(red, green, blue))
        pen.setStyle(pen_style)
        pen.setWidth(pen_width)
        
        # Read and create lines
        for i in range(line_count):
            x1 = in_stream.readFloat()
            y1 = in_stream.readFloat()
            x2 = in_stream.readFloat()
            y2 = in_stream.readFloat()
            
            line_item = QGraphicsLineItem(QLineF(x1, y1, x2, y2))
            line_item.setPen(pen)
            self.addToGroup(line_item)
        
        # Set position without offset
        self.setPos(pos_x, pos_y)

    