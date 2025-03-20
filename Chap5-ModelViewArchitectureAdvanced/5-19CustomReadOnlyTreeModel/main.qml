import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    visible: true
    width: 600
    height: 500
    title: "Family Tree Hierarchical Model"
    
    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 10
        
        TreeView {
            id: treeView
            Layout.fillWidth: true
            Layout.fillHeight: true
            
            clip: true
            model: personModel
            
            delegate: TreeViewDelegate {
                id: treeDelegate
                
                contentItem: RowLayout {
                    spacing: 10
                    
                    Label {
                        Layout.preferredWidth: 250
                        text: model.display
                        elide: Text.ElideRight
                        color: "#000000"
                    }
                    
                    Label {
                        Layout.fillWidth: true
                        text: model.profession
                        elide: Text.ElideRight
                        color: "#666666"
                        font.italic: true
                    }
                }
            }
            
            Component.onCompleted: {
                // Expand first level
                for (let i = 0; i < personModel.rowCount(); i++) {
                    treeView.expand(i)
                }
            }
        }
    }
}