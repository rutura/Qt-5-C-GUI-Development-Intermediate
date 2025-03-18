import QtQuick

Rectangle {
    id: root
    width: 300
    height: 300
    color: "transparent"
    
    // Counter for generating unique IDs
    property int iconCounter: 0
    
    // Reference to created components
    property var createdIcons: ({})
    
    // Create icons on component initialization
    Component.onCompleted: {
        createInitialIcons()
    }
    
    // Draw a border with rounded corners
    Rectangle {
        anchors.fill: parent
        anchors.margins: 5
        radius: 3
        color: "transparent"
        border.color: dropArea.containsDrag ? "blue" : "black"
        border.width: dropArea.containsDrag ? 2 : 1
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
                "iconId": iconId,
                "description": resourceController.getIconDescription(source)
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
        
        // Accept the drop if it has our custom format
        onEntered: function(drag) {
            if (drag.formats.indexOf("application/x-qml-icon-source") >= 0) {
                drag.accept();
                return;
            }
            drag.accepted = false;
        }
        
        // Handle an item being dropped in the area
        onDropped: function(drop) {
            // Check if this has our custom mime type
            if (drop.formats.indexOf("application/x-qml-icon-source") >= 0) {
                var iconSource = drop.getDataAsString("application/x-qml-icon-source");
                var description = drop.getDataAsString("text/plain");
                
                console.log("Creating new icon with source:", iconSource);
                
                // Create a new icon at the drop position
                var newIcon = createIcon(
                    iconSource,
                    drop.x - 32, // Center the icon at drop position
                    drop.y - 32
                );
                
                // If the drag operation was a move, accept as move
                if (drop.proposedAction === Qt.MoveAction) {
                    drop.acceptProposedAction();
                } else {
                    drop.accept(Qt.CopyAction);
                }
            } else {
                console.log("Drop with unsupported format");
                drop.accepted = false;
            }
        }
    }
}