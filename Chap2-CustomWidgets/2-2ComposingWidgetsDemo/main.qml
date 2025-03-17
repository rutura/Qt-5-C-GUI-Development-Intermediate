import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts

Window {
    id: mainWindow
    width: 400
    height: 500
    visible: true
    title: "Color Picker Example"
    
    // Main container
    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 11
        spacing: 6
        
        // Add our color picker
        ColorPicker {
            id: colorPicker
            Layout.fillWidth: true
            Layout.fillHeight: true
            
            // Handle the color changed signal from the color picker
            onColorChanged: function(colorName) {
                // Update status text
                statusText.text = "Selected color: " + colorName
            }
        }
        
        // Status text to show selected color
        Text {
            id: statusText
            text: "No color selected"
            Layout.fillWidth: true
            horizontalAlignment: Text.AlignHCenter
            padding: 10
        }
    }
}