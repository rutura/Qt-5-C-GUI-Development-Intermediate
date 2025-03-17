import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts

Window {
    id: mainWindow
    width: 400
    height: 300
    visible: true
    title: "QML Widget"
    
    // Use ColumnLayout to replicate the QVBoxLayout
    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 11
        spacing: 6
        
        // Add our custom components
        ChildButton {
            id: childButton
            Layout.fillWidth: true
            Layout.preferredHeight: 40
        }
        
        ChildLineEdit {
            id: childLineEdit
            Layout.fillWidth: true
            Layout.preferredHeight: 40
            placeholderText: "Type here (press Delete to clear)"
        }
        
        // Add some space at the bottom
        Item {
            Layout.fillHeight: true
        }
    }
}