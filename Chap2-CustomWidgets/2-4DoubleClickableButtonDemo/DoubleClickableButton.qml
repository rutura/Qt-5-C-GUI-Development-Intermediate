import QtQuick
import QtQuick.Controls

// Custom button that provides a double-click signal
Button {
    id: doubleClickableButton
    
    // Declare a custom signal for double-clicks
    signal doubleClicked()
    
    // Handle mouse area events to detect double-clicks
    MouseArea {
        anchors.fill: parent
        // Pass through normal single clicks to the button
        onClicked: mouse => mouse.accepted = false
        // Emit our custom signal on double-clicks
        onDoubleClicked: doubleClickableButton.doubleClicked()
    }
}