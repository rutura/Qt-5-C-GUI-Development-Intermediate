import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Dialogs
import Qt.labs.folderlistmodel

ApplicationWindow {
    id: window
    visible: true
    width: 600
    height: 400
    title: "File System Browser (Qt Quick)"

    // FolderListModel for file system access
    FolderListModel {
        id: folderModel
        folder: "file://" + currentDirPath
        showDirsFirst: true
        showDotAndDotDot: true
        nameFilters: ["*"]
    }

    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 10
        spacing: 10

        // Header with current path and navigation
        Rectangle {
            Layout.fillWidth: true
            height: 40
            color: "#f0f0f0"
            
            RowLayout {
                anchors.fill: parent
                anchors.margins: 5
                spacing: 5
                
                Button {
                    text: "⬆️ Up"
                    onClicked: {
                        // Go up one level
                        if (folderModel.parentFolder != "") {
                            folderModel.folder = folderModel.parentFolder
                        }
                    }
                }
                
                Label {
                    text: folderModel.folder.toString().replace("file://", "")
                    elide: Text.ElideMiddle
                    Layout.fillWidth: true
                }
            }
        }

        // Column headers
        Rectangle {
            Layout.fillWidth: true
            height: 30
            color: "#f5f5f5"
            
            RowLayout {
                anchors.fill: parent
                spacing: 5
                
                Text {
                    text: "Name"
                    font.bold: true
                    Layout.minimumWidth: 250
                    padding: 5
                }
                
                Text {
                    text: "Size"
                    font.bold: true
                    Layout.fillWidth: true
                    horizontalAlignment: Text.AlignRight
                    padding: 5
                }
            }
        }

        // File list
        ListView {
            id: listView
            Layout.fillWidth: true
            Layout.fillHeight: true
            model: folderModel
            clip: true
            
            delegate: Rectangle {
                id: delegateRect
                width: listView.width
                height: 30
                color: ListView.isCurrentItem ? "#e0e0e0" : (index % 2 === 0 ? "#f8f8f8" : "white")
                
                RowLayout {
                    anchors.fill: parent
                    anchors.leftMargin: 5
                    anchors.rightMargin: 5
                    spacing: 5
                    
                    // Folder/file icon
                    Text {
                        text: model.fileIsDir ? "📁" : "📄"
                        font.pixelSize: 14
                        Layout.leftMargin: 4
                    }
                    
                    // File name
                    Text {
                        text: model.fileName
                        font.pixelSize: 14
                        Layout.minimumWidth: 220
                        padding: 4
                    }
                    
                    // File size
                    Text {
                        text: !model.fileIsDir ? model.fileSize : ""
                        font.pixelSize: 14
                        Layout.fillWidth: true
                        horizontalAlignment: Text.AlignRight
                        elide: Text.ElideRight
                        padding: 4
                    }
                }
                
                MouseArea {
                    anchors.fill: parent
                    onClicked: {
                        listView.currentIndex = index
                    }
                    onDoubleClicked: {
                        if (model.fileIsDir) {
                            folderModel.folder = model.fileUrl
                        }
                    }
                }
            }
        }
        
        // Action buttons
        RowLayout {
            Layout.fillWidth: true
            Layout.preferredHeight: 40
            
            Item { Layout.fillWidth: true }  // Spacer
            
            Button {
                text: "Add Dir"
                onClicked: {
                    addDirDialog.open()
                }
            }
            
            Button {
                text: "Remove"
                enabled: listView.currentIndex >= 0
                onClicked: {
                    if (listView.currentIndex >= 0) {
                        var fileName = folderModel.get(listView.currentIndex, "fileName")
                        var isDir = folderModel.get(listView.currentIndex, "fileIsDir")
                        removeConfirmDialog.fileName = fileName
                        removeConfirmDialog.isDir = isDir
                        removeConfirmDialog.open()
                    }
                }
            }
        }
    }
    
    // Dialog for adding directory
    Dialog {
        id: addDirDialog
        title: "Create Directory"
        standardButtons: Dialog.Ok | Dialog.Cancel
        anchors.centerIn: parent
        
        ColumnLayout {
            width: parent.width
            
            TextField {
                id: dirNameField
                placeholderText: "Directory name"
                Layout.fillWidth: true
                focus: true
                onAccepted: addDirDialog.accept()
            }
        }
        
        onAccepted: {
            if (dirNameField.text.length > 0) {
                // Create a directory by modifying the model's nameFilters temporarily
                // This forces a refresh after operation
                var currentFilters = folderModel.nameFilters
                
                // Use system command to create directory
                var process = Qt.createQmlObject('import QtQuick; QtObject { 
                    property var xhr: new XMLHttpRequest();
                    function createDir(path, name) {
                        // This is a placeholder - in a real app, you would use proper file operations
                        console.log("Creating directory: " + name + " in " + path);
                        return true;
                    }
                }', addDirDialog)
                
                var currentPath = folderModel.folder.toString().replace("file://", "")
                var success = process.createDir(currentPath, dirNameField.text)
                
                if (success) {
                    // Force refresh by briefly changing nameFilters
                    folderModel.nameFilters = ["refresh_trigger"]
                    folderModel.nameFilters = currentFilters
                } else {
                    errorDialog.showError("Create Directory", "Failed to create directory")
                }
                
                dirNameField.text = ""
            }
        }
        
        onRejected: {
            dirNameField.text = ""
        }
    }
    
    // Confirmation dialog for removal
    Dialog {
        id: removeConfirmDialog
        title: "Confirm Delete"
        standardButtons: Dialog.Yes | Dialog.No
        anchors.centerIn: parent
        
        property string fileName: ""
        property bool isDir: false
        
        Text {
            text: removeConfirmDialog.isDir ? 
                  "Are you sure you want to delete the directory '" + removeConfirmDialog.fileName + "'?" :
                  "Are you sure you want to delete the file '" + removeConfirmDialog.fileName + "'?"
        }
        
        onAccepted: {
            // Create a temporary object to "perform" the operation
            var process = Qt.createQmlObject('import QtQuick; QtObject { 
                property var xhr: new XMLHttpRequest();
                function removeFile(name, isDir) {
                    // This is a placeholder - in a real app, you would use proper file operations
                    console.log("Removing " + (isDir ? "directory" : "file") + ": " + name);
                    return true;
                }
            }', removeConfirmDialog)
            
            var success = process.removeFile(removeConfirmDialog.fileName, removeConfirmDialog.isDir)
            
            if (success) {
                // Force refresh by briefly changing nameFilters
                var currentFilters = folderModel.nameFilters
                folderModel.nameFilters = ["refresh_trigger"]
                folderModel.nameFilters = currentFilters
            } else {
                errorDialog.showError("Delete", "Failed to delete " + removeConfirmDialog.fileName)
            }
        }
    }
    
    // Error dialog
    Dialog {
        id: errorDialog
        title: "Error"
        standardButtons: Dialog.Ok
        anchors.centerIn: parent
        
        Text {
            id: errorText
        }
        
        function showError(title, message) {
            errorDialog.title = title
            errorText.text = message
            errorDialog.open()
        }
    }
}