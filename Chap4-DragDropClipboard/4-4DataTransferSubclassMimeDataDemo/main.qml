import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts

Window {
    id: mainWindow
    width: 800
    height: 600
    visible: true
    title: "Drag and Drop with Custom MIME Data"
    color: "#f5f5f5"
    
    // Main layout
    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 10
        spacing: 10
        
        // Title text
        Text {
            Layout.fillWidth: true
            text: "Drag and drop icons between containers"
            font.pixelSize: 16
            horizontalAlignment: Text.AlignHCenter
        }
        
        // Container with two drag-drop areas side by side
        SplitView {
            Layout.fillWidth: true
            Layout.fillHeight: true
            orientation: Qt.Horizontal
            
            // Left container
            ContainerArea {
                id: leftContainer
                SplitView.minimumWidth: 150
                SplitView.preferredWidth: 380
                SplitView.fillHeight: true
            }
            
            // Right container
            ContainerArea {
                id: rightContainer
                SplitView.minimumWidth: 150
                SplitView.fillWidth: true
                SplitView.fillHeight: true
            }
        }
        
        // Instructions text
        Text {
            Layout.fillWidth: true
            text: "Drag icons to copy them. Hold Shift while dragging to move them instead."
            font.pixelSize: 12
            color: "#666666"
            horizontalAlignment: Text.AlignHCenter
        }
    }
}