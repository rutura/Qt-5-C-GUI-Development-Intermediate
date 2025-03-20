import QtQuick
import QtQuick.Controls

// In QML, we "extend" components by wrapping them
ParentButton {
    id: childButton
    text: "Child Button"
    
    // Add additional mouse handling for child
    MouseArea {
        anchors.fill: parent
        onPressed: function(mouse) {
            eventLogger.log("ChildButton mousePressEvent called")
            // Allow event to propagate to parent
            mouse.accepted = false
        }
        onClicked: eventLogger.button_clicked()
    }
}