import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Controls.Basic

ApplicationWindow {
    id: window
    visible: true
    width: 938
    height: 388
    title: "Drag and Drop Demo"

    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 10
        spacing: 10

        // Header labels
        RowLayout {
            Layout.fillWidth: true
            spacing: 10

            Label {
                Layout.fillWidth: true
                text: "ListView [CAN DRAG] [CAN DROP]"
                horizontalAlignment: Text.AlignHCenter
            }

            Label {
                Layout.fillWidth: true
                text: "TableView [CAN DRAG] [CAN'T DROP]"
                horizontalAlignment: Text.AlignHCenter
            }

            Label {
                Layout.fillWidth: true
                text: "TreeView [CAN'T DRAG] [CAN DROP]"
                horizontalAlignment: Text.AlignHCenter
            }
        }

        // Views
        RowLayout {
            Layout.fillWidth: true
            Layout.fillHeight: true
            spacing: 10

            // List View with drag and drop capabilities
            Rectangle {
                Layout.fillWidth: true
                Layout.fillHeight: true
                border.color: "#cccccc"
                border.width: 1

                ListView {
                    id: listView
                    anchors.fill: parent
                    anchors.margins: 2
                    model: itemModel
                    spacing: 1
                    
                    // Enable drop
                    property int draggedItemIndex: -1
                    
                    DropArea {
                        anchors.fill: parent
                        
                        onEntered: function(drag) {
                            listView.draggedItemIndex = drag.source.itemIndex
                        }
                        
                        onDropped: function(drop) {
                            var dropIndex = listView.indexAt(drop.x, drop.y)
                            if (dropIndex === -1) dropIndex = listView.count - 1
                            dragDropController.moveItem(listView.draggedItemIndex, dropIndex)
                            listView.draggedItemIndex = -1
                        }
                    }

                    delegate: Item {
                        id: listItem
                        width: listView.width
                        height: 40
                        
                        property int itemIndex: index

                        Rectangle {
                            id: listRect
                            anchors.fill: parent
                            anchors.margins: 1
                            color: listDragArea.containsMouse ? "#f0f0f0" : "#ffffff"
                            border.color: "#eeeeee"
                            border.width: 1

                            Text {
                                anchors.fill: parent
                                anchors.leftMargin: 10
                                verticalAlignment: Text.AlignVCenter
                                text: model.display
                                elide: Text.ElideRight
                            }
                        }

                        MouseArea {
                            id: listDragArea
                            anchors.fill: parent
                            hoverEnabled: true
                            drag.target: model.canDrag ? listItem : undefined
                            
                            onReleased: {
                                if (model.canDrag) {
                                    listItem.Drag.drop()
                                }
                                listItem.x = 0
                                listItem.y = 0
                            }
                        }

                        Drag.active: listDragArea.drag.active
                        Drag.source: model.canDrag ? listItem : undefined
                        Drag.hotSpot.x: width / 2
                        Drag.hotSpot.y: height / 2
                        
                        states: [
                            State {
                                when: listDragArea.drag.active
                                ParentChange {
                                    target: listItem
                                    parent: window.contentItem
                                }
                                AnchorChanges {
                                    target: listItem
                                    anchors.horizontalCenter: undefined
                                    anchors.verticalCenter: undefined
                                }
                            }
                        ]
                    }
                }
            }

            // Table View
            Rectangle {
                Layout.fillWidth: true
                Layout.fillHeight: true
                border.color: "#cccccc"
                border.width: 1

                TableView {
                    id: tableView
                    anchors.fill: parent
                    anchors.margins: 2
                    model: itemModel
                    rowSpacing: 1
                    columnSpacing: 1

                    // Define a column for the display text
                    TableViewColumn {
                        title: "Display"
                        role: "display"
                        width: tableView.width
                    }

                    delegate: Item {
                        id: tableItem
                        implicitWidth: tableView.width
                        implicitHeight: 40
                        
                        property int itemIndex: row

                        Rectangle {
                            anchors.fill: parent
                            anchors.margins: 1
                            color: tableDragArea.containsMouse ? "#f0f0f0" : "#ffffff"
                            border.color: "#eeeeee"
                            border.width: 1

                            Text {
                                anchors.fill: parent
                                anchors.leftMargin: 10
                                verticalAlignment: Text.AlignVCenter
                                text: display
                                elide: Text.ElideRight
                            }
                        }

                        MouseArea {
                            id: tableDragArea
                            anchors.fill: parent
                            hoverEnabled: true
                            drag.target: canDrag ? tableItem : undefined
                            
                            onReleased: {
                                // No drop allowed for table items
                                tableItem.x = 0
                                tableItem.y = 0
                            }
                        }

                        Drag.active: tableDragArea.drag.active
                        Drag.source: canDrag ? tableItem : undefined
                        Drag.hotSpot.x: width / 2
                        Drag.hotSpot.y: height / 2
                        
                        states: [
                            State {
                                when: tableDragArea.drag.active
                                ParentChange {
                                    target: tableItem
                                    parent: window.contentItem
                                }
                                AnchorChanges {
                                    target: tableItem
                                    anchors.horizontalCenter: undefined
                                    anchors.verticalCenter: undefined
                                }
                            }
                        ]
                    }
                }
            }

            // Tree View
            Rectangle {
                Layout.fillWidth: true
                Layout.fillHeight: true
                border.color: "#cccccc"
                border.width: 1
                
                DropArea {
                    anchors.fill: parent
                    
                    onDropped: function(drop) {
                        var dropIndex = treeView.currentIndex != -1 ? treeView.currentIndex : itemModel.rowCount() - 1
                        dragDropController.moveItem(drop.source.itemIndex, dropIndex)
                    }
                }

                TreeView {
                    id: treeView
                    anchors.fill: parent
                    anchors.margins: 2
                    model: itemModel
                    
                    delegate: TreeViewDelegate {
                        id: treeDelegate
                        
                        Rectangle {
                            color: "#ffffff"
                            border.color: "#eeeeee"
                            border.width: 1
                            implicitWidth: treeView.width
                            implicitHeight: 40
                            
                            Text {
                                anchors.fill: parent
                                anchors.leftMargin: 10 + (treeDelegate.depth * 20) // Indent based on depth
                                verticalAlignment: Text.AlignVCenter
                                text: model.display || ""
                                elide: Text.ElideRight
                            }
                        }
                    }
                }
            }
        }
    }
}