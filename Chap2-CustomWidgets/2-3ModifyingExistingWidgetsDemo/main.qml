import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts

Window {
    id: mainWindow
    width: 260
    height: 120
    visible: true
    title: "Date Time Widget"
    
    // Container with padding
    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 11
        spacing: 6
        
        // Add our DateTimeWidget component
        DateTimeWidget {
            Layout.fillWidth: true
            Layout.fillHeight: true
        }
    }
}