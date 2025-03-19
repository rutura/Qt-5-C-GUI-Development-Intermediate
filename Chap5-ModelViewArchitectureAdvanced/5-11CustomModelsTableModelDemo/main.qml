import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Dialogs
import Qt.labs.qmlmodels

ApplicationWindow {
    visible: true
    width: 940
    height: 460
    title: "Person Management (Qt Quick)"
    
    // Track selection state
    property int selectedPersonIndex: -1
    
    // Dialog for adding a new person
    Dialog {
        id: addPersonDialog
        title: "Add New Person"
        standardButtons: Dialog.Ok | Dialog.Cancel
        modal: true
        
        property alias nameText: nameField.text
        property alias ageValue: ageSpinBox.value
        
        onAccepted: {
            if (nameText.length > 0) {
                personController.addPerson(nameText, ageValue)
                nameText = ""
            } else {
                errorDialog.text = "Please enter a name"
                errorDialog.open()
            }
        }
        
        ColumnLayout {
            width: parent.width
            spacing: 10
            
            Label { text: "Person Name:" }
            TextField {
                id: nameField
                Layout.fillWidth: true
                placeholderText: "Enter name"
            }
            
            Label { text: "Age:" }
            SpinBox {
                id: ageSpinBox
                Layout.fillWidth: true
                from: 15
                to: 120
                value: 30
            }
        }
    }
    
    // Error dialog
    Dialog {
        id: errorDialog
        title: "Error"
        standardButtons: Dialog.Ok
        modal: true
        
        property alias text: errorText.text
        
        Label {
            id: errorText
            width: parent.width
            wrapMode: Text.WordWrap
        }
    }
    
    // Main layout
    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 10
        spacing: 6
        
        // Header row
        RowLayout {
            Layout.fillWidth: true
            
            Label {
                text: "ListView"
                Layout.fillWidth: true
                font.bold: true
                horizontalAlignment: Text.AlignHCenter
            }
            
            Label {
                text: "TableView"
                Layout.fillWidth: true
                font.bold: true
                horizontalAlignment: Text.AlignHCenter
            }
            
            Label {
                text: "ListView as Tree"
                Layout.fillWidth: true
                font.bold: true
                horizontalAlignment: Text.AlignHCenter
            }
        }
        
        // Main content row
        RowLayout {
            Layout.fillWidth: true
            Layout.fillHeight: true
            spacing: 6
            
            // ListView
            Rectangle {
                Layout.fillWidth: true
                Layout.fillHeight: true
                color: "white"
                border.color: "#ccc"
                
                ListView {
                    id: listView
                    anchors.fill: parent
                    anchors.margins: 1
                    model: personModel
                    clip: true
                    
                    delegate: Rectangle {
                        width: ListView.view.width
                        height: 40
                        color: ListView.isCurrentItem ? "#e0e0e0" : (index % 2 === 0 ? "#f8f8f8" : "white")
                        
                        Text {
                            anchors.fill: parent
                            anchors.leftMargin: 5
                            verticalAlignment: Text.AlignVCenter
                            text: names
                            elide: Text.ElideRight
                        }
                        
                        MouseArea {
                            anchors.fill: parent
                            onClicked: {
                                selectedPersonIndex = index
                                listView.currentIndex = index
                                personController.selectPerson(index)
                            }
                        }
                    }
                    
                    ScrollBar.vertical: ScrollBar {}
                }
            }
            
            // TableView
            Rectangle {
                Layout.fillWidth: true
                Layout.fillHeight: true
                color: "white"
                border.color: "#ccc"
                
                TableView {
                    id: tableView
                    anchors.fill: parent
                    anchors.margins: 1
                    clip: true
                    model: personModel
                    
                    // Use JavaScript array as column widths
                    property var columnWidths: [0.6, 0.2, 0.2]
                    
                    // Set up column widths
                    columnWidthProvider: function(column) {
                        return width * columnWidths[column]
                    }
                    
                    // Table header
                    Row {
                        id: header
                        y: tableView.contentY
                        z: 2
                        
                        Rectangle {
                            width: tableView.width * tableView.columnWidths[0]
                            height: 30
                            color: "#f0f0f0"
                            
                            Text {
                                anchors.fill: parent
                                anchors.leftMargin: 5
                                text: "Name"
                                font.bold: true
                                verticalAlignment: Text.AlignVCenter
                            }
                        }
                        
                        Rectangle {
                            width: tableView.width * tableView.columnWidths[1]
                            height: 30
                            color: "#f0f0f0"
                            
                            Text {
                                anchors.fill: parent
                                anchors.leftMargin: 5
                                text: "Age"
                                font.bold: true
                                verticalAlignment: Text.AlignVCenter
                            }
                        }
                        
                        Rectangle {
                            width: tableView.width * tableView.columnWidths[2]
                            height: 30
                            color: "#f0f0f0"
                            
                            Text {
                                anchors.fill: parent
                                anchors.leftMargin: 5
                                text: "Color"
                                font.bold: true
                                verticalAlignment: Text.AlignVCenter
                            }
                        }
                    }
                    
                    // Use DelegateChooser for different columns
                    delegate: DelegateChooser {
                        DelegateChoice {
                            column: 0
                            delegate: Rectangle {
                                implicitHeight: 40
                                color: selectedPersonIndex === row ? "#e0e0e0" : (row % 2 === 0 ? "#f8f8f8" : "white")
                                
                                Text {
                                    anchors.fill: parent
                                    anchors.leftMargin: 5
                                    text: names
                                    verticalAlignment: Text.AlignVCenter
                                    elide: Text.ElideRight
                                }
                                
                                MouseArea {
                                    anchors.fill: parent
                                    onClicked: {
                                        selectedPersonIndex = row
                                        listView.currentIndex = row
                                        personController.selectPerson(row)
                                    }
                                }
                            }
                        }
                        
                        DelegateChoice {
                            column: 1
                            delegate: Rectangle {
                                implicitHeight: 40
                                color: selectedPersonIndex === row ? "#e0e0e0" : (row % 2 === 0 ? "#f8f8f8" : "white")
                                
                                Text {
                                    anchors.fill: parent
                                    anchors.leftMargin: 5
                                    text: age
                                    verticalAlignment: Text.AlignVCenter
                                }
                                
                                MouseArea {
                                    anchors.fill: parent
                                    onClicked: {
                                        selectedPersonIndex = row
                                        listView.currentIndex = row
                                        personController.selectPerson(row)
                                    }
                                }
                            }
                        }
                        
                        DelegateChoice {
                            column: 2
                            delegate: Rectangle {
                                implicitHeight: 40
                                color: selectedPersonIndex === row ? "#e0e0e0" : (row % 2 === 0 ? "#f8f8f8" : "white")
                                
                                Row {
                                    anchors.fill: parent
                                    anchors.leftMargin: 5
                                    spacing: 5
                                    anchors.verticalCenter: parent.verticalCenter
                                    
                                    Rectangle {
                                        width: 16
                                        height: 16
                                        color: favoritecolor
                                        border.color: "#888"
                                        border.width: 1
                                        anchors.verticalCenter: parent.verticalCenter
                                    }
                                    
                                    Text {
                                        text: favoritecolor
                                        anchors.verticalCenter: parent.verticalCenter
                                        elide: Text.ElideRight
                                    }
                                }
                                
                                MouseArea {
                                    anchors.fill: parent
                                    onClicked: {
                                        selectedPersonIndex = row
                                        listView.currentIndex = row
                                        personController.selectPerson(row)
                                    }
                                }
                            }
                        }
                    }
                    
                    // Add space for header
                    topMargin: header.height
                }
            }
            
            // TreeView
            Rectangle {
                Layout.fillWidth: true
                Layout.fillHeight: true
                color: "white"
                border.color: "#ccc"
                
                ListView {
                    id: treeView
                    anchors.fill: parent
                    anchors.margins: 1
                    model: personModel
                    clip: true
                    
                    property int expandedIndex: -1
                    
                    delegate: Column {
                        width: treeView.width
                        
                        // Main item
                        Rectangle {
                            width: parent.width
                            height: 40
                            color: selectedPersonIndex === index ? "#e0e0e0" : (index % 2 === 0 ? "#f8f8f8" : "white")
                            
                            RowLayout {
                                anchors.fill: parent
                                anchors.leftMargin: 5
                                spacing: 5
                                
                                Text {
                                    text: treeView.expandedIndex === index ? "▼" : "▶"
                                    font.pixelSize: 12
                                }
                                
                                Text {
                                    text: names
                                    elide: Text.ElideRight
                                    Layout.fillWidth: true
                                }
                            }
                            
                            MouseArea {
                                anchors.fill: parent
                                onClicked: {
                                    selectedPersonIndex = index
                                    listView.currentIndex = index
                                    personController.selectPerson(index)
                                    
                                    if (treeView.expandedIndex === index) {
                                        treeView.expandedIndex = -1
                                    } else {
                                        treeView.expandedIndex = index
                                    }
                                }
                            }
                        }
                        
                        // Details (shown when expanded)
                        Rectangle {
                            width: parent.width
                            height: treeView.expandedIndex === index ? 80 : 0
                            color: "#f5f5f5"
                            visible: treeView.expandedIndex === index
                            
                            Column {
                                anchors.fill: parent
                                anchors.margins: 10
                                anchors.leftMargin: 25
                                spacing: 5
                                visible: treeView.expandedIndex === index
                                
                                Text {
                                    text: "Name: " + names
                                }
                                
                                Text {
                                    text: "Age: " + age
                                }
                                
                                Row {
                                    spacing: 5
                                    
                                    Text {
                                        text: "Favorite Color: "
                                    }
                                    
                                    Rectangle {
                                        width: 16
                                        height: 16
                                        color: favoritecolor
                                        border.width: 1
                                        border.color: "#888"
                                    }
                                    
                                    Text {
                                        text: favoritecolor
                                    }
                                }
                            }
                            
                            // Animation for smooth expanding/collapsing
                            Behavior on height {
                                NumberAnimation { duration: 100; easing.type: Easing.InOutQuad }
                            }
                        }
                    }
                    
                    ScrollBar.vertical: ScrollBar {}
                }
            }
        }
        
        // Buttons row
        RowLayout {
            Layout.fillWidth: true
            
            Item { Layout.fillWidth: true } // Spacer
            
            Button {
                text: "Add Person"
                onClicked: {
                    addPersonDialog.nameText = ""
                    addPersonDialog.open()
                }
            }
            
            Button {
                text: "Remove Person"
                enabled: selectedPersonIndex >= 0
                onClicked: {
                    if (selectedPersonIndex >= 0) {
                        personController.removePerson(selectedPersonIndex)
                    }
                }
            }
        }
    }
    
    // Connect to controller signals
    Connections {
        target: personController
        
        function onPersonSelected(index, name, favoriteColor, age) {
            // Update selection tracking
            selectedPersonIndex = index
            
            // Update ListView selection
            listView.currentIndex = index
        }
        
        function onPersonRemoved(index) {
            // Reset selection if needed
            if (selectedPersonIndex === index) {
                selectedPersonIndex = -1
                
                // Reset ListView selection
                listView.currentIndex = -1
            }
            
            // Reset expanded states in tree view if necessary
            if (treeView.expandedIndex === index) {
                treeView.expandedIndex = -1
            }
        }
    }
}