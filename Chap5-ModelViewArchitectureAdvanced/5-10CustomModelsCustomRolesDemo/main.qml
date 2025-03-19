import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Dialogs

ApplicationWindow {
    id: window
    visible: true
    width: 940
    height: 460
    title: "Person Management (Qt Quick)"
    color: "#f0f0f0"
    
    // Dialog for adding a new person
    Dialog {
        id: addPersonDialog
        title: "Add New Person"
        standardButtons: Dialog.Ok | Dialog.Cancel
        modal: true
        width: 300
        height: 200
        anchors.centerIn: parent
        
        property alias nameText: nameField.text
        property alias ageValue: ageSpinBox.value
        
        onAccepted: {
            if (nameText.length > 0) {
                personCrudController.addPerson(nameText, ageValue)
            } else {
                errorDialog.text = "Please enter a name"
                errorDialog.open()
            }
            nameText = ""
        }
        
        ColumnLayout {
            anchors.fill: parent
            anchors.margins: 10
            spacing: 10
            
            Label {
                text: "Person Name:"
            }
            
            TextField {
                id: nameField
                Layout.fillWidth: true
                placeholderText: "Enter name"
            }
            
            Label {
                text: "Age:"
            }
            
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
        width: 300
        height: 150
        anchors.centerIn: parent
        
        property alias text: errorText.text
        
        Label {
            id: errorText
            anchors.fill: parent
            wrapMode: Text.WordWrap
            anchors.margins: 10
        }
    }
    
    // Main layout
    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 11
        spacing: 6
        
        // Header row
        RowLayout {
            Layout.fillWidth: true
            height: 20
            spacing: 6
            
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
                text: "TreeView"
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
                                listView.currentIndex = index
                                personCrudController.selectPerson(index)
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
                
                ColumnLayout {
                    anchors.fill: parent
                    anchors.margins: 1
                    spacing: 0
                    
                    // Table header
                    Rectangle {
                        Layout.fillWidth: true
                        height: 40
                        color: "#f0f0f0"
                        
                        RowLayout {
                            anchors.fill: parent
                            anchors.leftMargin: 5
                            spacing: 0
                            
                            Label {
                                text: "Name"
                                font.bold: true
                                Layout.preferredWidth: parent.width * 0.6
                            }
                            
                            Label {
                                text: "Age"
                                font.bold: true
                                Layout.preferredWidth: parent.width * 0.2
                            }
                            
                            Label {
                                text: "Color"
                                font.bold: true
                                Layout.preferredWidth: parent.width * 0.2
                            }
                        }
                    }
                    
                    // Table content
                    ListView {
                        id: tableListView
                        Layout.fillWidth: true
                        Layout.fillHeight: true
                        clip: true
                        model: personModel
                        
                        delegate: Rectangle {
                            width: tableListView.width
                            height: 40
                            color: tableListView.currentIndex === index ? "#e0e0e0" : (index % 2 === 0 ? "#f8f8f8" : "white")
                            
                            RowLayout {
                                anchors.fill: parent
                                anchors.leftMargin: 5
                                anchors.rightMargin: 5
                                spacing: 0
                                
                                // Name
                                Text {
                                    text: names
                                    elide: Text.ElideRight
                                    Layout.preferredWidth: parent.width * 0.6
                                }
                                
                                // Age
                                Text {
                                    text: age
                                    Layout.preferredWidth: parent.width * 0.2
                                }
                                
                                // Color
                                RowLayout {
                                    spacing: 5
                                    Layout.preferredWidth: parent.width * 0.2
                                    
                                    Rectangle {
                                        width: 16
                                        height: 16
                                        color: favoritecolor
                                        border.width: 1
                                        border.color: "#888"
                                    }
                                    
                                    Text {
                                        text: favoritecolor
                                        elide: Text.ElideRight
                                    }
                                }
                            }
                            
                            MouseArea {
                                anchors.fill: parent
                                onClicked: {
                                    tableListView.currentIndex = index
                                    personCrudController.selectPerson(index)
                                }
                            }
                        }
                        
                        ScrollBar.vertical: ScrollBar {}
                    }
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
                            color: treeView.currentIndex === index ? "#e0e0e0" : (index % 2 === 0 ? "#f8f8f8" : "white")
                            
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
                                    treeView.currentIndex = index
                                    personCrudController.selectPerson(index)
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
                        }
                    }
                    
                    ScrollBar.vertical: ScrollBar {}
                }
            }
        }
        
        // Buttons row
        RowLayout {
            Layout.fillWidth: true
            spacing: 10
            
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
                enabled: listView.currentIndex >= 0 || 
                         tableListView.currentIndex >= 0 || 
                         treeView.currentIndex >= 0
                
                onClicked: {
                    let index = -1
                    
                    if (listView.currentIndex >= 0) {
                        index = listView.currentIndex
                    } else if (tableListView.currentIndex >= 0) {
                        index = tableListView.currentIndex
                    } else if (treeView.currentIndex >= 0) {
                        index = treeView.currentIndex
                    }
                    
                    if (index >= 0) {
                        personCrudController.removePerson(index)
                    }
                }
            }
        }
    }
    
    // Connect to controller signals
    Connections {
        target: personCrudController
        
        function onPersonSelected(index, name, favoriteColor, age) {
            // Sync selection across views
            listView.currentIndex = index
            tableListView.currentIndex = index
            treeView.currentIndex = index
        }
        
        function onPersonRemoved(index) {
            // Reset current indices if necessary
            if (listView.currentIndex === index) {
                listView.currentIndex = -1
            }
            
            if (tableListView.currentIndex === index) {
                tableListView.currentIndex = -1
            }
            
            if (treeView.currentIndex === index) {
                treeView.currentIndex = -1
            }
            
            // Reset expanded index in tree view if necessary
            if (treeView.expandedIndex === index) {
                treeView.expandedIndex = -1
            }
        }
    }
}