import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts

Window {
    id: mainWindow
    width: 600
    height: 400
    visible: true
    title: "Clipboard Image Paste Demo"
    color: "#f5f5f5"
    
    // Create a global shortcut handler
    Shortcut {
        sequence: StandardKey.Paste
        onActivated: {
            console.log("Paste shortcut activated")
            clipboardController.paste()
        }
    }
    
    // Main layout
    ColumnLayout {
        id: mainLayout
        anchors.fill: parent
        anchors.margins: 10
        spacing: 10
        
        // Image display area
        Rectangle {
            Layout.fillWidth: true
            Layout.fillHeight: true
            color: "white"
            border.color: "lightgray"
            border.width: 1
            
            // Label when no image is available
            Text {
                anchors.centerIn: parent
                text: "Press Ctrl+V to paste an image from clipboard"
                font.pixelSize: 14
                visible: !clipboardController.hasImage
            }
            
            // Image component for displaying pasted images
            Image {
                id: pastedImage
                anchors.fill: parent
                anchors.margins: 5
                source: clipboardController.imageUrl
                fillMode: Image.PreserveAspectFit
                visible: clipboardController.hasImage
                
                // When the source is invalid, hide the image
                onStatusChanged: {
                    if (status === Image.Error) {
                        visible = false;
                    }
                }
            }
            
            // Make it clickable to get focus
            MouseArea {
                anchors.fill: parent
                onClicked: parent.forceActiveFocus()
            }
        }
        
        // Alternative paste button
        Button {
            text: "Paste (Ctrl+V)"
            Layout.alignment: Qt.AlignHCenter
            onClicked: clipboardController.paste()
        }
    }
}