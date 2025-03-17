import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

// Custom ColorPicker component
Item {
    id: colorPicker
    implicitWidth: 300
    implicitHeight: 300
    
    // Signal to notify when a color is selected
    signal colorChanged(string colorName)
    
    // List of colors
    property var colorList: [
        "#FF0000", // red
        "#00FF00", // green
        "#0000FF", // blue
        "#00FFFF", // cyan
        "#8B0000", // darkRed
        "#A9A9A9", // darkGray
        "#808080", // gray
        "#FFFF00", // yellow
        "#8B8B00"  // darkYellow
    ]
    
    // Names for the buttons
    property var buttonNames: ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    // Current color
    property string currentColor: "#eeeab6"
    
    // Layout for the color picker
    ColumnLayout {
        anchors.fill: parent
        spacing: 10
        
        // Label to show the selected color
        Rectangle {
            id: colorLabel
            Layout.fillWidth: true
            Layout.preferredHeight: 50
            color: colorPicker.currentColor
            
            Text {
                anchors.centerIn: parent
                text: "Color"
                color: Qt.rgba(0, 0, 0, 0.7)
            }
        }
        
        // Grid layout for color buttons
        GridLayout {
            columns: 3
            rowSpacing: 5
            columnSpacing: 5
            Layout.fillWidth: true
            Layout.fillHeight: true
            
            // Create 9 buttons in a grid
            Repeater {
                model: 9
                
                Button {
                    text: colorPicker.buttonNames[index]
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                    background: Rectangle {
                        color: colorPicker.colorList[index]
                    }
                    
                    // When clicked, update the label color and emit the signal
                    onClicked: {
                        colorPicker.currentColor = colorPicker.colorList[index]
                        colorLabel.color = colorPicker.colorList[index]
                        
                        // Emit the signal
                        colorPicker.colorChanged(colorPicker.colorList[index])
                        
                        // Also send to our Python backend
                        colorHandler.colorChanged(colorPicker.colorList[index])
                    }
                }
            }
        }
    }
}