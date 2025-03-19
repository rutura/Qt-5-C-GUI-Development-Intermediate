import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Dialogs

ApplicationWindow {
    visible: true
    width: 940
    height: 460
    title: "Person Model with Color Selector (Qt Quick)"
    
    // Track selection state
    property int selectedPersonIndex: -1
    
    // Dialog for adding a new person
    Dialog {
        id: addPersonDialog
        title: "Add New Person"
        standardButtons: Dialog.Ok | Dialog.Cancel
        modal: true
        width: 350
        height: 200
        
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
            anchors.fill: parent
            anchors.margins: 10
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
    
    // Edit dialog for a person
    Dialog {
        id: editPersonDialog
        title: "Edit Person"
        standardButtons: Dialog.Ok | Dialog.Cancel
        modal: true
        width: 350
        height: 300
        
        property int personIndex: -1
        property alias nameText: editNameField.text
        property alias ageValue: editAgeSpinBox.value
        property alias colorValue: colorComboBox.currentText
        
        onAccepted: {
            if (nameText.length > 0 && personIndex >= 0) {
                personController.updatePerson(personIndex, nameText, colorValue, ageValue)
            }
        }
        
        ColumnLayout {
            anchors.fill: parent
            anchors.margins: 10
            spacing: 10
            
            Label { text: "Person Name:" }
            TextField {
                id: editNameField
                Layout.fillWidth: true
                placeholderText: "Enter name"
            }
            
            Label { text: "Age:" }
            SpinBox {
                id: editAgeSpinBox
                Layout.fillWidth: true
                from: 15
                to: 120
                value: 30
            }
            
            Label { text: "Favorite Color:" }
            ComboBox {
                id: colorComboBox
                Layout.fillWidth: true
                model: personController.getColorList()
                
                delegate: ItemDelegate {
                    width: colorComboBox.width
                    contentItem: RowLayout {
                        spacing: 10
                        Rectangle {
                            width: 20
                            height: 20
                            color: modelData
                            border.color: "#888"
                            border.width: 1
                        }
                        Text {
                            text: modelData
                            elide: Text.ElideRight
                            Layout.fillWidth: true
                        }
                    }
                }
                
                // Display color swatch in the combo box
                contentItem: RowLayout {
                    spacing: 10
                    Rectangle {
                        width: 20
                        height: 20
                        color: colorComboBox.currentText
                        border.color: "#888"
                        border.width: 1
                    }
                    Text {
                        text: colorComboBox.currentText
                        elide: Text.ElideRight
                        Layout.fillWidth: true
                    }
                }
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
                        
                        RowLayout {
                            anchors.fill: parent
                            anchors.leftMargin: 5
                            anchors.rightMargin: 5
                            spacing: 10
                            
                            Text {
                                text: names
                                Layout.fillWidth: true
                                elide: Text.ElideRight
                                verticalAlignment: Text.AlignVCenter
                            }
                            
                            Rectangle {
                                width: 16
                                height: 16
                                color: favoritecolor
                                border.color: "#888"
                                border.width: 1
                            }
                            
                            MouseArea {
                                width: 20
                                height: 20
                                onClicked: {
                                    selectedPersonIndex = index
                                    listView.currentIndex = index
                                    personController.selectPerson(index)
                                    editPersonDialog.personIndex = index
                                    editPersonDialog.nameText = names
                                    editPersonDialog.ageValue = age
                                    editPersonDialog.colorValue = favoritecolor
                                    editPersonDialog.open()
                                    event.accepted = true
                                }
                                
                                // Edit icon
                                Text {
                                    anchors.centerIn: parent
                                    text: "✏️"
                                    font.pixelSize: 14
                                }
                            }
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
                            anchors.rightMargin: 5
                            spacing: 0
                            
                            Label {
                                text: "Name"
                                font.bold: true
                                Layout.preferredWidth: parent.width * 0.5
                            }
                            
                            Label {
                                text: "Age"
                                font.bold: true
                                Layout.preferredWidth: parent.width * 0.15
                            }
                            
                            Label {
                                text: "Favorite Color"
                                font.bold: true
                                Layout.preferredWidth: parent.width * 0.25
                            }
                            
                            Label {
                                text: "Edit"
                                font.bold: true
                                Layout.preferredWidth: parent.width * 0.1
                                horizontalAlignment: Text.AlignHCenter
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
                                    Layout.preferredWidth: parent.width * 0.5
                                }
                                
                                // Age
                                Text {
                                    text: age
                                    Layout.preferredWidth: parent.width * 0.15
                                }
                                
                                // Color
                                RowLayout {
                                    spacing: 5
                                    Layout.preferredWidth: parent.width * 0.25
                                    
                                    Rectangle {
                                        width: 16
                                        height: 16
                                        color: favoritecolor
                                        border.color: "#888"
                                        border.width: 1
                                    }
                                    
                                    Text {
                                        text: favoritecolor
                                        elide: Text.ElideRight
                                    }
                                }
                                
                                // Edit button
                                Item {
                                    Layout.preferredWidth: parent.width * 0.1
                                    
                                    Button {
                                        anchors.centerIn: parent
                                        text: "Edit"
                                        implicitWidth: 50
                                        implicitHeight: 24
                                        
                                        onClicked: {
                                            selectedPersonIndex = index
                                            tableListView.currentIndex = index
                                            personController.selectPerson(index)
                                            editPersonDialog.personIndex = index
                                            editPersonDialog.nameText = names
                                            editPersonDialog.ageValue = age
                                            editPersonDialog.colorValue = favoritecolor
                                            editPersonDialog.open()
                                        }
                                    }
                                }
                            }
                            
                            MouseArea {
                                anchors.fill: parent
                                onClicked: {
                                    selectedPersonIndex = index
                                    tableListView.currentIndex = index
                                    personController.selectPerson(index)
                                }
                            }
                        }
                        
                        ScrollBar.vertical: ScrollBar {}
                    }
                }
            }
            
            // TreeView (Using ListView with hierarchy simulation)
            Rectangle {
                Layout.fillWidth: true
                Layout.fillHeight: true
                color: "white"
                border.color: "#ccc"
                
                ListView {
                    id: treeListView
                    anchors.fill: parent
                    anchors.margins: 1
                    model: personModel
                    clip: true
                    
                    property int expandedIndex: -1
                    
                    delegate: Column {
                        width: treeListView.width
                        
                        // Main item
                        Rectangle {
                            width: parent.width
                            height: 40
                            color: treeListView.currentIndex === index ? "#e0e0e0" : (index % 2 === 0 ? "#f8f8f8" : "white")
                            
                            RowLayout {
                                anchors.fill: parent
                                anchors.leftMargin: 5
                                anchors.rightMargin: 5
                                spacing: 5
                                
                                Text {
                                    text: treeListView.expandedIndex === index ? "▼" : "▶"
                                    font.pixelSize: 12
                                }
                                
                                Text {
                                    text: names
                                    elide: Text.ElideRight
                                    Layout.fillWidth: true
                                }
                                
                                Button {
                                    text: "Edit"
                                    implicitWidth: 50
                                    implicitHeight: 24
                                    
                                    onClicked: {
                                        selectedPersonIndex = index
                                        treeListView.currentIndex = index
                                        personController.selectPerson(index)
                                        editPersonDialog.personIndex = index
                                        editPersonDialog.nameText = names
                                        editPersonDialog.ageValue = age
                                        editPersonDialog.colorValue = favoritecolor
                                        editPersonDialog.open()
                                        event.accepted = true
                                    }
                                }
                            }
                            
                            MouseArea {
                                anchors.fill: parent
                                onClicked: {
                                    selectedPersonIndex = index
                                    treeListView.currentIndex = index
                                    personController.selectPerson(index)
                                    
                                    if (treeListView.expandedIndex === index) {
                                        treeListView.expandedIndex = -1
                                    } else {
                                        treeListView.expandedIndex = index
                                    }
                                }
                            }
                        }
                        
                        // Details (shown when expanded)
                        Rectangle {
                            width: parent.width
                            height: treeListView.expandedIndex === index ? 80 : 0
                            color: "#f5f5f5"
                            visible: treeListView.expandedIndex === index
                            
                            Column {
                                anchors.fill: parent
                                anchors.margins: 10
                                anchors.leftMargin: 25
                                spacing: 5
                                visible: treeListView.expandedIndex === index
                                
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
            tableListView.currentIndex = index 
            treeListView.currentIndex = index
        }
        
        function onPersonRemoved(index) {
            // Reset selection if needed
            if (selectedPersonIndex === index) {
                selectedPersonIndex = -1
                listView.currentIndex = -1
                tableListView.currentIndex = -1
                treeListView.currentIndex = -1
            }
            
            // Reset expanded states
            if (treeListView.expandedIndex === index) {
                treeListView.expandedIndex = -1
            }
        }
    }
}