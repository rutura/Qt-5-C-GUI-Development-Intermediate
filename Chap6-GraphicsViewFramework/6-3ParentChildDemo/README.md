# PySide6 Graphics Item Hierarchy - Implementation Guide

This guide demonstrates how to implement parent-child relationships between graphics items in PySide6's Graphics View Framework. This project shows how to create complex graphical objects by composing multiple items into hierarchies.

## Project Overview

This application demonstrates:
- Creating parent-child relationships between graphics items
- Including images from resources in a graphics scene
- Implementing a custom QGraphicsPixmapItem
- How parent transformations affect child items
- Show/hide and removal operations on item hierarchies

## Project Structure

```
graphics_item_hierarchy_demo/
│
├── main.py           # Application entry point
├── widget.py         # Main widget containing the scene and view
├── imageitem.py      # Custom image item implementation
├── resource.qrc      # Qt Resource Collection file
├── resource_rc.py    # Generated resource code
└── ui_widget.py      # Generated UI code from widget.ui
```

## Building and Running the Project

1. Generate UI Python files:
   ```bash
   pyside6-uic widget.ui -o ui_widget.py
   ```

2. Generate resource Python files:
   ```bash
   pyside6-rcc resource.qrc -o resource_rc.py
   ```

3. Run the application:
   ```bash
   python main.py
   ```

## Implementation Details

### Creating a Custom Image Item

The `ImageItem` class is a simple extension of `QGraphicsPixmapItem`:

```python
class ImageItem(QGraphicsPixmapItem):
    def __init__(self):
        super().__init__()
    
    def __del__(self):
        print("Image item deleted")
```

This class provides a way to create custom pixmap items and monitor their lifecycle.

### Setting Up the Item Hierarchy

The main widget creates a hierarchical structure of graphics items:

```python
# Create main rectangle that will be the parent item
self.rect1 = QGraphicsRectItem(-50, -50, 100, 100)
self.rect1.setFlag(QGraphicsRectItem.GraphicsItemFlag.ItemIsMovable)
self.rect1.setBrush(QBrush(Qt.yellow))

# Create first ellipse as a child of rect1
ellipse1 = QGraphicsEllipseItem(-20, -20, 40, 40)
ellipse1.setBrush(QBrush(Qt.red))
ellipse1.setParentItem(self.rect1)

# Create second ellipse as a child of rect1
ellipse2 = QGraphicsEllipseItem(20, 20, 20, 40)
ellipse2.setBrush(QBrush(Qt.green))
ellipse2.setParentItem(self.rect1)

# Create image item as a child of rect1
image_item = ImageItem()
image_item.setPixmap(QPixmap(":/images/Quick.png"))
image_item.setParentItem(self.rect1)
```

Note that only the parent item (`rect1`) is added to the scene directly - its children are automatically included through the parent-child relationship.

### Working with Resources

The application loads an image from Qt resources:

```python
# Load image from resources
image_item.setPixmap(QPixmap(":/images/Quick.png"))
```

To make this work, we need to:
1. Define a resource file (`resource.qrc`)
2. Compile it to Python code (`resource_rc.py`)
3. Import the resource module in our application

### Toggle and Remove Operations

The application demonstrates two operations on the item hierarchy:

```python
def on_showHideButton_clicked(self):
    """Toggle visibility of the rectangle and all its children"""
    is_visible = self.rect1.isVisible()
    self.rect1.setVisible(not is_visible)
    
def on_removeItem_clicked(self):
    """Remove the rectangle (and its children) from the scene"""
    self.scene.removeItem(self.rect1)
```

When a parent item's visibility is toggled, all child items are affected. Similarly, when a parent item is removed from the scene, all its children are removed as well.

## Key Concepts

### Parent-Child Relationships

In the Graphics View Framework, items can form parent-child relationships:

- **Parent Item**: An item that has one or more child items
- **Child Item**: An item that has a parent item

These relationships provide several benefits:

1. **Coordinate System**: Child items use the parent's coordinate system
2. **Transformations**: When a parent is moved, rotated, or scaled, all children are affected
3. **Visibility**: A child is only visible if its parent is visible
4. **Scene Membership**: Adding a parent to a scene adds all its children
5. **Stacking Order**: Child items are always drawn on top of their parent

### Setting Up Relationships

Parent-child relationships are established using `setParentItem()`:

```python
child_item.setParentItem(parent_item)
```

This makes `child_item` a child of `parent_item`. The child's position becomes relative to the parent's coordinate system.

### Coordinate Systems

Items in a hierarchy have different coordinate systems:

- **Scene Coordinates**: Global coordinates in the scene
- **Parent Coordinates**: Coordinates relative to the parent's position
- **Item Coordinates**: The item's local coordinate system

