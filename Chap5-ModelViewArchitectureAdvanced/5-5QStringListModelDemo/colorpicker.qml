import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    id: window
    visible: true
    width: 800
    height: 600
    title: "Color Picker Demo (Qt Quick)"

    RowLayout {
        anchors.fill: parent
        anchors.margins: 10
        spacing: 10

        // Color list
        Rectangle {
            Layout.preferredWidth: 250
            Layout.fillHeight: true
            border.color: "#cccccc"
            border.width: 1
            
            ListView {
                id: colorListView
                anchors.fill: parent
                anchors.margins: 2
                model: colorModel
                clip: true
                
                delegate: Rectangle {
                    width: colorListView.width
                    height: 40
                    color: colorListView.currentIndex === index ? "#e0e0e0" : "#ffffff"
                    
                    RowLayout {
                        anchors.fill: parent
                        anchors.leftMargin: 10
                        anchors.rightMargin: 10
                        
                        // Color swatch
                        Rectangle {
                            width: 24
                            height: 24
                            // Use display role directly
                            color: model.display
                            border.color: "#888888"
                            border.width: 1
                        }
                        
                        // Color name
                        Text {
                            Layout.fillWidth: true
                            // Use display role directly
                            text: model.display
                            font.pixelSize: 14
                            verticalAlignment: Text.AlignVCenter
                            elide: Text.ElideRight
                        }
                    }
                    
                    MouseArea {
                        anchors.fill: parent
                        onClicked: {
                            colorListView.currentIndex = index
                            colorController.selectColor(index)
                        }
                    }
                }
            }
        }
        
        // Color display
        Rectangle {
            id: colorDisplay
            Layout.fillWidth: true
            Layout.fillHeight: true
            color: "white"
            border.color: "#cccccc"
            border.width: 1
            
            property string selectedColorName: "white"
            
            Text {
                anchors.centerIn: parent
                text: colorDisplay.selectedColorName
                font.pixelSize: 18
                color: isDarkColor(colorDisplay.color) ? "white" : "black"
            }
            
            // Connect to controller signal
            Connections {
                target: colorController
                function onColorSelected(colorName) {
                    colorDisplay.color = colorName
                    colorDisplay.selectedColorName = colorName
                }
            }
        }
    }
    
    // Helper function to determine if a color is dark
    function isDarkColor(colorString) {
        // Simple algorithm to determine if text should be light or dark
        var color = Qt.color(colorString)
        var brightness = (color.r * 299 + color.g * 587 + color.b * 114) / 1000
        return brightness < 0.5
    }
    
    // Select the first color when the window loads
    Component.onCompleted: {
        if (colorModel.rowCount() > 0) {
            colorListView.currentIndex = 0
            colorController.selectColor(0)
        }
    }
}