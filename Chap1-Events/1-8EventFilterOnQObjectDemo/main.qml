import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts

Window {
    id: mainWindow
    width: 400
    height: 300
    visible: true
    title: "Keyboard Filter Example"
    
    // Use ColumnLayout to replicate the QVBoxLayout
    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 11
        spacing: 6
        
        // Button to remove the filter
        Button {
            id: removeFilterButton
            text: "Remove Filter"
            Layout.fillWidth: true
            
            onClicked: {
                keyboardFilter.removeFilter()
                text = "Filter Removed"
                reinstallButton.visible = true
                statusText.text = "Filter removed - you can now type numbers"
            }
        }
        
        // Button to reinstall the filter (initially hidden)
        Button {
            id: reinstallButton
            text: "Reinstall Filter"
            visible: false
            Layout.fillWidth: true
            
            onClicked: {
                keyboardFilter.installFilter()
                text = "Filter Reinstalled"
                removeFilterButton.text = "Remove Filter"
                statusText.text = "Filter active - numbers will be blocked"
            }
        }
        
        // Text field that will have the filter
        TextField {
            id: textInput
            objectName: "textInput"  // Used to find this object from Python
            placeholderText: "Type here (numbers will be blocked)"
            Layout.fillWidth: true
        }
        
        // Status text
        Text {
            id: statusText
            text: "Filter active - numbers will be blocked"
            Layout.fillWidth: true
            horizontalAlignment: Text.AlignHCenter
            Layout.topMargin: 20
        }
        
        // Explanation text
        Text {
            text: "This example demonstrates filtering keyboard events.\n" +
                  "The filter blocks numeric input in the text field."
            Layout.fillWidth: true
            wrapMode: Text.WordWrap
            horizontalAlignment: Text.AlignHCenter
            Layout.topMargin: 10
        }
        
        // Spacer
        Item {
            Layout.fillHeight: true
        }
    }
}