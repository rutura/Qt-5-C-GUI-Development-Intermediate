import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.12

ApplicationWindow {
    id: window
    visible: true
    width: 800
    height: 600
    title: "Person Data"

    Rectangle {
        anchors.fill: parent
        color: "#f0f0f0"
        
        ColumnLayout {
            anchors.fill: parent
            anchors.margins: 10
            spacing: 10
            
            // Main content area
            Rectangle {
                Layout.fillWidth: true
                Layout.fillHeight: true
                color: "white"
                border.color: "#cccccc"
                
                // Official TableView component
                TableView {
                    id: tableView
                    anchors.fill: parent
                    anchors.margins: 1
                    clip: true
                    
                    // Connect to our model
                    model: personListModel
                    
                    // Define columns with appropriate sizes
                    columnWidthProvider: function(column) { 
                        // Default column widths
                        const columnWidths = [100, 100, 70, 120, 100, 100, 100, 100];
                        return columnWidths[column];
                    }
                    
                    rowHeightProvider: function(row) { 
                        return 30; // Fixed row height
                    }
                    
                    // Selected row
                    property int selectedRow: -1
                    
                    // Table header
                    Row {
                        id: headerRow
                        y: tableView.contentY
                        z: 2 // Above table content
                        
                        Repeater {
                            model: ["First Name", "Last Name", "Age", "Profession", "Status", "Country", "City", "Score"]
                            
                            Rectangle {
                                width: tableView.columnWidthProvider(index)
                                height: 40
                                color: "#e0e0e0"
                                border.width: 1
                                border.color: "#cccccc"
                                
                                Text {
                                    anchors.centerIn: parent
                                    text: modelData
                                    font.bold: true
                                }
                            }
                        }
                    }
                    
                    // Table cell delegate
                    delegate: Rectangle {
                        implicitWidth: tableView.columnWidthProvider(column)
                        implicitHeight: tableView.rowHeightProvider(row)
                        
                        // Alternating row colors with selection highlight
                        color: tableView.selectedRow === row ? "#d0d0ff" : (row % 2 === 0 ? "#ffffff" : "#f7f7f7")
                        border.width: 1
                        border.color: "#e0e0e0"
                        
                        Text {
                            anchors.right: parent.right
                            anchors.rightMargin: 10
                            anchors.verticalCenter: parent.verticalCenter
                            
                            // Use the fixed method with only 2 arguments
                            text: personListModel.getPersonDataAt(row, column)
                        }
                        
                        // Handle selection
                        MouseArea {
                            anchors.fill: parent
                            onClicked: {
                                tableView.selectedRow = row;
                                console.log("Selected row:", row);
                            }
                        }
                    }
                    
                    // Scroll bars
                    ScrollBar.vertical: ScrollBar {}
                    ScrollBar.horizontal: ScrollBar {}
                }
            }
            
            // Status bar
            Rectangle {
                Layout.fillWidth: true
                height: 30
                color: "#f5f5f5"
                border.color: "#e0e0e0"
                
                RowLayout {
                    anchors.fill: parent
                    anchors.leftMargin: 10
                    anchors.rightMargin: 10
                    
                    Text {
                        text: "Total records: " + personListModel.count
                        font.pixelSize: 12
                        color: "#606060"
                    }
                    
                    Item { Layout.fillWidth: true }
                    
                    // Selected item information
                    Text {
                        visible: tableView.selectedRow >= 0
                        text: tableView.selectedRow >= 0 ? 
                              "Selected: " + personListModel.getPersonName(tableView.selectedRow) : ""
                        font.pixelSize: 12
                        color: "#606060"
                    }
                }
            }
        }
    }
}