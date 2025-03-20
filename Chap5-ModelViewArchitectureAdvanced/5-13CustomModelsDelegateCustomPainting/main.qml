import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Dialogs

ApplicationWindow {
    visible: true
    width: 940
    height: 460
    title: "Person Model with Custom Color Delegate (Qt Quick)"
    
    // Track selection state
    property int selectedPersonIndex: -1
    
    // Dialog for adding a new person
    Dialog {
        id: addPersonDialog
        title: "Add New Person"
        standardButtons: Dialog.Ok | Dialog.Cancel
        modal: true
        width: 350
        height: 300
        
        property alias nameText: nameField.text
        property alias ageValue: ageSpinBox.value
        property alias colorValue: colorComboBox.currentText
        
        onAccepted: {
            if (nameText.length > 0) {
                personController.addPersonWithColor(nameText, colorValue, ageValue)
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
            
            Label { text: "Favorite Color:" }
            ComboBox {
                id: colorComboBox
                Layout.fillWidth: true
                model: personController.getColorList()
                
                delegate: ItemDelegate {
                    width: colorComboBox.width
                    height: 40
                    
                    // Reproduce the look of the custom delegate
                    Rectangle {
                        anchors.fill: parent
                        anchors.margins: 2
                        color: modelData
                        border.color: "#888"
                        border.width: 1
                        
                        Rectangle {
                            anchors.centerIn: parent
                            width: colorText.width + 10
                            height: colorText.height + 4
                            color: "white"
                            border.color: "#888"
                            border.width: 1
                            
                            Text {
                                id: colorText
                                anchors.centerIn: parent
                                text: modelData
                                horizontalAlignment: Text.AlignHCenter
                                verticalAlignment: Text.AlignVCenter
                            }
                        }
                    }
                }
            }
        }
    }
    
    // Edit dialog for a person
    Dialog {
        id: editDialog
        title: "Edit Person"
        standardButtons: Dialog.Ok | Dialog.Cancel
        modal: true
        width: 350
        height: 300
        
        property int personIndex: -1
        property alias nameText: editNameField.text
        property alias ageValue: editAgeSpinBox.value
        property alias colorValue: editColorComboBox.currentText
        
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
                id: editColorComboBox
                Layout.fillWidth: true
                model: personController.getColorList()
                
                delegate: ItemDelegate {
                    width: editColorComboBox.width
                    height: 40
                    
                    // Reproduce the look of the custom delegate
                    Rectangle {
                        anchors.fill: parent
                        anchors.margins: 2
                        color: modelData
                        border.color: "#888"
                        border.width: 1
                        
                        Rectangle {
                            anchors.centerIn: parent
                            width: editColorText.width + 10
                            height: editColorText.height + 4
                            color: "white"
                            border.color: "#888"
                            border.width: 1
                            
                            Text {
                                id: editColorText
                                anchors.centerIn: parent
                                text: modelData
                                horizontalAlignment: Text.AlignHCenter
                                verticalAlignment: Text.AlignVCenter
                            }
                        }
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
                            anchors.margins: 5
                            spacing: 10
                            
                            Text {
                                text: names
                                Layout.fillWidth: true
                                elide: Text.ElideRight
                            }
                            
                            // Custom color item
                            ColorItem {
                                Layout.preferredWidth: 120
                                Layout.preferredHeight: 30
                                colorName: favoritecolor
                            }
                            
                            Button {
                                text: "Edit"
                                onClicked: {
                                    editDialog.personIndex = index
                                    editDialog.nameText = names
                                    editDialog.ageValue = age
                                    // Find index of color in the color list
                                    let colorList = personController.getColorList()
                                    let colorIndex = colorList.indexOf(favoritecolor)
                                    if (colorIndex !== -1) {
                                        editColorComboBox.currentIndex = colorIndex
                                    } else {
                                        editColorComboBox.currentIndex = 0
                                    }
                                    editDialog.open()
                                }
                            }
                        }
                        
                        MouseArea {
                            anchors.fill: parent
                            onClicked: {
                                listView.currentIndex = index
                                selectedPersonIndex = index
                                personController.selectPerson(index)
                            }
                        }
                    }
                    
                    ScrollBar.vertical: ScrollBar {}
                }
            }
            
            // TableView with Custom Color Delegate
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
                                
                                // Name column
                                Text {
                                    text: names
                                    elide: Text.ElideRight
                                    Layout.preferredWidth: parent.width * 0.4
                                }
                                
                                // Age column
                                Text {
                                    text: age
                                    Layout.preferredWidth: parent.width * 0.2
                                }
                                
                                // Favorite color column with custom delegate styling
                                Item {
                                    Layout.preferredWidth: parent.width * 0.4
                                    Layout.fillHeight: true
                                    
                                    ColorItem {
                                        anchors.fill: parent
                                        anchors.margins: 5
                                        colorName: favoritecolor
                                        
                                        MouseArea {
                                            anchors.fill: parent
                                            onClicked: {
                                                // Open color selector on click
                                                editDialog.personIndex = index
                                                editDialog.nameText = names
                                                editDialog.ageValue = age
                                                
                                                let colorList = personController.getColorList()
                                                let colorIndex = colorList.indexOf(favoritecolor)
                                                if (colorIndex !== -1) {
                                                    editColorComboBox.currentIndex = colorIndex
                                                } else {
                                                    editColorComboBox.currentIndex = 0
                                                }
                                                editDialog.open()
                                            }
                                        }
                                    }
                                }
                            }
                            
                            MouseArea {
                                anchors.fill: parent
                                onClicked: {
                                    tableListView.currentIndex = index
                                    selectedPersonIndex = index
                                    personController.selectPerson(index)
                                }
                            }
                        }
                        
                        ScrollBar.vertical: ScrollBar {}
                    }
                }
            }
            
            // TreeView with Custom Color Delegate
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
                        
                        // Main row
                        Rectangle {
                            width: parent.width
                            height: 40
                            color: treeListView.currentIndex === index ? "#e0e0e0" : (index % 2 === 0 ? "#f8f8f8" : "white")
                            
                            RowLayout {
                                anchors.fill: parent
                                anchors.leftMargin: 5
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
                            }
                            
                            MouseArea {
                                anchors.fill: parent
                                onClicked: {
                                    treeListView.currentIndex = index
                                    selectedPersonIndex = index
                                    personController.selectPerson(index)
                                    
                                    if (treeListView.expandedIndex === index) {
                                        treeListView.expandedIndex = -1
                                    } else {
                                        treeListView.expandedIndex = index
                                    }
                                }
                            }
                        }
                        
                        // Expanded details
                        Rectangle {
                            width: parent.width
                            height: treeListView.expandedIndex === index ? 100 : 0
                            color: "#f5f5f5"
                            visible: treeListView.expandedIndex === index
                            
                            ColumnLayout {
                                anchors.fill: parent
                                anchors.margins: 10
                                anchors.leftMargin: 25
                                spacing: 5
                                visible: treeListView.expandedIndex === index
                                
                                Text { text: "Name: " + names }
                                Text { text: "Age: " + age }
                                
                                RowLayout {
                                    spacing: 5
                                    Layout.fillWidth: true
                                    
                                    Text { text: "Favorite Color: " }
                                    
                                    ColorItem {
                                        Layout.preferredWidth: 150
                                        Layout.preferredHeight: 30
                                        colorName: favoritecolor
                                        
                                        MouseArea {
                                            anchors.fill: parent
                                            onClicked: {
                                                // Open color selector on click
                                                editDialog.personIndex = index
                                                editDialog.nameText = names
                                                editDialog.ageValue = age
                                                
                                                let colorList = personController.getColorList()
                                                let colorIndex = colorList.indexOf(favoritecolor)
                                                if (colorIndex !== -1) {
                                                    editColorComboBox.currentIndex = colorIndex
                                                } else {
                                                    editColorComboBox.currentIndex = 0
                                                }
                                                editDialog.open()
                                            }
                                        }
                                    }
                                }
                            }
                            
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
    
    // Handle controller signals
    Connections {
        target: personController
        
        function onPersonSelected(index, name, favoriteColor, age) {
            selectedPersonIndex = index
            listView.currentIndex = index
            tableListView.currentIndex = index
            treeListView.currentIndex = index
        }
        
        function onPersonRemoved(index) {
            if (selectedPersonIndex === index) {
                selectedPersonIndex = -1
                listView.currentIndex = -1
                tableListView.currentIndex = -1
                treeListView.currentIndex = -1
            }
            
            if (treeListView.expandedIndex === index) {
                treeListView.expandedIndex = -1
            }
        }
    }
}