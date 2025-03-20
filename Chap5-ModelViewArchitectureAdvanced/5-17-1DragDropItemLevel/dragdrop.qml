import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

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
                font.bold: true
            }

            Label {
                Layout.fillWidth: true
                text: "TableView [CAN DRAG] [CAN'T DROP]"
                horizontalAlignment: Text.AlignHCenter
                font.bold: true
            }

            Label {
                Layout.fillWidth: true
                text: "TreeView [CAN'T DRAG] [CAN DROP]"
                horizontalAlignment: Text.AlignHCenter
                font.bold: true
            }
        }

        // Views
        RowLayout {
            Layout.fillWidth: true
            Layout.fillHeight: true
            spacing: 10

            // List View - CAN DRAG, CAN DROP
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
                    spacing: 2
                    
                    // Enable drag and drop
                    property int draggedItemIndex: -1
                    
                    // This ListView can accept drops
                    DropArea {
                        anchors.fill: parent
                        onDropped: {
                            var dropIndex = listView.indexAt(listView.width/2, drop.y)
                            if (dropIndex === -1) dropIndex = listView.count
                            
                            if (drag.source.itemIndex !== undefined) {
                                dragDropController.moveItem(drag.source.itemIndex, dropIndex)
                            }
                        }
                    }

                    delegate: Rectangle {
                        id: listDelegate
                        width: ListView.view.width - 4
                        height: 40
                        color: "#ffffff"
                        border.color: "#e0e0e0"
                        border.width: 1
                        
                        property int itemIndex: index
                        property bool canDragItem: model.canDrag === true
                        property bool canDropItem: model.canDrop === true
                        
                        Text {
                            anchors.fill: parent
                            anchors.leftMargin: 10
                            verticalAlignment: Text.AlignVCenter
                            text: model.display || ""
                        }
                        
                        MouseArea {
                            id: dragArea
                            anchors.fill: parent
                            
                            drag.target: canDragItem ? parent : undefined
                            
                            onPressed: {
                                if (canDragItem) {
                                    listView.draggedItemIndex = index
                                    parent.grabToImage(function(result) {
                                        parent.Drag.imageSource = result.url
                                    }, Qt.size(parent.width, parent.height))
                                }
                            }
                            
                            onReleased: {
                                parent.Drag.drop()
                                parent.x = 0
                                parent.y = 0
                            }
                        }
                        
                        Drag.active: dragArea.drag.active && canDragItem
                        Drag.source: this
                        Drag.hotSpot.x: width / 2
                        Drag.hotSpot.y: height / 2
                    }
                }
            }

            // TableView - CAN DRAG, CAN'T DROP
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
                    
                    columnWidthProvider: function(column) {
                        return width
                    }
                    
                    rowHeightProvider: function(row) {
                        return 40
                    }
                    
                    delegate: Rectangle {
                        implicitWidth: tableView.width - 4
                        implicitHeight: 40
                        color: "#ffffff"
                        border.color: "#e0e0e0"
                        border.width: 1
                        
                        property int itemIndex: TableView.row
                        property bool canDragItem: model && model.canDrag === true
                        
                        Text {
                            anchors.fill: parent
                            anchors.leftMargin: 10
                            verticalAlignment: Text.AlignVCenter
                            text: model ? model.display || "" : ""
                        }
                        
                        MouseArea {
                            id: tableDragArea
                            anchors.fill: parent
                            
                            drag.target: canDragItem ? parent : undefined
                            
                            onPressed: {
                                if (canDragItem) {
                                    parent.grabToImage(function(result) {
                                        parent.Drag.imageSource = result.url
                                    }, Qt.size(parent.width, parent.height))
                                }
                            }
                            
                            onReleased: {
                                parent.Drag.drop()
                                parent.x = 0
                                parent.y = 0
                            }
                        }
                        
                        Drag.active: tableDragArea.drag.active && canDragItem
                        Drag.source: this
                        Drag.hotSpot.x: width / 2
                        Drag.hotSpot.y: height / 2
                    }
                }
            }

            // TreeView - CAN'T DRAG, CAN DROP
            Rectangle {
                Layout.fillWidth: true
                Layout.fillHeight: true
                border.color: "#cccccc"
                border.width: 1
                
                DropArea {
                    anchors.fill: parent
                    onDropped: function(drop) {
                        var dropY = drop.y
                        var dropIndex = Math.floor(dropY / 40)
                        
                        // Clamp to valid range
                        if (dropIndex < 0) dropIndex = 0
                        if (dropIndex >= itemModel.rowCount()) dropIndex = itemModel.rowCount()
                        
                        if (drop.source && drop.source.itemIndex !== undefined) {
                            dragDropController.moveItem(drop.source.itemIndex, dropIndex)
                        }
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
                            implicitWidth: treeView.width - 4
                            implicitHeight: 40
                            color: "#ffffff"
                            border.color: "#e0e0e0"
                            border.width: 1
                            
                            Text {
                                anchors.fill: parent
                                anchors.leftMargin: 10 + (treeDelegate.depth * 20)
                                verticalAlignment: Text.AlignVCenter
                                text: model ? model.display || "" : ""
                                elide: Text.ElideRight
                            }
                        }
                    }
                }
            }
        }
    }
}