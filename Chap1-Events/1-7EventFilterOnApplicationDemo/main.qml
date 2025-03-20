import QtQuick
import QtQuick.Window
import QtQuick.Controls

Window {
    id: mainWindow
    width: 400
    height: 300
    visible: true
    title: "Event Filter Example"
    
    // Center the button in the window similar to the original layout
    Button {
        id: pushButton
        text: "PushButton"
        width: 93
        height: 28
        anchors.centerIn: parent
        
        onClicked: eventLogger.buttonClicked()
    }
    
    // Add an explanatory text
    Text {
        anchors {
            horizontalCenter: parent.horizontalCenter
            top: pushButton.bottom
            topMargin: 20
        }
        width: parent.width * 0.8
        horizontalAlignment: Text.AlignHCenter
        wrapMode: Text.WordWrap
        text: "When you click or double-click the button, the event filter will intercept the event before it reaches the button."
    }
}