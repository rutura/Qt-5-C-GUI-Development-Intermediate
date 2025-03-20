import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts

Window {
    id: mainWindow
    width: 400
    height: 300
    visible: true
    title: "QML Widget"
    
    // ColumnLayout is the QML equivalent of QVBoxLayout
    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 11
        spacing: 6
        
        // Add our custom button
        CustomButton {
            text: "Button"
            Layout.alignment: Qt.AlignHCenter
            
            // Make the button a reasonable size
            implicitWidth: 200
            implicitHeight: 40
        }
        
        // Add explanation text
        Item {
            Layout.fillHeight: true
            Layout.fillWidth: true
            
            Text {
                anchors.centerIn: parent
                width: parent.width - 40
                wrapMode: Text.WordWrap
                horizontalAlignment: Text.AlignHCenter
                text: "This example demonstrates intercepting events in a custom button.\n\n" +
                      "When you click or double-click the button, it will log the event to the console " +
                      "through the custom event handler, similar to overriding the event() method in Qt Widgets."
            }
        }
    }
}