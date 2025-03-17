import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts

Window {
    id: mainWindow
    width: 400
    height: 300
    visible: true
    title: "QML Widget with Event Filtering"
    
    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 20
        spacing: 15
        
        Text {
            Layout.fillWidth: true
            text: "Event Interception Demo"
            font.pixelSize: 18
            font.bold: true
        }
        
        Text {
            Layout.fillWidth: true
            text: "Enable event interception to block mouse clicks from reaching UI elements."
            wrapMode: Text.WordWrap
        }
        
        // Toggle switch to enable/disable event interception
        RowLayout {
            Layout.topMargin: 10
            Text {
                text: "Intercept Mouse Events:"
            }
            
            Switch {
                id: interceptSwitch
                onToggled: {
                    eventFilter.setInterceptEvents(checked)
                    statusText.text = checked ? 
                        "Event interception ON - mouse clicks are blocked" : 
                        "Event interception OFF - mouse clicks work normally"
                }
            }
        }
        
        Text {
            id: statusText
            Layout.fillWidth: true
            text: "Event interception OFF - mouse clicks work normally"
            color: interceptSwitch.checked ? "red" : "green"
            font.italic: true
        }
        
        // Button for testing
        Button {
            text: "Test Button - Click Me"
            Layout.alignment: Qt.AlignCenter
            Layout.topMargin: 20
            onClicked: eventLogger.log("Button was clicked!")
        }
        
        Item {
            Layout.fillHeight: true
        }
    }
}