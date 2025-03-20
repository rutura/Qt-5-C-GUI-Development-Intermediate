import QtQuick 
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    id: window
    visible: true
    width: 600
    height: 400
    title: "Organization Tree (Qt Quick)"

    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 10
        spacing: 0

        // Header
        Rectangle {
            Layout.fillWidth: true
            height: 30
            color: "#f0f0f0"
            
            RowLayout {
                anchors.fill: parent
                spacing: 5
                
                Text {
                    text: "Organization"
                    font.bold: true
                    Layout.minimumWidth: 250
                    padding: 5
                }
                
                Text {
                    text: "Description"
                    font.bold: true
                    Layout.fillWidth: true
                    padding: 5
                }
            }
        }
        
        // Tree view using built-in TreeView
        TreeView {
            id: treeView
            Layout.fillWidth: true
            Layout.fillHeight: true
            
            // Use the model directly, not a property of it
            model: organizationModel
            
            // Keep track of selected index
            property var selectedIndex: null
            
            delegate: TreeViewDelegate {
                id: treeDelegate
                
                // Indent based on depth
                indentation: model.depth * 12
                
                contentItem: RowLayout {
                    spacing: 4
                    
                    // Folder/organization icon
                    Text {
                        text: "🏢"
                        font.pixelSize: 14
                        Layout.leftMargin: 4
                    }
                    
                    // Organization name
                    Text {
                        text: model ? model.name : ""
                        font.bold: treeView.selectedIndex === treeDelegate.index
                        font.pixelSize: 14
                        Layout.minimumWidth: 220
                        padding: 4
                    }
                    
                    // Description
                    Text {
                        text: model ? model.description : ""
                        font.pixelSize: 14
                        Layout.fillWidth: true
                        elide: Text.ElideRight
                        padding: 4
                    }
                }
                
                // Handle selection
                onClicked: {
                    treeView.selectedIndex = treeDelegate.index
                    orgController.onOrganizationSelected(model.name, model.description)
                }
                
                // When expanded state changes, notify controller
                onExpandedChanged: {
                    orgController.toggleExpanded(treeDelegate.index)
                }
            }
        }
        
        // Status bar to match widget version
        Rectangle {
            Layout.fillWidth: true
            height: 30
            color: "#f5f5f5"
            border.color: "#e0e0e0"
            
            Text {
                anchors.verticalCenter: parent.verticalCenter
                anchors.left: parent.left
                anchors.leftMargin: 10
                text: "Click an organization to see details in console"
                font.pixelSize: 12
                color: "#606060"
            }
        }
    }
}