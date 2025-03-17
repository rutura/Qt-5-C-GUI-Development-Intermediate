import QtQuick
import QtQuick.Window
import QtQuick.Controls

Window {
    id: mainWindow
    width: 400
    height: 300
    visible: true
    title: "QML Widget"
    
    // This is used to handle all window events (similar to paintEvent)
    onVisibleChanged: {
        if (visible) {
            eventLogger.log("Paint event triggered")
        }
    }
    
    // For window resize events
    onWidthChanged: {
        eventLogger.log(`Widget resized, old size: ${width-1}x${height}`)
        eventLogger.log(`new size: ${width}x${height}`)
    }
    
    onHeightChanged: {
        eventLogger.log(`Widget resized, old size: ${width}x${height-1}`)
        eventLogger.log(`new size: ${width}x${height}`)
    }
    
    // For window close events
    onClosing: function(close) {
        eventLogger.log("Widget about to close")
        // close.accepted = false // Uncomment to prevent closing
    }
    
    // Main container that will receive key events
    Item {
        anchors.fill: parent
        focus: true  // Set focus on this Item instead of the Window
        
        // Key handling
        Keys.onPressed: function(event) {
            if (event.modifiers & Qt.ControlModifier) {
                eventLogger.log(`Control + ${event.text}`)
            }
            if (event.modifiers & Qt.AltModifier) {
                eventLogger.log(`Alt + ${event.text}`)
            }
            if (event.modifiers & Qt.ShiftModifier) {
                if (event.key === Qt.Key_A) {
                    eventLogger.log("Shift + A detected")
                }
                eventLogger.log(`Shift + ${event.text}`)
            }
        }
    }
    
    // Mouse area to handle mouse and wheel events
    MouseArea {
        id: mouseArea
        anchors.fill: parent
        hoverEnabled: true  // Needed for enter/exit events
        acceptedButtons: Qt.LeftButton | Qt.RightButton
        
        // Mouse events
        onPressed: function(mouse) {
            eventLogger.log(`Widget, Mouse Pressed at ${mouse.x},${mouse.y}`)
        }
        
        onReleased: function(mouse) {
            eventLogger.log(`Widget, Mouse Released at ${mouse.x},${mouse.y}`)
        }
        
        onPositionChanged: function(mouse) {
            if (pressed) {
                eventLogger.log(`Widget, Mouse Move at ${mouse.x},${mouse.y}`)
            }
        }
        
        // Enter/Leave events
        onEntered: {
            eventLogger.log("Enter event")
        }
        
        onExited: {
            eventLogger.log("Leave event")
        }
        
        // Wheel events
        onWheel: function(wheel) {
            let pixelDelta = wheel.pixelDelta.y ? 
                             `${wheel.pixelDelta.x},${wheel.pixelDelta.y}` : "0,0"
            eventLogger.log(`Wheel Event Delta: ${pixelDelta}`)
            eventLogger.log(`x: ${wheel.x}, y: ${wheel.y}`)
            eventLogger.log(`Orientation: ${wheel.angleDelta.x},${wheel.angleDelta.y}`)
        }
        
        // Context menu
        onClicked: function(mouse) {
            if (mouse.button === Qt.RightButton) {
                eventLogger.log("ContextMenu event")
                eventLogger.log(`Event x: ${mouse.x} event y: ${mouse.y}`)
                eventLogger.log("Event reason: 1") // 1 represents mouse trigger in Qt
                contextMenu.popup()
            }
        }
    }
    
    // Context menu implementation
    Menu {
        id: contextMenu
        
        MenuItem {
            text: "Action1"
            onTriggered: eventLogger.log("Action1 selected")
        }
        
        MenuItem {
            text: "Action2" 
            onTriggered: eventLogger.log("Action2 selected")
        }
    }
}