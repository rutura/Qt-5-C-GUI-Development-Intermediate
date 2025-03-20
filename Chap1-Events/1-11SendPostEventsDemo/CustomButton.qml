import QtQuick
import QtQuick.Controls

// Custom button that logs mouse events
Button {
    id: customButton
    
    // Handle mouse events
    MouseArea {
        anchors.fill: parent
        hoverEnabled: true
        
        // Allow events to pass through to the button
        propagateComposedEvents: true
        
        onPressed: function(mouse) {
            eventBridge.log(`Button: Mouse press at ${mouse.x},${mouse.y}`)
            mouse.accepted = false  // Let the event pass through to the button
        }
        
        onReleased: function(mouse) {
            eventBridge.log(`Button: Mouse release at ${mouse.x},${mouse.y}`)
            mouse.accepted = false  // Let the event pass through to the button
        }
        
        onPositionChanged: function(mouse) {
            if (pressed) {
                eventBridge.log(`Button: Mouse move at ${mouse.x},${mouse.y}`)
            }
            mouse.accepted = false  // Let the event pass through to the button
        }
    }
}