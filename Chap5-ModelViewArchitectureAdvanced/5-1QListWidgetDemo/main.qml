import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts

Window {
    id: mainWindow
    width: 467
    height: 373
    visible: true
    title: "Fruit List Demo"
    color: "#2D2D2D"  
    
    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 0
        spacing: 0
        
        // Fruit list view
        ListView {
            id: fruitListView
            Layout.fillWidth: true
            Layout.fillHeight: true
            clip: true
            
            model: fruitModel
            
            // Add a scroll bar
            ScrollBar.vertical: ScrollBar {}
            
            // Handle selection
            currentIndex: -1
            onCurrentIndexChanged: {
                fruitController.selectedIndex = currentIndex
            }
            
            // Delegate for list items
            delegate: Rectangle {
                width: fruitListView.width
                height: 60
                color: ListView.isCurrentItem ? "#3D3D3D" : "#2D2D2D"
                
                // Layout for the icon and text
                RowLayout {
                    anchors.fill: parent
                    anchors.margins: 5
                    spacing: 10
                    
                    // Fruit icon
                    Image {
                        source: iconSource
                        Layout.preferredWidth: 50
                        Layout.preferredHeight: 50
                        fillMode: Image.PreserveAspectFit
                    }
                    
                    // Fruit text
                    Label {
                        text: display  // Uses the DisplayRole which returns "NameFunny"
                        Layout.fillWidth: true
                        font.pointSize: this.truncated ? 10 : 12
                        color: "white"
                        elide: Text.ElideRight
                    }
                }
                
                // Handle click to select the item
                MouseArea {
                    anchors.fill: parent
                    onClicked: {
                        fruitListView.currentIndex = index
                    }
                }
            }
        }
        
        // Read data button
        Button {
            id: readDataButton
            text: "Read Data"
            Layout.fillWidth: true
            Layout.minimumHeight: 40
            Layout.margins: 0
            
            onClicked: {
                var result = fruitController.readData()
                statusLabel.text = result
            }
        }
        
        // Status label 
        Label {
            id: statusLabel
            text: "No fruit selected"
            Layout.fillWidth: true
            Layout.minimumHeight: 20
            Layout.margins: 5
            horizontalAlignment: Text.AlignCenter
            font.italic: true
            color: "white"
            visible: true
        }
    }
}