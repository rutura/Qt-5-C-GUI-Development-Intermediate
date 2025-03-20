import QtQuick
import QtQuick.Controls

// Custom button component that intercepts events
Button {
    id: customButton
    
    // In QML we can't directly override the event method like in Qt Widgets
    // Instead, we'll use a MouseArea to capture the events
    
    // This allows us to intercept mouse events before they reach the Button's handlers
    MouseArea {
        id: eventInterceptor
        anchors.fill: parent
        
        // We need to handle these events
        onPressed: function(mouse) {
            eventLogger.log("Button: mouse press detected")
            
            // Pass the event to the parent Button (don't consume it)
            // This is equivalent to returning false from event() in Qt
            mouse.accepted = false
        }
        
        onDoubleClicked: function(mouse) {
            eventLogger.log("Button: doubleclick detected")
            
            // Pass the event to the parent Button (don't consume it)
            // This is equivalent to returning false from event() in Qt
            mouse.accepted = false
        }
    }
    
    // Connect the button's click signal to our handler
    onClicked: eventLogger.buttonClicked()
}