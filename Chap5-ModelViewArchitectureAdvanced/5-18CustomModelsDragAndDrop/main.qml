import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Window

Window {
    id: root
    visible: true
    width: 977
    height: 462
    title: "Drag and Drop Model Views"
    color: "#2D2D2D"  

    // Drag item for drag and drop operations
    Rectangle {
        id: dragItem
        width: 200
        height: 30
        color: "#4A90E2"  
        radius: 3
        opacity: 0.8
        visible: false
        z: 1000
        
        property string text: ""
        
        Text {
            anchors.centerIn: parent
            text: parent.text
            color: "white"
        }
        
        Drag.active: dragItem.visible
        Drag.hotSpot.x: width / 2
        Drag.hotSpot.y: height / 2
        Drag.keys: ["text/plain"]
        
        states: State {
            when: dragItem.Drag.active
            ParentChange {
                target: dragItem
                parent: root
            }
        }
    }

    RowLayout {
        anchors.fill: parent
        anchors.margins: 11
        spacing: 6

        // ListView 
        Rectangle {
            Layout.fillHeight: true
            Layout.fillWidth: true
            color: "#2D2D2D"
            border.color: "#3D3D3D"
            border.width: 1

            ListView {
                id: listView
                anchors.fill: parent
                model: personModel
                clip: true

                delegate: Rectangle {
                    width: listView.width
                    height: 30
                    color: "#2D2D2D"
                    
                    Text {
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.left: parent.left
                        anchors.leftMargin: 5
                        text: display
                        color: "white"
                    }

                    MouseArea {
                        anchors.fill: parent
                        drag.target: dragItem
                        
                        onPressed: function(mouse) {
                            dragItem.text = display;
                            dragItem.visible = true;
                            dragItem.x = mapToItem(root, mouse.x, mouse.y).x;
                            dragItem.y = mapToItem(root, mouse.x, mouse.y).y;
                        }
                        
                        onReleased: {
                            dragItem.visible = false;
                        }
                    }

                    DropArea {
                        anchors.fill: parent
                        keys: ["text/plain"]
                        
                        onEntered: function(drag) {
                            // Visual feedback
                            parent.color = "#3D3D3D";
                        }
                        
                        onExited: {
                            // Reset visual feedback
                            parent.color = "#2D2D2D";
                        }
                        
                        onDropped: function(drop) {
                            if (drop.hasText) {
                                var idx = personModel.index(index, 0);
                                personModel.setData(idx, drop.text);
                            }
                            // Reset visual feedback
                            parent.color = "#2D2D2D";
                        }
                    }
                }
            }
        }

        // TableView
        Rectangle {
            Layout.fillHeight: true
            Layout.fillWidth: true
            color: "#2D2D2D"
            border.color: "#3D3D3D"
            border.width: 1

            ColumnLayout {
                anchors.fill: parent
                spacing: 0

                // Header for TableView
                Rectangle {
                    Layout.fillWidth: true
                    height: 30
                    color: "#3D3D3D"
                    
                    Text {
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.left: parent.left
                        anchors.leftMargin: 5
                        text: "Names"
                        color: "white"
                        font.bold: true
                    }
                }

                // TableView content
                TableView {
                    id: tableView
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                    model: personModel
                    clip: true
                    
                    columnWidthProvider: function(column) {
                        return width;
                    }
                    
                    rowHeightProvider: function(row) {
                        return 30;
                    }
                    
                    delegate: Rectangle {
                        id: tableCell
                        implicitHeight: 30
                        color: "#2D2D2D"
                        border.color: "#3D3D3D"
                        border.width: 1
                        
                        Text {
                            anchors.verticalCenter: parent.verticalCenter
                            anchors.left: parent.left
                            anchors.leftMargin: 5
                            text: display
                            color: "white"
                        }
                        
                        MouseArea {
                            anchors.fill: parent
                            drag.target: dragItem
                            
                            onPressed: function(mouse) {
                                dragItem.text = display;
                                dragItem.visible = true;
                                var pos = mapToItem(root, mouse.x, mouse.y);
                                dragItem.x = pos.x;
                                dragItem.y = pos.y;
                            }
                            
                            onReleased: {
                                dragItem.visible = false;
                            }
                        }
                        
                        DropArea {
                            anchors.fill: parent
                            keys: ["text/plain"]
                            
                            onEntered: function(drag) {
                                // Visual feedback
                                tableCell.color = "#3D3D3D";
                            }
                            
                            onExited: {
                                // Reset visual feedback
                                tableCell.color = "#2D2D2D";
                            }
                            
                            onDropped: function(drop) {
                                if (drop.hasText) {
                                    try {
                                        var idx = personModel.index(row, 0);
                                        personModel.setData(idx, drop.text);
                                    } catch (e) {
                                        console.error("Error in drop handling:", e);
                                    }
                                }
                                // Reset visual feedback
                                tableCell.color = "#2D2D2D";
                            }
                        }
                    }
                }
            }
        }

        // TreeView
        Rectangle {
            Layout.fillHeight: true
            Layout.fillWidth: true
            color: "#2D2D2D"
            border.color: "#3D3D3D"
            border.width: 1

            ColumnLayout {
                anchors.fill: parent
                spacing: 0

                // Header for TreeView
                Rectangle {
                    Layout.fillWidth: true
                    height: 30
                    color: "#3D3D3D"
                    
                    Text {
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.left: parent.left
                        anchors.leftMargin: 5
                        text: "Names"
                        color: "white"
                        font.bold: true
                    }
                }
                
                // TreeView content
                TreeView {
                    id: treeView
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                    model: personModel
                    clip: true
                    
                    delegate: TreeViewDelegate {
                        indentation: 20
                        
                        contentItem: Rectangle {
                            id: treeItem
                            implicitHeight: 30
                            color: "#2D2D2D"
                            
                            Text {
                                anchors.verticalCenter: parent.verticalCenter
                                anchors.left: parent.left
                                anchors.leftMargin: 5
                                text: model.display
                                color: "white"
                            }
                            
                            MouseArea {
                                anchors.fill: parent
                                drag.target: dragItem
                                
                                onPressed: function(mouse) {
                                    dragItem.text = model.display;
                                    dragItem.visible = true;
                                    var pos = mapToItem(root, mouse.x, mouse.y);
                                    dragItem.x = pos.x;
                                    dragItem.y = pos.y;
                                }
                                
                                onReleased: {
                                    dragItem.visible = false;
                                }
                            }
                            
                            DropArea {
                                anchors.fill: parent
                                keys: ["text/plain"]
                                
                                onEntered: function(drag) {
                                    // Visual feedback
                                    treeItem.color = "#3D3D3D";
                                }
                                
                                onExited: {
                                    // Reset visual feedback
                                    treeItem.color = "#2D2D2D";
                                }
                                
                                onDropped: function(drop) {
                                    if (drop.hasText) {
                                        try {
                                            // For TreeView, we need to be careful with the model indexing
                                            var row = model.row !== undefined ? model.row : index;
                                            var idx = personModel.index(row, 0);
                                            personModel.setData(idx, drop.text);
                                        } catch (e) {
                                            console.error("Error in TreeView drop handling:", e);
                                        }
                                    }
                                    // Reset visual feedback
                                    treeItem.color = "#2D2D2D";
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}