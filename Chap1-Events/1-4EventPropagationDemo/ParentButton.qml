import QtQuick
import QtQuick.Controls

Button {
    // Default properties for all parent buttons
    width: 200
    height: 40
    
    // We need to override the mouse press event
    MouseArea {
        anchors.fill: parent
        onPressed: function(mouse) {
            eventLogger.log("ParentButton mousePressEvent Called")
            // Allow the event to propagate to the underlying button
            mouse.accepted = false
        }
    }
}