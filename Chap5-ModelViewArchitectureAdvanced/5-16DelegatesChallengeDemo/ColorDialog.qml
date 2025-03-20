import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Dialog {
    id: root
    
    property string currentColor: "blue"
    property var colorList: []
    
    signal colorSelected(string color)
    
    title: "Select Color"
    standardButtons: Dialog.Ok | Dialog.Cancel
    modal: true
    
    width: 320
    height: 400
    
    onAccepted: {
        if (colorGrid.currentIndex >= 0) {
            colorSelected(colorList[colorGrid.currentIndex])
        }
    }
    
    ColumnLayout {
        anchors.fill: parent
        spacing: 10
        
        Label {
            text: "Current color:"
            font.bold: true
        }
        
        ColorItem {
            Layout.preferredWidth: parent.width
            Layout.preferredHeight: 40
            colorName: currentColor
            editable: false
        }
        
        Label {
            text: "Available colors:"
            font.bold: true
        }
        
        // Grid of color swatches
        GridView {
            id: colorGrid
            Layout.fillWidth: true
            Layout.fillHeight: true
            clip: true
            
            model: colorList
            cellWidth: width / 4
            cellHeight: 60
            
            delegate: Item {
                width: colorGrid.cellWidth
                height: colorGrid.cellHeight
                
                ColorItem {
                    anchors.fill: parent
                    anchors.margins: 4
                    colorName: modelData
                    
                    // Highlight current selection
                    Rectangle {
                        anchors.fill: parent
                        color: "transparent"
                        border.width: colorGrid.currentIndex === index ? 2 : 0
                        border.color: "#0066cc"
                    }
                    
                    onColorClicked: {
                        colorGrid.currentIndex = index
                    }
                }
            }
            
            ScrollBar.vertical: ScrollBar {}
        }
    }
}