Methods to convert between these:

```python
# Scene to item coordinates
scene_pos = QPointF(100, 100)
item_pos = item.mapFromScene(scene_pos)

# Item to scene coordinates
item_pos = QPointF(0, 0)  # Center of the item
scene_pos = item.mapToScene(item_pos)

# Item to parent coordinates
parent_pos = item.mapToParent(QPointF(0, 0))
```

### Resource System

Qt's resource system allows embedding binary resources (like images) in your application:

1. **Create a qrc file** defining resources:
   ```xml
   <RCC>
       <qresource prefix="/">
           <file>images/Quick.png</file>
       </qresource>
   </RCC>
   ```

2. **Compile the qrc file** to Python:
   ```bash
   pyside6-rcc resource.qrc -o resource_rc.py
   ```

3. **Import the resource module** in your application:
   ```python
   import resource_rc
   ```

4. **Access resources** using the path defined in the qrc file:
   ```python
   pixmap = QPixmap(":/images/Quick.png")
   ```

## Advanced Techniques

### Custom Item Types

To create custom graphics items, you can subclass any of the standard items:

```python
class CustomRectItem(QGraphicsRectItem):
    def __init__(self):
        super().__init__()
        
    def paint(self, painter, option, widget):
        # Custom painting
        super().paint(painter, option, widget)
        
    def mousePressEvent(self, event):
        # Custom event handling
        super().mousePressEvent(event)
```

### Composite Items

For more complex items, create a composite structure:

```python
class CarItem(QGraphicsItem):
    def __init__(self):
        super().__init__()
        
        # Create body
        self.body = QGraphicsRectItem(0, 0, 100, 30, self)
        self.body.setBrush(QBrush(Qt.blue))
        
        # Create wheels
        self.wheel1 = QGraphicsEllipseItem(10, 25, 20, 20, self)
        self.wheel1.setBrush(QBrush(Qt.black))
        
        self.wheel2 = QGraphicsEllipseItem(70, 25, 20, 20, self)
        self.wheel2.setBrush(QBrush(Qt.black))
```

### Z-Value and Stacking Order

Control the stacking order of items using z-values:

```python
# Item with higher z-value appears on top
item1.setZValue(1)
item2.setZValue(2)  # This will be on top of item1
```

Within a parent-child relationship, child items are always drawn on top of their parent, regardless of z-values.

### Item Groups

You can also group items temporarily using `QGraphicsItemGroup`:

```python
group = scene.createItemGroup([item1, item2, item3])
# Move all items together
group.setPos(100, 100)
# Ungroup when done
scene.destroyItemGroup(group)
```

## Best Practices

1. **Design with Hierarchy in Mind**

   Plan your graphics items with parent-child relationships in mind:
   
   ```python
   # Good organization
   car_item = QGraphicsItem()
   car_body = QGraphicsRectItem(parent=car_item)
   wheel1 = QGraphicsEllipseItem(parent=car_item)
   wheel2 = QGraphicsEllipseItem(parent=car_item)
   ```

2. **Position Children Relative to Parent**

   Remember that child positions are relative to the parent:
   
   ```python
   # Position wheels relative to car body
   wheel1.setPos(10, 25)  # 10px from left of car, 25px from top
   wheel2.setPos(70, 25)  # 70px from left of car, 25px from top
   ```

3. **Handle Item Removal Carefully**

   Removing a parent item affects all its children:
   
   ```python
   # This removes all child items as well
   scene.removeItem(parent_item)
   
   # To keep children, reparent them first
   child_item.setParentItem(None)  # or another parent
   scene.removeItem(parent_item)
   ```

4. **Use Resource System for Images**

   Package images with your application using Qt's resource system:
   
   ```python
   # Load from resource instead of file system
   item.setPixmap(QPixmap(":/images/my_image.png"))
   ```

5. **Optimize Complex Hierarchies**

   For complex scenes with many items, consider:
   - Using `ItemIgnoresTransformations` for text or icons
   - Setting `ItemHasNoContents` for items that only serve as containers
   - Using `setVisible(False)` instead of removing and re-adding items

## Conclusion

The PySide6 Graphics View Framework provides powerful tools for creating complex graphical applications through item hierarchies. By understanding parent-child relationships, coordinate systems, and the resource system, you can create sophisticated interactive graphics.

This implementation demonstrates how to create a basic item hierarchy with a rectangle parent and multiple children (ellipses and an image). The project also shows how operations on parent items affect their children, such as visibility toggling and scene removal.

These techniques can be extended to create more complex graphical applications like diagrams, games, or visualization tools.