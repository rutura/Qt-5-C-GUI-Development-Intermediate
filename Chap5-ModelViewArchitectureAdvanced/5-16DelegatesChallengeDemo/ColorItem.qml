import QtQuick
import QtQuick.Controls

Rectangle {
    id: root
    
    property string colorName: "blue"
    property bool editable: true
    
    signal colorClicked()
    
    // Border for the colored rectangle
    color: colorName
    border.color: "#888"
    border.width: 1
    
    // White rectangle with text
    Rectangle {
        anchors.centerIn: parent
        width: colorText.width + 10
        height: colorText.height + 6
        color: "white"
        border.color: "#888"
        border.width: 1
        
        Text {
            id: colorText
            anchors.centerIn: parent
            text: colorName
            color: "black"
        }
    }
    
    // Mouse handling for editing
    MouseArea {
        anchors.fill: parent
        enabled: editable
        onClicked: {
            root.colorClicked()
        }
    }
}