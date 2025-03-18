import QtQuick

Rectangle {
    id: root
    width: 300
    height: 300
    color: "transparent"
    border.color: "black"
    border.width: 1
    radius: 3
    
    // Counter for generating unique IDs
    property int iconCounter: 0
    
    // Reference to created components
    property var createdIcons: ({})
    
    // Create icons on component initialization
    Component.onCompleted: {
        createInitialIcons()
    }
    
    // Create the initial set of icons
    function createInitialIcons() {
        // Create Qt icon
        createIcon(resourceController.qtIconPath, 20, 20)
        
        // Create C++ icon
        createIcon(resourceController.cppIconPath, 150, 20)
        
        // Create Terminal icon
        createIcon(resourceController.terminalIconPath, 20, 150)
    }
    
    // Create a new icon at the specified position
    function createIcon(source, x, y) {
        var iconComponent = Qt.createComponent("DraggableIcon.qml")
        if (iconComponent.status === Component.Ready) {
            var iconId = "icon_" + iconCounter++
            var icon = iconComponent.createObject(root, {
                "x": x,
                "y": y,
                "source": source,
                "iconId": iconId
            })
            
            // Store reference to the created icon
            createdIcons[iconId] = icon
            return icon
        } else {
            console.error("Error creating icon component:", iconComponent.errorString())
            return null
        }
    }
    
    // DropArea to handle dropping icons
    DropArea {
        id: dropArea
        anchors.fill: parent
        
        // Handle entering the drop area
        onEntered: function(drag) {
            console.log("Drag entered with keys:", Object.keys(drag.keys))
            
            // Only highlight if it's our custom type
            if (drag.keys.indexOf("application/x-draggableicon") >= 0) {
                // Highlight the drop area
                root.border.color = "blue"
                root.border.width = 2
                drag.accepted = true
            } else {
                drag.accepted = false
            }
        }
        
        // Handle drag move events
        onPositionChanged: function(drag) {
            // We accept the drag if it's our custom type
            if (drag.keys.indexOf("application/x-draggableicon") >= 0) {
                drag.accepted = true
            } else {
                drag.accepted = false
            }
        }
        
        // Handle exiting the drop area
        onExited: function() {
            // Reset the highlight
            root.border.color = "black"
            root.border.width = 1
        }
        
        // Handle an item being dropped in the area
        onDropped: function(drop) {
            // Reset the highlight
            root.border.color = "black"
            root.border.width = 1
            
            console.log("Drop received, formats:", Object.keys(drop.keys))
            
            // Check if this is our custom mime type
            if (drop.keys.indexOf("application/x-draggableicon") >= 0) {
                var iconSource = drop.getDataAsString("iconSource")
                var sourceId = drop.getDataAsString("iconId")
                
                console.log("Creating new icon with source:", iconSource)
                
                // Create a new icon at the drop position
                var newIcon = createIcon(
                    iconSource,
                    drop.x - 32, // Center the icon at drop position
                    drop.y - 32
                )
                
                // If the drag operation was a move, accept as move
                if (drop.proposedAction === Qt.MoveAction) {
                    drop.acceptProposedAction()
                } else {
                    drop.accept(Qt.CopyAction)
                }
            } else {
                console.log("Drop with unsupported format")
                drop.accepted = false
            }
        }
    }
}