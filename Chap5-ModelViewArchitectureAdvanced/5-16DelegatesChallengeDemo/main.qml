import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    visible: true
    width: 940
    height: 460
    title: "Multiple Custom Delegates Demo (Qt Quick)"
    color: "#f0f0f0"
    
    // Keep track of selection state
    property int selectedIndex: -1
    
    // Color selector dialog
    ColorDialog {
        id: colorDialog
        colorList: personController.getColorList()
        
        onColorSelected: function(color) {
            if (colorDialog.personIndex >= 0) {
                personController.updateColor(colorDialog.personIndex, color);
            }
        }
        
        property int personIndex: -1
    }
    
    // Dialog for adding a new person
    Dialog {
        id: addPersonDialog
        title: "Add New Person"
        standardButtons: Dialog.Ok | Dialog.Cancel
        modal: true
        width: 400
        height: 350
        
        property alias nameText: nameField.text
        property alias ageValue: ageSpinBox.value
        property string colorValue: "blue"
        property int scoreValue: 3
        
        onAccepted: {
            if (nameText.length > 0) {
                personController.addPerson(nameText, ageValue, colorValue, scoreValue)
                nameText = ""
                colorValue = "blue"
                scoreValue = 3
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
            ColorItem {
                id: colorItem
                Layout.fillWidth: true
                Layout.preferredHeight: 40
                colorName: addPersonDialog.colorValue
                
                onColorClicked: {
                    colorDialog.currentColor = addPersonDialog.colorValue;
                    colorDialog.personIndex = -1;
                    colorDialog.accepted.connect(function() {
                        addPersonDialog.colorValue = colorDialog.currentColor;
                        colorItem.colorName = colorDialog.currentColor;
                        colorDialog.accepted.disconnect(arguments.callee);
                    });
                    colorDialog.open();
                }
            }
            
            Label { text: "Social Score:" }
            StarRating {
                id: starRating
                Layout.fillWidth: true
                Layout.preferredHeight: 40
                rating: addPersonDialog.scoreValue
                readOnly: false
                
                onEdited: function(newRating) {
                    addPersonDialog.scoreValue = newRating;
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
        spacing: 10
        
        // Header row
        Rectangle {
            Layout.fillWidth: true
            height: 40
            color: "#f0f0f0"
            border.color: "#ccc"
            
            RowLayout {
                anchors.fill: parent
                anchors.leftMargin: 5
                anchors.rightMargin: 5
                spacing: 0
                
                Text {
                    text: "Name"
                    font.bold: true
                    Layout.preferredWidth: parent.width * 0.3
                    color: "black"
                }
                
                Text {
                    text: "Age"
                    font.bold: true
                    Layout.preferredWidth: parent.width * 0.1
                    color: "black"
                }
                
                Text {
                    text: "Favorite Color"
                    font.bold: true
                    Layout.preferredWidth: parent.width * 0.3
                    color: "black"
                }
                
                Text {
                    text: "Social Score"
                    font.bold: true
                    Layout.preferredWidth: parent.width * 0.3
                    color: "black"
                }
            }
        }
        
        // Table content
        Rectangle {
            Layout.fillWidth: true
            Layout.fillHeight: true
            color: "white"
            border.color: "#ccc"
            
            ListView {
                id: personListView
                anchors.fill: parent
                anchors.margins: 1
                clip: true
                model: personModel  // Use personModel directly
                
                delegate: Rectangle {
                    width: personListView.width
                    height: 60
                    color: index === selectedIndex ? "#e0e0e0" : (index % 2 === 0 ? "#f8f8f8" : "white")
                    
                    // Row content
                    RowLayout {
                        anchors.fill: parent
                        anchors.leftMargin: 5
                        anchors.rightMargin: 5
                        spacing: 0
                        
                        // Name column
                        Text {
                            text: model.names  // Match roleNames in personmodel.py
                            color: "black"
                            Layout.preferredWidth: parent.width * 0.3
                            elide: Text.ElideRight
                        }
                        
                        // Age column
                        Text {
                            text: model.age
                            color: "black"
                            Layout.preferredWidth: parent.width * 0.1
                        }
                        
                        // Favorite color column with custom delegate
                        Item {
                            Layout.preferredWidth: parent.width * 0.3
                            Layout.fillHeight: true
                            
                            ColorItem {
                                anchors.fill: parent
                                anchors.margins: 5
                                colorName: model.favoritecolor  // Match roleNames in personmodel.py
                                
                                onColorClicked: {
                                    colorDialog.currentColor = model.favoritecolor;
                                    colorDialog.personIndex = index;
                                    colorDialog.open();
                                }
                            }
                        }
                        
                        // Social score column with star rating
                        Item {
                            Layout.preferredWidth: parent.width * 0.3
                            Layout.fillHeight: true
                            
                            StarRating {
                                anchors.fill: parent
                                anchors.margins: 5
                                rating: model.socialscore  // Match roleNames in personmodel.py
                                
                                onEdited: function(newRating) {
                                    personController.updateScore(index, newRating);
                                }
                            }
                        }
                    }
                    
                    // Row selection
                    MouseArea {
                        anchors.fill: parent
                        onClicked: {
                            selectedIndex = index;
                        }
                    }
                }
                
                ScrollBar.vertical: ScrollBar {}
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
                    addPersonDialog.nameText = "";
                    addPersonDialog.open();
                }
            }
            
            Button {
                text: "Remove Person"
                enabled: selectedIndex >= 0
                onClicked: {
                    if (selectedIndex >= 0) {
                        personController.removePerson(selectedIndex);
                        selectedIndex = -1;
                    }
                }
            }
        }
    }
}