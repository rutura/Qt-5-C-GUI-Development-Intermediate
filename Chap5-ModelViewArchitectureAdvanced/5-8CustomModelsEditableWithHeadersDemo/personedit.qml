import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    id: window
    visible: true
    width: 900
    height: 500
    title: "Editable Custom Model Demo (Qt Quick)"

    // Person detail view
    Rectangle {
        id: detailView
        anchors.top: parent.top
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        width: 250
        color: "#f5f5f5"
        border.color: "#cccccc"
        border.width: 1
        visible: false
        
        property int selectedIndex: -1
        property string selectedName: ""
        property string selectedColor: "white"
        property int selectedAge: 0
        
        ColumnLayout {
            anchors.fill: parent
            anchors.margins: 15
            spacing: 15
            
            Text {
                text: "Person Details"
                font.pixelSize: 18
                font.bold: true
            }
            
            // Name
            ColumnLayout {
                Layout.fillWidth: true
                spacing: 5
                
                Text {
                    text: "Name:"
                    font.bold: true
                }
                
                TextField {
                    id: nameField
                    Layout.fillWidth: true
                    text: detailView.selectedName
                    placeholderText: "Enter name"
                    onEditingFinished: {
                        if (detailView.selectedIndex >= 0 && text !== detailView.selectedName) {
                            personEditController.editPersonName(detailView.selectedIndex, text)
                        }
                    }
                }
            }
            
            // Favorite Color
            ColumnLayout {
                Layout.fillWidth: true
                spacing: 5
                
                Text {
                    text: "Favorite Color:"
                    font.bold: true
                }
                
                Rectangle {
                    Layout.fillWidth: true
                    height: 30
                    color: detailView.selectedColor
                    border.color: "#888888"
                    border.width: 1
                    
                    Text {
                        anchors.centerIn: parent
                        text: detailView.selectedColor
                        color: isColorDark(detailView.selectedColor) ? "white" : "black"
                    }
                }
            }
            
            // Age
            ColumnLayout {
                Layout.fillWidth: true
                spacing: 5
                
                Text {
                    text: "Age:"
                    font.bold: true
                }
                
                Text {
                    text: detailView.selectedAge
                }
            }
            
            Item { Layout.fillHeight: true } // Spacer
        }
        
        // Function to determine if color is dark
        function isColorDark(colorString) {
            var color = Qt.color(colorString)
            var brightness = (color.r * 299 + color.g * 587 + color.b * 114) / 1000
            return brightness < 0.5
        }
    }

    // Connect to controller signal
    Connections {
        target: personEditController
        function onPersonSelected(index, name, favoriteColor, age) {
            detailView.selectedIndex = index
            detailView.selectedName = name
            detailView.selectedColor = favoriteColor
            detailView.selectedAge = age
            detailView.visible = true
            
            // Update the editing state of currently selected items
            if (listView.currentIndex === index) {
                listViewEditor.updateText(name)
            }
            if (tableView.currentIndex === index) {
                tableViewEditor.updateText(name)
            }
            if (treeView.currentIndex === index) {
                treeViewEditor.updateText(name)
            }
        }
        
        function onPersonEdited(index, name) {
            if (detailView.selectedIndex === index) {
                detailView.selectedName = name
            }
            
            // Update the editing state of currently selected items
            if (listView.currentIndex === index) {
                listViewEditor.updateText(name)
            }
            if (tableView.currentIndex === index) {
                tableViewEditor.updateText(name)
            }
            if (treeView.currentIndex === index) {
                treeViewEditor.updateText(name)
            }
        }
    }

    // Main content with three views
    RowLayout {
        anchors.fill: parent
        anchors.rightMargin: detailView.visible ? detailView.width : 0
        spacing: 5
        
        // ListView
        Rectangle {
            Layout.fillWidth: true
            Layout.fillHeight: true
            border.color: "#cccccc"
            border.width: 1
            
            ColumnLayout {
                anchors.fill: parent
                anchors.margins: 5
                spacing: 5
                
                Text {
                    text: "ListView (Double-click to edit)"
                    font.bold: true
                    font.pixelSize: 14
                }
                
                ListView {
                    id: listView
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                    model: personModel
                    clip: true
                    
                    delegate: Rectangle {
                        width: listView.width
                        height: 40
                        color: listView.currentIndex === index ? "#e0e0e0" : (index % 2 === 0 ? "#f8f8f8" : "white")
                        
                        Text {
                            id: listText
                            anchors.fill: parent
                            anchors.margins: 10
                            text: name
                            verticalAlignment: Text.AlignVCenter
                            elide: Text.ElideRight
                            visible: !(listView.currentIndex === index && listViewEditor.editing)
                        }
                        
                        TextInput {
                            id: listViewEditor
                            anchors.fill: parent
                            anchors.margins: 10
                            verticalAlignment: TextInput.AlignVCenter
                            text: name
                            visible: listView.currentIndex === index && editing
                            property bool editing: false
                            
                            Keys.onReturnPressed: {
                                if (text !== name) {
                                    personEditController.editPersonName(index, text)
                                }
                                editing = false
                            }
                            
                            Keys.onEscapePressed: {
                                text = name
                                editing = false
                            }
                            
                            function updateText(newText) {
                                if (!editing) {
                                    text = newText
                                }
                            }
                        }
                        
                        MouseArea {
                            anchors.fill: parent
                            onClicked: {
                                listView.currentIndex = index
                                personEditController.selectPerson(index)
                            }
                            onDoubleClicked: {
                                listView.currentIndex = index
                                listViewEditor.editing = true
                                listViewEditor.forceActiveFocus()
                            }
                        }
                    }
                }
            }
        }
        
        // TableView-style
        Rectangle {
            Layout.fillWidth: true
            Layout.fillHeight: true
            border.color: "#cccccc"
            border.width: 1
            
            ColumnLayout {
                anchors.fill: parent
                anchors.margins: 5
                spacing: 5
                
                Text {
                    text: "TableView-style (Double-click to edit)"
                    font.bold: true
                    font.pixelSize: 14
                }
                
                // Header row
                Rectangle {
                    Layout.fillWidth: true
                    height: 30
                    color: "#f0f0f0"
                    
                    RowLayout {
                        anchors.fill: parent
                        anchors.leftMargin: 5
                        anchors.rightMargin: 5
                        
                        Text {
                            text: "Name"
                            font.bold: true
                            Layout.preferredWidth: 150
                        }
                        
                        Text {
                            text: "Age"
                            font.bold: true
                            Layout.preferredWidth: 50
                        }
                        
                        Text {
                            text: "Favorite Color"
                            font.bold: true
                            Layout.fillWidth: true
                        }
                    }
                }
                
                ListView {
                    id: tableView
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                    model: personModel
                    clip: true
                    
                    delegate: Rectangle {
                        width: tableView.width
                        height: 40
                        color: tableView.currentIndex === index ? "#e0e0e0" : (index % 2 === 0 ? "#f8f8f8" : "white")
                        
                        RowLayout {
                            anchors.fill: parent
                            anchors.leftMargin: 5
                            anchors.rightMargin: 5
                            
                            Item {
                                Layout.preferredWidth: 150
                                Layout.fillHeight: true
                                
                                Text {
                                    id: tableText
                                    anchors.fill: parent
                                    text: name
                                    verticalAlignment: Text.AlignVCenter
                                    elide: Text.ElideRight
                                    visible: !(tableView.currentIndex === index && tableViewEditor.editing)
                                }
                                
                                TextInput {
                                    id: tableViewEditor
                                    anchors.fill: parent
                                    verticalAlignment: TextInput.AlignVCenter
                                    text: name
                                    visible: tableView.currentIndex === index && editing
                                    property bool editing: false
                                    
                                    Keys.onReturnPressed: {
                                        if (text !== name) {
                                            personEditController.editPersonName(index, text)
                                        }
                                        editing = false
                                    }
                                    
                                    Keys.onEscapePressed: {
                                        text = name
                                        editing = false
                                    }
                                    
                                    function updateText(newText) {
                                        if (!editing) {
                                            text = newText
                                        }
                                    }
                                }
                            }
                            
                            Text {
                                text: age
                                Layout.preferredWidth: 50
                            }
                            
                            Rectangle {
                                Layout.fillWidth: true
                                Layout.preferredHeight: 24
                                color: favoriteColor
                                border.color: "#888888"
                                border.width: 1
                                
                                Text {
                                    anchors.centerIn: parent
                                    text: favoriteColor
                                    color: detailView.isColorDark(favoriteColor) ? "white" : "black"
                                }
                            }
                        }
                        
                        MouseArea {
                            anchors.fill: parent
                            onClicked: {
                                tableView.currentIndex = index
                                personEditController.selectPerson(index)
                            }
                            onDoubleClicked: {
                                tableView.currentIndex = index
                                tableViewEditor.editing = true
                                tableViewEditor.forceActiveFocus()
                            }
                        }
                    }
                }
            }
        }
        
        // TreeView-style
        Rectangle {
            Layout.fillWidth: true
            Layout.fillHeight: true
            border.color: "#cccccc"
            border.width: 1
            
            ColumnLayout {
                anchors.fill: parent
                anchors.margins: 5
                spacing: 5
                
                Text {
                    text: "TreeView-style (Double-click to edit)"
                    font.bold: true
                    font.pixelSize: 14
                }
                
                ListView {
                    id: treeView
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                    model: personModel
                    clip: true
                    
                    delegate: Column {
                        width: treeView.width
                        
                        Rectangle {
                            width: treeView.width
                            height: 30
                            color: treeView.currentIndex === index ? "#e0e0e0" : (index % 2 === 0 ? "#f8f8f8" : "white")
                            
                            RowLayout {
                                anchors.fill: parent
                                anchors.leftMargin: 5
                                anchors.rightMargin: 5
                                
                                Text {
                                    text: "👤"
                                    font.pixelSize: 16
                                    Layout.preferredWidth: 20
                                }
                                
                                Item {
                                    Layout.fillWidth: true
                                    Layout.fillHeight: true
                                    
                                    Text {
                                        id: treeText
                                        anchors.fill: parent
                                        text: name
                                        verticalAlignment: Text.AlignVCenter
                                        elide: Text.ElideRight
                                        visible: !(treeView.currentIndex === index && treeViewEditor.editing)
                                    }
                                    
                                    TextInput {
                                        id: treeViewEditor
                                        anchors.fill: parent
                                        verticalAlignment: TextInput.AlignVCenter
                                        text: name
                                        visible: treeView.currentIndex === index && editing
                                        property bool editing: false
                                        
                                        Keys.onReturnPressed: {
                                            if (text !== name) {
                                                personEditController.editPersonName(index, text)
                                            }
                                            editing = false
                                        }
                                        
                                        Keys.onEscapePressed: {
                                            text = name
                                            editing = false
                                        }
                                        
                                        function updateText(newText) {
                                            if (!editing) {
                                                text = newText
                                            }
                                        }
                                    }
                                }
                            }
                            
                            MouseArea {
                                anchors.fill: parent
                                onClicked: {
                                    treeView.currentIndex = index
                                    personEditController.selectPerson(index)
                                    detailItem.expanded = !detailItem.expanded
                                }
                                onDoubleClicked: {
                                    treeView.currentIndex = index
                                    treeViewEditor.editing = true
                                    treeViewEditor.forceActiveFocus()
                                    event.accepted = true
                                }
                            }
                        }
                        
                        // Expandable item
                        Item {
                            id: detailItem
                            width: treeView.width
                            height: expanded ? 80 : 0
                            clip: true
                            property bool expanded: false
                            
                            Column {
                                anchors.fill: parent
                                anchors.leftMargin: 25
                                anchors.rightMargin: 5
                                spacing: 5
                                
                                Text {
                                    text: "Age: " + age
                                    leftPadding: 20
                                }
                                
                                RowLayout {
                                    width: parent.width
                                    height: 24
                                    
                                    Text {
                                        text: "Favorite Color: "
                                        leftPadding: 20
                                    }
                                    
                                    Rectangle {
                                        Layout.preferredWidth: 100
                                        Layout.preferredHeight: 24
                                        color: favoriteColor
                                        border.color: "#888888"
                                        border.width: 1
                                        
                                        Text {
                                            anchors.centerIn: parent
                                            text: favoriteColor
                                            color: detailView.isColorDark(favoriteColor) ? "white" : "black"
                                        }
                                    }
                                }
                            }
                            
                            Behavior on height {
                                NumberAnimation { duration: 200 }
                            }
                        }
                    }
                }
            }
        }
    }
}