import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Dialogs
import Qt.labs.qmlmodels 1.0

ApplicationWindow {
    id: window
    visible: true
    width: 940
    height: 460
    title: "Advanced Custom Model Demo (Qt Quick)"
    color: "#f0f0f0"
    
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
                personCrudController.addPerson(nameText, ageValue)
            } else {
                errorDialog.text = "Please enter a name"
                errorDialog.open()
            }
            nameText = ""
        }
        
        ColumnLayout {
            width: parent.width
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
                        height: 30
                        color: ListView.isCurrentItem ? "#e0e0e0" : (index % 2 === 0 ? "#f8f8f8" : "white")
                        
                        Text {
                            anchors.fill: parent
                            anchors.leftMargin: 5
                            verticalAlignment: Text.AlignVCenter
                            text: name
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
                        height: 30
                        color: "#f0f0f0"
                        
                        RowLayout {
                            anchors.fill: parent
                            anchors.leftMargin: 5
                            spacing: 0
                            
                            Label {
                                text: "Name"
                                font.bold: true
                                Layout.preferredWidth: parent.width * 0.4
                            }
                            
                            Label {
                                text: "Age"
                                font.bold: true
                                Layout.preferredWidth: parent.width * 0.2
                            }
                            
                            Label {
                                text: "Favorite Color"
                                font.bold: true
                                Layout.preferredWidth: parent.width * 0.4
                            }
                        }
                    }
                    
                    // Modern TableView
                    HorizontalHeaderView {
                        id: horizontalHeader
                        syncView: tableView
                        model: ["Name", "Age", "Favorite Color"]
                        visible: false  // Hide this as we're using our custom header above
                    }
                    
                    TableView {
                        id: tableView
                        Layout.fillWidth: true
                        Layout.fillHeight: true
                        clip: true
                        model: personModel
                        
                        property int selectedRow: -1
                        
                        columnWidthProvider: function(column) {
                            if (column === 0) return width * 0.4
                            if (column === 1) return width * 0.2
                            return width * 0.4
                        }
                        
                        rowHeightProvider: function(row) {
                            return 30
                        }
                        
                        delegate: DelegateChooser {
                            role: "column"
                            
                            // Name column
                            DelegateChoice {
                                column: 0
                                delegate: Rectangle {
                                    color: tableView.selectedRow === row ? "#e0e0e0" :
                                          (row % 2 === 0 ? "#f8f8f8" : "white")
                                    
                                    Text {
                                        anchors.fill: parent
                                        anchors.leftMargin: 5
                                        text: name
                                        verticalAlignment: Text.AlignVCenter
                                        elide: Text.ElideRight
                                    }
                                    
                                    MouseArea {
                                        anchors.fill: parent
                                        onClicked: {
                                            tableView.selectedRow = row
                                            listView.currentIndex = row
                                            personCrudController.selectPerson(row)
                                        }
                                    }
                                }
                            }
                            
                            // Age column
                            DelegateChoice {
                                column: 1
                                delegate: Rectangle {
                                    color: tableView.selectedRow === row ? "#e0e0e0" :
                                          (row % 2 === 0 ? "#f8f8f8" : "white")
                                    
                                    Text {
                                        anchors.fill: parent
                                        anchors.leftMargin: 5
                                        text: age
                                        verticalAlignment: Text.AlignVCenter
                                    }
                                    
                                    MouseArea {
                                        anchors.fill: parent
                                        onClicked: {
                                            tableView.selectedRow = row
                                            listView.currentIndex = row
                                            personCrudController.selectPerson(row)
                                        }
                                    }
                                }
                            }
                            
                            // Favorite Color column
                            DelegateChoice {
                                column: 2
                                delegate: Rectangle {
                                    color: tableView.selectedRow === row ? "#e0e0e0" :
                                          (row % 2 === 0 ? "#f8f8f8" : "white")
                                    
                                    RowLayout {
                                        anchors.fill: parent
                                        anchors.leftMargin: 5
                                        spacing: 5
                                        
                                        Rectangle {
                                            width: 20
                                            height: 20
                                            color: favoriteColor
                                            border.color: "#888"
                                            border.width: 1
                                        }
                                        
                                        Text {
                                            text: favoriteColor
                                            Layout.fillWidth: true
                                            verticalAlignment: Text.AlignVCenter
                                            elide: Text.ElideRight
                                        }
                                    }
                                    
                                    MouseArea {
                                        anchors.fill: parent
                                        onClicked: {
                                            tableView.selectedRow = row
                                            listView.currentIndex = row
                                            personCrudController.selectPerson(row)
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
            
            // For TreeView, use a ListView with custom indentation (since TreeView is challenging in Qt 6)
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
                    
                    property int currentIndex: -1
                    
                    delegate: Item {
                        width: treeView.width
                        height: rowItem.height + (isExpanded ? detailsItem.height : 0)
                        
                        property bool isExpanded: false
                        
                        // Main row
                        Rectangle {
                            id: rowItem
                            width: parent.width
                            height: 30
                            color: treeView.currentIndex === index ? "#e0e0e0" : (index % 2 === 0 ? "#f8f8f8" : "white")
                            
                            RowLayout {
                                anchors.fill: parent
                                anchors.leftMargin: 5
                                
                                Text {
                                    text: isExpanded ? "🔽" : "▶️"
                                    font.pixelSize: 12
                                    Layout.preferredWidth: 20
                                }
                                
                                Text {
                                    text: name
                                    Layout.fillWidth: true
                                    elide: Text.ElideRight
                                }
                            }
                            
                            MouseArea {
                                anchors.fill: parent
                                onClicked: {
                                    treeView.currentIndex = index
                                    listView.currentIndex = index
                                    tableView.selectedRow = index
                                    personCrudController.selectPerson(index)
                                    isExpanded = !isExpanded
                                }
                            }
                        }
                        
                        // Expanded details
                        Rectangle {
                            id: detailsItem
                            width: parent.width
                            height: isExpanded ? 60 : 0
                            anchors.top: rowItem.bottom
                            color: "#f8f8f8"
                            visible: isExpanded
                            
                            Column {
                                anchors.fill: parent
                                anchors.margins: 5
                                anchors.leftMargin: 25
                                spacing: 5
                                
                                Text { 
                                    text: "Age: " + age 
                                }
                                
                                Row {
                                    spacing: 5
                                    
                                    Text { 
                                        text: "Favorite color: " 
                                    }
                                    
                                    Rectangle {
                                        width: 16
                                        height: 16
                                        color: favoriteColor
                                        border.color: "#888"
                                        border.width: 1
                                    }
                                    
                                    Text { 
                                        text: favoriteColor 
                                    }
                                }
                            }
                            
                            Behavior on height {
                                NumberAnimation { duration: 100 }
                            }
                        }
                    }
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
                enabled: listView.currentIndex >= 0
                onClicked: {
                    if (listView.currentIndex >= 0) {
                        personCrudController.removePerson(listView.currentIndex)
                    }
                }
            }
        }
    }
    
    // Connect to controller signals to handle removals
    Connections {
        target: personCrudController
        
        function onPersonSelected(index, name, favoriteColor, age) {
            // Sync selection across views
            listView.currentIndex = index
            tableView.selectedRow = index
            treeView.currentIndex = index
        }
        
        function onPersonRemoved(index) {
            // Reset current indices if necessary
            if (listView.currentIndex === index) {
                listView.currentIndex = -1
            }
            if (tableView.selectedRow === index) {
                tableView.selectedRow = -1
            }
            if (treeView.currentIndex === index) {
                treeView.currentIndex = -1
            }
        }
    }
}