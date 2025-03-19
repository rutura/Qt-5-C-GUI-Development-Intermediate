import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    visible: true
    width: 892
    height: 540
    title: "Drag and Drop Demo with ListView and TableView"

    RowLayout {
        anchors.fill: parent
        anchors.margins: 10
        spacing: 10

        // Color ListView
        Rectangle {
            Layout.fillHeight: true
            Layout.preferredWidth: 350
            border.color: "#cccccc"
            border.width: 1

            ListView {
                id: colorListView
                anchors.fill: parent
                anchors.margins: 2
                model: colorModel
                spacing: 2
                
                // Drop area
                DropArea {
                    anchors.fill: parent
                    onDropped: function(drop) {
                        var dropIndex = colorListView.indexAt(10, drop.y)
                        if (dropIndex === -1) dropIndex = colorListView.count
                        
                        if (drop.source && drop.source.itemIndex !== undefined) {
                            colorController.moveItem(drop.source.itemIndex, dropIndex)
                        }
                    }
                }

                delegate: Rectangle {
                    id: colorDelegate
                    width: ListView.view.width - 4
                    height: 40
                    color: model.color || "white"
                    border.color: "#e0e0e0"
                    border.width: 1
                    
                    property int itemIndex: index
                    
                    Text {
                        anchors.fill: parent
                        anchors.leftMargin: 10
                        verticalAlignment: Text.AlignVCenter
                        text: model.display || ""
                        color: Qt.rgba(0, 0, 0, 0.8)
                    }
                    
                    // Drag handling
                    MouseArea {
                        id: dragArea
                        anchors.fill: parent
                        
                        drag.target: parent
                        
                        onPressed: function(mouse) {
                            colorDelegate.grabToImage(function(result) {
                                colorDelegate.Drag.imageSource = result.url
                            }, Qt.size(colorDelegate.width, colorDelegate.height))
                        }
                        
                        onReleased: function() {
                            parent.Drag.drop()
                            parent.x = 0
                            parent.y = 0
                        }
                    }
                    
                    states: [
                        State {
                            when: dragArea.drag.active
                            PropertyChanges {
                                target: colorDelegate
                                opacity: 0.6
                                z: 10
                            }
                        }
                    ]
                    
                    Drag.active: dragArea.drag.active
                    Drag.source: colorDelegate
                    Drag.hotSpot.x: width / 2
                    Drag.hotSpot.y: height / 2
                }
            }
        }

        // TableView
        Rectangle {
            id: tableContainer
            Layout.fillHeight: true
            Layout.fillWidth: true
            border.color: "#cccccc"
            border.width: 1
            clip: true

            // Table header
            Rectangle {
                id: tableHeader
                width: parent.width
                height: 30
                color: "#f0f0f0"
                z: 2

                Row {
                    Repeater {
                        model: ["First Name", "Last Name", "Age", "Profession", "Marital Status", 
                                "Country", "City", "Social Score"]
                        
                        Rectangle {
                            width: {
                                switch (index) {
                                    case 0: return 100;
                                    case 1: return 100;
                                    case 2: return 50;
                                    case 3: return 100;
                                    case 4: return 120;
                                    case 5: return 100;
                                    case 6: return 100;
                                    case 7: return 80;
                                    default: return 100;
                                }
                            }
                            height: 30
                            border.color: "#d0d0d0"
                            
                            Text {
                                anchors.fill: parent
                                anchors.margins: 4
                                text: modelData
                                font.bold: true
                                horizontalAlignment: Text.AlignHCenter
                                verticalAlignment: Text.AlignVCenter
                            }
                        }
                    }
                }
            }
            
            // Drop area covering the table content
            DropArea {
                anchors.fill: parent
                anchors.topMargin: 30 // Below header
                
                onDropped: function(drop) {
                    var dropRow = Math.floor(drop.y / 40)
                    if (dropRow < 0) dropRow = 0
                    if (dropRow > tableModel.rowCount()) dropRow = tableModel.rowCount()
                    
                    if (drop.source && typeof drop.source.itemIndex !== 'undefined') {
                        tableController.moveRow(drop.source.itemIndex, dropRow)
                    }
                }
            }

            // Actual TableView
            TableView {
                id: tableView
                anchors.fill: parent
                anchors.topMargin: 30 // Below header
                model: tableModel
                
                columnWidthProvider: function(column) {
                    switch (column) {
                        case 0: return 100; // First Name
                        case 1: return 100; // Last Name
                        case 2: return 50;  // Age
                        case 3: return 100; // Profession
                        case 4: return 120; // Marital Status
                        case 5: return 100; // Country
                        case 6: return 100; // City
                        case 7: return 80;  // Social Score
                        default: return 100;
                    }
                }
                
                rowHeightProvider: function(row) {
                    return 40
                }
                
                // This is the cell delegate
                delegate: Rectangle {
                    id: cellDelegate
                    implicitWidth: tableView.columnWidthProvider(column)
                    implicitHeight: 40
                    color: "#ffffff"
                    border.color: "#e0e0e0"
                    
                    // Store row/column for drag reference
                    readonly property int row: TableView.row
                    readonly property int column: TableView.column
                    
                    Text {
                        anchors.fill: parent
                        anchors.margins: 4
                        text: display || ""
                        horizontalAlignment: Text.AlignRight
                        verticalAlignment: Text.AlignVCenter
                    }
                    
                    // Only allow drag on first column
                    MouseArea {
                        id: cellDragArea
                        anchors.fill: parent
                        visible: column === 0
                        
                        drag.target: visible ? dragProxy : undefined
                        
                        onPressed: function() {
                            if (column === 0) {
                                // Position the drag proxy
                                dragProxy.row = row
                                dragProxy.x = tableContainer.mapToItem(null, 0, 0).x
                                dragProxy.y = tableContainer.mapToItem(null, 0, parent.y).y
                                dragProxy.width = tableContainer.width
                                dragProxy.visible = true
                                
                                // Create visual feedback for dragging
                                dragProxy.grabToImage(function(result) {
                                    dragProxy.Drag.imageSource = result.url
                                }, Qt.size(dragProxy.width, dragProxy.height))
                            }
                        }
                        
                        onReleased: function() {
                            if (column === 0) {
                                dragProxy.Drag.drop()
                                dragProxy.visible = false
                            }
                        }
                    }
                }
            }
            
            // This rectangle is used as the drag visual/proxy
            Rectangle {
                id: dragProxy
                visible: false
                height: 40
                opacity: 0.8
                color: "#f8f8f8"
                border.color: "#0066cc"
                border.width: 2
                z: 100
                
                property int row: -1
                property int itemIndex: row
                
                Text {
                    anchors.centerIn: parent
                    text: dragProxy.row >= 0 ? "Row " + (dragProxy.row + 1) : ""
                    font.bold: true
                    color: "#0066cc"
                }
                
                Drag.active: dragProxy.visible
                Drag.source: dragProxy
                Drag.hotSpot.x: width / 2
                Drag.hotSpot.y: height / 2
            }
        }
    }
}