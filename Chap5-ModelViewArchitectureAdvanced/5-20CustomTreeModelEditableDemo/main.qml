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
                    
                    // Name field (editable)
                    TextField {
                        id: nameField
                        Layout.preferredWidth: 250
                        text: model.display
                        background: Rectangle {
                            color: "transparent"
                            border.color: nameField.activeFocus ? "#2196F3" : "transparent"
                        }
                        
                        onEditingFinished: {
                            personModel.editName(model.row, text)
                        }
                    }
                    
                    // Profession field(editable)
                    TextField {
                        id: professionField
                        Layout.fillWidth: true
                        text: model.profession
                        color: "#666666"
                        font.italic: true
                        background: Rectangle {
                            color: "transparent"
                            border.color: professionField.activeFocus ? "#2196F3" : "transparent"
                        }
                        
                        onEditingFinished: {
                            personModel.editProfession(model.row, text)
                        }
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