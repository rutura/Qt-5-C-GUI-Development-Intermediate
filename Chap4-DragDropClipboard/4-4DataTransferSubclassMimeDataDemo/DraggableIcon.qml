import QtQuick

Item {
    id: root
    width: 64
    height: 64
    
    // Properties
    property string source: ""       // Image source
    property string iconId: ""       // Unique identifier for this icon
    property string description: ""  // Description of the icon
    property bool dragging: false
    
    // The actual image
    Image {
        id: iconImage
        anchors.fill: parent
        source: root.source
        sourceSize.width: 64
        sourceSize.height: 64
        smooth: true
        
        // Visual effect when being dragged
        opacity: root.dragging ? 0.5 : 1.0
    }
    
    // Component to handle drag operation
    Drag.hotSpot.x: width / 2
    Drag.hotSpot.y: height / 2
    
    // Use mimeData to store our custom data
    Drag.mimeData: {
        "text/plain": root.description,
        "application/x-qml-icon-source": root.source
    }
    
    Drag.dragType: Drag.Automatic
    Drag.supportedActions: Qt.CopyAction | Qt.MoveAction
    Drag.proposedAction: Qt.CopyAction
    
    // Allow dragging when a mouse is pressed over the icon
    MouseArea {
        id: mouseArea
        anchors.fill: parent
        
        drag.target: parent
        drag.threshold: 5
        
        onPressed: function(mouse) {
            root.z = 10  // Bring to front when dragging
        }
        
        onPositionChanged: function(mouse) {
            if (pressed && !root.dragging && drag.active) {
                root.dragging = true
                
                // Manually activate drag instead of binding
                root.Drag.active = true
                
                // Set action based on Shift key (move vs copy)
                if (mouse.modifiers & Qt.ShiftModifier) {
                    root.Drag.proposedAction = Qt.MoveAction
                } else {
                    root.Drag.proposedAction = Qt.CopyAction
                }
            }
        }
        
        onReleased: function() {
            if (root.dragging) {
                // End the active drag
                var result = root.Drag.drop()
                
                // Turn off dragging flag
                root.Drag.active = false
                root.dragging = false
                
                // If this was dropped in a valid drop area with move action
                if (result === Qt.MoveAction) {
                    // Only destroy the item if it was a move
                    root.destroy()
                } else {
                    // Reset z-order
                    root.z = 1
                }
            } else {
                root.z = 1
            }
        }
    }
}