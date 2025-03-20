import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    id: window
    visible: true
    width: 900
    height: 500
    title: "Custom Model Demo (Qt Quick)"

    // Person detail view
    Rectangle {
        id: detailView
        anchors.top: parent.top
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        width: 250
        color: "#f5f5f5"
        border.color: "#cccccc"
        border.width: 1
        visible: false
        
        property int selectedIndex: -1
        property string selectedName: ""
        property string selectedColor: "white"
        property int selectedAge: 0

        ColumnLayout {
            anchors.fill: parent
            anchors.margins: 15
            spacing: 15
            
            Text {
                text: "Person Details"
                font.pixelSize: 18
                font.bold: true
            }
            
            // Name
            ColumnLayout {
                Layout.fillWidth: true
                spacing: 5
                
                Text {
                    text: "Name:"
                    font.bold: true
                }
                
                Text {
                    text: detailView.selectedName
                    Layout.fillWidth: true
                    wrapMode: Text.WordWrap
                }
            }
            
            // Favorite Color
            ColumnLayout {
                Layout.fillWidth: true
                spacing: 5
                
                Text {
                    text: "Favorite Color:"
                    font.bold: true
                }
                
                Rectangle {
                    Layout.fillWidth: true
                    height: 30
                    color: detailView.selectedColor
                    border.color: "#888888"
                    border.width: 1
                    
                    Text {
                        anchors.centerIn: parent
                        text: detailView.selectedColor
                        color: isColorDark(detailView.selectedColor) ? "white" : "black"
                    }
                }
            }
            
            // Age
            ColumnLayout {
                Layout.fillWidth: true
                spacing: 5
                
                Text {
                    text: "Age:"
                    font.bold: true
                }
                
                Text {
                    text: detailView.selectedAge
                }
            }
            
            Item { Layout.fillHeight: true } // Spacer
        }
        // Function to determine if color is dark
        function isColorDark(colorString) {
            var color = Qt.color(colorString)
            var brightness = (color.r * 299 + color.g * 587 + color.b * 114) / 1000
            return brightness < 0.5
        }
    }
    // Connect to controller signal
    Connections {
        target: personController
        function onPersonSelected(index, name, favoriteColor, age) {
            detailView.selectedIndex = index
            detailView.selectedName = name
            detailView.selectedColor = favoriteColor
            detailView.selectedAge = age
            detailView.visible = true
        }
    }

    // Main content with three views
    RowLayout {
        anchors.fill: parent
        anchors.rightMargin: detailView.visible ? detailView.width : 0
        spacing: 5
        
        // ListView
        Rectangle {
            Layout.fillWidth: true
            Layout.fillHeight: true
            border.color: "#cccccc"
            border.width: 1
            
            ColumnLayout {
                anchors.fill: parent
                anchors.margins: 5
                spacing: 5
                
                Text {
                    text: "ListView"
                    font.bold: true
                    font.pixelSize: 14
                }
                
                ListView {
                    id: personListView
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                    model: personModel
                    clip: true
                    
                    delegate: Rectangle {
                        width: personListView.width
                        height: 40
                        color: personListView.currentIndex === index ? "#e0e0e0" : (index % 2 === 0 ? "#f8f8f8" : "white")
                        
                        Text {
                            anchors.fill: parent
                            anchors.margins: 10
                            text: name + " (" + age + ")"
                            verticalAlignment: Text.AlignVCenter
                            elide: Text.ElideRight
                        }
                        
                        MouseArea {
                            anchors.fill: parent
                            onClicked: {
                                personListView.currentIndex = index
                                personController.selectPerson(index)
                            }
                        }
                    }
                }
            }
        }
        
        // TableView-style
        Rectangle {
            Layout.fillWidth: true
            Layout.fillHeight: true
            border.color: "#cccccc"
            border.width: 1
            
            ColumnLayout {
                anchors.fill: parent
                anchors.margins: 5
                spacing: 5
                
                Text {
                    text: "TableView"
                    font.bold: true
                    font.pixelSize: 14
                }
                
                // Header row
                Rectangle {
                    Layout.fillWidth: true
                    height: 30
                    color: "#f0f0f0"
                    
                    RowLayout {
                        anchors.fill: parent
                        anchors.leftMargin: 5
                        anchors.rightMargin: 5
                        
                        Text {
                            text: "Name"
                            font.bold: true
                            Layout.preferredWidth: 150
                        }
                        
                        Text {
                            text: "Age"
                            font.bold: true
                            Layout.preferredWidth: 50
                        }
                        
                        Text {
                            text: "Favorite Color"
                            font.bold: true
                            Layout.fillWidth: true
                        }
                    }
                }
                
                ListView {
                    id: personTableView
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                    model: personModel
                    clip: true
                    
                    delegate: Rectangle {
                        width: personTableView.width
                        height: 40
                        color: personTableView.currentIndex === index ? "#e0e0e0" : (index % 2 === 0 ? "#f8f8f8" : "white")
                        
                        RowLayout {
                            anchors.fill: parent
                            anchors.leftMargin: 5
                            anchors.rightMargin: 5
                            
                            Text {
                                text: name
                                Layout.preferredWidth: 150
                                elide: Text.ElideRight
                            }
                            
                            Text {
                                text: age
                                Layout.preferredWidth: 50
                            }
                            
                            Rectangle {
                                Layout.fillWidth: true
                                Layout.preferredHeight: 24
                                color: favoriteColor
                                border.color: "#888888"
                                border.width: 1
                                
                                Text {
                                    anchors.centerIn: parent
                                    text: favoriteColor
                                    color: detailView.isColorDark(favoriteColor) ? "white" : "black"
                                }
                            }
                        }
                        
                        MouseArea {
                            anchors.fill: parent
                            onClicked: {
                                personTableView.currentIndex = index
                                personController.selectPerson(index)
                            }
                        }
                    }
                }
            }
        }
        
        // TreeView-style
        Rectangle {
            Layout.fillWidth: true
            Layout.fillHeight: true
            border.color: "#cccccc"
            border.width: 1
            
            ColumnLayout {
                anchors.fill: parent
                anchors.margins: 5
                spacing: 5
                
                Text {
                    text: "TreeView-style"
                    font.bold: true
                    font.pixelSize: 14
                }
                
                ListView {
                    id: personTreeView
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                    model: personModel
                    clip: true
                    
                    delegate: Column {
                        width: personTreeView.width
                        
                        Rectangle {
                            width: personTreeView.width
                            height: 30
                            color: personTreeView.currentIndex === index ? "#e0e0e0" : (index % 2 === 0 ? "#f8f8f8" : "white")
                            
                            RowLayout {
                                anchors.fill: parent
                                anchors.leftMargin: 5
                                anchors.rightMargin: 5
                                
                                Text {
                                    text: "👤"
                                    font.pixelSize: 16
                                    Layout.preferredWidth: 20
                                }
                                
                                Text {
                                    text: name
                                    Layout.fillWidth: true
                                    elide: Text.ElideRight
                                }
                            }
                            
                            MouseArea {
                                anchors.fill: parent
                                onClicked: {
                                    personTreeView.currentIndex = index
                                    personController.selectPerson(index)
                                    detailItem.expanded = !detailItem.expanded
                                }
                            }
                        }
                        
                        // Expandable item
                        Item {
                            id: detailItem
                            width: personTreeView.width
                            height: expanded ? 80 : 0
                            clip: true
                            property bool expanded: false
                            
                            Column {
                                anchors.fill: parent
                                anchors.leftMargin: 25
                                anchors.rightMargin: 5
                                spacing: 5
                                
                                Text {
                                    text: "Age: " + age
                                    leftPadding: 20
                                }
                                
                                RowLayout {
                                    width: parent.width
                                    height: 24
                                    
                                    Text {
                                        text: "Favorite Color: "
                                        leftPadding: 20
                                    }
                                    
                                    Rectangle {
                                        Layout.preferredWidth: 100
                                        Layout.preferredHeight: 24
                                        color: favoriteColor
                                        border.color: "#888888"
                                        border.width: 1
                                        
                                        Text {
                                            anchors.centerIn: parent
                                            text: favoriteColor
                                            color: detailView.isColorDark(favoriteColor) ? "white" : "black"
                                        }
                                    }
                                }
                            }
                            
                            Behavior on height {
                                NumberAnimation { duration: 200 }
                            }
                        }
                    }
                }
            }
        }
    }
}