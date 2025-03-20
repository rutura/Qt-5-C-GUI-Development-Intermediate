import QtQuick
import QtQuick.Controls

// Custom component for displaying a color in the same style as the PersonDelegate
Rectangle {
    id: root
    property string colorName: ""
    
    // Fill with the specified color
    color: colorName
    border.color: "#888"
    border.width: 1
    
    // Central white rectangle with text
    Rectangle {
        anchors.centerIn: parent
        width: textLabel.width + 10
        height: textLabel.height + 6
        color: "white"
        border.color: "#888"
        border.width: 1
        
        // Color name text
        Text {
            id: textLabel
            anchors.centerIn: parent
            text: colorName
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            elide: Text.ElideRight
        }
    }
}