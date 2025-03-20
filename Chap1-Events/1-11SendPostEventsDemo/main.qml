import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts

Window {
    id: mainWindow
    width: 400
    height: 300
    visible: true
    title: "Synthetic Event Example"
    
    // Container for our buttons
    ColumnLayout {
        anchors.centerIn: parent
        spacing: 20
        width: parent.width * 0.8
        
        // Custom button that will receive synthetic events
        CustomButton {
            id: button1
            text: "I am the phoenix king"
            Layout.alignment: Qt.AlignHCenter
            Layout.preferredWidth: 150
            Layout.preferredHeight: 28
        }
        
        // Regular button that will send events to the custom button
        Button {
            id: button2
            text: "Button2"
            Layout.alignment: Qt.AlignHCenter
            Layout.preferredWidth: 93
            Layout.preferredHeight: 28
            
            onClicked: {
                // Send a synthetic mouse event to button1
                eventBridge.sendSyntheticMousePress(button1)
            }
        }
        
        // Explanation text
        Text {
            text: "Click 'Button2' to send a synthetic mouse press event to the top button"
            wrapMode: Text.WordWrap
            horizontalAlignment: Text.AlignHCenter
            Layout.fillWidth: true
            Layout.topMargin: 20
        }
    }
}